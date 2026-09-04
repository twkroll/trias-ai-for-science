# Trias Practical Utility Test (TPUT) v0.1 — Research Program

**Status:** DESIGNED / NOT STARTED / SIDE PROJECT  
**Date:** 2026-09-04  
**Relation to main paper:** Follow-up project only. It must not be used to strengthen the current Perspective manuscript before data exist.  
**Primary purpose:** Test the currently explicit open claim `practical usefulness = UNTESTED`.

## 1. Motivation

The source-hardened Perspective argues only that a claim-relative Target–Theory–Computation (`R/T/C`) vocabulary can coherently localize heterogeneous forms of computational scientific evidence. It does **not** show that scientists reason more accurately, communicate more clearly, or make better review/credibility judgments when using that vocabulary.

TPUT v0.1 tests exactly that residual practical question:

> **Does an explicit R/T/C role-and-evidence profile reduce unwarranted scientific claim transfer compared with an equally structured generic claim–evidence summary?**

The project is deliberately small, falsifiable, and independent of the publication decision for the current Perspective.

---

## 2. Scientific question

### Primary research question

Given the same factual information about a computational/AI-for-Science case, does a Trias-style role profile reduce acceptance of claims that are **not directly warranted by the reported evidence**?

### Secondary questions

1. Does the Trias format preserve correct acceptance of claims that *are* directly supported?
2. Does it improve identification of the relevant referent and evidential relation?
3. Does it increase agreement among readers about what has and has not been established?
4. Does it improve confidence calibration rather than merely making readers more conservative?
5. Does any benefit generalize to an unformatted post-test case after the explicit Trias card is removed?

---

## 3. Core hypotheses

### H1 — Overclaim reduction (primary)

Participants using the Trias profile will endorse fewer **unsupported cross-relation claims** than participants using a strong generic structured control.

Examples of the targeted errors are:

```text
teacher fidelity            -> real-world validation
low physics residual        -> empirical adequacy of target model
strong real prediction      -> unique mechanistic explanation
dynamical agreement         -> structural/mechanistic identification
```

### H2 — No-harm condition

Any reduction in overclaiming must **not** be achieved merely by making participants reject claims indiscriminately. Correct endorsement of directly supported claims should therefore be non-inferior to the control condition.

### H3 — Evidence localization

Trias users should more accurately identify:

```text
referent type: REAL / SYNTHETIC / HYBRID
relevant evidence relation: R-T / T-C / C-R
status: ESTABLISHED / PARTIAL / UNCERTAIN / UNTESTED / NOT_APPLICABLE
```

### H4 — Agreement / calibration (secondary)

Trias users may show higher inter-rater agreement and better confidence calibration. These are secondary, not required for the primary success decision.

---

## 4. What would count as a genuine failure?

The project is falsifiable only if several apparently positive outcomes are **not** accepted as success.

The Trias practical-utility claim is **not supported** if:

- it does not reduce unsupported claim transfer relative to a strong structured control;
- it reduces overclaiming only because participants become globally more reluctant to endorse *any* claim;
- subjective clarity improves but objective claim judgments do not;
- benefits disappear when item ambiguity and formatting differences are controlled;
- apparent effects are driven by one vignette, one archetype, or one participant subgroup;
- the instrument cannot establish sufficiently stable expert keys for what is directly supported.

A particularly informative negative result would be:

> A generic `claim / evidence / scope / limitation` checklist performs as well as the full R/T/C profile, with sufficient precision to exclude a practically meaningful Trias advantage.

That outcome would not refute the current philosophical Perspective. It would show that the additional Trias typing has not demonstrated incremental practical value over simpler claim–evidence discipline.

---

## 5. Experimental design

### 5.1 Design choice

Use a **randomized parallel-arm experiment**, not a within-subject crossover.

Reason: once a participant has been trained in the Trias semantics, those concepts can contaminate subsequent control judgments. A parallel design avoids this carry-over problem.

### 5.2 Conditions

#### Condition A — Strong generic structured control

Each vignette is presented as a compact card with the same factual content organized under:

```text
Scientific question / use
Reported evidence
Scope / regime
Known limitations / unresolved claims
```

This is intentionally a strong comparator. The experiment must not establish only that structured presentation is better than prose.

#### Condition B — Trias role/evidence profile

The exact same factual content is organized under:

```text
R — target / referent and type
T — theory-level claim and status
C — computational practice
Directly assessed relation
Evidence
Use / scope
Status / explicit non-implication
```

The Trias condition may reorganize and label information but must contain **no factual information unavailable in the control condition**.

### 5.3 Training

Both groups receive an approximately equal-duration tutorial (target: 7–10 min) and two worked examples.

Control tutorial:

```text
claim
supporting evidence
scope
limitations
```

Trias tutorial:

```text
R / T / C roles
relation-specific evidence
status semantics
no automatic cross-relation transfer
```

Participants are told only that the study compares two scientific reporting formats. They are not told that one format is expected to reduce overclaiming.

---

## 6. Vignette bank

### 6.1 Minimal bank

Create **12 main vignettes**, three from each of the four manuscript archetypes:

```text
3 predictive black-box cases
3 synthetic-surrogate cases
3 physics-informed / hybrid cases
3 equation-discovery cases
```

Add two short **unformatted transfer vignettes** at the end for an exploratory generalization test.

### 6.2 Vignette construction rule

Each vignette should be approximately 150–220 words and contain enough information to justify at least one direct claim while leaving at least one tempting cross-relation inference unsupported.

The two conditions must be generated from one canonical fact sheet so that the scientific content is identical.

### 6.3 Suggested case logic

#### Black-box prediction

- strong held-out or prospective prediction against `R_REAL`;
- no mechanistic theory claim;
- temptation: infer mechanism/explanation from prediction.

#### Synthetic surrogate

- excellent held-out agreement with simulator teacher;
- no independent real-target evidence in at least one case;
- temptation: rewrite teacher fidelity as empirical validation.

#### Physics-informed / hybrid

- strong constraint/PDE residual or invariant satisfaction;
- separate, incomplete, or absent target validation;
- temptation: treat physics consistency as global physical validity.

#### Equation discovery

- good trajectory/statistical agreement;
- ambiguous or unstable recovered structure in at least one case;
- temptation: infer unique mechanism from dynamical adequacy.

### 6.4 Claim questions per vignette

For each main vignette, present six scored judgments:

```text
2 directly supported claims
2 unsupported cross-relation transfer claims
1 status/scope judgment
1 referent/relation-localization judgment
```

Primary analysis uses the unsupported-transfer items. Directly supported items implement the no-harm test.

---

## 7. Expert key and item-validity gate

The study requires an expert-derived answer key because the project concerns epistemic interpretation rather than elementary factual recall.

### Expert panel

Target **five experts**, with at least:

```text
2 with philosophy-of-science / methodology expertise
2 with computational science / Scientific ML expertise
3 not involved in developing the Trias project
```

Each expert independently classifies every candidate judgment as:

```text
DIRECTLY_SUPPORTED
PARTIALLY_SUPPORTED
UNSUPPORTED_TRANSFER
UNTESTED
UNCERTAIN
NOT_APPLICABLE
```

### Item-validity gate G0

A scored claim item enters the participant study only if at least **4/5 experts agree** on its intended key after the first independent round, or if a revision obtains 4/5 agreement in a second blinded round.

A vignette is retained only if:

- all primary unsupported-transfer items pass the keying criterion;
- at least one directly supported item passes;
- wording does not rely on specialist knowledge not supplied in the vignette.

The participant study does **not** begin if fewer than 10 of 12 main vignettes survive or if any of the four archetypes has fewer than two valid vignettes.

This produces classification:

```text
INCONCLUSIVE_INSTRUMENT
```

rather than silently rewriting ambiguous items.

---

## 8. Information-equivalence / formatting gate

Before participant recruitment, two independent reviewers who did not write the cards compare the control and Trias versions against the canonical fact sheet.

### Gate G1

Required:

```text
same factual propositions
no added result in Trias condition
no omitted limitation in control condition
word count difference ideally <= 10%
comparable visual density
same numerical values and scope statements
```

Any failed item is revised before preregistration.

---

## 9. Participants

### Target population

Researchers or advanced graduate students who regularly interpret computational or machine-learning results in science or engineering.

Suggested inclusion pool:

```text
advanced MSc students
PhD researchers
postdoctoral researchers
faculty / research scientists
```

Record, but do not make primary inclusion depend on:

```text
discipline
career stage
ML experience
numerical-methods experience
philosophy-of-science training
prior familiarity with V&V
```

These variables are exploratory moderators only.

### Sample-size strategy

Do **not** choose the final confirmatory `N` after viewing the main outcome.

Recommended workflow:

1. small usability/item pilot with participants who will not enter the main analysis;
2. use pilot item difficulty and plausible random-effect variances in a simulation-based power/precision calculation;
3. power the main study to detect the preregistered minimum useful reduction in unsupported endorsement;
4. freeze `N` before the main run.

For planning, an analyzable sample around **48–60 participants** (24–30 per arm) is a realistic MSc-project target, but this number is provisional until the simulation is completed.

If the required sample for the frozen minimum effect exceeds a predefined feasibility cap of **80 analyzable participants**, classify the current design as:

```text
NOT_FEASIBLE_AS_SMALL_MVP
```

and redesign before collection rather than running an underpowered study.

---

## 10. Outcomes

### Primary outcome P1 — unsupported-claim endorsement

For each `UNSUPPORTED_TRANSFER` item:

```text
1 = participant endorses the claim as warranted by the vignette
0 = participant correctly does not endorse it
```

Primary estimand:

```text
Delta_overclaim = P(endorse unsupported | Trias)
                - P(endorse unsupported | Control)
```

Negative values favor Trias.

### Secondary outcome P2 — supported-claim sensitivity

```text
Delta_supported = P(endorse supported | Trias)
                - P(endorse supported | Control)
```

This protects against a merely conservative response strategy.

### Secondary outcome P3 — localization accuracy

Accuracy for:

```text
referent type
R-T / T-C / C-R relation
status semantics
```

### Secondary outcome P4 — inter-rater agreement

Compare agreement across participants in the two conditions for the same vignette/claim judgments.

### Exploratory P5 — confidence calibration

Participants provide confidence ratings for each claim judgment. Compare calibration against the expert key rather than raw confidence alone.

### Exploratory P6 — response time

Record per-vignette response time. A useful format need not be faster, so time is descriptive unless a later study explicitly targets efficiency.

### Exploratory P7 — unformatted transfer

After the main task, both groups receive two identical plain-text vignettes without either card. This asks whether Trias training produces transferable reasoning rather than only card-dependent performance.

---

## 11. Primary analysis

### Main model

Analyze claim-level binary outcomes with a mixed-effects logistic model using crossed participant and item effects, conceptually:

```text
unsupported_endorsement ~ condition + archetype
                        + (1 | participant)
                        + (1 | claim_item)
```

The primary test is the marginal condition effect. `condition × archetype` is exploratory unless a later preregistration explicitly promotes it.

Report:

```text
odds ratio
model-based marginal probabilities
absolute risk difference Delta_overclaim
95% confidence interval
```

### Robustness / fallback

If the mixed model is singular or fails prespecified convergence diagnostics, use a preregistered cluster-bootstrap analysis of participant-level overclaim rates. The fallback is fixed before the main data are inspected.

No researcher degrees of freedom are allowed in choosing whichever analysis gives a more favorable result.

---

## 12. Frozen practical-effect threshold

For v0.1, the recommended **minimum useful effect** is an absolute reduction of

```text
10 percentage points
```

in unsupported claim endorsement:

\[
\Delta^*_{overclaim} = -0.10.
\]

This is a project decision threshold, not a universal psychological constant. It must be frozen before the main run.

The no-harm non-inferiority margin for directly supported claims is:

\[
\Delta^*_{supported} = -0.05.
\]

A Trias format that reduces overclaiming by causing a large loss in correct claim acceptance does not count as practical success.

---

## 13. Decision gates

### G2 — Main data quality

Required before interpreting H1:

```text
predefined completion threshold met
no condition-specific technical failure
no catastrophic floor/ceiling created by broken items
randomization integrity verified
expert key unchanged after data collection begins
```

### G3 — Primary practical-utility gate

Pass only if both are true:

```text
point estimate Delta_overclaim <= -0.10
95% CI excludes 0 in the beneficial direction
```

### G4 — No-harm gate

Pass if the lower confidence bound for `Delta_supported` is above the frozen `-0.05` non-inferiority margin.

### G5 — Mechanism/supporting evidence

Referent/relation localization should improve in the expected direction. This supports interpretation but is not allowed to rescue a failed G3.

---

## 14. Result taxonomy

### POSITIVE_POC

```text
G0/G1/G2 pass
G3 overclaim reduction passes
G4 no-harm passes
```

Interpretation: evidence supports incremental practical utility of the Trias profile over a strong generic structured comparator within the tested population and vignettes.

### MIXED_POC

Examples:

```text
G3 passes but G4 is inconclusive
or
objective effect is positive but limited to a prespecified subset
```

No global utility claim.

### INFORMATIVE_NEGATIVE

Use only if the instrument and main study are decision-capable and the confidence interval is sufficiently precise to rule out the frozen `10 percentage point` minimum benefit.

Interpretation:

> The study did not support practically meaningful incremental Trias utility over the generic structured comparator in the tested setting.

### INCONCLUSIVE_PRECISION

Use if the confidence interval spans both a practically meaningful benefit and little/no benefit.

### INCONCLUSIVE_INSTRUMENT

Use if expert keying, information equivalence, or item validity fails.

### NOT_FEASIBLE_AS_SMALL_MVP

Use if the required main-study sample exceeds the frozen feasibility cap.

---

## 15. Anti-cherry-picking rules

Before the main run:

- freeze all vignette texts and answer keys;
- freeze the primary outcome and minimum effect;
- freeze exclusion rules;
- freeze the main statistical model and fallback;
- freeze the success taxonomy;
- preregister archetype interactions as exploratory unless explicitly powered;
- do not replace difficult vignettes after observing condition effects;
- do not redefine `UNSUPPORTED_TRANSFER` after participant data are visible.

Negative and inconclusive outcomes remain publishable project outcomes and must not trigger an unplanned v0.2 designed solely to manufacture a positive result.

---

## 16. Ethics and data governance

Because the study involves human participants, institutional ethics requirements must be checked before recruitment. The default design should collect only minimal professional-background metadata, avoid sensitive personal data, use informed consent, and store de-identified responses.

Recommended reproducibility package:

```text
frozen vignette bank
canonical fact sheets
condition renderings
expert-key data
preregistration
analysis code
de-identified participant data where ethically permitted
result report
```

---

## 17. Work packages

### PU0 — Concept freeze

Deliverables:

```text
research_program_v0_1.md
preregistration_spec_v0_1.md
accepted primary estimand
accepted result taxonomy
```

No participant data.

### PU1 — Vignette bank

Create 18–20 candidate vignettes, expert-key them, retain the best 12 + 2 transfer cases.

**Exit criterion:** G0 + G1 pass.

### PU2 — Survey / experiment implementation

Build both condition renderings from canonical fact sheets, randomization, timers, confidence ratings, export schema, and deterministic item IDs.

**Exit criterion:** technical dry run passes; no scientific results analyzed.

### PU3 — Pilot + sample-size freeze

Run a small non-confirmatory usability pilot, estimate item difficulty, perform simulation-based power/precision analysis, and freeze main `N`.

**Exit criterion:** design is decision-capable within feasibility cap.

### PU4 — Main preregistered run

Recruit, randomize, collect, lock dataset, then analyze once under the frozen plan.

### PU5 — Result classification

Produce exactly one main classification:

```text
POSITIVE_POC
MIXED_POC
INFORMATIVE_NEGATIVE
INCONCLUSIVE_PRECISION
INCONCLUSIVE_INSTRUMENT
NOT_FEASIBLE_AS_SMALL_MVP
```

### PU6 — Only after result acceptance

If positive: design a stronger external-validity study on real manuscript excerpts/reviewer tasks.  
If negative: do not rescue the claim with arbitrary redesign; identify whether the generic checklist is sufficient.  
If inconclusive: repair only the failed decision-capability component.

---

## 18. Eight-week MSc-scale schedule

A realistic small-project schedule after ethics/participant access is available:

```text
Week 1   candidate vignette bank + canonical fact sheets
Week 2   expert keying + revision
Week 3   survey implementation + information-equivalence audit
Week 4   usability pilot + sample-size simulation + preregistration freeze
Weeks 5–6  participant recruitment and main collection
Week 7   locked analysis + robustness checks
Week 8   result report + archive + decision
```

Ethics-review time is external to this schedule.

---

## 19. Why this is a useful follow-up to the current paper

The current Perspective can legitimately end with:

```text
practical usefulness = UNTESTED
```

TPUT tests that statement without rewriting the paper retrospectively.

A positive result would permit a later, separate claim:

> In a controlled claim-interpretation task, the R/T/C profile reduced unsupported cross-relation inference relative to a strong generic claim–evidence control without reducing sensitivity to supported claims.

A negative result would be equally clarifying:

> The philosophical synthesis may remain descriptively coherent, but its additional practical value over a simpler structured claim–evidence checklist was not supported.

That is the desired scientific asymmetry: the follow-up can genuinely strengthen, narrow, or fail to support the practical-utility hypothesis.

---

## 20. Recommended project boundary

**Recommendation:** accept TPUT v0.1 as a side-project design, but keep it outside the main Perspective until an actual preregistered result exists.

The next action, if accepted, should be **PU1 only**: build and expert-key the vignette bank. Do not implement the participant study before the instrument itself passes G0/G1.