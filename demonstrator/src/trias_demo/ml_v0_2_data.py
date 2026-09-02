from __future__ import annotations
from dataclasses import replace
import numpy as np
from .ml_data import MLDataset, generate_dataset


def phase_block_split(n: int) -> tuple[np.ndarray, np.ndarray]:
    if n % 25 != 0:
        raise ValueError("n must be divisible by 25")
    block_id = np.arange(n, dtype=np.int64) // 5
    mod = block_id % 5
    split = np.empty(n, dtype="<U10")
    split[np.isin(mod, [0, 1, 2])] = "train"
    split[mod == 3] = "validation"
    split[mod == 4] = "test"
    return block_id, split


def generate_dataset_v0_2(n: int = 1000) -> tuple[MLDataset, np.ndarray]:
    base = generate_dataset(n)
    block_id, split = phase_block_split(n)
    return replace(base, split=split), block_id


def input_scaler(dataset: MLDataset) -> tuple[np.ndarray, np.ndarray]:
    train = dataset.x[dataset.split == "train"]
    return train.mean(axis=0), np.maximum(train.std(axis=0), 1e-12)


def shared_target_scaler(dataset: MLDataset) -> tuple[np.ndarray, np.ndarray]:
    train = dataset.split == "train"
    shared = np.concatenate((dataset.delta_ref[train], dataset.delta_rk4[train]), axis=0)
    return shared.mean(axis=0), np.maximum(shared.std(axis=0), 1e-12)


def scale_target(delta, mu_delta, sigma_delta):
    return (np.asarray(delta) - mu_delta) / sigma_delta


def unscale_target(z, mu_delta, sigma_delta):
    return mu_delta + sigma_delta * np.asarray(z)
