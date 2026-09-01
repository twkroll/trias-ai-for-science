import numpy as np

from trias_demo.config import FigureEightConfig
from trias_demo.dynamics import (
    accelerations,
    angular_momentum_z,
    center_of_mass,
    total_linear_momentum,
)


def test_figure_eight_initial_constraints():
    cfg = FigureEightConfig()
    state = cfg.initial_state()
    masses = cfg.masses_array()
    assert np.linalg.norm(center_of_mass(state, masses)) < 1e-14
    assert np.linalg.norm(total_linear_momentum(state, masses)) < 1e-14
    assert abs(angular_momentum_z(state, masses)) < 1e-14


def test_pair_force_antisymmetry_via_total_internal_force():
    masses = np.array([1.0, 2.0, 3.0])
    positions = np.array([[0.2, -0.3], [1.1, 0.4], [-0.7, 1.3]])
    acc = accelerations(positions, masses, G=1.0)
    total_force = np.sum(masses[:, None] * acc, axis=0)
    assert np.linalg.norm(total_force) < 1e-12
