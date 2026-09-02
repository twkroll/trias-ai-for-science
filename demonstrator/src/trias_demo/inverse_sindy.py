from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .inverse_data import feature_library, true_coefficient_matrix


def _ridge_fit(theta: np.ndarray, y: np.ndarray, alpha: float) -> np.ndarray:
    gram = theta.T @ theta
    rhs = theta.T @ y
    return np.linalg.solve(gram + alpha * np.eye(gram.shape[0]), rhs)


def stlsq_fit(
    theta: np.ndarray,
    derivatives: np.ndarray,
    *,
    threshold: float = 0.05,
    ridge_alpha: float = 1e-8,
    max_iterations: int = 20,
) -> np.ndarray:
    theta = np.asarray(theta, dtype=np.float64)
    derivatives = np.asarray(derivatives, dtype=np.float64)
    n_features = theta.shape[1]
    n_outputs = derivatives.shape[1]
    coef = np.zeros((n_features, n_outputs), dtype=np.float64)
    for out in range(n_outputs):
        active = np.ones(n_features, dtype=bool)
        beta = _ridge_fit(theta, derivatives[:, out], ridge_alpha)
        for _ in range(max_iterations):
            new_active = np.abs(beta) >= threshold
            if not np.any(new_active):
                beta[:] = 0.0
                active = new_active
                break
            if np.array_equal(new_active, active):
                active = new_active
                break
            active = new_active
            beta_new = np.zeros_like(beta)
            beta_new[active] = _ridge_fit(theta[:, active], derivatives[:, out], ridge_alpha)
            beta = beta_new
        if np.any(active):
            beta_final = np.zeros_like(beta)
            beta_final[active] = _ridge_fit(theta[:, active], derivatives[:, out], ridge_alpha)
            beta = beta_final
            beta[np.abs(beta) < threshold] = 0.0
        coef[:, out] = beta
    return coef


def inferred_vector_field(states: np.ndarray, coefficients: np.ndarray) -> np.ndarray:
    return feature_library(np.asarray(states, dtype=np.float64)) @ np.asarray(coefficients, dtype=np.float64)


@dataclass(frozen=True)
class StructuralMetrics:
    precision: float
    recall: float
    spurious_terms: int
    missing_true_terms: int
    jaccard_vs_truth: float
    max_relative_coefficient_error: float
    rms_relative_coefficient_error: float


def _support(coef: np.ndarray) -> np.ndarray:
    return np.asarray(coef) != 0.0


def structural_metrics(
    coefficients: np.ndarray,
    reference_coefficients: np.ndarray | None = None,
) -> StructuralMetrics:
    true = (
        true_coefficient_matrix()
        if reference_coefficients is None
        else np.asarray(reference_coefficients)
    )
    pred_support = _support(coefficients)
    true_support = _support(true)
    tp = int(np.sum(pred_support & true_support))
    fp = int(np.sum(pred_support & ~true_support))
    fn = int(np.sum(~pred_support & true_support))
    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0
    union = int(np.sum(pred_support | true_support))
    jaccard = tp / union if union else 1.0
    rel = (
        np.abs(np.asarray(coefficients)[true_support] - true[true_support])
        / np.abs(true[true_support])
    )
    return StructuralMetrics(
        precision=float(precision),
        recall=float(recall),
        spurious_terms=fp,
        missing_true_terms=fn,
        jaccard_vs_truth=float(jaccard),
        max_relative_coefficient_error=float(np.max(rel)),
        rms_relative_coefficient_error=float(np.sqrt(np.mean(rel**2))),
    )


def support_jaccard(a: np.ndarray, b: np.ndarray) -> float:
    sa, sb = _support(a), _support(b)
    inter = int(np.sum(sa & sb))
    union = int(np.sum(sa | sb))
    return float(inter / union if union else 1.0)


def max_relative_deviation_on_true_terms(a: np.ndarray, b: np.ndarray) -> float:
    true_support = _support(true_coefficient_matrix())
    denom = np.maximum(np.abs(np.asarray(b)[true_support]), 1e-15)
    return float(
        np.max(
            np.abs(np.asarray(a)[true_support] - np.asarray(b)[true_support]) / denom
        )
    )
