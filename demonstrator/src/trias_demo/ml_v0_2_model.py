from __future__ import annotations
from copy import deepcopy
import numpy as np
import torch
from .ml_model import ResidualMLP
from .ml_v0_2_data import scale_target, unscale_target


def paired_models_v0_2(seed: int) -> tuple[ResidualMLP, ResidualMLP]:
    torch.manual_seed(seed)
    reference_model = ResidualMLP().double()
    gain = torch.nn.init.calculate_gain("tanh")
    for module in reference_model.modules():
        if isinstance(module, torch.nn.Linear):
            torch.nn.init.xavier_uniform_(module.weight, gain=gain)
            torch.nn.init.zeros_(module.bias)
    rk4_model = ResidualMLP().double()
    rk4_model.load_state_dict(deepcopy(reference_model.state_dict()))
    return reference_model, rk4_model


def train_model_v0_2(
    model,
    x,
    delta,
    split,
    mu_x,
    sigma_x,
    mu_delta,
    sigma_delta,
    max_epochs=5000,
    patience=500,
    min_delta=1e-10,
    learning_rate=1e-3,
):
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    xt = torch.tensor((x - mu_x) / sigma_x, dtype=torch.float64)
    yt = torch.tensor(scale_target(delta, mu_delta, sigma_delta), dtype=torch.float64)
    train_idx = np.where(split == "train")[0]
    val_idx = np.where(split == "validation")[0]
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
    history = []
    for epoch in range(max_epochs):
        model.train()
        optimizer.zero_grad()
        loss = torch.mean((model(xt[train_idx]) - yt[train_idx]) ** 2)
        if not torch.isfinite(loss):
            raise FloatingPointError("non-finite training loss")
        loss.backward()
        optimizer.step()
        model.eval()
        with torch.no_grad():
            validation_loss = float(torch.mean((model(xt[val_idx]) - yt[val_idx]) ** 2))
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


def predict_next_v0_2(model, x, mu_x, sigma_x, mu_delta, sigma_delta):
    x = np.asarray(x, dtype=np.float64)
    xt = torch.tensor((x - mu_x) / sigma_x, dtype=torch.float64)
    model.eval()
    with torch.no_grad():
        z = model(xt).cpu().numpy()
    return x + unscale_target(z, mu_delta, sigma_delta)
