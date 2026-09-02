from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import wasserstein_distance

from .inverse_data import lorenz_rhs
from .inverse_sindy import inferred_vector_field


def integrate_inferred(
    coefficients: np.ndarray,
    x0: np.ndarray,
    t_eval: np.ndarray,
    *,
    rtol: float = 1e-10,
    atol: float = 1e-12,
) -> np.ndarray:
    coefficients = np.asarray(coefficients, dtype=np.float64)
    t_eval = np.asarray(t_eval, dtype=np.float64)

    def rhs(_t: float, state: np.ndarray) -> np.ndarray:
        return inferred_vector_field(
            np.asarray(state, dtype=np.float64)[None, :], coefficients
        )[0]

    sol = solve_ivp(
        rhs,
        (float(t_eval[0]), float(t_eval[-1])),
        np.asarray(x0, dtype=np.float64),
        method="DOP853",
        t_eval=t_eval,
        rtol=rtol,
        atol=atol,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return np.asarray(sol.y.T, dtype=np.float64)


def integrate_true(
    x0: np.ndarray,
    t_eval: np.ndarray,
    *,
    rtol: float = 1e-10,
    atol: float = 1e-12,
) -> np.ndarray:
    t_eval = np.asarray(t_eval, dtype=np.float64)
    sol = solve_ivp(
        lorenz_rhs,
        (float(t_eval[0]), float(t_eval[-1])),
        np.asarray(x0, dtype=np.float64),
        method="DOP853",
        t_eval=t_eval,
        rtol=rtol,
        atol=atol,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return np.asarray(sol.y.T, dtype=np.float64)


def normalized_rms_state_error(pred: np.ndarray, ref: np.ndarray) -> float:
    pred = np.asarray(pred, dtype=np.float64)
    ref = np.asarray(ref, dtype=np.float64)
    num = np.sqrt(np.mean(np.sum((pred - ref) ** 2, axis=1)))
    den = np.sqrt(np.mean(np.sum(ref**2, axis=1)))
    return float(num / max(den, 1e-15))


@dataclass(frozen=True)
class LongTimeStats:
    mean: tuple[float, float, float]
    std: tuple[float, float, float]
    corr: tuple[tuple[float, float, float], ...]


def long_time_stats(states: np.ndarray) -> LongTimeStats:
    states = np.asarray(states, dtype=np.float64)
    return LongTimeStats(
        mean=tuple(float(v) for v in np.mean(states, axis=0)),
        std=tuple(float(v) for v in np.std(states, axis=0)),
        corr=tuple(
            tuple(float(v) for v in row) for row in np.corrcoef(states.T)
        ),
    )


def operational_metrics(
    model_states: np.ndarray,
    reference_states: np.ndarray,
) -> dict:
    model_states = np.asarray(model_states, dtype=np.float64)
    reference_states = np.asarray(reference_states, dtype=np.float64)
    model_stats = long_time_stats(model_states)
    reference_stats = long_time_stats(reference_states)
    ref_std = np.maximum(np.asarray(reference_stats.std), 1e-15)
    mean_scaled = (
        np.abs(np.asarray(model_stats.mean) - np.asarray(reference_stats.mean)) / ref_std
    )
    std_scaled = (
        np.abs(np.asarray(model_stats.std) - np.asarray(reference_stats.std)) / ref_std
    )
    corr_delta = np.asarray(model_stats.corr) - np.asarray(reference_stats.corr)
    w1_scaled = np.array(
        [
            wasserstein_distance(model_states[:, j], reference_states[:, j])
            / ref_std[j]
            for j in range(3)
        ]
    )
    return {
        "mean_scaled_max": float(np.max(mean_scaled)),
        "std_scaled_max": float(np.max(std_scaled)),
        "corr_frobenius": float(np.linalg.norm(corr_delta, ord="fro")),
        "wasserstein_scaled_max": float(np.max(w1_scaled)),
        "model_stats": model_stats,
        "reference_stats": reference_stats,
    }


def is_dynamically_valid(states: np.ndarray) -> bool:
    states = np.asarray(states, dtype=np.float64)
    return bool(
        np.all(np.isfinite(states))
        and np.max(np.linalg.norm(states, axis=1)) < 100.0
    )


def passes_operational_equivalence(
    vf_nrmse: float,
    metrics: dict,
    states: np.ndarray,
) -> bool:
    return bool(
        is_dynamically_valid(states)
        and vf_nrmse <= 0.20
        and metrics["mean_scaled_max"] <= 0.25
        and metrics["std_scaled_max"] <= 0.20
        and metrics["corr_frobenius"] <= 0.30
        and metrics["wasserstein_scaled_max"] <= 0.25
    )
