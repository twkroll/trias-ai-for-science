# From Model Credibility to AI for Science: Claim-Relative Evidence Across Target, Theory, and Computation

**Status:** SOURCE-HARDENED DRAFT v0.3 / W10  
**Stand:** 2026-09-03  
**Depends on:** D039 / P3 / W9 Source & Bibliography Audit  
**Bibliography:** `paper/references_v0_3.bib`

> **Source note:** Citation keys use Pandoc-style `[@key]` notation and are journal-neutral. All externally grounded claims in this draft are restricted to the source boundaries documented in W9. Project-specific numerical results remain project-internal evidence and are not attributed to external literature.

## Abstract

Classical model-credibility methodology already distinguishes a problem entity or reality, a conceptual model, and a computerized model, together with corresponding questions of qualification or conceptual validity, verification, and operational validation. AI-for-Science workflows do not invalidate this structure, but they make its elements less natural as fixed lifecycle stages: computation may act as predictor, simulator surrogate, physics-constrained learner, reconstruction pipeline, or inference procedure that produces a candidate theory. We therefore propose a descriptive, claim-relative reinterpretation in which `R` denotes the target or referent, `T` the theory-, mechanism-, structure-, or explanation-level content actually claimed, and `C` the concrete computational practice. Evidence is localized to target–theory, theory–computation, or computation–target claims within a stated use and scope; support on one relation does not automatically establish the others without an explicit bridge argument. The same vocabulary is applied to predictive black-box models, synthetic surrogates, physics-informed learning, and equation discovery, with classical numerical controls and negative/inconclusive project results used to test evidence-status discipline. The proposal does not replace verification and validation, provenance, assurance cases, identifiability, system identification, or Scientific ML methodology. Its contribution is a modest cross-domain synthesis: a genealogically grounded evidence-localization vocabulary for comparing heterogeneous forms of computational scientific success without reducing them to a single global model-quality label. Its practical usefulness remains to be tested.

## 1. Introduction: when “the model works” is epistemically incomplete

Suppose two scientific machine-learning systems report the same low root-mean-square error. In one case, the error is measured against independent observations of a physical system. In the other, it is measured against the outputs of a numerical simulator used as a training teacher. The numerical values may be identical, yet the two results do not directly support the same scientific claim. The first concerns performance relative to an empirical target. The second concerns fidelity to a synthetic or simulator-defined referent. Whether the second can also support a claim about the physical system depends on additional premises about the simulator, the quantity of interest, the regime of use, and the size of the surrogate error. The phrase “the model works” therefore omits an important question: **what has been shown to work, relative to what, and for which claim?**

This question becomes especially visible in AI for Science because computation no longer occupies one uniform role. Learned systems may predict observations without making a mechanistic claim, emulate expensive numerical models, combine data with physical constraints, reconstruct partially observed states, or participate in the inference of candidate equations. None of these practices is new. Recent methodological work on machine learning explicitly distinguishes prediction, explanation, discovery, understanding, and decision-making as different epistemic functions [@naser2025]. Scientific-ML perspectives likewise organize the role of machine learning by the amount of governing-equation knowledge available [@vinuesa2026], physics-informed learning integrates data with mathematical or physical structure [@karniadakis2021], and equation-discovery research uses computation to produce interpretable candidate models [@kramer2026; @brunton2016]. The problem addressed here is not that these roles have gone unnoticed. It is that success in them is easily compressed into broad labels such as *accurate*, *validated*, *physics-informed*, or *discovered*, even when the supporting evidence attaches to different scientific relations.

There is equally no novelty in a triangle of reality, model, and computation. A direct historical ancestor is the model-credibility terminology associated with the Society for Computer Simulation and later verification-and-validation practice. The 1979 terminology distinguishes reality, a conceptual model, and a computerized model and connects them through model qualification, model verification, and model validation [@schlesinger1979]. Sargent’s later V&V formulation distinguishes conceptual-model validity, model verification, operational validity, and data validity [@sargent2013]. Modern model-credibility practice further binds acceptance to purpose, quantities of interest, uncertainty, sensitivity, and explicit criteria [@nasa7009b2024; @nasahdbk7009b2026]. Recent Scientific ML credibility work extends many of these concerns to learned and hybrid models [@jakeman2026]. Any contribution of the present paper must therefore lie not in inventing the three-part structure, but in how it is interpreted across contemporary computational workflows.

The proposal developed here is to read the classical structure as a set of **claim-relative epistemic roles** rather than as a fixed sequence of lifecycle stages. We use `R` for the target or referent of the claim, which may be real, synthetic, or hybrid; `T` for the theory-, mechanism-, structure-, or explanation-level content actually being asserted; and `C` for the concrete computational practice. In a conventional simulation, a theory may be specified before it is implemented computationally. In predictive black-box learning, no theory-level claim may be part of the stated scientific use. In equation discovery, a candidate `T` can instead be an output of `C`. In a surrogate workflow, one computational model can become part of the synthetic referent for another. The roles are therefore fixed by the claim under assessment, not by a permanent ontology of artifacts or by their chronological order.

The residual contribution is deliberately modest. The paper proposes a **genealogically grounded evidence-localization vocabulary** for comparing heterogeneous computational scientific workflows. It does not replace V&V, provenance analysis, assurance cases, identifiability theory, system identification, or the methodology of Scientific ML. Those frameworks provide the substantive technical and argumentative machinery. The role profile asks a narrower cross-case question: which target, which theory-level claim, and which computational practice are connected by the reported evidence, and what remains partial, uncertain, untested, or not applicable?

Four AI-for-Science configurations provide the main conceptual test: predictive black-box models, synthetic surrogates, physics-informed or hybrid learning, and equation discovery. Two classical controls then show where ordinary numerical analysis and V&V already suffice, while two project stress tests distinguish informative negative evidence from inconclusive evidence. The resulting position is descriptive rather than normative. It proposes neither a scalar model-quality score nor an ideal point at which all relations are maximized, and it does not assert a necessary trade-off among target, theory, and computation.

## 2. Genealogy: from model credibility to the present problem

The distinction between a target system, a scientific representation of that system, and a computational realization is historically well established. The 1979 SCS credibility terminology organized simulation credibility around **reality**, a **conceptual model**, and a **computerized model**. In that terminology, model qualification concerns whether the conceptual model is acceptable for the intended application, model verification concerns whether the computerized model sufficiently represents the conceptual model, and model validation concerns whether the computerized model achieves satisfactory agreement over its intended domain of applicability [@schlesinger1979]. Sargent’s later account uses the related but not identical terminology of **conceptual-model validity**, **model verification**, and **operational validity** [@sargent2013].

The mapping to the present notation is therefore only genealogical and approximate:

\[
R-T \sim \text{model qualification / conceptual-model validity},
\]

\[
T-C \sim \text{model verification},
\]

and

\[
C-R \sim \text{model validation / operational validity}.
\]

The approximation is close enough to rule out any claim that the basic three-part topology or its three pairwise adequacy relations are original contributions of this paper.

Modern V&V and VVUQ reinforce this conclusion. NASA’s current model-and-simulation standard and handbook treat credibility as a lifecycle and use-context issue involving V&V, sensitivity and uncertainty analysis, and explicit program or project acceptance criteria [@nasa7009b2024; @nasahdbk7009b2026]. In the medical-device domain, ASME V&V 40 provides a domain-specific example in which required credibility depends on model risk and decision context [@asmevv402018]. Scientific ML credibility work extends the same general logic to learned and hybrid components, including model purpose, prior knowledge, quantities of interest, code and solution verification, validation evidence, data characteristics and processing, uncertainty, sensitivity, hyperparameters, reproducibility, and interpolation or extrapolation scope [@jakeman2026]. Distinguishing fidelity to a synthetic reference from validation against a physical system is likewise familiar in surrogate and simulation-credibility practice.

The present proposal therefore does not argue that classical credibility frameworks cannot express AI-for-Science cases. The narrower claim is that their familiar objects can be useful as **roles** rather than only as elements of a forward modeling picture. In a classical simulation, a conceptual or mathematical model is naturally read as prior to its computerized implementation. AI-for-Science workflows make that order less stable: a predictive learner can be scientifically useful without an explicit theory claim; a surrogate can be evaluated against a simulator-defined reference; a hybrid learner can combine data and theoretical constraints inside one computational practice; and equation discovery can produce a candidate theory-level object as an output of computation. These configurations are individually established [@naser2025; @vinuesa2026; @karniadakis2021; @kramer2026]. What changes is the usefulness of treating theory and computation as fixed stages.

The proposal is thus genealogical rather than replacement-based. The credibility tradition supplies the relational skeleton. The reinterpretation asks whether that skeleton becomes analytically useful across heterogeneous AI-for-Science workflows when `R`, `T`, and `C` are treated as claim-relative epistemic roles and when reported evidence is explicitly attached to the relation and referent it directly supports.

### Table 1. Genealogy and contribution boundary

| Element used here | Classical / modern analogue | Status in this paper | Residual role |
|---|---|---|---|
| `R`: target / referent | Reality / Problem Entity; validation target | **not new** | typed as claim-relative `REAL`, `SYNTHETIC`, or `HYBRID` referent |
| `T`: theory-level claim | Conceptual Model; prior scientific model | **strongly preceded** | may be `PRESENT`, `PARTIAL`, `NONE_CLAIMED`, or `INFERRED` for the claim at issue |
| `C`: computational practice | Computerized Model; numerical or learned implementation | **not new** | used functionally for solver, predictor, surrogate, reconstruction, hybrid or inference practice |
| `R-T` | model qualification; later conceptual-model validity | **not new** | localizes target–theory claims |
| `T-C` | model verification | **not new** | localizes theory operationalization, fidelity, tractability or resolvability |
| `C-R` | model validation / operational validity | **not new** | localizes computational success relative to the specified target |
| intended use / scope | central in V&V/VVUQ | **not new** | required index for every profile statement |
| synthetic vs real reference | surrogate / metamodel credibility | **strongly preceded** | made explicit in the same profile as other AI configurations |
| evidence should not transfer silently | credibility / assurance logic | **strongly preceded** | stated as a cross-case anti-overreach default |
| dynamic role occupation | distributed across ML/SciML/discovery literatures | **not new individually** | central ingredient of the synthesis |
| one common role/evidence grammar across the four AI configurations | **no direct analogue identified in our documented audits** | **possible synthesis contribution** | exact residual claim of the paper |

## 3. From lifecycle stages to claim-relative epistemic roles

A role in the present sense is fixed by the scientific claim under assessment, not by a permanent classification of an artifact. The same object can occupy different roles in different arguments. A simulator output can be a computational prediction in one analysis and the synthetic reference for a surrogate in another. A symbolic equation can be a prior theory in forward simulation and an inferred theory-level output in equation discovery. A neural network can be a predictor, a surrogate, part of a reconstruction pipeline, or an inference device. Before assigning evidential meaning, the analysis therefore asks: **what is the referent, what theory-level content is actually being asserted, and what computational practice generated or operationalized the result?**

### 3.1 The target role `R`

`R` denotes the target or referent relative to which a scientific claim is evaluated. Three types are sufficient for the present analysis:

```text
R_REAL       empirical or physical target
R_SYNTHETIC  explicitly constructed or simulator-defined referent
R_HYBRID     reference combining empirical and constructed components
```

The distinction is claim-relative rather than metaphysical. Calling a referent synthetic does not make it epistemically inferior. It states what the evidence is directly about. A high-fidelity surrogate evaluated against a simulator can therefore be strongly supported relative to `R_SYNTHETIC`. If the scientific claim is changed to the corresponding physical system, the referent changes and the evidential profile must be specified again. The semantic rule is simple: **a change of referent is a change of claim, even when the computational model and performance metric remain unchanged.**

### 3.2 The theory role `T`

`T` denotes the theory-, mechanism-, structure-, or explanation-level content actually being claimed. It should not automatically be identified with every architectural bias or mathematical object in a workflow. Four statuses are enough for the cases considered here:

```text
PRESENT       an explicit theory-level claim is part of the analysis
PARTIAL       only part of the relevant theoretical structure is asserted or available
NONE_CLAIMED  no theory-level claim is made for the stated use
INFERRED      a candidate theory-level object is produced computationally
```

These statuses are not a ranking. `NONE_CLAIMED` is especially important because a descriptive framework should not turn mechanism into a hidden universal norm. A black-box predictor can be successful for a narrowly specified prediction task without being classified as defective merely because it makes no mechanistic claim. Conversely, `INFERRED` captures the equation-discovery case in which a theory-level object is a result of computation rather than a prior stage.

### 3.3 The computation role `C`

`C` denotes the concrete computational practice whose behavior and evidential role are at issue. It may be a numerical solver, a learned predictor, a surrogate, a reconstruction procedure, a hybrid physics–ML system, or an equation-inference pipeline. The category is functional rather than hardware-based. In a forward simulation, `C` can realize a prior `T`; in equation discovery, `C` can help produce a candidate `T`; in a surrogate workflow, one computational realization can become part of the referent for another.

### 3.4 Relations and evidence status

Once the roles are fixed, the three pairwise relations can be read as evidential questions:

```text
R-T: What supports the theory/mechanism/structure claim about the target?
T-C: What supports operationalization, fidelity, tractability or resolvability of theory-level content in computation?
C-R: What supports the computational output relative to the specified target?
```

These are not three scalar scores. A `T-C` claim may concern implementation fidelity, numerical convergence, tractability, structure preservation, surrogate fidelity, or resolvability. A `C-R` claim may concern prediction, calibration, distributional agreement, transfer, or another quantity of interest. The minimal unit is therefore an evidence entry rather than a point in a quality space:

```text
relation | facet | claim | evidence | use case | scope | status
```

For descriptive purposes, five status labels are sufficient:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

`ESTABLISHED` means sufficiently supported within the documented use and scope, not universally true. `PARTIAL` marks positive but limited support. `UNCERTAIN` applies when the claim is relevant but the available method or data cannot discriminate it reliably. `UNTESTED` means relevant but not directly assessed. `NOT_APPLICABLE` means that the relation is not part of the specified claim.

A central default is that evidence attached to one relation is not automatically transferred to another:

\[
A_{RT}+A_{TC}\not\Rightarrow A_{CR},\qquad
A_{TC}+A_{CR}\not\Rightarrow A_{RT},\qquad
A_{RT}+A_{CR}\not\Rightarrow A_{TC}.
\]

These expressions are not logical impossibility theorems. They state a weaker methodological rule: **cross-relation inference requires an explicit bridge argument.** For a synthetic surrogate, strong fidelity to a simulator can contribute to a real-target claim only if additional premises are supplied—for example, that the simulator is credible for the same quantity and regime, the surrogate is used within that domain, and its additional approximation error is acceptable relative to the relevant error budget. This kind of inferential structure is already familiar from assurance cases and model credibility [@goodenough2012; @gsn2021; @sargent2013]. The role profile merely makes the bridge visible.

## 4. Four AI-for-Science role configurations

The proposal is useful only if the same small grammar can distinguish heterogeneous workflows without adding case-specific rules. The four configurations below serve as the main conceptual test.

### 4.1 Predictive black-box systems: useful computation without an explicit theory claim

Consider a predictive model trained on observations from a real target system. The narrow scientific aim may be to estimate a future state, material property, or experimentally relevant quantity. A schematic workflow is

\[
R_{\mathrm{real}} \rightarrow D \rightarrow C_{\mathrm{pred}},
\]

with

\[
T=\mathrm{NONE\_CLAIMED}
\]

for the specified prediction claim. This does not mean that background theory played no role in data collection or model design. It means only that the result being assessed is not itself a claim that the learned representation constitutes the mechanism or explanation of the target system.

If the model is evaluated prospectively or on representative held-out observations and achieves sufficiently accurate predictions, the direct evidential achievement concerns `C-R`: the computational practice agrees with the selected real-world quantity within the stated scope. This can be a substantial scientific success. It need not be downgraded because an `R-T` mechanistic claim is absent. Conversely, strong predictive evidence does not by itself establish a unique mechanism or explanation. Naser’s P.E.D.U.D. framework provides one explicit recent example of distinguishing prediction, explanation, discovery, understanding, and decision-making as different epistemic functions [@naser2025]. The role profile does not introduce that distinction. It localizes the evidence so that theory-related entries can be `NOT_APPLICABLE` for the narrow claim rather than implicitly `FAILED`.

The case therefore separates epistemic incompleteness from epistemic failure. “The model works” can legitimately mean “it predicts the stated target quantity adequately” without also meaning “it reveals how the target system works.”

### 4.2 Synthetic surrogates: the referent changes while the metric may not

A second configuration arises when machine learning emulates a numerical simulator or synthetic teacher:

\[
T \rightarrow C_{\mathrm{sim}} \rightarrow D_{\mathrm{syn}} \rightarrow C_{\mathrm{surr}}.
\]

Suppose the surrogate achieves

\[
\mathrm{RMSE}_{\mathrm{teacher}}=\varepsilon
\]

on held-out simulator outputs. This directly supports fidelity to a simulator-defined referent. Depending on the chosen representation, that can be described as a `T-C` surrogate-fidelity claim or a `C-R_{syn}` claim. Now suppose an otherwise similar model achieves

\[
\mathrm{RMSE}_{\mathrm{real}}=\varepsilon
\]

against independent observations of the physical system. The numerical value is identical, but the evidential claim differs because the referent differs.

Scientific ML credibility work already distinguishes verification and validation and explicitly discusses simulation-trained surrogates alongside independent observational validation [@jakeman2026]. The residual benefit of the role profile is that the referent switch remains explicit in the same grammar used for other AI workflows. A surrogate can reproduce a simulator extremely well while a real-target claim remains `UNTESTED`. If the simulator is itself validated for the same quantity and regime, teacher fidelity may contribute to a real-target assessment, but only through an additional bridge argument. The phrase “the surrogate is accurate” is therefore incomplete without “relative to which referent?”

This configuration is one of the strongest examples for the present synthesis because it shows how the same metric can support different scientific propositions without any change in its numerical value.

### 4.3 Physics-informed and hybrid machine learning: one label, several relations

Physics-informed and theory-guided machine learning combine data-driven optimization with physical or mathematical structure [@karniadakis2021]. A schematic workflow is

\[
T + D(R) \rightarrow C_{\mathrm{hybrid}}.
\]

The label *physics-informed* can nevertheless compress several logically different questions. First, does the computational system actually implement or satisfy the claimed theoretical constraint? A small differential-equation residual, invariant error, or verified limiting case can support a `T-C` claim. Second, is the embedded theory itself adequate for the real target and regime? Idealizations, missing physics, closure assumptions, or parameter uncertainty belong to `R-T`. Third, does the hybrid model perform adequately against the target quantity of interest? That is a `C-R` question.

These relations can have different evidence statuses. A model may strongly satisfy its encoded equations while the theory is only partially adequate for the target regime; another may predict empirical data well even though the encoded theory is approximate. Recent Scientific ML perspectives explicitly vary the role of machine learning with the amount of governing-equation knowledge available [@vinuesa2026]. The role profile does not claim that physics-informed methods systematically confuse these questions. It simply prevents the label *physics-informed* from functioning as a global epistemic endorsement. Specialist Scientific ML and V&V methods remain responsible for the substantive assessment of each claim.

### 4.4 Equation discovery: computation can produce the theory claim

Equation discovery reverses the ordering most natural in forward simulation. A minimal workflow is

\[
R \rightarrow D \rightarrow C_{\mathrm{infer}} \rightarrow \widehat{T}.
\]

Here the theory-level object is an output of computational inference rather than necessarily an input to a computerized model. Equation discovery and automated scientific discovery are established fields [@brunton2016; @kramer2026]; computational theory generation is not a Trias novelty. The relevance of this case is structural: it makes especially clear why `T` and `C` are better treated as roles than as fixed chronological stages.

A discovered equation can reproduce trajectories, long-time statistics, or attractor properties well without being uniquely identified as the correct mechanism. Parametric structural identifiability asks whether parameters of a specified model structure can be determined uniquely from idealized outputs [@villaverde2016]. Model-form uncertainty and near-equivalence require a broader vocabulary: Hadaegh and Bekey explicitly analyze system identification in the presence of structural model error and define near-equivalence and near-identifiability [@hadaegh1985], while sparse equation-discovery methods and robust variants directly address data-driven recovery of governing equations and sensitivity to noise [@brunton2016; @kaheman2020].

Zhai, Lucarini, and Lai provide a recent concrete chaotic example in which altered observation/reconstruction conditions lead to structurally different inferred equations while selected long-time dynamical properties remain similar [@zhai2025preprint]. Their study is, at the time of the present audit, an arXiv preprint and is treated as such. It does not show that equation discovery is generally non-identifiable, that dynamically similar equations are physically equivalent, or that direct machine learning is generally superior. It illustrates the narrower distinction

\[
\text{dynamical/statistical adequacy}
\not\Rightarrow
\text{structural/mechanistic identification}.
\]

The role profile can therefore separate at least three claims: whether the inferred model reproduces selected target observables (`C-R` or target-relative adequacy), whether the candidate symbolic structure is supported as a theory-level description of the target (`R-T`), and whether the computational inference pipeline could reliably resolve the relevant structural alternatives (`T-C` in the broader resolvability sense). Identifiability and system-identification theory analyze these issues more deeply. The synthesis contributes only the cross-case localization that places this inverse configuration in the same vocabulary as prediction and surrogation.

### Table 2. Cross-case role profiles for four AI-for-Science configurations

| Configuration | `R` | `T` status | `C` role | Principal direct evidence | Explicit non-implication |
|---|---|---|---|---|---|
| Predictive black-box | usually `REAL` | `NONE_CLAIMED` | predictor | held-out / prospective target performance | prediction does not automatically establish mechanism |
| Synthetic surrogate | `SYNTHETIC` for teacher fidelity; possibly `REAL` downstream | typically `PRESENT` via simulator/model | surrogate / learned operator | teacher holdout; separate real validation if available | teacher fidelity is not real validation |
| Physics-informed / hybrid ML | usually `REAL` or `HYBRID` | `PRESENT` or `PARTIAL` | hybrid learned practice | constraint satisfaction plus independent target evidence | physics satisfaction is not automatically theory adequacy or empirical validity |
| Equation discovery | `REAL` or explicit synthetic benchmark | `INFERRED` | inference / symbolic discovery | structural recovery and dynamical validation | dynamical adequacy is not automatic structural identification |

The table does not exhaust AI for Science. Its purpose is narrower: the same role/evidence grammar distinguishes four established scientific practices whose computational components occupy different epistemic positions. The resulting descriptive principle is modest: **a computational success should be reported together with the referent and claim to which its evidence attaches.**

## 5. Classical controls: where ordinary numerical analysis and V&V already suffice

A useful synthesis should remain unambitious where established analysis already provides the relevant distinctions. Two cases from the development of this project therefore function as controls.

### 5.1 Sundman: analytical availability without practical evaluability

Sundman’s 1912 treatment of the Newtonian three-body problem provides a clean theory–computation example [@sundman1912]. Under the classical nonzero-total-angular-momentum condition, binary collisions can be regularized and a transformed time variable introduced so that the motion is represented by convergent power series in a regularized variable. The relevant historical point is not failure of convergence. The series do converge under the theorem’s assumptions. The practical difficulty is their extremely slow convergence, which makes the representation unsuitable for ordinary trajectory or ephemeris computation [@belorizky1930; @henkel2001; @chenciner2007; @musielak2014].

The case therefore separates formal analytical availability from practical computational availability. A mathematically valid representation can be strong with respect to one theory–computation facet while weak with respect to tractability or evaluability:

\[
\text{formal analytical availability}
\not\Rightarrow
\text{practical computational availability}.
\]

This is not a Trias novelty. It is a control showing that the vocabulary should remain compatible with familiar distinctions without claiming to improve them.

### 5.2 Figure-eight: use-dependent numerical profiles

A second control uses the periodic equal-mass figure-eight orbit as a synthetic target. The target system, Newtonian theory, initial conditions, and reference solution were fixed, while classical RK4 and Velocity-Verlet were compared over a short trajectory-oriented horizon and a long structure-oriented horizon. In the project full run, RK4 exhibited the expected higher-order trajectory convergence and was far more accurate against the reference trajectory at equal step counts. Velocity-Verlet, however, showed much smaller secular energy drift at representative long-horizon resolutions and preserved total angular momentum near roundoff scale.

The result does not identify a globally superior solver. It shows that different numerical realizations can have different use-dependent profiles. Standard numerical analysis, geometric integration, and V&V already explain this through convergence, trajectory error, invariants, quantities of interest, and intended use. The control therefore places a boundary on the paper: applying the same vocabulary to a solver comparison is not itself evidence of a new validation method. The numerical values used for this control are project-internal and belong in the accompanying repository or supplement rather than in an external citation.

## 6. Stress tests: negative and inconclusive evidence

The role profile must also preserve the difference between a claim that was tested and not supported and a claim that could not be decided because a prerequisite failed. Two preregistered project studies provide these stress tests. Their numerical values and classifications are project-internal evidence.

### 6.1 Lorenz/SINDy: informative negative evidence

The inverse-direction study used the Lorenz-63 system with a high-accuracy numerical reference. In the discovery window, 20% of observations were removed using paired random masks and reconstructed either linearly or with a cubic spline. A fixed derivative estimator, quadratic feature library, sparse-regression procedure, and preregistered structural and dynamical criteria were then applied. The baseline path without missingness first had to recover the intended Lorenz support accurately before any reconstruction effect could be interpreted.

Those technical gates passed. The baseline recovered the true support with very small coefficient error. The experiment was therefore capable of addressing its preregistered structural question. The positive criterion nevertheless failed: a substantive structural perturbation appeared in only one of three linear-reconstruction seeds and in none of the three cubic-spline seeds, below the required seed consistency. The accepted classification is therefore

```text
INFORMATIVE_NEGATIVE.
```

The single structurally different linear case remains exploratory. No missingness rate, regression threshold, feature library, structural criterion, or decision rule was altered after the result was observed. The evidence profile is thus asymmetric: baseline validity and several dynamical/technical adequacy claims are supported, but the specific claim of a robust reconstruction-induced structural change is not supported in the frozen configuration. This does not refute structural non-identifiability in general or external equation-discovery results obtained under different conditions.

### 6.2 ML provenance v0.1: inconclusive because the learner could not resolve the signal

The ML-provenance study asked whether a learned one-step surrogate could resolve a small difference between two numerical teachers for the same figure-eight system: a high-accuracy DOP853 teacher and a coarser RK4 map. The numerical teachers were cleanly separated. On the held-out test block, their difference was approximately

\[
1.3\times10^{-5},
\]

while reference uncertainty was negligible in comparison.

The learner-resolvability gate, however, failed by a large margin. Median one-step test error relative to each model’s own teacher was about `0.72`, roughly `5.5×10^4` times larger than the teacher difference. The learned models therefore could not resolve the provenance signal the experiment was designed to test. The accepted status is

```text
INCONCLUSIVE_LEARNER_ERROR,
```

not negative evidence against the provenance hypothesis. The run establishes that the paired-teacher design and teacher separation were technically meaningful, but the downstream claim remains undecided because a necessary resolution condition was not met.

The distinction is simple but important:

```text
negative       -> the test was decision-capable and the criterion was not met
inconclusive   -> a necessary resolution condition failed, so the target claim was not decided
untested       -> the relevant relation was not evaluated
not applicable -> the relation was not part of the stated claim
```

### Table 3. Evidence-status discipline across project cases

| Case | Role in the manuscript | Relevant evidence status | Supported | Explicitly not supported |
|---|---|---|---|---|
| Sundman | classical conceptual control | positive historical/conceptual illustration | formal availability can coexist with poor practical evaluability | no claim of divergence; no unique Trias diagnosis |
| Figure-eight | standard V&V control | positive, use-dependent numerical evidence | solver realizations can have different trajectory/structure profiles | no new error category; no global solver winner |
| Lorenz/SINDy | inverse stress test | `INFORMATIVE_NEGATIVE` | baseline validity and several adequacy checks | no seed-robust reconstruction-induced structural effect in the frozen setup |
| ML provenance v0.1 | resolvability stress test | `INCONCLUSIVE_LEARNER_ERROR` | teacher separation and paired design | no support or refutation of the downstream provenance claim |

The cases are intentionally heterogeneous. A positive control, a negative result, and an inconclusive result are not points on one quality scale. They answer different claims.

## 7. What the role profile adds, and what adjacent frameworks already do better

The descriptive Trias is not intended to compete with mature frameworks that already govern verification, validation, provenance, scientific inference, or claim–evidence reasoning. In most cases, those frameworks provide substantially more technical detail. The relevant question is whether a small target–theory–computation vocabulary adds useful **cross-case organization** once those functions are acknowledged.

**Verification, validation, VVUQ, and model credibility** are the strongest comparator. Classical and modern approaches already distinguish qualification or conceptual validity, implementation verification, empirical or operational validation, intended use, quantities of interest, uncertainty, sensitivity, acceptance criteria, and domains of applicability [@schlesinger1979; @sargent2013; @nasa7009b2024; @nasahdbk7009b2026]. In one domain-specific example, ASME V&V 40 relates credibility requirements to medical-device decision context and model risk [@asmevv402018]. Scientific ML V&V extends credibility reasoning to learned components and data-processing choices [@jakeman2026]. For a conventional forward simulation, the role profile adds little that careful V&V cannot express more precisely. Its residual role is only to reuse the credibility relations across workflows in which theory and computation are occupied differently.

**Workflow and data provenance** represent lineage in much greater operational detail than an `R/T/C` diagram. W3C PROV centers on `Entity`, `Activity`, and `Agent`, together with relations such as usage, generation, and derivation [@w3cprov2013]; scientific-workflow systems such as CWLProv capture prospective and retrospective workflow provenance and interoperable packaging [@khan2019]. Parameters can be represented within such provenance records, but they are not a separate W3C PROV core class. The role profile contributes no new directionality or provenance semantics. At most, it adds a claim-relative epistemic typing of selected artifacts: whether an object is functioning as referent, theory-level content, or computational practice in the argument currently being assessed.

**Assurance cases and Claims–Arguments–Evidence approaches** already require evidence to be linked to a particular claim through an explicit argument and assumptions [@goodenough2012; @gsn2021]. Bridge claims are therefore not a new assurance method. The role profile supplies only a small domain-specific typing of recurrent scientific claims, indicating where an assurance-style argument is needed when evidence is intentionally carried across relations.

**Identifiability, observability, and system identification** are substantially deeper for inverse problems. Parametric structural identifiability concerns uniqueness of parameter recovery for a specified model structure [@villaverde2016]. Near-identifiability work explicitly treats structural model error and output-near-equivalence [@hadaegh1985]. SINDy and SINDy-PI supply concrete equation-discovery and robustness methods [@brunton2016; @kaheman2020]. The role profile supplies no new identifiability criterion. Its contribution is to place inverse claims—where `T` can be an output of `C`—in the same descriptive language as forward simulation, prediction, and surrogation.

**Methodological and philosophical work on machine learning** already distinguishes multiple epistemic functions; Naser’s P.E.D.U.D. framework is one explicit recent example [@naser2025]. Recent Scientific ML perspectives likewise organize methods by the degree of prior theoretical knowledge [@vinuesa2026]. The role profile does not claim to discover the plurality of scientific success. Its narrower question is what a concrete piece of evidence warrants within a particular epistemic function.

**Scientific ML, physics-informed learning, and surrogate credibility** already supply the domain-specific methods for hybrid modeling, teacher fidelity, constraint satisfaction, validation, and transfer [@karniadakis2021; @jakeman2026; @vinuesa2026]. The value of a common role profile is comparative rather than technical: the same minimal grammar can state why a physics residual concerns a different claim from a real held-out prediction, why teacher fidelity is conditional on a synthetic referent, and why a discovered symbolic equation introduces a theory-level claim requiring its own support.

The exact contribution boundary is therefore modest. The proposal is best understood as a **genealogically grounded evidence-localization vocabulary** for comparing heterogeneous computational scientific workflows. It inherits its relational skeleton from model credibility, relies on V&V for technical credibility assessment, on provenance for lineage, on assurance cases for claim–evidence argumentation, and on identifiability and system identification for inverse recoverability. Methodological and philosophical ML work and Scientific ML provide richer accounts of the individual epistemic roles AI can play.

What remains is a compact synthesis: a claim-relative referent, a theory-status, a computational role, a directly supported relation, and an explicit statement of which conclusions require a bridge. In the documented project audits, **no direct analogue was identified that combines this exact cross-case role/evidence grammar across the selected forward, predictive, surrogate, hybrid, and inverse configurations**. This is not a universal non-existence claim. The residual is a **moderate cross-domain compression**, not a new theory of credibility, and it remains vulnerable to a concrete future comparator that performs the same synthesis without loss.

## 8. Discussion: scientific success without global success

The preceding cases suggest a simple way of reading claims that a computational or AI system “works.” A model may predict measured quantities accurately, reproduce a simulator almost exactly, satisfy an embedded physical constraint, preserve selected numerical structure, or recover an interpretable equation. Each can constitute genuine scientific success. They need not be successes of the same kind, and they do not support the same further conclusions. The role profile therefore treats success as **claim-relative and relation-specific** rather than as a single global property.

This should not be read as a demand that all three relations be maximized. A black-box predictor need not be defective merely because no mechanistic theory claim is made. For a narrowly specified predictive use, `T = NONE_CLAIMED` can be the correct description rather than a low score. Likewise, `NOT_APPLICABLE` is not a penalty, and an untested relation is not automatically a failed one. The profile is not an optimization objective and does not define an ideal model at the center of a triangle.

Nor is the proposal a necessary trade-off theory. The relations can come into tension in particular scientific situations: computational tractability can motivate approximations, synthetic-data fidelity can leave real-target grounding unresolved, or a physical constraint can change the flexibility of a learned model. But none of these examples establishes a universal zero-sum geometry. There is no claim that improving one relation must worsen another, nor that every scientific model lies on a Pareto frontier between reality, theory, and computation. The descriptive claim is weaker: evidence for one relation does not, without further argument, settle the others.

“Scientific success without global success” therefore does not imply that higher-level scientific judgments are illegitimate. Projects routinely conclude that a model is credible, adequate for purpose, useful, or ready for deployment. Such judgments require V&V, uncertainty quantification, assurance arguments, domain expertise, and decision analysis. The role profile does not replace them. It asks that the evidential ingredients remain visible: which claims are directly supported, which depend on bridge premises, and which remain partial, uncertain, untested, or not applicable.

This is particularly relevant to AI for Science because learned systems can compress several epistemic roles into one computational artifact. A single model may contain physical constraints, emulate a simulator, infer latent structure, and generate predictions compared with experiment. A single performance report can therefore mix evidence with different referents and claim objects. The role profile provides a small translation layer across those activities, not a new error metric.

The practical value of this translation layer remains **untested**. The present paper establishes only internal analytical coherence across its selected cases. It has not shown that scientists make better decisions when using the vocabulary, that reviewer disagreements are reduced, or that interdisciplinary communication improves measurably. Those are empirical hypotheses for future work. A comparative case-study audit or an inter-rater study could test whether explicitly recording referent, theory status, computational role, and evidence relation changes how scientific claims are interpreted.

Several limitations follow from the same modest positioning. Assignments to `R`, `T`, and `C` can themselves be contestable; data are theory-laden, hybrid systems blur boundaries, and nested computational workflows can make a single artifact occupy different roles under different claims. The three roles are intentionally coarse and do not subsume the technical distinctions of specialist frameworks. Their purpose is only to keep a small number of recurrent epistemic questions visible across domains.

The philosophical conclusion is therefore limited but nontrivial: **computational scientific success need not be represented as an undifferentiated model property.** For interpretation, success should be localized to the claim, referent, computational role, scope, and evidence relation actually established. Scientific judgment comes afterwards, relative to the purpose of inquiry and with the specialist methods appropriate to the claims at stake.

## 9. Conclusion

The proposal developed here is not a new triangle of reality, model, and computation. Its relational skeleton is strongly anticipated by classical model credibility and modern V&V, while its individual AI-for-Science configurations are well established in their respective literatures. The residual contribution is narrower: to reinterpret target, theory, and computation as **claim-relative epistemic roles** and to use the resulting structure as a compact evidence-localization vocabulary across heterogeneous computational workflows.

This role-based reading becomes especially useful when the same computational artifact can predict, emulate, enforce theory, or infer a candidate theory. It also preserves distinctions among positive, informative negative, inconclusive, untested, and non-applicable evidence without collapsing them into a single global judgment of model quality.

The practical usefulness of the synthesis remains to be tested. Its central interpretive lesson is therefore modest: when a computational or AI system is said to work, the scientifically relevant question is what claim has actually been established, relative to which referent and scope, by which computational practice, and what additional conclusions still require independent evidence or an explicit bridge argument.

## Bibliography and project evidence

External references are maintained in `paper/references_v0_3.bib`. Citation keys in this manuscript are standardized against that file.

Project-internal numerical evidence should be cited in a final submission through the project repository and/or supplementary material, especially:

- Figure-eight Full Demonstrator v0.1;
- Inverse-Direction Scientific Full Run v0.1 (`INFORMATIVE_NEGATIVE`);
- ML Provenance Full Run v0.1 (`INCONCLUSIVE_LEARNER_ERROR`).

No external source is used as the source of those project-specific numerical values or classifications.
