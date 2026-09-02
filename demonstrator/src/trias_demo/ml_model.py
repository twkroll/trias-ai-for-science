from __future__ import annotations

from copy import deepcopy

import numpy as np
import torch
from torch import nn


class ResidualMLP(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(12, 128),
            nn.Tanh(),
            nn.Linear(128, 128),
            nn.Tanh(),
            nn.Linear(128, 128),
            nn.Tanh(),
            nn.Linear(128, 12),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def init_model(seed: int) -> ResidualMLP:
    torch.manual_seed(seed)
    model = ResidualMLP().double()
    gain = nn.init.calculate_gain("tanh")
    for module in model.modules():
        if isinstance(module, nn.Linear):
            nn.init.xavier_uniform_(module.weight, gain=gain)
            nn.init.zeros_(module.bias)
    return model


def paired_models(seed: int) -> tuple[ResidualMLP, ResidualMLP]:
    reference_model = init_model(seed)
    rk4_model = ResidualMLP().double()
    rk4_model.load_state_dict(deepcopy(reference_model.state_dict()))
    return reference_model, rk4_model


def train_model(
    model: ResidualMLP,
    x: np.ndarray,
    delta: np.ndarray,
    split: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    max_epochs: int = 5000,
    patience: int = 500,
    min_delta: float = 1e-10,
    learning_rate: float = 1e-3,
) -> tuple[np.ndarray, int]:
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)

    x_norm = (x - mu) / sigma
    xt = torch.tensor(x_norm, dtype=torch.float64)
    yt = torch.tensor(delta, dtype=torch.float64)
    train_idx = np.where(split == "train")[0]
    validation_idx = np.where(split == "validation")[0]

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=learning_rate,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=0.0,
    )

    best_validation = float("inf")
    best_state = None
    stale = 0
    history: list[tuple[float, float]] = []

    for epoch in range(max_epochs):
        model.train()
        optimizer.zero_grad()
        prediction = model(xt[train_idx])
        loss = torch.mean((prediction - yt[train_idx]) ** 2)
        if not torch.isfinite(loss):
            raise FloatingPointError("non-finite training loss")
        loss.backward()
        optimizer.step()

        model.eval()
        with torch.no_grad():
            validation_loss = float(
                torch.mean((model(xt[validation_idx]) - yt[validation_idx]) ** 2)
            )
        history.append((float(loss.detach()), validation_loss))

        if validation_loss < best_validation - min_delta:
            best_validation = validation_loss
            best_state = deepcopy(model.state_dict())
            stale = 0
        else:
            stale += 1
        if stale >= patience:
            break

    if best_state is not None:
        model.load_state_dict(best_state)
    return np.asarray(history, dtype=np.float64), epoch + 1


def predict_next(
    model: ResidualMLP,
    x: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
) -> np.ndarray:
    x_array = np.asarray(x, dtype=np.float64)
    normalized = torch.tensor((x_array - mu) / sigma, dtype=torch.float64)
    model.eval()
    with torch.no_grad():
        delta = model(normalized).cpu().numpy()
    return x_array + delta
