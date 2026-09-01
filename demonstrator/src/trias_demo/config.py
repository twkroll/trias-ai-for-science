from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

import numpy as np


@dataclass(frozen=True)
class FigureEightConfig:
    G: float = 1.0
    masses: tuple[float, float, float] = (1.0, 1.0, 1.0)
    positions: tuple[tuple[float, float], ...] = (
        (0.97000436, -0.24308753),
        (-0.97000436, 0.24308753),
        (0.0, 0.0),
    )
    velocities: tuple[tuple[float, float], ...] = (
        (0.466203685, 0.43236573),
        (0.466203685, 0.43236573),
        (-0.93240737, -0.86473146),
    )
    T_pub: float = 6.32591398

    def masses_array(self) -> np.ndarray:
        return np.asarray(self.masses, dtype=np.float64)

    def positions_array(self) -> np.ndarray:
        return np.asarray(self.positions, dtype=np.float64)

    def velocities_array(self) -> np.ndarray:
        return np.asarray(self.velocities, dtype=np.float64)

    def initial_state(self) -> np.ndarray:
        return np.concatenate((self.positions_array().ravel(), self.velocities_array().ravel()))


@dataclass(frozen=True)
class DemoConfig:
    system: FigureEightConfig = field(default_factory=FigureEightConfig)
    periods_u1: int = 1
    periods_u2: int = 100
    output_points_per_period: int = 50
    refinements: tuple[int, ...] = (50, 100, 200, 400, 800)
    reference_rtol: float = 1e-12
    reference_atol: float = 1e-14
    tight_reference_rtol: float = 1e-13
    tight_reference_atol: float = 1e-15
    min_pair_distance_abort: float = 0.1
    runtime_repeats: int = 3

    @property
    def dt_out(self) -> float:
        return self.system.T_pub / self.output_points_per_period

    def horizon(self, use_case: str) -> float:
        if use_case == "u1":
            return self.periods_u1 * self.system.T_pub
        if use_case == "u2":
            return self.periods_u2 * self.system.T_pub
        raise ValueError(f"unknown use case: {use_case}")

    def output_grid(self, use_case: str) -> np.ndarray:
        periods = self.periods_u1 if use_case == "u1" else self.periods_u2
        n_intervals = periods * self.output_points_per_period
        return np.linspace(0.0, self.horizon(use_case), n_intervals + 1, dtype=np.float64)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
