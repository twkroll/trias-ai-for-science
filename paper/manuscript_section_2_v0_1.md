# Section 2 — Genealogy: From model credibility to the present problem

**Status:** DRAFT v0.1 / W2  
**Stand:** 2026-09-03  
**Depends on:** D031 / P3 / C08-D-R3

> **Manuscript note:** This is near-manuscript prose. Author–year citations are placeholders for the final bibliography. The section deliberately treats classical model credibility as a constitutive ancestor rather than as an opponent to the proposed synthesis.

## 2. Genealogy: from model credibility to the present problem

The distinction between a target system, a scientific representation of that system, and a computational realization is not new. A direct historical ancestor is the model-credibility tradition that emerged in simulation methodology in the late 1970s and was subsequently developed in the verification-and-validation literature. The terminology associated with Schlesinger and the Society for Computer Simulation distinguished the real or problem entity, a conceptual model of that entity, and a computerized model used to execute the representation computationally (Schlesinger et al., 1979). Later V&V accounts, especially Sargent's work on the verification and validation of simulation models, made the relations among these objects explicit by distinguishing conceptual-model validity, computerized-model verification, and operational validity (Sargent, various editions).

This genealogy matters because it places a strict boundary on the present proposal. In the classical simulation setting, the three relations already correspond closely to the distinctions that motivate the descriptive Trias. Conceptual-model validity asks whether the assumptions, theories, and representation encoded in the conceptual model are sufficiently appropriate for the problem entity and intended purpose. Computerized-model verification asks whether the implemented model adequately represents the conceptual model. Operational validity asks whether the behavior of the computerized model is sufficiently accurate for the intended application domain and purpose. In the notation used later in this paper, these relations are approximately

\[
R\!-​T \;\sim\; \text{conceptual-model validity},
\]

\[
T\!-​C \;\sim\; \text{computerized-model verification},
\]

and

\[
C\!-​R \;\sim\; \text{operational validity / validation}.
\]

The mapping is not exact in every detail, but it is sufficiently close to rule out any claim that a three-part Reality–Theory–Computation topology, or the distinction among its three pairwise adequacy relations, is an original contribution of the present paper.

Modern verification, validation, and uncertainty-quantification practice reinforces rather than weakens this conclusion. Contemporary standards and credibility frameworks distinguish verification from validation, bind model acceptability to an intended use or context of use, and require explicit attention to assumptions, quantities of interest, uncertainty, sensitivity, acceptance criteria, and domains of applicability. In this tradition, the fact that a model is correctly implemented does not by itself establish that it adequately represents a physical system, and validation for one purpose does not automatically license use for another. Scientific-machine-learning V&V has already extended much of this logic to learned and hybrid models by considering model purpose, prior knowledge, data characteristics and processing, code and solution verification, validation evidence, uncertainty, and interpolation or extrapolation scope (e.g. Jakeman et al., 2026). The present proposal therefore neither replaces V&V nor identifies a validation gap that those frameworks are in principle unable to formulate.

The same historical comparison also limits several narrower claims. Distinguishing fidelity to a synthetic reference from validation against a physical system has close analogues in surrogate, metamodel, and simulation-credibility practice. Likewise, the idea that evidence should be interpreted relative to an intended use, quantity of interest, and defined scope is already central to credibility assessment. Even the general warning against transferring evidence silently from one relation to another is strongly anticipated by the separation of conceptual validity, verification, and validation. The descriptive Trias should thus not be read as a rediscovery of these methodological distinctions under new labels.

The remaining question is instead one of interpretation and scope. Classical model credibility is especially natural for a forward modeling picture in which a conceptual or mathematical model is specified and then realized computationally. In such a workflow, the conceptual model and computerized model can be read, at least approximately, as successive elements of a modeling lifecycle. AI-for-Science workflows make this ordering less stable. A learned predictor may be scientifically useful without an explicit mechanistic theory claim; a surrogate may be evaluated primarily against a simulator-defined synthetic referent; a physics-informed model may combine data and theoretical constraints inside one computational practice; and equation-discovery methods may produce a candidate theory-level object as an output of computation rather than take it as a prior input. None of these configurations is itself novel. What changes is the usefulness of reading the three elements as fixed stages.

For that reason, the present paper adopts a role-based rather than a stage-based reinterpretation of the classical structure. `R` denotes the claim-relative target or referent; `T` denotes the scientific theory-, mechanism-, or explanation-level content actually being claimed; and `C` denotes the concrete computational practice. The three roles may occur in different temporal orders, and one role may be absent for a narrowly specified claim. This reinterpretation preserves the central insight of classical model credibility—that different relations require different evidence—while allowing the theory and computation roles to be occupied differently across contemporary AI-for-Science workflows.

The contribution is therefore genealogical rather than replacement-based. The classical credibility tradition supplies the relational skeleton. The proposed synthesis asks whether that skeleton becomes more useful for AI for Science when its elements are treated as claim-relative epistemic roles rather than as fixed lifecycle stages, and when performance evidence is explicitly localized to the relation and referent it actually supports. Section 4 tests that proposal across predictive black-box models, synthetic surrogates, physics-informed learning, and equation discovery. The relevant standard for success is not whether these individual cases are new, but whether the same small role-and-evidence vocabulary can compare them without collapsing prediction, theory fidelity, and target grounding into a single notion of model success.

### Table 1 — Genealogy and contribution boundary

| Descriptive-Trias element | Classical model-credibility analogue | Modern V&V / SciML status | Novelty status in this paper | Role in the argument |
|---|---|---|---|---|
| `R`: target / referent | Reality / Problem Entity | validation target; intended-use/context-of-use reference | **not new** | retyped as claim-relative `REAL`, `SYNTHETIC`, or `HYBRID` referent |
| `T`: scientific theory/mechanism/explanation claim | Conceptual Model, including assumptions/theories | mathematical/conceptual model; prior knowledge/model structure in SciML | **classical role strongly preceded** | broadened analytically to `PRESENT`, `PARTIAL`, `NONE_CLAIMED`, or `INFERRED` for the claim at issue |
| `C`: computational practice | Computerized Model | numerical implementation; learned/hybrid computational model | **not new as computation** | read broadly as solver, predictor, surrogate, reconstruction, hybrid model, or inference procedure |
| `R–T` relation | conceptual-model validity / qualification | model-form adequacy, assumptions, scope, intended use | **not new** | theory-/mechanism-level claim about the target |
| `T–C` relation | computerized-model verification | code/solution verification; implementation fidelity; structure satisfaction | **not new** | localizes whether claimed theory content is operationalized or computationally resolvable |
| `C–R` relation | operational validity / validation | empirical validation, prediction, calibration, target-specific adequacy | **not new** | localizes computational success relative to the specified target |
| intended use / scope | central in Sargent-style credibility | central in V&V/VVUQ and SciML credibility | **not new** | required index for every profile statement |
| synthetic vs real referent | high-fidelity-model / metamodel and surrogate credibility distinctions | strongly established in surrogate/SciML validation | **strongly preceded** | made explicit in the same profile used for other AI configurations |
| evidence should not transfer automatically between relations | implicit in separation of qualification, verification, validation | standard credibility logic | **strongly preceded** | stated as a default anti-overreach rule rather than a new theorem |
| dynamic role occupation (`T` absent, partial, or inferred; `C` predictive or inferential) | less natural in the classical forward lifecycle reading | individual configurations strongly established across ML/SciML/discovery literatures | **not new individually** | central ingredient of the cross-case synthesis |
| one common role/evidence grammar across forward simulation, predictive ML, surrogate ML, PIML, and equation discovery | no single direct analogue identified in the project audits | components distributed across several mature literatures | **possible synthesis contribution** | exact residual contribution tested in the manuscript |

## Reference anchors for final bibliography

- Schlesinger, S. et al. (1979). *Terminology for model credibility*. SIMULATION 32(3), 103–104.
- Sargent, R. G. *Verification and Validation of Simulation Models* (multiple versions/reviews).
- Relevant ASME/AIAA/NASA V&V and model-credibility standards/guidance.
- Jakeman, J. D., Barba, L. A., Martins, J. R. R. A., & O'Leary-Roseberry, T. (2026). *Verification and validation for trustworthy scientific machine learning*. Machine Learning: Science and Technology 7, 025055.
