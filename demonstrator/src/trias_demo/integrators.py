from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Literal

import numpy as np

from .dynamics import accelerations, join_state, minimum_pair_distance, rhs, split_state


@dataclass
class IntegrationResult:
    times: np.ndarray
    states: np.ndarray
    force_evals: int
    runtime_seconds: float
    valid: bool
    invalid_reason: str | None = None


def _validate_grid_step(times: np.ndarray, h: float) -> int:
    dt_out = float(times[1] - times[0])
    ratio = dt_out / h
    stride = int(round(ratio))
    if stride < 1 or not np.isclose(ratio, stride, rtol=0.0, atol=1e-10):
        raise ValueError("output-grid spacing must be an integer multiple of fixed step size")
    return stride


def integrate_rk4(
    state0: np.ndarray,
    times: np.ndarray,
    h: float,
    masses: np.ndarray,
    G: float,
    min_pair_distance_abort: float,
) -> IntegrationResult:
    stride = _validate_grid_step(times, h)
    n_steps = stride * (len(times) - 1)
    y = np.asarray(state0, dtype=np.float64).copy()
    out = np.empty((len(times), 12), dtype=np.float64)
    out[0] = y
    force_evals = 0
    t = float(times[0])
    out_idx = 1
    start = perf_counter()

    for step in range(1, n_steps + 1):
        k1 = rhs(t, y, masses, G)
        force_evals += 1
        k2 = rhs(t + 0.5 * h, y + 0.5 * h * k1, masses, G)
        force_evals += 1
        k3 = rhs(t + 0.5 * h, y + 0.5 * h * k2, masses, G)
        force_evals += 1
        k4 = rhs(t + h, y + h * k3, masses, G)
        force_evals += 1
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
        if minimum_pair_distance(y) < min_pair_distance_abort:
            return IntegrationResult(
                times[:out_idx],
                out[:out_idx],
                force_evals,
                perf_counter() - start,
                False,
                "minimum pair-distance guard triggered",
            )
        if step % stride == 0:
            out[out_idx] = y
            out_idx += 1
    return IntegrationResult(times, out, force_evals, perf_counter() - start, True)


def integrate_verlet(
    state0: np.ndarray,
    times: np.ndarray,
    h: float,
    masses: np.ndarray,
    G: float,
    min_pair_distance_abort: float,
) -> IntegrationResult:
    stride = _validate_grid_step(times, h)
    n_steps = stride * (len(times) - 1)
    positions, velocities = split_state(np.asarray(state0, dtype=np.float64))
    positions = positions.copy()
    velocities = velocities.copy()
    out = np.empty((len(times), 12), dtype=np.float64)
    out[0] = join_state(positions, velocities)
    acc = accelerations(positions, masses, G)
    force_evals = 1
    out_idx = 1
    start = perf_counter()

    for step in range(1, n_steps + 1):
        velocities += 0.5 * h * acc
        positions += h * velocities
        acc_new = accelerations(positions, masses, G)
        force_evals += 1
        velocities += 0.5 * h * acc_new
        acc = acc_new
        y = join_state(positions, velocities)
        if minimum_pair_distance(y) < min_pair_distance_abort:
            return IntegrationResult(
                times[:out_idx],
                out[:out_idx],
                force_evals,
                perf_counter() - start,
                False,
                "minimum pair-distance guard triggered",
            )
        if step % stride == 0:
            out[out_idx] = y
            out_idx += 1
    return IntegrationResult(times, out, force_evals, perf_counter() - start, True)


def integrate_fixed(
    method: Literal["rk4", "verlet"],
    state0: np.ndarray,
    times: np.ndarray,
    h: float,
    masses: np.ndarray,
    G: float,
    min_pair_distance_abort: float,
) -> IntegrationResult:
    if method == "rk4":
        return integrate_rk4(state0, times, h, masses, G, min_pair_distance_abort)
    if method == "verlet":
        return integrate_verlet(state0, times, h, masses, G, min_pair_distance_abort)
    raise ValueError(method)
