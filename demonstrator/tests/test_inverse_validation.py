import numpy as np

from trias_demo.inverse_data import true_coefficient_matrix
from trias_demo.inverse_validation import (
    integrate_inferred,
    integrate_true,
    is_dynamically_valid,
    normalized_rms_state_error,
    operational_metrics,
    passes_operational_equivalence,
)


def test_true_coefficients_forward_model_matches_lorenz_short_horizon():
    t = np.linspace(0.0, 0.2, 21)
    x0 = np.array([1.0, 1.0, 1.0])
    true = integrate_true(x0, t)
    inferred = integrate_inferred(true_coefficient_matrix(), x0, t)
    assert normalized_rms_state_error(inferred, true) < 1e-10
    metrics = operational_metrics(inferred, true)
    assert is_dynamically_valid(inferred)
    assert passes_operational_equivalence(0.0, metrics, inferred)
