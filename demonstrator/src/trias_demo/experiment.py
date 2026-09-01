from __future__ import annotations

import argparse
import csv
import json
import platform
from pathlib import Path
from statistics import median
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from .config import DemoConfig
from .dynamics import angular_momentum_z, center_of_mass, total_linear_momentum
from .integrators import integrate_fixed
from .metrics import energy_drift_slope, invariant_series, observed_order, position_error
from .reference import integrate_reference


def _json_dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


def _reference_pair(cfg: DemoConfig, use_case: str):
    times = cfg.output_grid(use_case)
    masses = cfg.system.masses_array()
    y0 = cfg.system.initial_state()
    G = cfg.system.G
    main = integrate_reference(
        y0, times, masses, G, cfg.reference_rtol, cfg.reference_atol
    )
    tight = integrate_reference(
        y0,
        times,
        masses,
        G,
        cfg.tight_reference_rtol,
        cfg.tight_reference_atol,
    )
    if not main.success or not tight.success:
        raise RuntimeError(f"reference failure: {main.message} / {tight.message}")
    ref_gap = position_error(main.states, tight.states, y0)
    return main, tight, ref_gap


def _run_fixed_repeated(cfg: DemoConfig, method: str, use_case: str, n: int):
    times = cfg.output_grid(use_case)
    h = cfg.system.T_pub / n
    runs = [
        integrate_fixed(
            method,
            cfg.system.initial_state(),
            times,
            h,
            cfg.system.masses_array(),
            cfg.system.G,
            cfg.min_pair_distance_abort,
        )
        for _ in range(cfg.runtime_repeats)
    ]
    result = runs[0]
    result.runtime_seconds = median(r.runtime_seconds for r in runs)
    return result


def _plot_u1_error(figdir: Path, series: list[dict[str, Any]]) -> None:
    fig, ax = plt.subplots()
    for row in series:
        ax.semilogy(
            row["times"],
            row["position_error"],
            label=f'{row["method"]} n={row["n"]}',
        )
    ax.set_xlabel("t")
    ax.set_ylabel("normalized RMS position error")
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(figdir / "u1_trajectory_error.png", dpi=160)
    plt.close(fig)


def _plot_u2_energy(figdir: Path, series: list[dict[str, Any]], T_pub: float) -> None:
    fig, ax = plt.subplots()
    for row in series:
        ax.plot(
            np.asarray(row["times"]) / T_pub,
            row["energy_error"],
            label=f'{row["method"]} n={row["n"]}',
        )
    ax.set_xlabel("nominal periods")
    ax.set_ylabel("relative energy error")
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(figdir / "u2_energy_error.png", dpi=160)
    plt.close(fig)


def _plot_cost(figdir: Path, rows: list[dict[str, Any]]) -> None:
    fig, ax = plt.subplots()
    for method in ("rk4", "verlet"):
        selected = [
            r
            for r in rows
            if r["use_case"] == "u1" and r["method"] == method and r["valid"]
        ]
        ax.loglog(
            [r["force_evals"] for r in selected],
            [r["max_position_error"] for r in selected],
            marker="o",
            label=method,
        )
    ax.set_xlabel("force/RHS evaluations")
    ax.set_ylabel("max U1 position error")
    ax.legend()
    fig.tight_layout()
    fig.savefig(figdir / "error_vs_cost.png", dpi=160)
    plt.close(fig)


def _plot_refinement(figdir: Path, rows: list[dict[str, Any]]) -> None:
    fig, ax = plt.subplots()
    for method in ("rk4", "verlet"):
        selected = [
            r
            for r in rows
            if r["use_case"] == "u1" and r["method"] == method and r["valid"]
        ]
        ax.loglog(
            [1 / r["n"] for r in selected],
            [r["final_position_error"] for r in selected],
            marker="o",
            label=method,
        )
    ax.set_xlabel("h / T_pub")
    ax.set_ylabel("E_pos(T_pub)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(figdir / "refinement_u1.png", dpi=160)
    plt.close(fig)


def _audit_text(reference_checks: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    u1 = [r for r in rows if r["use_case"] == "u1" and r["valid"]]
    u2 = [r for r in rows if r["use_case"] == "u2" and r["valid"]]
    return f"""# Trias audit — demonstrator v0.1

## Status

This file is generated from fixed numerical rules; it is not an LLM interpretation.

## Target system → theory

The run uses the frozen equal-mass planar Newtonian figure-eight target instance. Rounded published initial data are treated as a nominal target specification, not exact periodic data.

## Theory → computation

Compared operationalizations: DOP853 reference, classical RK4, and velocity-Verlet. Energy and angular momentum are tracked as theory-linked structures.

## Computation → target system

Reference uncertainty is estimated by primary-versus-tight DOP853 discrepancy. U1 reference max gap: {reference_checks['u1']['max_position_gap']:.3e}. U2 reference max gap: {reference_checks['u2']['max_position_gap']:.3e}.

## Baseline versus Trias view

U1 valid fixed-step runs: {len(u1)}. U2 valid fixed-step runs: {len(u2)}. Solver ranking is intentionally not declared here. The next research step must determine whether use-case-specific structure/refinement information changes or merely restates the baseline numerical interpretation.
"""


def run(output_dir: Path, quick: bool = False) -> None:
    cfg = DemoConfig(
        periods_u2=5 if quick else 100,
        refinements=(50, 100, 200) if quick else (50, 100, 200, 400, 800),
        runtime_repeats=1 if quick else 3,
    )
    results_dir = output_dir / "results"
    figdir = output_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figdir.mkdir(parents=True, exist_ok=True)

    y0 = cfg.system.initial_state()
    masses = cfg.system.masses_array()
    initial_checks = {
        "center_of_mass_norm": float(np.linalg.norm(center_of_mass(y0, masses))),
        "linear_momentum_norm": float(
            np.linalg.norm(total_linear_momentum(y0, masses))
        ),
        "angular_momentum_z": float(angular_momentum_z(y0, masses)),
    }

    refs = {}
    reference_checks = {}
    for use_case in ("u1", "u2"):
        main_ref, tight_ref, gap = _reference_pair(cfg, use_case)
        refs[use_case] = main_ref
        reference_checks[use_case] = {
            "max_position_gap": float(np.max(gap)),
            "final_position_gap": float(gap[-1]),
            "primary_nfev": main_ref.nfev,
            "tight_nfev": tight_ref.nfev,
            "primary_runtime_seconds": main_ref.runtime_seconds,
            "tight_runtime_seconds": tight_ref.runtime_seconds,
        }
    _json_dump(results_dir / "reference_check.json", reference_checks)

    rows = []
    u1_plot = []
    u2_plot = []
    for use_case in ("u1", "u2"):
        ref = refs[use_case]
        for method in ("rk4", "verlet"):
            for n in cfg.refinements:
                result = _run_fixed_repeated(cfg, method, use_case, n)
                row = {
                    "use_case": use_case,
                    "method": method,
                    "n": n,
                    "h": cfg.system.T_pub / n,
                    "valid": result.valid,
                    "force_evals": result.force_evals,
                    "runtime_seconds": result.runtime_seconds,
                    "invalid_reason": result.invalid_reason or "",
                }
                if result.valid:
                    pos_err = position_error(result.states, ref.states, y0)
                    inv = invariant_series(result.states, masses, cfg.system.G, y0)
                    row.update(
                        {
                            "final_position_error": float(pos_err[-1]),
                            "max_position_error": float(np.max(pos_err)),
                            "max_abs_energy_error": float(
                                np.max(np.abs(inv["energy_error"]))
                            ),
                            "final_energy_error": float(inv["energy_error"][-1]),
                            "energy_drift_slope_per_period": energy_drift_slope(
                                result.times,
                                inv["energy_error"],
                                cfg.system.T_pub,
                            ),
                            "max_angular_momentum_error": float(
                                np.max(inv["angular_momentum_error"])
                            ),
                            "max_linear_momentum_norm": float(
                                np.max(inv["linear_momentum_norm"])
                            ),
                            "max_center_of_mass_norm": float(
                                np.max(inv["center_of_mass_norm"])
                            ),
                            "min_pair_distance": float(
                                np.min(inv["min_pair_distance"])
                            ),
                            "max_radius_from_com": float(
                                np.max(inv["max_radius_from_com"])
                            ),
                        }
                    )
                    plotrow = {
                        "method": method,
                        "n": n,
                        "times": result.times,
                        "position_error": pos_err,
                        "energy_error": inv["energy_error"],
                    }
                    (u1_plot if use_case == "u1" else u2_plot).append(plotrow)
                rows.append(row)

    for method in ("rk4", "verlet"):
        mrows = [
            r
            for r in rows
            if r["use_case"] == "u1" and r["method"] == method and r["valid"]
        ]
        mrows.sort(key=lambda r: r["n"])
        for left, right in zip(mrows[:-1], mrows[1:]):
            left["observed_order_to_next"] = observed_order(
                left["final_position_error"], right["final_position_error"]
            )
        if mrows:
            mrows[-1]["observed_order_to_next"] = float("nan")

    fieldnames = sorted({k for row in rows for k in row})
    with (results_dir / "metrics.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "config": cfg.to_dict(),
        "initial_checks": initial_checks,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "quick_mode": quick,
        "run_status": "complete",
    }
    _json_dump(results_dir / "summary.json", summary)
    (results_dir / "trias_audit.md").write_text(
        _audit_text(reference_checks, rows), encoding="utf-8"
    )

    _plot_u1_error(figdir, u1_plot)
    _plot_u2_energy(figdir, u2_plot, cfg.system.T_pub)
    _plot_cost(figdir, rows)
    _plot_refinement(figdir, rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("run"))
    parser.add_argument(
        "--quick", action="store_true", help="smoke run: U2=5 periods, n up to 200"
    )
    args = parser.parse_args()
    run(args.output_dir, quick=args.quick)


if __name__ == "__main__":
    main()
