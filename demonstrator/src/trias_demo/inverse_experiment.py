from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path

import numpy as np

from .inverse_data import (
    exact_vector_field,
    feature_library,
    five_point_derivative,
    generate_missing_mask,
    integrate_reference,
    mask_hash,
    normalized_max_state_gap,
    reconstruct_states,
    reconstruction_diagnostics,
)
from .inverse_sindy import inferred_vector_field, structural_metrics, stlsq_fit


@dataclass(frozen=True)
class InverseConfig:
    dt: float = 0.01
    t_end: float = 60.0
    discovery_start: float = 10.0
    discovery_end: float = 50.0
    holdout_end: float = 60.0
    missing_count: int = 800
    mask_seeds: tuple[int, ...] = (0, 1, 2)
    threshold: float = 0.05
    ridge_alpha: float = 1e-8
    max_iterations: int = 20


def _slice_grid(
    t: np.ndarray,
    states: np.ndarray,
    lo: float,
    hi: float,
    *,
    left_closed: bool = True,
) -> tuple[np.ndarray, np.ndarray]:
    if left_closed:
        keep = (t >= lo - 1e-12) & (t <= hi + 1e-12)
    else:
        keep = (t > lo + 1e-12) & (t <= hi + 1e-12)
    return t[keep], states[keep]


def fit_path(
    t: np.ndarray,
    states: np.ndarray,
    config: InverseConfig,
) -> tuple[np.ndarray, np.ndarray]:
    derivatives, idx = five_point_derivative(states, config.dt)
    theta = feature_library(states[idx])
    coef = stlsq_fit(
        theta,
        derivatives,
        threshold=config.threshold,
        ridge_alpha=config.ridge_alpha,
        max_iterations=config.max_iterations,
    )
    return coef, idx


def vf_nrmse(states: np.ndarray, coefficients: np.ndarray) -> float:
    pred = inferred_vector_field(states, coefficients)
    true = exact_vector_field(states)
    num = np.sqrt(np.mean(np.sum((pred - true) ** 2, axis=1)))
    den = np.sqrt(np.mean(np.sum(true**2, axis=1)))
    return float(num / den)


def run_pipeline(config: InverseConfig) -> dict:
    t = np.arange(0.0, config.t_end + 0.5 * config.dt, config.dt, dtype=np.float64)
    primary = integrate_reference(t, rtol=1e-12, atol=1e-14)
    tight = integrate_reference(t, rtol=1e-13, atol=1e-15)
    ref_keep = t <= min(10.0, config.t_end) + 1e-12
    ref_gap = normalized_max_state_gap(primary[ref_keep], tight[ref_keep])
    g1 = ref_gap < 1e-8

    td, xd = _slice_grid(t, primary, config.discovery_start, config.discovery_end)
    _, xh = _slice_grid(
        t,
        primary,
        config.discovery_end,
        config.holdout_end,
        left_closed=False,
    )

    p0_coef, _ = fit_path(td, xd, config)
    p0_struct = structural_metrics(p0_coef)
    g3 = (
        p0_struct.precision == 1.0
        and p0_struct.recall == 1.0
        and p0_struct.spurious_terms == 0
        and p0_struct.missing_true_terms == 0
        and p0_struct.max_relative_coefficient_error <= 0.05
    )

    paths = []
    for seed in config.mask_seeds:
        mask = generate_missing_mask(td.size, config.missing_count, seed)
        g2 = bool(
            mask.sum() == config.missing_count
            and not np.any(mask[:2])
            and not np.any(mask[-2:])
        )
        for method in ("linear", "cubic"):
            reconstructed = reconstruct_states(td, xd, mask, method)
            coef, _ = fit_path(td, reconstructed, config)
            sm = structural_metrics(coef)
            paths.append(
                {
                    "seed": seed,
                    "method": method,
                    "mask_hash": mask_hash(mask),
                    "g2": g2,
                    "reconstruction": asdict(
                        reconstruction_diagnostics(xd, reconstructed, mask)
                    ),
                    "structural": asdict(sm),
                    "vf_nrmse_holdout": vf_nrmse(xh, coef) if xh.size else None,
                }
            )

    return {
        "config": asdict(config),
        "reference": {
            "max_normalized_gap_0_to_10": ref_gap,
            "G1": g1,
        },
        "P0": {
            "coefficients": p0_coef.tolist(),
            "structural": asdict(p0_struct),
            "G3": g3,
            "vf_nrmse_holdout": vf_nrmse(xh, p0_coef) if xh.size else None,
        },
        "paths": paths,
        "note": (
            "Smoke/skeleton output only unless run with the frozen full scientific "
            "configuration after explicit approval."
        ),
    }


def smoke_config() -> InverseConfig:
    # Deliberately shortened non-scientific pipeline check.
    return InverseConfig(
        dt=0.02,
        t_end=12.0,
        discovery_start=2.0,
        discovery_end=8.0,
        holdout_end=12.0,
        missing_count=60,
        mask_seeds=(0,),
        threshold=0.05,
        ridge_alpha=1e-8,
        max_iterations=20,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Run a shortened non-scientific pipeline check.",
    )
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    config = smoke_config() if args.smoke else InverseConfig()
    result = run_pipeline(config)
    text = json.dumps(result, indent=2)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
