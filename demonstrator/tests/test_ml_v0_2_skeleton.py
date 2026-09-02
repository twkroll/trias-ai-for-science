import numpy as np

from trias_demo.ml_v0_2_data import (
    generate_dataset_v0_2,
    input_scaler,
    phase_block_split,
    scale_target,
    shared_target_scaler,
    unscale_target,
)
from trias_demo.ml_v0_2_model import (
    paired_models_v0_2,
    predict_next_v0_2,
    train_model_v0_2,
)


def test_full_split_contract():
    block, split = phase_block_split(1000)
    assert len(np.unique(block)) == 200
    assert {
        s: int(np.sum(split == s)) for s in ["train", "validation", "test"]
    } == {"train": 600, "validation": 200, "test": 200}
    for block_id in np.unique(block):
        assert len(set(split[block == block_id])) == 1


def test_shared_scaler_and_roundtrip():
    dataset, _ = generate_dataset_v0_2(100)
    mu_x, sigma_x = input_scaler(dataset)
    mu_delta, sigma_delta = shared_target_scaler(dataset)
    train = dataset.split == "train"
    shared = np.concatenate(
        (dataset.delta_ref[train], dataset.delta_rk4[train]), axis=0
    )
    assert np.allclose(mu_x, dataset.x[train].mean(axis=0))
    assert np.allclose(sigma_x, np.maximum(dataset.x[train].std(axis=0), 1e-12))
    assert np.allclose(mu_delta, shared.mean(axis=0))
    assert np.allclose(sigma_delta, np.maximum(shared.std(axis=0), 1e-12))
    roundtrip = unscale_target(
        scale_target(dataset.delta_ref, mu_delta, sigma_delta),
        mu_delta,
        sigma_delta,
    )
    assert np.max(np.abs(roundtrip - dataset.delta_ref)) < 1e-15


def test_paired_initialization_and_tiny_training():
    dataset, _ = generate_dataset_v0_2(100)
    mu_x, sigma_x = input_scaler(dataset)
    mu_delta, sigma_delta = shared_target_scaler(dataset)
    reference_model, rk4_model = paired_models_v0_2(0)
    assert all(
        np.array_equal(a.detach().numpy(), b.detach().numpy())
        for a, b in zip(reference_model.parameters(), rk4_model.parameters())
    )
    history, _ = train_model_v0_2(
        reference_model,
        dataset.x,
        dataset.delta_ref,
        dataset.split,
        mu_x,
        sigma_x,
        mu_delta,
        sigma_delta,
        max_epochs=3,
        patience=3,
    )
    prediction = predict_next_v0_2(
        reference_model,
        dataset.x[:5],
        mu_x,
        sigma_x,
        mu_delta,
        sigma_delta,
    )
    assert np.all(np.isfinite(history))
    assert np.all(np.isfinite(prediction))
