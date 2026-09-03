# Section 3 — From lifecycle stages to claim-relative epistemic roles

**Status:** DRAFT v0.1 / W3  
**Stand:** 2026-09-03  
**Depends on:** D032 / P3 / C08-D-R3 / D025

> **Manuscript note:** This section introduces only the semantic machinery needed for the four AI-for-Science configurations in Section 4. It is not intended as a new formal logic of scientific inference, a scoring framework, or a replacement for V&V, provenance, assurance cases, or identifiability analysis.

## 3. From lifecycle stages to claim-relative epistemic roles

The genealogical comparison in Section 2 suggests a useful constraint on the present proposal. If target, model, and computerized realization are already familiar objects in classical model credibility, then the purpose of the present terminology cannot be to redescribe the same forward lifecycle with different labels. The useful shift, if there is one, is instead to treat `R`, `T`, and `C` as **claim-relative epistemic roles**. A role is fixed by the scientific claim currently under assessment, not by a permanent ontological classification of an artifact and not necessarily by the chronological order in which artifacts were produced.

This distinction matters because the same object can occupy different roles under different scientific claims. A simulator output can be a computational prediction in one analysis and the synthetic reference target for a surrogate in another. A symbolic equation can be a prior theory in a forward simulation and an inferred theory-level output in equation discovery. A neural network can be a predictor, a surrogate, part of a reconstruction pipeline, or an inference device. The role vocabulary therefore indexes a claim by asking three prior questions: **what is the referent of the claim, what theory-level content is actually being asserted, and what computational practice generated or operationalized the relevant result?**

### 3.1 The target role `R`

`R` denotes the target or referent relative to which a scientific claim is evaluated. For the present purpose, three target types are sufficient:

```text
R_REAL       empirical or physical target
R_SYNTHETIC  explicitly constructed or simulator-defined target
R_HYBRID     target whose relevant reference combines empirical and constructed components
```

The distinction is claim-relative rather than metaphysical. Calling a target `SYNTHETIC` does not make it epistemically inferior; it states what the evidence is directly about. A high-fidelity surrogate evaluated against a simulator can therefore be strongly supported relative to `R_SYNTHETIC`. If the scientific claim is later changed to the corresponding physical system, however, the target has changed and the evidential profile must be specified again. The central semantic rule is simple: **a change of referent is a change of claim, even when the computational model and numerical metric remain unchanged.**

This rule is what gives the equal-RMSE example in Section 4 its force. An error value measured against a simulator and the numerically identical value measured against independent physical observations need not support the same scientific proposition because the referents differ. Nothing in this claim is intended to replace established surrogate-validation or sim-to-real methodology; the point is to carry the referent explicitly into the cross-case epistemic description.

### 3.2 The theory role `T`

`T` denotes the theory-, mechanism-, structure-, or explanation-level content that is actually being claimed. It should not be identified automatically with every architectural bias, preprocessing choice, or mathematical object contained somewhere in a workflow. For the present analysis, four statuses are sufficient:

```text
PRESENT       an explicit theory/mechanism/explanation claim is part of the analysis
PARTIAL       only part of the relevant theoretical structure is asserted or available
NONE_CLAIMED  no theory-level claim is made for the stated use case
INFERRED      a candidate theory-level object is produced by computational inference
```

`NONE_CLAIMED` is especially important because it prevents a descriptive framework from turning mechanism into a hidden universal norm. A black-box predictor can be successful for a narrowly specified prediction task without being treated as deficient merely because no mechanistic interpretation is asserted. Conversely, `INFERRED` captures the situation in equation discovery in which a theory-level object is not a prior stage that computation implements, but a candidate result that computation helps produce.

The status of `T` is therefore not a ranking. It records the logical position of a theory-level claim in the scientific argument. This is also why a theory-related relation can be `NOT_APPLICABLE` for one use case and relevant for another analysis of the same computational system.

### 3.3 The computation role `C`

`C` denotes the concrete computational practice that realizes, transforms, predicts, reconstructs, or infers the object relevant to the claim. It may be a numerical solver, a learned predictor, a surrogate, a reconstruction procedure, a hybrid physics–ML system, or an equation-inference pipeline. The category is deliberately functional. `C` is not simply computer hardware or source code; it is the operative computational realization whose behavior and evidential role are at issue.

This broader functional reading permits a common description of forward and inverse workflows. In a conventional simulation, `C` may realize a prior `T`. In equation discovery, `C` may instead generate a candidate `T`. In a surrogate workflow, one computational realization can even become part of the referent for another. The role distinction survives these direction changes because it concerns what an object is doing in the claim, not where it must occur in a fixed chronology.

### 3.4 Three relations, but no three global scores

Once the roles are fixed for a claim, the three pairwise relations can be read as different evidential questions:

```text
R-T: What evidence supports the theory/mechanism/explanation claim about the target?
T-C: What evidence supports the operationalization, fidelity, tractability, or resolvability of theory-level content in computation?
C-R: What evidence supports the computational output relative to the specified target?
```

These relations are intentionally broad enough to host domain-specific facets. An `R-T` claim may concern empirical, mechanistic, explanatory, structural, or scope adequacy. A `T-C` claim may concern implementation fidelity, numerical convergence, stability, tractability, structure preservation, surrogate fidelity, or whether the computational procedure can resolve a theoretically relevant difference at all. A `C-R` claim may concern prediction, calibration, distributional agreement, transfer, robustness, or another target-relative quantity of interest.

For that reason, the Trias is not represented as a vector such as

\[
P=(0.8,0.7,0.9).
\]

Such a score would collapse distinct facets and invite comparisons that the framework is meant to keep explicit. The minimal unit is instead a claim entry of the form

```text
relation | facet | claim | evidence | use case | scope | status
```

For example, a physics-informed model could have strong evidence that a conservation constraint is implemented in the learned system (`T-C`), only partial evidence that the underlying physical approximation is adequate in the full target regime (`R-T`), and strong predictive evidence on a specified empirical holdout (`C-R`). These are not three components of one latent quality variable. They are three different statements supported by different evidence.

### 3.5 Evidence status is scoped support, not truth

For descriptive purposes, five status labels are sufficient:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

`ESTABLISHED` means that the specified claim is sufficiently supported by the documented evidence within the stated use case and scope; it does not mean universally true. `PARTIAL` marks positive but limited support, for example because only a restricted regime, subset of observables, or idealized setting has been tested. `UNCERTAIN` applies when the claim is relevant but the evidence cannot discriminate it reliably, as in a resolvability or identifiability problem. `UNTESTED` means that the claim is relevant but has not been directly assessed. `NOT_APPLICABLE` means that the relation is not part of the specified claim.

The last two categories carry significant semantic load in AI-for-Science cases. `UNTESTED` prevents strong teacher-relative performance from being silently rewritten as real-world validation. `NOT_APPLICABLE` prevents a prediction-only system from being marked down for not supporting a theory claim that was never made. In both cases, the status language distinguishes absence of evidence or absence of a claim from evidence of failure.

### 3.6 No automatic evidential transfer

A central default rule of the role profile is that evidence attached to one relation is not automatically transferred to another:

\[
A_{RT}+A_{TC}\not\Rightarrow A_{CR},
\]

\[
A_{TC}+A_{CR}\not\Rightarrow A_{RT},
\]

\[
A_{RT}+A_{CR}\not\Rightarrow A_{TC}.
\]

These expressions are not proposed as logical impossibility theorems. They encode a weaker methodological default: **a cross-relation inference requires an explicit bridge argument.** This is continuous with classical credibility practice, assurance reasoning, and provenance-aware analysis. Its role here is to prevent the compact R/T/C vocabulary from becoming a vehicle for precisely the overextension it is meant to expose.

Consider a synthetic surrogate. Strong evidence that a learned surrogate reproduces a simulator supports teacher-relative fidelity. To use that result as evidence about a physical target requires further premises: the simulator must itself be credible for the same quantity of interest and regime; the surrogate must operate within that validated domain; and the additional surrogate approximation error must be compatible with the intended tolerance. Only then can the teacher-relative result contribute conditionally to a real-target claim.

The converse direction is equally important. Strong real-world prediction by a model that contains a theoretical constraint can provide empirical support for some theory-related claims, but it does not automatically establish a unique mechanism, explanation, or symbolic structure. The relevant `R-T` facet must be named. Prediction evidence can therefore contribute to `RT_EMPIRICAL` while leaving `RT_MECHANISTIC` or `RT_STRUCTURAL` uncertain.

### 3.7 Bridge claims as explicit inferential steps

Whenever evidence is intentionally carried from one relation to another, the transfer should be represented as an explicit bridge claim. In minimal form, the bridge records

```text
source relation and claim
source evidence
target relation and claim
bridge premises
scope
status
```

For a surrogate, a bridge might state:

```text
source: surrogate reproduces simulator within epsilon
premise 1: simulator is validated for the same quantity and regime
premise 2: surrogate operates inside that validated domain
premise 3: surrogate error is small relative to the accepted simulator-to-target error budget
target: conditional support for surrogate adequacy relative to R_REAL
```

The bridge is not an additional edge in the triangle and not a new kind of scientific evidence. It is an explicit statement of the inferential work required to move from evidence about one relation to a claim about another. Established assurance-case and credibility approaches can perform analogous reasoning. The value of including the bridge here is narrower: the same representation can be used whether the workflow concerns a solver, a surrogate, a black-box predictor, a hybrid model, or an inferred theory.

### 3.8 Minimal profile and interpretive constraint

The resulting profile is therefore a ledger rather than a score. A minimal entry can be written as:

| Relation | Facet | Claim | Evidence | Use case / scope | Status |
|---|---|---|---|---|---|
| `T-C` | surrogate fidelity | learned operator reproduces simulator outputs within tolerance | held-out synthetic test | parameter domain A | `ESTABLISHED` |
| `R-T` | scope adequacy | governing model is adequate for the physical regime of interest | limited experimental comparison | low-Re regime only | `PARTIAL` |
| `C-R` | real prediction | learned operator predicts the physical target within tolerance | none yet | intended deployment regime | `UNTESTED` |

This representation makes no recommendation about whether the model should be used. It states what has been established, what remains limited, and what has not yet been tested. Its interpretive constraint is correspondingly modest: **global success labels should not carry more epistemic content than the underlying claim-relative evidence supports.**

The four configurations in Section 4 are intended as the substantive test of whether this minimal semantics does useful work. If the same rules can distinguish a prediction-only model, a synthetic surrogate, a physics-informed hybrid, and an equation-discovery workflow without adding case-specific exceptions, the role language has more than mnemonic value. If it merely renames familiar V&V distinctions without improving cross-case comparison, then the proposal should be reduced to a shorter perspective rather than treated as an independent framework.