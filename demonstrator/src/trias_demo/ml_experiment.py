from __future__ import annotations

import argparse
import csv
import json
import platform
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
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


def _write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def _write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in rows for key in row}) if rows else ["status"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        if rows:
            writer.writerows(rows)


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
    energies = np.array([total_energy(state, masses, cfg.G) for state in states])
    angular = np.array([angular_momentum_z(state, masses) for state in states])
    return {
        "final_position_error": float(pos_error[-1]),
        "max_position_error": float(np.max(pos_error)),
        "final_energy_error": float((energies[-1] - H0) / abs(H0)),
        "max_abs_energy_error": float(np.max(np.abs((energies - H0) / abs(H0)))),
        "max_angular_momentum_error": float(np.max(np.abs(angular - L0) / L_scale)),
        "min_pair_distance": float(min(minimum_pair_distance(state) for state in states)),
        "max_radius_from_com": float(max(max_radius_from_com(state, masses) for state in states)),
        "max_abs_standardized_input": max_abs_standardized_input,
    }


def _decomposition(y_hat, y_rk4, y_ref):
    e_model = y_hat - y_rk4
    e_teacher = y_rk4 - y_ref
    e_total = y_hat - y_ref
    model_term = float(np.mean(np.sum(e_model * e_model, axis=1)))
    teacher_term = float(np.mean(np.sum(e_teacher * e_teacher, axis=1)))
    total_term = float(np.mean(np.sum(e_total * e_total, axis=1)))
    cross_term = float(2.0 * np.mean(np.sum(e_model * e_teacher, axis=1)))
    return {
        "mean_sq_model_vec": model_term,
        "mean_sq_teacher_vec": teacher_term,
        "mean_sq_total_vec": total_term,
        "cross_term": cross_term,
        "identity_residual": total_term - model_term - teacher_term - cross_term,
    }


def _plots(figdir, dataset, one_step_rows, rollout_series, cfg):
    figdir.mkdir(parents=True, exist_ok=True)
    teacher_difference = np.sqrt(
        np.mean((dataset.y_rk4 - dataset.y_ref) ** 2, axis=1)
    )
    fig, ax = plt.subplots()
    ax.plot(dataset.phase_time / cfg.T_pub, teacher_difference)
    ax.set_xlabel("phase / T_pub")
    ax.set_ylabel("teacher RMSE per sample")
    fig.tight_layout()
    fig.savefig(figdir / "teacher_difference_by_phase.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots()
    labels = [f"{row['teacher']}-s{row['seed']}" for row in one_step_rows]
    x = np.arange(len(labels))
    ax.bar(x, [row["rmse_own_teacher"] for row in one_step_rows], label="own teacher")
    ax.scatter(x, [row["rmse_vs_ref"] for row in one_step_rows], label="vs ref")
    ax.set_xticks(x, labels, rotation=45, ha="right")
    ax.set_yscale("log")
    ax.legend()
    fig.tight_layout()
    fig.savefig(figdir / "one_step_own_vs_ref.png", dpi=160)
    plt.close(fig)

    for use_case, filename in (
        ("MU1", "mu1_rollout_position_error.png"),
        ("MU2", "mu2_rollout_position_error.png"),
    ):
        fig, ax = plt.subplots()
        for row in rollout_series:
            if row["use_case"] == use_case:
                ax.semilogy(
                    np.arange(len(row["pos_error"])) / 50.0,
                    row["pos_error"],
                    label=f"{row['teacher']}-s{row['seed']}",
                )
        ax.set_xlabel("nominal periods")
        ax.set_ylabel("normalized RMS position error")
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(figdir / filename, dpi=160)
        plt.close(fig)

    fig, ax = plt.subplots()
    for row in rollout_series:
        if row["use_case"] == "MU2":
            ax.plot(
                np.arange(len(row["energy_error"])) / 50.0,
                row["energy_error"],
                label=f"{row['teacher']}-s{row['seed']}",
            )
    ax.set_xlabel("nominal periods")
    ax.set_ylabel("relative energy error")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(figdir / "mu2_energy_error.png", dpi=160)
    plt.close(fig)


def run(output_dir: Path, smoke: bool = False) -> dict:
    results_dir = output_dir / "results"
    figures_dir = output_dir / "figures"
    checkpoints_dir = output_dir / "checkpoints"
    results_dir.mkdir(parents=True, exist_ok=True)
    checkpoints_dir.mkdir(parents=True, exist_ok=True)

    n = 60 if smoke else 1000
    max_epochs = 20 if smoke else 5000
    patience = 5 if smoke else 500
    seeds = [0] if smoke else [0, 1, 2]

    dataset = generate_dataset(n)
    mu, sigma = training_scaler(dataset)
    np.savez_compressed(
        results_dir / "dataset.npz",
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
    tight_rollout = integrate_reference(
        x0, rollout_times, cfg.masses_array(), cfg.G, 1e-13, 1e-15
    ).states

    one_step_rows = []
    training_rows = []
    rollout_rows = []
    paired_rows = []
    rollout_series = []
    test_mask = dataset.split == "test"

    for seed in seeds:
        ref_model, rk4_model = paired_models(seed)
        initial_parameters_equal = all(
            np.array_equal(a.detach().numpy(), b.detach().numpy())
            for a, b in zip(ref_model.parameters(), rk4_model.parameters())
        )
        ref_history, ref_epochs = train_model(
            ref_model,
            dataset.x,
            dataset.delta_ref,
            dataset.split,
            mu,
            sigma,
            max_epochs=max_epochs,
            patience=patience,
        )
        rk4_history, rk4_epochs = train_model(
            rk4_model,
            dataset.x,
            dataset.delta_rk4,
            dataset.split,
            mu,
            sigma,
            max_epochs=max_epochs,
            patience=patience,
        )
        torch.save(ref_model.state_dict(), checkpoints_dir / f"ref_seed{seed}.pt")
        torch.save(rk4_model.state_dict(), checkpoints_dir / f"rk4_seed{seed}.pt")

        for teacher, history in (("ref", ref_history), ("rk4", rk4_history)):
            for epoch, (train_mse, validation_mse) in enumerate(history, start=1):
                training_rows.append(
                    {
                        "seed": seed,
                        "teacher": teacher,
                        "epoch": epoch,
                        "train_mse": float(train_mse),
                        "validation_mse": float(validation_mse),
                    }
                )

        y_hat_ref = predict_next(ref_model, dataset.x[test_mask], mu, sigma)
        y_hat_rk4 = predict_next(rk4_model, dataset.x[test_mask], mu, sigma)
        paired_rows.append(
            {
                "seed": seed,
                "paired_initialization": initial_parameters_equal,
                **_decomposition(
                    y_hat_rk4,
                    dataset.y_rk4[test_mask],
                    dataset.y_ref[test_mask],
                ),
            }
        )

        for teacher, model, epochs, prediction, own_teacher in (
            ("ref", ref_model, ref_epochs, y_hat_ref, dataset.y_ref[test_mask]),
            ("rk4", rk4_model, rk4_epochs, y_hat_rk4, dataset.y_rk4[test_mask]),
        ):
            one_step_rows.append(
                {
                    "seed": seed,
                    "teacher": teacher,
                    "paired_initialization": initial_parameters_equal,
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
                        pos_error = _position_error(
                            states, ref_rollout[: steps + 1], x0
                        )
                        energies = np.array(
                            [total_energy(state, cfg.masses_array(), cfg.G) for state in states]
                        )
                        H0 = total_energy(x0, cfg.masses_array(), cfg.G)
                        rollout_series.append(
                            {
                                "seed": seed,
                                "teacher": teacher,
                                "use_case": use_case,
                                "pos_error": pos_error,
                                "energy_error": (energies - H0) / abs(H0),
                            }
                        )
                    rollout_rows.append(record)

    test_metrics = split_metrics["test"]
    reference_gate = bool(
        test_metrics["D_ref"] <= 0.01 * test_metrics["D_teacher"]
    )
    rollout_reference_max_position_gap = float(
        np.max(_position_error(ref_rollout, tight_rollout, x0))
    )

    if smoke:
        status = "SMOKE_ONLY"
        learner_gate = None
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

    environment = {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "torch": torch.__version__,
    }
    config = {
        "smoke": smoke,
        "N": n,
        "seeds": seeds,
        "max_epochs": max_epochs,
        "patience": patience,
        "delta_t": dt,
        "architecture": [12, 128, 128, 128, 12],
        "activation": "tanh",
        "dtype": "float64",
        "device": "cpu",
    }

    _write_json(results_dir / "config.json", config)
    _write_json(
        results_dir / "dataset_summary.json",
        {
            "N": n,
            "split_counts": {
                key: int(np.sum(dataset.split == key))
                for key in ("train", "validation", "test")
            },
            "finite": bool(
                np.all(np.isfinite(dataset.x))
                and np.all(np.isfinite(dataset.y_ref))
                and np.all(np.isfinite(dataset.y_rk4))
            ),
        },
    )
    _write_json(
        results_dir / "teacher_metrics.json",
        {
            "splits": split_metrics,
            "rollout_reference_max_position_gap": rollout_reference_max_position_gap,
        },
    )
    _write_csv(results_dir / "training_metrics.csv", training_rows)
    _write_csv(results_dir / "one_step_metrics.csv", one_step_rows)
    _write_csv(results_dir / "rollout_metrics.csv", rollout_rows)
    _write_csv(results_dir / "paired_provenance.csv", paired_rows)

    summary = {
        "status": status,
        "reference_gate": reference_gate,
        "learner_gate": learner_gate,
        "split_metrics": split_metrics,
        "rollout_reference_max_position_gap": rollout_reference_max_position_gap,
        "environment": environment,
        "smoke": smoke,
    }
    _write_json(results_dir / "summary.json", summary)
    (results_dir / "trias_ml_audit.md").write_text(
        f"# Trias ML audit v0.1\n\nStatus: `{status}`\n\n"
        "This report records provenance structure only; scientific interpretation is deferred until the frozen full run is reviewed.\n\n"
        f"Reference gate: `{reference_gate}`.\n",
        encoding="utf-8",
    )

    if not smoke:
        _plots(figures_dir, dataset, one_step_rows, rollout_series, cfg)

    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("ml_run_v0_1"))
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    run(args.output_dir, smoke=args.smoke)


if __name__ == "__main__":
    main()
