import numpy as np

from trias_demo.inverse_data import (
    exact_vector_field,
    feature_library,
    five_point_derivative,
    generate_missing_mask,
    reconstruct_states,
    true_coefficient_matrix,
)
from trias_demo.inverse_experiment import run_pipeline, smoke_config
from trias_demo.inverse_sindy import stlsq_fit, structural_metrics


def test_true_library_represents_lorenz_exactly():
    states = np.array(
        [[1.0, 2.0, 3.0], [-4.0, 5.0, 20.0], [7.0, -3.0, 15.0]]
    )
    recovered = feature_library(states) @ true_coefficient_matrix()
    assert np.allclose(
        recovered,
        exact_vector_field(states),
        atol=1e-13,
        rtol=1e-13,
    )


def test_mask_and_reconstruction_integrity():
    t = np.linspace(0.0, 1.0, 101)
    states = np.column_stack((np.sin(t), np.cos(t), t**2))
    mask = generate_missing_mask(len(t), 20, seed=0)
    assert mask.sum() == 20
    assert not mask[:2].any() and not mask[-2:].any()
    for method in ("linear", "cubic"):
        rec = reconstruct_states(t, states, mask, method)
        assert np.isfinite(rec).all()
        assert np.array_equal(rec[~mask], states[~mask])


def test_five_point_derivative_is_exact_for_quartic_up_to_roundoff():
    t = np.linspace(-1.0, 1.0, 101)
    dt = t[1] - t[0]
    states = np.column_stack((t**4, t**3, t**2))
    deriv, idx = five_point_derivative(states, dt)
    truth = np.column_stack((4 * t[idx] ** 3, 3 * t[idx] ** 2, 2 * t[idx]))
    assert np.allclose(deriv, truth, atol=2e-11, rtol=2e-11)


def test_stlsq_recovers_exact_lorenz_support_from_exact_vector_field():
    rng = np.random.default_rng(123)
    states = rng.normal(size=(500, 3)) * np.array([10.0, 10.0, 20.0])
    theta = feature_library(states)
    derivatives = exact_vector_field(states)
    coef = stlsq_fit(
        theta,
        derivatives,
        threshold=0.05,
        ridge_alpha=1e-8,
        max_iterations=20,
    )
    metrics = structural_metrics(coef)
    assert metrics.precision == 1.0
    assert metrics.recall == 1.0
    assert metrics.max_relative_coefficient_error < 1e-7


def test_smoke_pipeline_executes_and_pairs_masks():
    result = run_pipeline(smoke_config())
    assert result["reference"]["G1"]
    linear, cubic = result["paths"]
    assert linear["mask_hash"] == cubic["mask_hash"]
    assert linear["g2"] and cubic["g2"]
    assert np.isfinite(linear["reconstruction"]["rmse"])
    assert np.isfinite(cubic["reconstruction"]["rmse"])
