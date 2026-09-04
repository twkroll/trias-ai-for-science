# TPUT v0.1 — Preregistration Specification

**Status:** TEMPLATE / NOT PREREGISTERED / NO DATA  
**Date:** 2026-09-04  
**Parent:** `practical_utility/research_program_v0_1.md`

This file is a freeze template for the first confirmatory Trias Practical Utility Test. Values marked `TO_FREEZE` must be fixed before the main participant dataset is opened.

---

## A. Primary research question

Does a claim-relative `R/T/C` role-and-evidence profile reduce endorsement of unsupported cross-relation scientific claims compared with an information-equivalent generic structured claim–evidence summary?

---

## B. Design

```text
design              = randomized parallel-arm
arms                = 2
condition A          = generic structured claim/evidence/scope/limitations control
condition B          = Trias R/T/C role/evidence profile
main vignettes       = 12
unformatted transfer = 2 exploratory items
allocation           = 1:1
participant blinding = hypothesis masked; format-comparison framing
```

No participant sees both experimental reporting formats.

---

## C. Instrument freeze

Before preregistration the following must be archived and hash-identified:

```text
canonical_fact_sheets_v0_1
control_cards_v0_1
trias_cards_v0_1
claim_items_v0_1
expert_key_v0_1
training_control_v0_1
training_trias_v0_1
randomization_spec_v0_1
```

No wording changes after the first main participant is randomized unless a technical fault makes the experiment unusable. Such a fault terminates the run; it does not authorize silent item replacement.

---

## D. Expert-key gate G0

Panel target:

```text
N_experts = 5
>= 2 philosophy/methodology
>= 2 computational science/SciML
>= 3 external to Trias development
```

Primary item inclusion requires:

```text
>= 4/5 agreement on intended classification
```

Required instrument coverage:

```text
>= 10 valid main vignettes overall
>= 2 valid vignettes per archetype
all primary unsupported-transfer items keyed successfully
```

Failure classification:

```text
INCONCLUSIVE_INSTRUMENT
```

---

## E. Information-equivalence gate G1

For every vignette pair:

```text
same scientific facts
same numerical values
same reported limitations
no extra empirical result in Trias arm
no omitted negative fact in control arm
word-count ratio between arms = TO_FREEZE, recommended 0.90–1.10
```

Two independent format reviewers sign off before preregistration.

---

## F. Population and exclusions

### Inclusion

```text
advanced MSc / PhD / postdoc / research scientist / faculty
regularly reads or evaluates computational or ML-based scientific results
consent completed
```

### Primary analysis population

Intention-to-treat style: all randomized participants who satisfy only the pre-randomization inclusion criteria and the frozen minimal technical completion rule.

### Technical completion rule

`TO_FREEZE`; recommendation:

```text
>= 10 of 12 main vignettes completed
```

Do not exclude participants merely because they perform poorly on the training comprehension quiz. Comprehension is a manipulation/heterogeneity variable, not a post-randomization success filter.

### Exclusions allowed

Only preregistered reasons such as:

```text
consent withdrawn
duplicate participation
technical corruption of response file
completion below frozen threshold
```

No outcome-based exclusions.

---

## G. Sample size

Final main-study `N`:

```text
N_main = TO_FREEZE
```

Procedure:

1. usability/item pilot participants are permanently excluded from confirmatory analysis;
2. simulate the primary mixed model using pilot item difficulty and plausible participant/item variance;
3. target adequate power/precision for the frozen minimum useful effect `Delta* = -0.10`;
4. freeze `N_main` before the main run;
5. feasibility cap: `N_main <= 80 analyzable participants`.

If required `N_main > 80`:

```text
classification = NOT_FEASIBLE_AS_SMALL_MVP
```

No main collection begins.

---

## H. Primary and secondary outcomes

### P1 Primary

Binary endorsement of items expert-keyed as `UNSUPPORTED_TRANSFER`.

Primary estimand:

\[
\Delta_{overclaim}=P(Y=1\mid Trias)-P(Y=1\mid Control).
\]

Negative values favor Trias.

### P2 No-harm

Binary endorsement of directly supported claims.

\[
\Delta_{supported}=P(S=1\mid Trias)-P(S=1\mid Control).
\]

### P3 Localization

Correct classification of referent/relation/status.

### P4 Agreement

Condition-specific inter-rater agreement across keyed judgments.

### P5 Confidence calibration — exploratory

Confidence score vs expert-key correctness.

### P6 Response time — exploratory

Per-vignette time after predefined trimming rules.

### P7 Transfer — exploratory

Performance on two final unformatted vignettes common to both groups.

---

## I. Primary statistical model

Preferred model:

```text
logit(P(unsupported endorsement)) =
    beta0
  + beta1 * condition
  + beta2 * archetype
  + random_intercept(participant)
  + random_intercept(claim_item)
```

Primary inferential quantity: marginal absolute risk difference for `condition` with 95% CI.

Archetype interactions, expertise interactions, and career-stage interactions are exploratory unless the final preregistration explicitly states otherwise.

### Model diagnostics

`TO_FREEZE`; at minimum:

```text
optimizer convergence
no pathological fitted probabilities
random-effect singularity check
```

### Frozen fallback

If the main model fails its frozen diagnostics:

```text
participant-level unsupported-endorsement rate
condition difference
cluster/bootstrap CI with resampling at participant level
```

The fallback is not chosen according to which result favors Trias.

---

## J. Effect thresholds

### Minimum useful primary effect

\[
\Delta^*_{overclaim}=-0.10.
\]

### No-harm margin

\[
\Delta^*_{supported}=-0.05.
\]

Both are project decision thresholds and must remain unchanged after main outcome data are visible.

---

## K. Decision rules

### G2 Main data quality

All must pass:

```text
randomization audit passes
condition rendering technically correct
expert key remains frozen
no study-wide item corruption
completion requirements met
```

### G3 Primary utility

Pass only if:

```text
estimated Delta_overclaim <= -0.10
AND
95% CI upper bound < 0
```

### G4 No-harm

Pass only if:

```text
95% CI lower bound for Delta_supported > -0.05
```

### G5 Localization mechanism

Direction expected:

```text
Trias localization accuracy > Control localization accuracy
```

G5 is supportive and cannot rescue G3.

---

## L. Final classification algorithm

### POSITIVE_POC

```text
G0 PASS
G1 PASS
G2 PASS
G3 PASS
G4 PASS
```

### MIXED_POC

Use only for a prespecified combination such as:

```text
G3 PASS + G4 inconclusive
```

The exact mixed cases must be enumerated before preregistration completion.

### INFORMATIVE_NEGATIVE

Use only if:

```text
G0/G1/G2 PASS
AND
95% CI excludes a benefit as large as the frozen minimum useful effect
```

Operationally, if the full CI lies above `-0.10`, the study is sufficiently precise to rule out the prespecified minimum incremental benefit.

### INCONCLUSIVE_PRECISION

Use if the CI overlaps both:

```text
meaningful benefit region (<= -0.10)
and
little/no benefit region
```

### INCONCLUSIVE_INSTRUMENT

Use if G0/G1 fails or a validated instrument cannot be maintained.

### NOT_FEASIBLE_AS_SMALL_MVP

Use if the prespecified precision/power target requires more than 80 analyzable participants.

---

## M. Floor/ceiling guardrail

The usability pilot should identify obviously broken items before preregistration.

Recommended pilot target for `UNSUPPORTED_TRANSFER` items under the generic control:

```text
avoid near-zero endorsement on essentially all items
avoid near-universal endorsement on essentially all items
```

Do not use a post-hoc main-study floor/ceiling observation to delete unfavorable items. If the frozen instrument unexpectedly produces no decision range, classify the result according to the preregistered precision/instrument rules rather than repairing it after the fact.

---

## N. Multiple outcomes

Only P1/G3 is the primary superiority test.

P2/G4 is a co-required safety/no-harm gate, not an independent novelty claim.

All other outcomes are secondary or exploratory. No multiplicity-adjusted fishing across archetypes is allowed to rescue a failed primary outcome.

---

## O. Reporting obligations

Always report:

```text
participant flow by condition
all frozen vignettes and expert keys
raw condition-wise endorsement rates
primary mixed-model estimate
absolute risk difference + 95% CI
supported-claim sensitivity
all preregistered gate outcomes
all exclusions with reasons
all deviations from preregistration
```

A negative or inconclusive classification must receive the same archival treatment as a positive result.

---

## P. Non-claims

The v0.1 experiment, even if positive, will **not** establish:

```text
universal superiority of Trias
better scientific decisions in real laboratories
better peer review in general
better model validity
new V&V or assurance theory
that all scientists should use R/T/C notation
that all AI-for-Science claims fit only three relations
```

A positive result supports only the tested claim-interpretation task, population, comparator, vignette set, and scope.

---

## Q. Required freeze decisions before PU1/PU3

Before the participant experiment is authorized, the author must explicitly accept or revise:

```text
D-PU1 primary comparator = strong generic structured control
D-PU2 parallel-arm design
D-PU3 Delta* overclaim = -0.10
D-PU4 no-harm margin = -0.05
D-PU5 feasibility cap = 80 analyzable participants
D-PU6 expert-key threshold = 4/5
D-PU7 12 main + 2 transfer vignettes
D-PU8 result taxonomy
```

Until those decisions are accepted, this file is a design template rather than a preregistration.