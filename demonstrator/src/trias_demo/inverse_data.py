from __future__ import annotations

from dataclasses import dataclass
import hashlib

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline

SIGMA = 10.0
RHO = 28.0
BETA = 8.0 / 3.0
FEATURE_NAMES = ("1", "x", "y", "z", "x^2", "x*y", "x*z", "y^2", "y*z", "z^2")


def lorenz_rhs(_t: float, state: np.ndarray) -> np.ndarray:
    x, y, z = np.asarray(state, dtype=np.float64)
    return np.array(
        [SIGMA * (y - x), x * (RHO - z) - y, x * y - BETA * z],
        dtype=np.float64,
    )


def exact_vector_field(states: np.ndarray) -> np.ndarray:
    states = np.asarray(states, dtype=np.float64)
    x = states[..., 0]
    y = states[..., 1]
    z = states[..., 2]
    return np.stack(
        (SIGMA * (y - x), x * (RHO - z) - y, x * y - BETA * z),
        axis=-1,
    )


def integrate_reference(
    t_eval: np.ndarray,
    *,
    x0: tuple[float, float, float] = (1.0, 1.0, 1.0),
    rtol: float = 1e-12,
    atol: float = 1e-14,
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


def normalized_max_state_gap(primary: np.ndarray, tight: np.ndarray) -> float:
    primary = np.asarray(primary, dtype=np.float64)
    tight = np.asarray(tight, dtype=np.float64)
    denom = np.maximum(1.0, np.linalg.norm(tight, axis=1))
    gap = np.linalg.norm(primary - tight, axis=1) / denom
    return float(np.max(gap))


def generate_missing_mask(n_samples: int, n_missing: int, seed: int) -> np.ndarray:
    if n_samples < 6:
        raise ValueError("Need at least 6 samples for protected two-point boundaries.")
    allowed = np.arange(2, n_samples - 2, dtype=np.int64)
    if n_missing > allowed.size:
        raise ValueError("Requested more missing samples than allowed interior points.")
    rng = np.random.Generator(np.random.PCG64(seed))
    chosen = np.sort(rng.choice(allowed, size=n_missing, replace=False))
    mask = np.zeros(n_samples, dtype=bool)
    mask[chosen] = True
    return mask


def mask_hash(mask: np.ndarray) -> str:
    packed = np.packbits(np.asarray(mask, dtype=np.uint8))
    return hashlib.sha256(packed.tobytes()).hexdigest()


def reconstruct_states(
    t: np.ndarray,
    states: np.ndarray,
    mask: np.ndarray,
    method: str,
) -> np.ndarray:
    t = np.asarray(t, dtype=np.float64)
    states = np.asarray(states, dtype=np.float64)
    mask = np.asarray(mask, dtype=bool)
    observed = ~mask
    if states.shape != (t.size, 3):
        raise ValueError("states must have shape (N, 3)")
    if method not in {"linear", "cubic"}:
        raise ValueError("method must be 'linear' or 'cubic'")
    out = states.copy()
    for j in range(3):
        if method == "linear":
            out[mask, j] = np.interp(t[mask], t[observed], states[observed, j])
        else:
            spline = CubicSpline(
                t[observed],
                states[observed, j],
                bc_type="not-a-knot",
                extrapolate=False,
            )
            out[mask, j] = spline(t[mask])
    if not np.all(np.isfinite(out)):
        raise FloatingPointError("Reconstruction produced non-finite values.")
    out[observed] = states[observed]
    return out


def five_point_derivative(states: np.ndarray, dt: float) -> tuple[np.ndarray, np.ndarray]:
    states = np.asarray(states, dtype=np.float64)
    deriv = (
        states[:-4]
        - 8.0 * states[1:-3]
        + 8.0 * states[3:-1]
        - states[4:]
    ) / (12.0 * dt)
    idx = np.arange(2, states.shape[0] - 2, dtype=np.int64)
    return deriv, idx


def feature_library(states: np.ndarray) -> np.ndarray:
    states = np.asarray(states, dtype=np.float64)
    x, y, z = states[:, 0], states[:, 1], states[:, 2]
    return np.column_stack(
        (
            np.ones(states.shape[0]),
            x,
            y,
            z,
            x * x,
            x * y,
            x * z,
            y * y,
            y * z,
            z * z,
        )
    ).astype(np.float64)


def true_coefficient_matrix() -> np.ndarray:
    # rows = features, columns = dx, dy, dz
    c = np.zeros((10, 3), dtype=np.float64)
    c[1, 0] = -10.0
    c[2, 0] = 10.0
    c[1, 1] = 28.0
    c[2, 1] = -1.0
    c[6, 1] = -1.0
    c[3, 2] = -BETA
    c[5, 2] = 1.0
    return c


@dataclass(frozen=True)
class ReconstructionDiagnostics:
    rmse: float
    max_abs: float
    state_rmse: tuple[float, float, float]


def reconstruction_diagnostics(
    reference: np.ndarray,
    reconstructed: np.ndarray,
    mask: np.ndarray,
) -> ReconstructionDiagnostics:
    err = np.asarray(reconstructed)[mask] - np.asarray(reference)[mask]
    return ReconstructionDiagnostics(
        rmse=float(np.sqrt(np.mean(err**2))),
        max_abs=float(np.max(np.abs(err))),
        state_rmse=tuple(float(v) for v in np.sqrt(np.mean(err**2, axis=0))),
    )
