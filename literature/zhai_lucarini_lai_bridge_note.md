# Literature Note — Zhai, Lucarini & Lai and the inverse Trias edge

**Status:** SOURCE-VERIFIED LITERATURE NOTE / PROJECT INTERPRETATION SEPARATED  
**Stand:** 2026-09-02

## Primary source

Zheng-Meng Zhai, Valerio Lucarini, Ying-Cheng Lai, **“Deficiency of equation-finding approach to data-driven modeling of dynamical systems,”** arXiv:2509.03769, first submitted 2025. Current arXiv text accessed 2026-09-02.

## Source-supported findings

The paper studies data-driven governing-equation discovery for chaotic systems under imperfect observations. Its explicit pipeline includes randomly missing observations, machine-learning-based reconstruction/imputation, sparse optimization/equation discovery, forward simulation of the recovered equations, and Koopman/statistical comparison.

The paper reports that different observation/missingness realizations can lead to substantially different inferred equation sets, including additional/missing terms and strongly changed coefficients. For Lorenz, example equation sets differ markedly from the ground-truth algebraic form.

Despite this structural difference, the resulting systems can produce very similar chaotic attractors according to the paper's diagnostics, including Lyapunov exponents, KL-based attractor comparison, and a substantial agreement of leading Koopman eigenvalues. Differences appear more strongly in subdominant Koopman structure. The authors further analyze local velocity-field discrepancies and report predominantly small mismatch with intermittent larger deviations.

The authors therefore warn that physical interpretation of a single inferred equation set can be misleading when the recovered equations depend strongly on the measurement/reconstruction procedure.

## Important scope limits

The source does **not** establish that all equation-discovery methods are generally non-identifiable, nor that all alternative equation sets are physically equivalent. It studies particular chaotic systems, observation corruption/reconstruction procedures and sparse equation-discovery settings.

The paper's suggestion that direct machine-learning approaches may in some contexts be more useful than equation finding is the authors' methodological conclusion; the Trias project does not adopt it automatically.

The paper also does not establish that its phenomenon is identical to classical structural identifiability. The connection to identifiability/equifinality is a comparative question for our project.

## Project interpretation

The paper naturally occupies the inverse direction of the current Trias:

```text
R -> C_observation/preprocessing -> data -> C_inference -> T_hat
```

whereas Sundman and the Figure-eight solver demonstrator primarily stress the forward direction:

```text
T -> C_forward -> R_hat
```

The project-level synthesis is therefore:

```text
forward: same T need not imply the same operational profile
inverse: similar operational/dynamical adequacy need not imply unique T
```

This synthesis is ours; it is not a claim made by Zhai, Lucarini & Lai.

## Comparator literature that must be audited before novelty claims

The bridge overlaps established fields:

1. **Structural identifiability** — whether parameters/model structure are theoretically uniquely recoverable from idealized input-output information.
2. **Practical identifiability** — recoverability under finite/noisy/incomplete experiments.
3. **Observability** — recoverability of internal state from outputs.
4. **Equifinality / observational equivalence** — multiple models or parameterizations producing acceptably similar observed behavior.

Useful starting anchors:

- Heinrich et al. (2025), *On structural and practical identifiability: Current status and update of results*.
- Villaverde (2019), *Observability and Structural Identifiability of Nonlinear Biological Systems*.
- Cobelli & DiStefano (1980), review of parameter and structural identifiability.
- Beven & Freer (2001), equifinality in mechanistic environmental modelling.
- classical system-identification literature on structural identifiability and near-identifiability.

## Novelty risk

A claim of the form “different data can imply non-unique equations” is not sufficient novelty. The only promising Trias-specific contribution is the possible integration of inverse identifiability with forward operationalization and scientific-use auditing in one directed provenance framework.

## Immediate evidence task

Before C07-L can be accepted:

1. map every clause of C07-L to the primary paper or mark it as project inference;
2. distinguish structural identifiability, practical identifiability, observational equivalence and the Zhai–Lucarini–Lai phenomenon;
3. test whether a directed `R -> C -> T` plus `T -> C -> R_hat` audit adds any diagnostic content beyond established system-identification/credibility language;
4. only then design a minimal replication/demonstrator.