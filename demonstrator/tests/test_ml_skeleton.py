import numpy as np

from trias_demo.ml_data import generate_dataset, rmse, training_scaler
from trias_demo.ml_model import paired_models, predict_next, train_model


def test_dataset_pairing_and_reference_gate_small():
    dataset = generate_dataset(30)
    assert dataset.x.shape == (30, 12)
    assert np.all(np.isfinite(dataset.y_ref))
    assert np.all(np.isfinite(dataset.y_rk4))
    test = dataset.split == "test"
    assert rmse(dataset.y_ref_tight[test], dataset.y_ref[test]) < 0.01 * rmse(
        dataset.y_rk4[test], dataset.y_ref[test]
    )


def test_split_and_scaler_training_only():
    dataset = generate_dataset(20)
    mu, sigma = training_scaler(dataset)
    train = dataset.x[dataset.split == "train"]
    assert np.allclose(mu, train.mean(axis=0))
    assert np.all(sigma >= 1e-12)


def test_paired_initialization_is_bitwise_identical():
    reference_model, rk4_model = paired_models(1)
    for a, b in zip(reference_model.parameters(), rk4_model.parameters()):
        assert np.array_equal(a.detach().numpy(), b.detach().numpy())


def test_tiny_training_is_finite():
    dataset = generate_dataset(30)
    mu, sigma = training_scaler(dataset)
    model, _ = paired_models(0)
    history, _ = train_model(
        model,
        dataset.x,
        dataset.delta_ref,
        dataset.split,
        mu,
        sigma,
        max_epochs=3,
        patience=2,
    )
    assert np.all(np.isfinite(history))
    prediction = predict_next(model, dataset.x[dataset.split == "test"], mu, sigma)
    assert np.all(np.isfinite(prediction))
