# Section 7 — What the Trias adds, and what adjacent frameworks already do better

**Status:** DRAFT v0.1 / W4  
**Stand:** 2026-09-03  
**Depends on:** D033 / P3 / C08-D-R3 / W1–W3 PASS

> **Manuscript note:** This section is the principal contribution-boundary test. It is intentionally asymmetrical: adjacent frameworks are credited with the technical and methodological work they already perform better or more deeply. The residual Trias claim is accepted only if something remains after that comparison.

## 7. What the Trias adds, and what adjacent frameworks already do better

The descriptive Trias is not intended to replace the mature frameworks that already govern verification, validation, provenance, scientific inference, or claim–evidence reasoning. In most of the cases discussed above, those frameworks provide substantially more technical detail than the Trias does. The relevant question is therefore not whether the Trias can reproduce their functions, but whether a small target–theory–computation vocabulary adds a useful cross-case organization once those functions are acknowledged.

### 7.1 Verification, validation, VVUQ, and model credibility

Verification-and-validation and broader model-credibility frameworks are the strongest comparator. They already distinguish conceptual-model adequacy, computerized-model verification, empirical or operational validation, intended use, quantities of interest, uncertainty, sensitivity, acceptance criteria, and domains of applicability. Modern Scientific-ML credibility work extends these concerns to learned components, data characteristics and processing, hyperparameters, extrapolation, and reproducibility (Schlesinger et al., 1979; Sargent; NASA-STD-7009B; Jakeman et al., 2026). For a conventional forward simulation, the descriptive Trias adds little that a careful V&V analysis could not express more precisely.

The residual role of the Trias is therefore not a new validation category. It is to use the classical credibility relations as an epistemic vocabulary across workflows in which the theory and computation roles are occupied differently. A black-box predictor, a simulator-trained surrogate, a physics-informed learner, and an equation-discovery pipeline can all be described with the same questions—what is the referent, what theory-level claim is actually at issue, what computational practice produced the evidence, and which relation does that evidence directly support? This is a reorganization of credibility reasoning, not an alternative to it.

### 7.2 Workflow and data provenance

Provenance frameworks perform a different task better. W3C PROV and scientific-workflow provenance represent entities, activities, agents, usage, generation, derivation, parameters, and intermediate artifacts. A complete AI-for-Science pipeline can therefore be represented in much greater operational detail as a provenance graph than as an `R/T/C` diagram. The Trias should not claim novelty for directionality, intermediate data products, or the observation that preprocessing choices propagate downstream.

What provenance does not by itself fix is the scientific role assigned to each artifact in the claim under assessment. A reconstructed time series, an inferred equation, a simulator output, and a held-out measurement are all provenance entities, but they can play different epistemic roles. The Trias contribution, if useful, is to annotate that lineage with a small claim-relative distinction between target, theory-level content, and computational realization. This does not improve provenance as a representation of lineage; it specifies what kind of scientific claim a particular part of that lineage is being used to support.

### 7.3 Claims, arguments, evidence, and assurance cases

Assurance cases and Claims–Arguments–Evidence approaches already make explicit that evidence must be connected to a specific claim through an argument and stated assumptions. They therefore cover one of the most important safeguards that motivated the Trias: successful evidence at one level does not automatically license a broader scientific conclusion. A surrogate-validation argument, for example, can be represented directly as a chain of claims about the simulator, the surrogate error, the domain of use, and the resulting permissible application.

The Trias does not offer a richer argument language. Its possible contribution is narrower: it supplies a domain-specific typing of the claims that recur across computational science. The distinction between `R–T`, `T–C`, and `C–R` can be read as a compact way of asking what kind of claim an assurance argument concerns. In this sense, Bridge Claims are not a new assurance method; they mark where an assurance-style argument is required when evidence is transferred from one relation to another.

### 7.4 Identifiability, observability, and system identification

For inverse problems, identifiability, observability, and system-identification theory are substantially deeper than the Trias. They address whether internal states, parameters, or model structures can be recovered from observations and how finite data, noise, sampling, differentiation, libraries, and regularization affect that recovery. Structural-error and near-identifiability traditions also already recognize that structurally different models can remain close with respect to selected outputs. Sparse equation-discovery methods and their robustness variants directly study the instability of recovered support and coefficients.

The Trias therefore contributes no new uniqueness criterion and no new error mechanism. Its role is again cross-case localization. In equation discovery, the candidate theory object `T_hat` can be the output of `C_infer`; structural identification of that theory, dynamical adequacy of its forward realization, and empirical agreement with selected observables are then different claims even when they are evaluated in the same workflow. Identifiability and system identification explain the inverse problem more deeply; the Trias connects that inverse case to forward simulation, prediction, and surrogate modeling with the same claim-role vocabulary.

### 7.5 Philosophy of machine learning and plural epistemic functions

Philosophy-of-ML work already distinguishes prediction from explanation, discovery, understanding, and decision-making, and recent scientific-ML perspectives classify the role of machine learning by how much governing-equation knowledge is available (Naser, 2025; Vinuesa et al., 2026). The Trias therefore cannot claim that prediction without mechanism is a newly recognized form of scientific success, nor that theory can be absent, partial, or computationally generated.

Its narrower question is what a concrete piece of evidence warrants within those epistemic functions. A high predictive score against real observations supports a different relation from a low residual against an embedded equation or successful symbolic recovery on a synthetic benchmark. The Trias thus sits one level below a taxonomy of scientific aims: it asks which target, theory claim, and computational practice the reported evidence actually connects.

### 7.6 Scientific machine learning, physics-informed learning, and surrogate credibility

Scientific machine learning itself already integrates data, numerical simulation, physical constraints, surrogates, reduced-order models, and inverse inference. PIML and surrogate-credibility literatures also distinguish internal constraint satisfaction, emulator fidelity, physical validation, and transfer across domains. Nothing in the Trias replaces these domain-specific methods.

The value of the common role profile is therefore comparative rather than technical. The same minimal grammar can describe why a physics residual primarily concerns a theory–computation relation, why teacher fidelity is conditional on a synthetic referent, why real held-out prediction concerns computation–target adequacy, and why a discovered symbolic equation introduces a theory-level claim that requires its own support. The individual distinctions are established; the synthesis keeps them comparable without turning them into a single global model score.

### 7.7 Exact contribution boundary

The resulting boundary is deliberately modest. The descriptive Trias is best understood as a **genealogically grounded evidence-localization vocabulary** for comparing heterogeneous computational scientific workflows. It inherits its relational skeleton from classical model credibility, relies on V&V for technical credibility assessment, on provenance for lineage, on assurance cases for claim–evidence argumentation, and on identifiability and system identification for inverse recoverability. Philosophy of ML and SciML already provide richer accounts of the individual epistemic roles that AI can play.

What remains is a compact cross-domain synthesis: the same role grammar distinguishes a real or synthetic referent, an explicit, partial, absent, or inferred theory claim, and a numerical, learned, or inferential computational practice; it then asks which relation the available evidence directly supports and which additional claims require a bridge. This vocabulary is useful only insofar as it reduces ambiguity across cases such as black-box prediction, surrogate modeling, physics-informed learning, and equation discovery. It should not be treated as a substitute for the specialist frameworks that provide the substantive evidence.

This boundary also supplies a direct answer to the objection that the Trias is merely new notation. If `R/T/C` only renamed reality, model, and computation, the proposal would add nothing beyond classical credibility diagrams. Its residual content lies instead in the repeated use of the same claim-relative semantics across workflows with different role orderings and referents, together with explicit non-transfer rules. That residual is a **moderate synthesis contribution**, not a new theory of credibility. Whether the synthesis is practically useful for communication, review, or scientific decision-making remains an empirical question outside the claims of the present paper.

## Reference anchors for final bibliography

- Schlesinger et al. (1979), *Terminology for model credibility*.
- Sargent, *Verification and Validation of Simulation Models*.
- NASA-STD-7009B and related V&V/VVUQ guidance.
- Jakeman et al. (2026), *Verification and validation for trustworthy scientific machine learning*.
- W3C PROV and scientific-workflow provenance literature.
- Assurance-case / Claims–Arguments–Evidence / Goal Structuring Notation literature.
- Villaverde et al. and related structural/practical identifiability and observability literature.
- Hadaegh & Bekey and related near-identifiability / structural-error literature.
- SINDy / robust sparse equation-identification literature.
- Naser (2025), P.E.D.U.D. epistemic-functions framework.
- Vinuesa et al. (2026), scientific-ML roles by theory availability.
- Karniadakis et al. (2021), physics-informed machine learning.
