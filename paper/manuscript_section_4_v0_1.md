# Section 4 — Four AI-for-Science Role Configurations

**Status:** DRAFT v0.1 / W1 SURVIVAL TEST  
**Stand:** 2026-09-03  
**Depends on:** D030 / P3 / C08-D-R3

> **Manuscript note:** This is intended as near-manuscript prose. Author–year citations are placeholders for the final bibliography. No claim in this section should be read as asserting that the individual AI practices discussed below are novel.

## 4. Four AI-for-Science role configurations

The usefulness of treating target, theory, and computation as claim-relative epistemic roles becomes clearest when the role of computation changes across scientific workflows. In a classical forward simulation, a conceptual or mathematical model is typically specified first and then realized computationally. Contemporary AI-for-Science workflows are less uniform. A learned system may be used only to predict observations, it may emulate a simulator, it may combine theoretical constraints with data, or it may participate in the inference of a scientific model itself. None of these practices is new as such. The point of the present analysis is narrower: the evidential meaning of a successful computational result depends on which role the computation occupies, which target is taken as the relevant referent, and which scientific claim is being evaluated.

We therefore use the same minimal vocabulary throughout the four cases. `R` denotes the claim-relative target or referent, which may be real, synthetic, or hybrid. `T` denotes the theory-, mechanism-, or explanation-level content that is actually being claimed; for some purposes no such claim is made. `C` denotes the concrete computational practice. The three pairwise relations are then read as questions about target–theory adequacy (`R–T`), theory–computation fidelity or operationalization (`T–C`), and computation–target adequacy (`C–R`). These labels do not assign a global score to a model. They localize what a given piece of evidence does, and does not, directly support.

### 4.1 Predictive black-box systems: useful computation without an explicit theory claim

Consider first a predictive model trained on observations from a real target system. The narrow scientific goal may be entirely predictive: given measurements or covariates, estimate a future state, a material property, or an experimentally relevant quantity. In that use case, a schematic workflow is

\[
R_{\mathrm{real}} \rightarrow D \rightarrow C_{\mathrm{pred}},
\]

with no explicit mechanistic or explanatory theory claim required for the prediction task. We denote this situation by

\[
T = \mathrm{NONE\_CLAIMED}
\]

for the specified use case. This notation does not imply that the model is theory-free in every possible sense, nor that background knowledge played no role in data collection, architecture selection, or interpretation. It means only that the scientific claim under assessment is not a claim that the learned representation constitutes the mechanism or explanation of the target system.

Suppose such a model is evaluated prospectively or on representative held-out observations and achieves sufficiently accurate predictions for the stated purpose. The immediate evidential achievement is then naturally located on the `C–R` relation: the computational practice produces outputs that agree with the chosen real-world target quantity in the stated regime. This can be a substantial scientific success. It need not be downgraded because an `R–T` mechanistic claim is absent. Indeed, philosophical and methodological discussions of machine learning already distinguish prediction from explanation, discovery, understanding, and other epistemic goals. Naser's P.E.D.U.D. framework explicitly treats prediction, explanation, discovery, understanding, and decision-making as distinct epistemic functions, while Vinuesa et al. discuss scientific uses of machine learning under different degrees of prior theoretical knowledge (Naser, 2025; Vinuesa et al., 2026).

The Trias reading adds no new category of predictive success. Its role is to prevent the success from being silently widened. Strong evidence for

\[
C_{\mathrm{pred}} \leftrightarrow R_{\mathrm{real}}
\]

with respect to a prediction claim is not, without further argument, evidence that a particular mechanistic or explanatory `T` has been established. Conversely, the absence of such a `T` claim is not evidence against the predictive use. In the ledger terminology, `CR_PREDICTION` may be `ESTABLISHED` within a defined scope, while theory-related entries can be `NOT_APPLICABLE` for that narrow claim rather than `FAILED`. This is a small but important descriptive distinction: “the model works” can mean “it predicts the target quantity adequately,” without carrying an implicit commitment to “it reveals how the target system works.”

The case therefore illustrates the first benefit of role-relative profiling. It separates epistemic incompleteness from epistemic failure. A model can be deliberately successful on one relation without being defective for not satisfying a claim that was never made.

### 4.2 Synthetic surrogates: the referent changes while the metric may not

A second configuration arises when machine learning is used to emulate a numerical simulator or other synthetic teacher. A typical workflow is

\[
T \rightarrow C_{\mathrm{sim}} \rightarrow D_{\mathrm{syn}} \rightarrow C_{\mathrm{surr}}.
\]

Here a governing model or simulator generates synthetic examples, and a surrogate is trained to reproduce the simulator more cheaply or at larger scale. Surrogates, reduced-order models, and learned operators of this kind are standard tools in scientific machine learning. Contemporary SciML verification-and-validation work already emphasizes that model purpose, verification, validation data, data processing, uncertainty, and the domain of intended application must be distinguished (Jakeman et al., 2026). The Trias does not introduce the sim-to-real problem or the distinction between emulator fidelity and empirical validation.

What the role notation makes explicit is that the referent of the performance metric is part of its epistemic content. Let a surrogate achieve

\[
\mathrm{RMSE}_{\mathrm{teacher}} = \varepsilon
\]

on held-out simulator outputs. This is direct evidence that the surrogate reproduces the teacher within the tested synthetic domain. Depending on how the target is fixed, this can be represented either as `TC_SURROGATE` fidelity to the computational realization of `T`, or as `C–R` adequacy relative to an explicitly synthetic target `R_{\mathrm{syn}}`. In either description, the referent is the simulator-defined system.

Now imagine an otherwise similar model with

\[
\mathrm{RMSE}_{\mathrm{real}} = \varepsilon
\]

on independent observations of the physical target. The numerical value is identical, yet the evidential claim is different. The second result directly concerns `C–R_{\mathrm{real}}`; the first does not. The equality of the error metric does not erase the difference between the referents.

This distinction matters particularly in multi-level AI-for-Science pipelines. A surrogate can be an excellent approximation of a simulator even when the simulator is imperfect for the intended real system. Conversely, a simulator may be well validated for a narrowly defined quantity and regime, in which case surrogate-to-simulator fidelity can contribute to a real-target claim, but only through an additional bridge argument. Schematically,

\[
\text{surrogate fidelity to simulator}
+
\text{simulator credibility for the same quantity and regime}
+
\text{controlled surrogate error}
\Rightarrow
\text{conditional support for a real-target claim}.
\]

The implication is conditional rather than automatic. It requires the simulator's validation scope to match the surrogate use, the relevant quantities of interest to coincide, and the surrogate error to be sufficiently controlled relative to the simulator-to-reality uncertainty. These requirements are fully compatible with established V&V and credibility practice. The descriptive contribution is to encode the change of referent directly in the epistemic profile: `R_syn` and `R_real` are not interchangeable targets merely because the same metric is used.

The surrogate case therefore sharpens a second sense in which the phrase “the model works” is incomplete. It must be supplemented by “relative to what?” A high-fidelity emulator and an empirically validated predictor may have equally impressive error statistics while supporting different scientific claims.

### 4.3 Physics-informed and hybrid machine learning: one label, several relations

Physics-informed and theory-guided machine learning combine data-driven optimization with mathematical or physical structure. The literature encompasses many distinct strategies, including constraints derived from differential equations, conservation laws, symmetries, constitutive relations, and combinations of data with partial mechanistic knowledge (Karniadakis et al., 2021). Recent perspectives similarly organize scientific machine learning by the degree of prior knowledge available about governing dynamics (Vinuesa et al., 2026). The existence and usefulness of hybrid physics–ML approaches are therefore not at issue.

The epistemic difficulty is that the label “physics-informed” can compress several logically different questions. A schematic hybrid workflow may be written as

\[
T + D(R) \rightarrow C_{\mathrm{hybrid}}.
\]

At least three claims can then be separated.

First, does the computational system actually implement or satisfy the theoretical constraint that it is claimed to use? A small PDE residual, preservation of a specified invariant, or successful verification against a known limiting case can support a `T–C` claim. This is a question about theory–computation fidelity: whether the relevant theoretical structure is correctly represented or enforced in the computational realization.

Second, is the embedded theory itself adequate for the real target and regime? A perfectly enforced physical constraint may still be an approximation with a restricted domain of validity. Idealizations, missing physics, closure assumptions, parameter uncertainty, or regime changes belong to the `R–T` relation. Satisfaction of the constraint in `C` does not by itself establish that the constraint is an adequate description of `R` for the intended scientific claim.

Third, does the resulting hybrid model perform adequately against the target quantity of interest? Comparison with independent observations, prospective prediction, calibration, or other target-specific validation supports a `C–R` claim. A model can therefore be strongly physics-consistent yet empirically inadequate, empirically accurate while only partially satisfying the encoded theory, or strong on both relations within a restricted scope.

This decomposition is deliberately non-normative. It does not imply that a model should maximize all three relations, nor that physics-informed models are superior to black-box alternatives. It instead prevents the single descriptor “physics-informed” from functioning as a global epistemic endorsement. The relevant profile might, for example, contain an `ESTABLISHED` `TC_STRUCTURE` claim, a `PARTIAL` `RT_SCOPE` claim because the governing model is known to be approximate, and an `ESTABLISHED` `CR_PREDICTION` claim in a calibrated operating regime. Another system could exhibit the reverse pattern.

This case is where the relation-based vocabulary offers perhaps the most immediate compression. A familiar methodological debate—whether incorporating physics improves learning—can be decomposed into distinct questions about implementation of theory, adequacy of theory, and adequacy of output. Existing V&V and SciML frameworks contain tools for each of these questions. The Trias claim is only that keeping their epistemic targets distinct in a common profile makes clear what a positive result has actually warranted.

### 4.4 Equation discovery: computation can produce the theory claim

The fourth configuration reverses the direction that is most natural in classical forward simulation. In equation discovery and automated scientific discovery, computational procedures use observations to infer symbolic or otherwise interpretable model structure. A minimal schematic is

\[
R \rightarrow D \rightarrow C_{\mathrm{infer}} \rightarrow \widehat{T}.
\]

Here the theory-level object is not necessarily the input to the computerized model. It is an output of a computational inference procedure. Equation discovery, symbolic regression, sparse identification, and broader automated-discovery systems are established research areas, and recent reviews explicitly place equation discovery on a continuum toward increasingly autonomous scientific discovery (Kramer et al., 2026). The Trias therefore does not claim novelty for computational theory generation.

What changes is the evidential structure. A discovered model may reproduce trajectories, long-time statistics, attractor geometry, or other dynamical observables well. Such evidence can support a target-related adequacy claim for the inferred model or its computational realization. It does not automatically establish that the recovered symbolic structure is the unique or physically correct theory of the target system. Questions of structural identifiability, practical identifiability, observability, model equivalence, and robustness of equation-finding procedures remain relevant and are handled by mature neighboring literatures.

The distinction is especially visible in recent work by Zhai, Lucarini, and Lai, who show a chaotic equation-discovery setting in which different observation/reconstruction conditions can lead sparse equation-finding procedures to structurally different inferred equations while selected long-time dynamical properties remain similar (Zhai et al., 2025/2026). Their result does not imply that equation discovery is generally incapable of identifying governing equations, nor that dynamically similar equations are physically equivalent. It does, however, provide a concrete example in which

\[
\text{dynamical/statistical adequacy}
\not\Rightarrow
\text{structural/mechanistic identification}.
\]

The role profile localizes these as different claims. Long-time agreement of an inferred model with target observables can support a `C–R` or target-relative dynamical-adequacy entry. The claim that the inferred symbolic terms correspond to the actual governing mechanism belongs to `R–T`, and the question whether the inference pipeline could reliably resolve the relevant structural alternatives belongs to `T–C` in the broader sense of computational resolvability of a theory claim. A successful discovery workflow may therefore be strong on dynamical adequacy yet uncertain on structural fidelity, without contradiction.

This inversion is also the clearest reason not to treat `R`, `T`, and `C` simply as chronological lifecycle stages. In a forward simulation, `T` may precede `C`; in equation discovery, `C` can be the means by which a candidate `T` is generated. The roles remain analytically distinguishable even when their temporal ordering changes. That is the strongest structural difference between the present role-based reading and a simple forward implementation picture.

The same discipline applies when the result is negative. If an inference pipeline is sufficiently well resolved but a hypothesized reconstruction-induced structural effect is not robust across pre-specified trials, the proper output of the profile is that the structural claim remains unsupported—not that the workflow has somehow failed globally. Conversely, if the computational method cannot resolve the signal that would distinguish candidate theory claims, the corresponding structural question is uncertain rather than refuted. These possibilities motivate the negative and inconclusive stress tests discussed later in the paper.

## 4.5 Cross-case comparison: the same grammar, different success claims

The four configurations can be summarized with one small descriptive grammar rather than four independent quality vocabularies:

| Configuration | `R` | `T` status | `C` role | Principal evidence | Directly supported relation | Explicit non-implication |
|---|---|---|---|---|---|---|
| Predictive black-box | usually `REAL` for the prediction claim | `NONE_CLAIMED` | learned predictor | real held-out / prospective performance | `C–R` prediction | no automatic mechanism/explanation claim |
| Synthetic surrogate | `SYNTHETIC` for teacher fidelity; possibly `REAL` for downstream use | typically present through simulator/model | emulator / learned operator | teacher holdout, plus separate real validation if available | `T–C` or `C–R_syn`; separately `C–R_real` | teacher fidelity is not real validation |
| Physics-informed / hybrid ML | usually `REAL` or `HYBRID` | present or partial | hybrid learned realization | physics residuals, verification, and real validation | potentially all three, but via different evidence | physics satisfaction is not theory adequacy or empirical validation |
| Equation discovery | usually `REAL` or explicitly synthetic benchmark | `INFERRED` | inverse inference / symbolic discovery | structural recovery tests and dynamical validation | `R–T`, `T–C` resolvability, and `C–R` must be distinguished | dynamical adequacy is not automatic structural identification |

The table does not claim that these categories exhaust AI for Science. Its purpose is to test whether a single relation-based semantics can compare workflows whose computational components occupy substantially different scientific roles. On this restricted test, the answer is positive. The same vocabulary distinguishes predictive success without theory, fidelity to a synthetic referent, theory-constrained computation, and computationally inferred theory without forcing any of them into a single ranking.

The resulting descriptive principle is modest: a computational success should be reported together with the referent and claim to which its evidence attaches. This principle is compatible with established V&V, philosophy of machine learning, SciML, and equation-discovery methodology. The proposed contribution is the common genealogical organization of those distinctions, not their replacement.

## Reference anchors for final bibliography

- Jakeman, J. D., Barba, L. A., Martins, J. R. R. A., & O'Leary-Roseberry, T. (2026). *Verification and validation for trustworthy scientific machine learning*. Machine Learning: Science and Technology 7, 025055.
- Karniadakis, G. E., Kevrekidis, I. G., Lu, L., et al. (2021). *Physics-informed machine learning*. Nature Reviews Physics 3, 422–440.
- Kramer, S., Cerrato, M., Brugger, J., et al. (2026). *Automated Scientific Discovery: From Equation Discovery to Autonomous Discovery Systems*. Machine Learning 115, 109.
- Naser, M. Z. (2025). *A decision architecture for epistemic prioritization: Machine learning at the intersection of technology and society*. Technology in Society 83, 103039.
- Vinuesa, R., Cinnella, P., Rabault, J., et al. (2026). *Decoding complexity through machine learning is redefining scientific discovery*. Communications Physics 9, 168.
- Zhai, Z.-M., Lucarini, V., & Lai, Y.-C. (2025/2026). *Deficiency of equation-finding approach to data-driven modeling of dynamical systems*. arXiv:2509.03769; final bibliographic status to be checked at manuscript submission.
