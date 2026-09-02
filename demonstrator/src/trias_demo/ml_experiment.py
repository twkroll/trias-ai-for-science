from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
import torch

from .config import FigureEightConfig
from .dynamics import (
    angular_momentum_z,
    max_radius_from_com,
    minimum_pair_distance,
    total_energy,
)
from .ml_data import generate_dataset, rmse, training_scaler
from .ml_model import paired_models, predict_next, train_model
from .reference import integrate_reference


def _mse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean((np.asarray(a) - np.asarray(b)) ** 2))


def _position_scale(x0: np.ndarray) -> float:
    positions = x0[:6].reshape(3, 2)
    return float(np.sqrt(np.mean(np.sum(positions**2, axis=1))))


def _position_error(a: np.ndarray, b: np.ndarray, x0: np.ndarray) -> np.ndarray:
    pa = np.asarray(a)[:, :6].reshape(-1, 3, 2)
    pb = np.asarray(b)[:, :6].reshape(-1, 3, 2)
    return np.sqrt(np.mean(np.sum((pa - pb) ** 2, axis=2), axis=1)) / _position_scale(x0)


def _rollout(model, x0, steps, mu, sigma):
    states = np.empty((steps + 1, 12), dtype=np.float64)
    states[0] = x0
    max_abs_standardized_input = 0.0
    for k in range(steps):
        standardized = (states[k] - mu) / sigma
        max_abs_standardized_input = max(
            max_abs_standardized_input,
            float(np.max(np.abs(standardized))),
        )
        states[k + 1] = predict_next(model, states[k : k + 1], mu, sigma)[0]
        if not np.all(np.isfinite(states[k + 1])):
            return states[: k + 2], False, "non-finite state", max_abs_standardized_input
        if minimum_pair_distance(states[k + 1]) < 0.1:
            return (
                states[: k + 2],
                False,
                "minimum pair-distance guard triggered",
                max_abs_standardized_input,
            )
    return states, True, "", max_abs_standardized_input


def _rollout_metrics(states, reference, x0, cfg, max_abs_standardized_input):
    masses = cfg.masses_array()
    H0 = total_energy(x0, masses, cfg.G)
    L0 = angular_momentum_z(x0, masses)
    p0 = x0[:6].reshape(3, 2)
    v0 = x0[6:].reshape(3, 2)
    L_scale = float(
        np.sum(masses * np.linalg.norm(p0, axis=1) * np.linalg.norm(v0, axis=1))
    )
    pos_error = _position_error(states, reference[: len(states)], x0)
    energies = np.array([total_energy(s, masses, cfg.G) for s in states])
    angular = np.array([angular_momentum_z(s, masses) for s in states])
    return {
        "final_position_error": float(pos_error[-1]),
        "max_position_error": float(np.max(pos_error)),
        "final_energy_error": float((energies[-1] - H0) / abs(H0)),
        "max_abs_energy_error": float(np.max(np.abs((energies - H0) / abs(H0)))),
        "max_angular_momentum_error": float(np.max(np.abs(angular - L0) / L_scale)),
        "min_pair_distance": float(min(minimum_pair_distance(s) for s in states)),
        "max_radius_from_com": float(max(max_radius_from_com(s, masses) for s in states)),
        "max_abs_standardized_input": max_abs_standardized_input,
    }


def _decomposition(y_hat, y_rk4, y_ref):
    e_model = y_hat - y_rk4
    e_teacher = y_rk4 - y_ref
    e_total = y_hat - y_ref
    model_term = float(np.mean(np.sum(e_model**2, axis=1)))
    teacher_term = float(np.mean(np.sum(e_teacher**2, axis=1)))
    total_term = float(np.mean(np.sum(e_total**2, axis=1)))
    cross_term = float(2.0 * np.mean(np.sum(e_model * e_teacher, axis=1)))
    return {
        "mean_sq_model_vec": model_term,
        "mean_sq_teacher_vec": teacher_term,
        "mean_sq_total_vec": total_term,
        "cross_term": cross_term,
        "identity_residual": total_term - model_term - teacher_term - cross_term,
    }


def run(output_dir: Path, smoke: bool = False) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    n = 60 if smoke else 1000
    max_epochs = 20 if smoke else 5000
    patience = 5 if smoke else 500
    seeds = [0] if smoke else [0, 1, 2]

    dataset = generate_dataset(n=n)
    mu, sigma = training_scaler(dataset)
    np.savez_compressed(
        output_dir / "dataset.npz",
        phase_index=dataset.phase_index,
        phase_time=dataset.phase_time,
        x=dataset.x,
        y_ref=dataset.y_ref,
        y_ref_tight=dataset.y_ref_tight,
        y_rk4=dataset.y_rk4,
        delta_ref=dataset.delta_ref,
        delta_rk4=dataset.delta_rk4,
        split=dataset.split,
        mu_x=mu,
        sigma_x=sigma,
    )

    split_metrics = {}
    for split_name in ("train", "validation", "test"):
        mask = dataset.split == split_name
        split_metrics[split_name] = {
            "D_teacher": rmse(dataset.y_rk4[mask], dataset.y_ref[mask]),
            "D_ref": rmse(dataset.y_ref_tight[mask], dataset.y_ref[mask]),
        }

    cfg = FigureEightConfig()
    x0 = cfg.initial_state()
    dt = cfg.T_pub / 50.0
    rollout_times = np.arange(501, dtype=np.float64) * dt
    ref_rollout = integrate_reference(
        x0, rollout_times, cfg.masses_array(), cfg.G, 1e-12, 1e-14
    ).states

    one_step_rows = []
    rollout_rows = []
    decompositions = []
    test_mask = dataset.split == "test"

    for seed in seeds:
        ref_model, rk4_model = paired_models(seed)
        paired = all(
            np.array_equal(a.detach().cpu().numpy(), b.detach().cpu().numpy())
            for a, b in zip(ref_model.parameters(), rk4_model.parameters())
        )

        _, ref_epochs = train_model(
            ref_model,
            dataset.x,
            dataset.delta_ref,
            dataset.split,
            mu,
            sigma,
            max_epochs=max_epochs,
            patience=patience,
        )
        _, rk4_epochs = train_model(
            rk4_model,
            dataset.x,
            dataset.delta_rk4,
            dataset.split,
            mu,
            sigma,
            max_epochs=max_epochs,
            patience=patience,
        )

        y_hat_ref = predict_next(ref_model, dataset.x[test_mask], mu, sigma)
        y_hat_rk4 = predict_next(rk4_model, dataset.x[test_mask], mu, sigma)
        decompositions.append(
            {
                "seed": seed,
                **_decomposition(
                    y_hat_rk4,
                    dataset.y_rk4[test_mask],
                    dataset.y_ref[test_mask],
                ),
            }
        )

        for teacher, model, epochs, prediction in (
            ("ref", ref_model, ref_epochs, y_hat_ref),
            ("rk4", rk4_model, rk4_epochs, y_hat_rk4),
        ):
            own_teacher = (
                dataset.y_ref[test_mask]
                if teacher == "ref"
                else dataset.y_rk4[test_mask]
            )
            one_step_rows.append(
                {
                    "seed": seed,
                    "teacher": teacher,
                    "paired_initialization": paired,
                    "epochs": epochs,
                    "rmse_own_teacher": rmse(prediction, own_teacher),
                    "rmse_vs_ref": rmse(prediction, dataset.y_ref[test_mask]),
                    "rmse_vs_rk4": rmse(prediction, dataset.y_rk4[test_mask]),
                    "mse_own_teacher": _mse(prediction, own_teacher),
                    "mse_vs_ref": _mse(prediction, dataset.y_ref[test_mask]),
                    "mse_vs_rk4": _mse(prediction, dataset.y_rk4[test_mask]),
                }
            )

            if not smoke:
                for use_case, steps in (("MU1", 50), ("MU2", 500)):
                    states, valid, reason, zmax = _rollout(
                        model, x0, steps, mu, sigma
                    )
                    record = {
                        "seed": seed,
                        "teacher": teacher,
                        "use_case": use_case,
                        "valid": valid,
                        "invalid_reason": reason,
                    }
                    if valid:
                        record.update(
                            _rollout_metrics(
                                states,
                                ref_rollout[: steps + 1],
                                x0,
                                cfg,
                                zmax,
                            )
                        )
                    rollout_rows.append(record)

    test_metrics = split_metrics["test"]
    reference_gate = bool(
        test_metrics["D_ref"] <= 0.01 * test_metrics["D_teacher"]
    )
    if smoke:
        status = "SMOKE_ONLY"
    else:
        medians = {
            teacher: float(
                np.median(
                    [
                        row["rmse_own_teacher"]
                        for row in one_step_rows
                        if row["teacher"] == teacher
                    ]
                )
            )
            for teacher in ("ref", "rk4")
        }
        learner_gate = all(
            value < test_metrics["D_teacher"] for value in medians.values()
        )
        if not reference_gate:
            status = "INCONCLUSIVE_REFERENCE"
        elif not learner_gate:
            status = "INCONCLUSIVE_LEARNER_ERROR"
        else:
            status = "READY_FOR_SCIENTIFIC_REVIEW"

    summary = {
        "status": status,
        "smoke": smoke,
        "n": n,
        "split_metrics": split_metrics,
        "reference_gate": reference_gate,
        "one_step_models": one_step_rows,
        "provenance_decomposition": decompositions,
        "rollouts": rollout_rows,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "torch": torch.__version__,
        },
    }
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("ml_run"))
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    run(args.output_dir, smoke=args.smoke)


if __name__ == "__main__":
    main()
