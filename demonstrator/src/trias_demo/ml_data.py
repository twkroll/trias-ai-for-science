from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp

from .config import FigureEightConfig
from .dynamics import rhs


@dataclass(frozen=True)
class MLDataset:
    phase_index: np.ndarray
    phase_time: np.ndarray
    x: np.ndarray
    y_ref: np.ndarray
    y_ref_tight: np.ndarray
    y_rk4: np.ndarray
    delta_ref: np.ndarray
    delta_rk4: np.ndarray
    split: np.ndarray


def _one_ref(
    state: np.ndarray,
    dt: float,
    cfg: FigureEightConfig,
    rtol: float,
    atol: float,
) -> np.ndarray:
    sol = solve_ivp(
        lambda t, y: rhs(t, y, cfg.masses_array(), cfg.G),
        (0.0, dt),
        np.asarray(state, dtype=np.float64),
        method="DOP853",
        t_eval=[dt],
        rtol=rtol,
        atol=atol,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1]


def rk4_teacher_step(state: np.ndarray, h: float, cfg: FigureEightConfig) -> np.ndarray:
    state = np.asarray(state, dtype=np.float64)
    masses = cfg.masses_array()
    k1 = rhs(0.0, state, masses, cfg.G)
    k2 = rhs(0.5 * h, state + 0.5 * h * k1, masses, cfg.G)
    k3 = rhs(0.5 * h, state + 0.5 * h * k2, masses, cfg.G)
    k4 = rhs(h, state + h * k3, masses, cfg.G)
    return state + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


def generate_dataset(n: int = 1000) -> MLDataset:
    cfg = FigureEightConfig()
    phase_index = np.arange(n, dtype=np.int64)
    phase_time = phase_index * cfg.T_pub / n

    phase_solution = solve_ivp(
        lambda t, y: rhs(t, y, cfg.masses_array(), cfg.G),
        (0.0, cfg.T_pub),
        cfg.initial_state(),
        method="DOP853",
        t_eval=phase_time,
        rtol=1e-12,
        atol=1e-14,
    )
    if not phase_solution.success:
        raise RuntimeError(phase_solution.message)
    x = phase_solution.y.T.copy()

    dt = cfg.T_pub / 50.0
    y_ref = np.empty_like(x)
    y_ref_tight = np.empty_like(x)
    y_rk4 = np.empty_like(x)
    for j, state in enumerate(x):
        y_ref[j] = _one_ref(state, dt, cfg, 1e-12, 1e-14)
        y_ref_tight[j] = _one_ref(state, dt, cfg, 1e-13, 1e-15)
        y_rk4[j] = rk4_teacher_step(state, dt, cfg)

    split = np.full(n, "test", dtype="<U10")
    train_end = int(round(0.6 * n))
    validation_end = int(round(0.8 * n))
    split[:train_end] = "train"
    split[train_end:validation_end] = "validation"

    return MLDataset(
        phase_index=phase_index,
        phase_time=phase_time,
        x=x,
        y_ref=y_ref,
        y_ref_tight=y_ref_tight,
        y_rk4=y_rk4,
        delta_ref=y_ref - x,
        delta_rk4=y_rk4 - x,
        split=split,
    )


def training_scaler(dataset: MLDataset) -> tuple[np.ndarray, np.ndarray]:
    train = dataset.x[dataset.split == "train"]
    mu = train.mean(axis=0)
    sigma = np.maximum(train.std(axis=0), 1e-12)
    return mu, sigma


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))
