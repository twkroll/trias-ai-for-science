from __future__ import annotations
import argparse, csv, json, platform
from pathlib import Path
import numpy as np
import scipy, torch
from .config import FigureEightConfig
from .dynamics import total_energy, angular_momentum_z, minimum_pair_distance, max_radius_from_com
from .reference import integrate_reference
from .ml_data import rmse
from .ml_v0_2_data import generate_dataset_v0_2, input_scaler, shared_target_scaler, unscale_target
from .ml_v0_2_model import paired_models_v0_2, train_model_v0_2, predict_next_v0_2


def _mse(a, b):
    return float(np.mean((np.asarray(a) - np.asarray(b)) ** 2))


def _write_csv(path, rows):
    fields = sorted({k for row in rows for k in row}) if rows else ["status"]
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _decomposition(y_hat, y_rk4, y_ref):
    e_model = y_hat - y_rk4
    e_teacher = y_rk4 - y_ref
    e_total = y_hat - y_ref
    model = float(np.mean(np.sum(e_model * e_model, axis=1)))
    teacher = float(np.mean(np.sum(e_teacher * e_teacher, axis=1)))
    total = float(np.mean(np.sum(e_total * e_total, axis=1)))
    cross = float(2 * np.mean(np.sum(e_model * e_teacher, axis=1)))
    return {
        "mean_sq_model_vec": model,
        "mean_sq_teacher_vec": teacher,
        "mean_sq_total_vec": total,
        "cross_term": cross,
        "identity_residual": total - model - teacher - cross,
    }


def _position_scale(x0):
    positions = x0[:6].reshape(3, 2)
    return float(np.sqrt(np.mean(np.sum(positions * positions, axis=1))))


def _position_error(a, b, x0):
    pa = np.asarray(a)[:, :6].reshape(-1, 3, 2)
    pb = np.asarray(b)[:, :6].reshape(-1, 3, 2)
    return np.sqrt(np.mean(np.sum((pa - pb) ** 2, axis=2), axis=1)) / _position_scale(x0)


def _rollout(model, x0, steps, mu_x, sigma_x, mu_delta, sigma_delta):
    states = np.empty((steps + 1, 12), dtype=np.float64)
    states[0] = x0
    max_abs_x_norm = 0.0
    max_abs_z_delta = 0.0
    for k in range(steps):
        x_norm = (states[k] - mu_x) / sigma_x
        max_abs_x_norm = max(max_abs_x_norm, float(np.max(np.abs(x_norm))))
        xt = torch.tensor(x_norm[None, :], dtype=torch.float64)
        model.eval()
        with torch.no_grad():
            z_delta = model(xt).cpu().numpy()[0]
        max_abs_z_delta = max(max_abs_z_delta, float(np.max(np.abs(z_delta))))
        states[k + 1] = states[k] + unscale_target(z_delta, mu_delta, sigma_delta)
        if not np.all(np.isfinite(states[k + 1])):
            return states[: k + 2], False, "non-finite state", max_abs_x_norm, max_abs_z_delta
        if minimum_pair_distance(states[k + 1]) < 0.1:
            return states[: k + 2], False, "minimum pair-distance guard triggered", max_abs_x_norm, max_abs_z_delta
    return states, True, "", max_abs_x_norm, max_abs_z_delta


def _rollout_metrics(states, reference, x0, cfg, max_abs_x_norm, max_abs_z_delta):
    masses = cfg.masses_array()
    H0 = total_energy(x0, masses, cfg.G)
    L0 = angular_momentum_z(x0, masses)
    p0 = x0[:6].reshape(3, 2)
    v0 = x0[6:].reshape(3, 2)
    L_scale = float(np.sum(masses * np.linalg.norm(p0, axis=1) * np.linalg.norm(v0, axis=1)))
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
        "max_abs_standardized_input": max_abs_x_norm,
        "max_abs_standardized_target_increment": max_abs_z_delta,
    }


def run(output_dir: Path, smoke: bool = False):
    output_dir = Path(output_dir)
    results_dir = output_dir / "results"
    checkpoints_dir = output_dir / "checkpoints"
    results_dir.mkdir(parents=True, exist_ok=True)
    checkpoints_dir.mkdir(parents=True, exist_ok=True)

    n = 100 if smoke else 1000
    seeds = [0] if smoke else [0, 1, 2]
    max_epochs = 30 if smoke else 5000
    patience = 10 if smoke else 500

    dataset, block_id = generate_dataset_v0_2(n)
    mu_x, sigma_x = input_scaler(dataset)
    mu_delta, sigma_delta = shared_target_scaler(dataset)
    cfg = FigureEightConfig()
    dt = cfg.T_pub / 50

    split_metrics = {
        split_name: {
            "D_teacher": rmse(
                dataset.y_rk4[dataset.split == split_name],
                dataset.y_ref[dataset.split == split_name],
            ),
            "D_ref": rmse(
                dataset.y_ref_tight[dataset.split == split_name],
                dataset.y_ref[dataset.split == split_name],
            ),
        }
        for split_name in ["train", "validation", "test"]
    }

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
        block_id=block_id,
        split=dataset.split,
        mu_x=mu_x,
        sigma_x=sigma_x,
        mu_delta=mu_delta,
        sigma_delta=sigma_delta,
    )

    one_step_rows = []
    training_rows = []
    paired_rows = []
    rollout_rows = []
    paired_ok = True

    x0 = cfg.initial_state()
    rollout_times = np.arange(501, dtype=np.float64) * dt
    ref_rollout = integrate_reference(
        x0, rollout_times, cfg.masses_array(), cfg.G, 1e-12, 1e-14
    ).states
    tight_rollout = integrate_reference(
        x0, rollout_times, cfg.masses_array(), cfg.G, 1e-13, 1e-15
    ).states

    for seed in seeds:
        ref_model, rk4_model = paired_models_v0_2(seed)
        paired_initialization = all(
            np.array_equal(a.detach().numpy(), b.detach().numpy())
            for a, b in zip(ref_model.parameters(), rk4_model.parameters())
        )
        paired_ok &= paired_initialization

        ref_history, ref_epochs = train_model_v0_2(
            ref_model,
            dataset.x,
            dataset.delta_ref,
            dataset.split,
            mu_x,
            sigma_x,
            mu_delta,
            sigma_delta,
            max_epochs=max_epochs,
            patience=patience,
        )
        rk4_history, rk4_epochs = train_model_v0_2(
            rk4_model,
            dataset.x,
            dataset.delta_rk4,
            dataset.split,
            mu_x,
            sigma_x,
            mu_delta,
            sigma_delta,
            max_epochs=max_epochs,
            patience=patience,
        )
        torch.save(ref_model.state_dict(), checkpoints_dir / f"ref_seed{seed}.pt")
        torch.save(rk4_model.state_dict(), checkpoints_dir / f"rk4_seed{seed}.pt")

        for teacher, history in [("ref", ref_history), ("rk4", rk4_history)]:
            for epoch, (train_loss, validation_loss) in enumerate(history, 1):
                training_rows.append(
                    {
                        "seed": seed,
                        "teacher": teacher,
                        "epoch": epoch,
                        "train_loss_scaled": float(train_loss),
                        "validation_loss_scaled": float(validation_loss),
                    }
                )

        predictions = {}
        for split_name in ["train", "validation", "test"]:
            mask = dataset.split == split_name
            predictions["ref", split_name] = predict_next_v0_2(
                ref_model, dataset.x[mask], mu_x, sigma_x, mu_delta, sigma_delta
            )
            predictions["rk4", split_name] = predict_next_v0_2(
                rk4_model, dataset.x[mask], mu_x, sigma_x, mu_delta, sigma_delta
            )
            for teacher, epochs, own_teacher in [
                ("ref", ref_epochs, dataset.y_ref[mask]),
                ("rk4", rk4_epochs, dataset.y_rk4[mask]),
            ]:
                prediction = predictions[teacher, split_name]
                one_step_rows.append(
                    {
                        "seed": seed,
                        "teacher": teacher,
                        "split": split_name,
                        "epochs": epochs,
                        "rmse_own_teacher": rmse(prediction, own_teacher),
                        "rmse_vs_ref": rmse(prediction, dataset.y_ref[mask]),
                        "rmse_vs_rk4": rmse(prediction, dataset.y_rk4[mask]),
                        "mse_own_teacher": _mse(prediction, own_teacher),
                        "mse_vs_ref": _mse(prediction, dataset.y_ref[mask]),
                        "mse_vs_rk4": _mse(prediction, dataset.y_rk4[mask]),
                    }
                )

        test = dataset.split == "test"
        decomposition = _decomposition(
            predictions["rk4", "test"], dataset.y_rk4[test], dataset.y_ref[test]
        )
        decomposition.update(seed=seed, paired_initialization=paired_initialization)
        paired_rows.append(decomposition)

        if not smoke:
            for teacher, model in [("ref", ref_model), ("rk4", rk4_model)]:
                for use_case, steps in [("MU1", 50), ("MU2", 500)]:
                    states, valid, reason, max_x, max_z = _rollout(
                        model, x0, steps, mu_x, sigma_x, mu_delta, sigma_delta
                    )
                    row = {
                        "seed": seed,
                        "teacher": teacher,
                        "use_case": use_case,
                        "valid": valid,
                        "invalid_reason": reason,
                    }
                    if valid:
                        row.update(
                            _rollout_metrics(
                                states,
                                ref_rollout[: steps + 1],
                                x0,
                                cfg,
                                max_x,
                                max_z,
                            )
                        )
                    rollout_rows.append(row)

    median_test = {
        teacher: float(
            np.median(
                [
                    row["rmse_own_teacher"]
                    for row in one_step_rows
                    if row["teacher"] == teacher and row["split"] == "test"
                ]
            )
        )
        for teacher in ["ref", "rk4"]
    }
    median_train = {
        teacher: float(
            np.median(
                [
                    row["rmse_own_teacher"]
                    for row in one_step_rows
                    if row["teacher"] == teacher and row["split"] == "train"
                ]
            )
        )
        for teacher in ["ref", "rk4"]
    }
    g1_by_split = {
        split_name: bool(values["D_ref"] <= 0.01 * values["D_teacher"])
        for split_name, values in split_metrics.items()
    }
    g1 = g1_by_split["test"]
    g2 = bool(paired_ok)
    g3 = all(
        median_test[teacher] < split_metrics["test"]["D_teacher"]
        for teacher in ["ref", "rk4"]
    )
    g3a = all(
        median_train[teacher] < split_metrics["train"]["D_teacher"]
        for teacher in ["ref", "rk4"]
    )

    if smoke:
        status = "SMOKE_ONLY"
    elif not g2:
        status = "INVALID_IMPLEMENTATION"
    elif not g1:
        status = "INCONCLUSIVE_REFERENCE"
    elif not g3:
        status = "INCONCLUSIVE_LEARNER_ERROR"
    else:
        status = "GATES_PASSED_AWAITING_SCIENTIFIC_CLASSIFICATION"

    config = {
        "version": "v0.2",
        "smoke": smoke,
        "N": n,
        "seeds": seeds,
        "block_length": 5,
        "max_epochs": max_epochs,
        "patience": patience,
        "learning_rate": 1e-3,
        "delta_t": dt,
        "architecture": [12, 128, 128, 128, 12],
        "activation": "tanh",
        "dtype": "float64",
        "device": "cpu",
    }
    (results_dir / "config.json").write_text(json.dumps(config, indent=2))
    (results_dir / "dataset_summary.json").write_text(
        json.dumps(
            {
                "N": n,
                "block_count": int(len(np.unique(block_id))),
                "split_counts": {
                    split_name: int(np.sum(dataset.split == split_name))
                    for split_name in ["train", "validation", "test"]
                },
            },
            indent=2,
        )
    )
    (results_dir / "scalers.json").write_text(
        json.dumps(
            {
                "mu_x": mu_x.tolist(),
                "sigma_x": sigma_x.tolist(),
                "mu_delta": mu_delta.tolist(),
                "sigma_delta": sigma_delta.tolist(),
            },
            indent=2,
        )
    )
    (results_dir / "teacher_metrics.json").write_text(
        json.dumps(
            {
                "splits": split_metrics,
                "rollout_reference_max_position_gap": float(
                    np.max(_position_error(ref_rollout, tight_rollout, x0))
                ),
            },
            indent=2,
        )
    )
    _write_csv(results_dir / "training_metrics.csv", training_rows)
    _write_csv(results_dir / "one_step_metrics.csv", one_step_rows)
    _write_csv(results_dir / "rollout_metrics.csv", rollout_rows)
    _write_csv(results_dir / "paired_provenance.csv", paired_rows)

    gates = {
        "G1_reference_separation": g1,
        "G1_by_split": g1_by_split,
        "G2_paired_control_integrity": g2,
        "G3_learner_resolvability_test": g3,
        "G3a_train_resolvability": g3a,
        "median_test_rmse": median_test,
        "median_train_rmse": median_train,
    }
    (results_dir / "gates.json").write_text(json.dumps(gates, indent=2))
    summary = {
        "gate_status": status,
        "gates": gates,
        "teacher_metrics": split_metrics,
        "smoke": smoke,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "torch": torch.__version__,
        },
    }
    (results_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    (results_dir / "trias_ml_audit.md").write_text(
        f"# Trias ML audit v0.2\n\nGate status: `{status}`.\n\n"
        "No provenance interpretation is licensed unless G1–G3 pass.\n"
    )
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("ml_run_v0_2"))
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    run(args.output_dir, args.smoke)


if __name__ == "__main__":
    main()
