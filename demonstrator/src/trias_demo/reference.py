from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

import numpy as np
from scipy.integrate import solve_ivp

from .dynamics import rhs


@dataclass
class ReferenceResult:
    times: np.ndarray
    states: np.ndarray
    nfev: int
    runtime_seconds: float
    rtol: float
    atol: float
    success: bool
    message: str


def integrate_reference(
    state0: np.ndarray,
    times: np.ndarray,
    masses: np.ndarray,
    G: float,
    rtol: float,
    atol: float,
) -> ReferenceResult:
    start = perf_counter()
    sol = solve_ivp(
        fun=lambda t, y: rhs(t, y, masses, G),
        t_span=(float(times[0]), float(times[-1])),
        y0=np.asarray(state0, dtype=np.float64),
        method="DOP853",
        t_eval=np.asarray(times, dtype=np.float64),
        rtol=rtol,
        atol=atol,
        dense_output=True,
    )
    runtime = perf_counter() - start
    return ReferenceResult(
        np.asarray(sol.t),
        sol.y.T,
        int(sol.nfev),
        runtime,
        rtol,
        atol,
        bool(sol.success),
        str(sol.message),
    )
