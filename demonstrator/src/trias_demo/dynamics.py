from __future__ import annotations

import numpy as np


def split_state(state: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    state = np.asarray(state, dtype=np.float64)
    if state.shape != (12,):
        raise ValueError(f"expected state shape (12,), got {state.shape}")
    return state[:6].reshape(3, 2), state[6:].reshape(3, 2)


def join_state(positions: np.ndarray, velocities: np.ndarray) -> np.ndarray:
    return np.concatenate(
        (
            np.asarray(positions, dtype=np.float64).ravel(),
            np.asarray(velocities, dtype=np.float64).ravel(),
        )
    )


def accelerations(positions: np.ndarray, masses: np.ndarray, G: float = 1.0) -> np.ndarray:
    positions = np.asarray(positions, dtype=np.float64)
    masses = np.asarray(masses, dtype=np.float64)
    if positions.shape != (3, 2) or masses.shape != (3,):
        raise ValueError("expected positions (3,2) and masses (3,)")

    acc = np.zeros_like(positions)
    for i in range(3):
        for j in range(i + 1, 3):
            delta = positions[j] - positions[i]
            r2 = float(np.dot(delta, delta))
            if r2 == 0.0:
                raise FloatingPointError("coincident bodies in unregularized model")
            inv_r3 = r2 ** -1.5
            acc[i] += G * masses[j] * delta * inv_r3
            acc[j] -= G * masses[i] * delta * inv_r3
    return acc


def rhs(_t: float, state: np.ndarray, masses: np.ndarray, G: float = 1.0) -> np.ndarray:
    positions, velocities = split_state(state)
    return join_state(velocities, accelerations(positions, masses, G))


def total_energy(state: np.ndarray, masses: np.ndarray, G: float = 1.0) -> float:
    positions, velocities = split_state(state)
    masses = np.asarray(masses, dtype=np.float64)
    kinetic = 0.5 * np.sum(masses[:, None] * velocities**2)
    potential = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            r = np.linalg.norm(positions[j] - positions[i])
            potential -= G * masses[i] * masses[j] / r
    return float(kinetic + potential)


def total_linear_momentum(state: np.ndarray, masses: np.ndarray) -> np.ndarray:
    _, velocities = split_state(state)
    return np.sum(np.asarray(masses)[:, None] * velocities, axis=0)


def center_of_mass(state: np.ndarray, masses: np.ndarray) -> np.ndarray:
    positions, _ = split_state(state)
    masses = np.asarray(masses, dtype=np.float64)
    return np.sum(masses[:, None] * positions, axis=0) / np.sum(masses)


def angular_momentum_z(state: np.ndarray, masses: np.ndarray) -> float:
    positions, velocities = split_state(state)
    masses = np.asarray(masses, dtype=np.float64)
    return float(
        np.sum(
            masses
            * (
                positions[:, 0] * velocities[:, 1]
                - positions[:, 1] * velocities[:, 0]
            )
        )
    )


def minimum_pair_distance(state: np.ndarray) -> float:
    positions, _ = split_state(state)
    return float(
        min(
            np.linalg.norm(positions[j] - positions[i])
            for i in range(3)
            for j in range(i + 1, 3)
        )
    )


def max_radius_from_com(state: np.ndarray, masses: np.ndarray) -> float:
    positions, _ = split_state(state)
    com = center_of_mass(state, masses)
    return float(np.max(np.linalg.norm(positions - com, axis=1)))
