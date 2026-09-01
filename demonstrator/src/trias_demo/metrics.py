from __future__ import annotations

import numpy as np

from .dynamics import (
    angular_momentum_z,
    center_of_mass,
    max_radius_from_com,
    minimum_pair_distance,
    split_state,
    total_energy,
    total_linear_momentum,
)


def position_scale(state0: np.ndarray) -> float:
    positions, _ = split_state(state0)
    return float(np.sqrt(np.mean(np.sum(positions**2, axis=1))))


def position_error(
    states: np.ndarray, reference_states: np.ndarray, state0: np.ndarray
) -> np.ndarray:
    scale = position_scale(state0)
    pos = states[:, :6].reshape(-1, 3, 2)
    ref = reference_states[:, :6].reshape(-1, 3, 2)
    return np.sqrt(np.mean(np.sum((pos - ref) ** 2, axis=2), axis=1)) / scale


def invariant_series(
    states: np.ndarray, masses: np.ndarray, G: float, state0: np.ndarray
) -> dict[str, np.ndarray]:
    H0 = total_energy(state0, masses, G)
    L0 = angular_momentum_z(state0, masses)
    p0, v0 = split_state(state0)
    L_scale = float(
        np.sum(
            np.asarray(masses)
            * np.linalg.norm(p0, axis=1)
            * np.linalg.norm(v0, axis=1)
        )
    )
    energies = np.array([total_energy(s, masses, G) for s in states])
    angular = np.array([angular_momentum_z(s, masses) for s in states])
    momentum = np.array(
        [np.linalg.norm(total_linear_momentum(s, masses)) for s in states]
    )
    com = np.array([np.linalg.norm(center_of_mass(s, masses)) for s in states])
    min_dist = np.array([minimum_pair_distance(s) for s in states])
    max_radius = np.array([max_radius_from_com(s, masses) for s in states])
    return {
        "energy_error": (energies - H0) / abs(H0),
        "angular_momentum_error": np.abs(angular - L0) / L_scale,
        "linear_momentum_norm": momentum,
        "center_of_mass_norm": com,
        "min_pair_distance": min_dist,
        "max_radius_from_com": max_radius,
    }


def energy_drift_slope(
    times: np.ndarray, energy_error: np.ndarray, T_pub: float
) -> float:
    x = np.asarray(times, dtype=np.float64) / T_pub
    return float(np.polyfit(x, np.asarray(energy_error, dtype=np.float64), 1)[0])


def observed_order(err_h: float, err_h2: float) -> float:
    if err_h <= 0.0 or err_h2 <= 0.0:
        return float("nan")
    return float(np.log(err_h / err_h2) / np.log(2.0))
