# TPUT PU1 Candidate-Bank Evaluation v0.1

**Status:** INTERNAL INSTRUMENT BUILD COMPLETE / EXTERNAL G0+G1 PENDING  
**Date:** 2026-09-04  
**Decision:** D040

## 1. Scope completed internally

PU1-A has produced a complete first candidate pool:

```text
20 paired main candidates
= 5 black-box prediction
+ 5 synthetic surrogate
+ 5 physics-informed / hybrid ML
+ 5 equation discovery

4 unformatted transfer candidates
```

For all 20 main candidates the repository now contains:

```text
canonical fact sheet
generic structured control rendering
Trias role/evidence rendering
2 directly-supported candidate items
2 unsupported-transfer candidate items
1 status item
1 relation/referent localization item
```

Separate author-intended keys and reviewer procedures are also prepared.

## 2. Main scientific balance

The bank deliberately samples different non-implication structures rather than repeating one teacher-fidelity pattern.

### Black-box prediction

```text
prediction -> mechanism                 BB01/BB02/BB03/BB05
held-out domain -> new domain           BB01–BB05
cross-lab vs cross-family distinction   BB04
rare-regime evidence                    BB05
```

### Synthetic surrogate

```text
teacher fidelity -> real validation     SS01–SS05
solver/calibration evidence -> target validity  SS01/SS05
single simulator -> model-form certainty       SS02
chosen DFT level -> experimental truth          SS03
in-domain fidelity -> extrapolation             SS04/SS05
```

### Physics-informed / hybrid

```text
constraint satisfaction -> theory adequacy      PI01–PI04
average prediction -> difficult-regime claim    PI01/PI02/PI04
learned closure -> unique mechanism              PI05
structure preservation -> target ontology        PI03
```

### Equation discovery

```text
dynamical adequacy -> unique structure           ED01–ED04
seed/bootstrap instability                       ED02/ED05
reduced model -> full mechanism                   ED03
constraint satisfaction -> unique pathway        ED04
small-disturbance fit -> large-event stability   ED05
```

This gives the intended instrument more semantic breadth than a single archetype would provide.

## 3. Strength of comparator

The generic control condition is intentionally strong. It explicitly lists scientific question/use, evidence, scope, and unresolved limitations. Therefore a positive TPUT result cannot be interpreted merely as “structured reporting beats prose.” It would have to reflect incremental value of the role/evidence organization.

This makes a null or informative-negative result genuinely possible and scientifically meaningful.

## 4. Author-side concerns identified before external review

### C1 — PI03-J5 wording

The current Bank-B text asks about an “exact-conservativity claim,” but the five status options do not contain a simple `REFUTED/CONTRADICTED` category. This is already flagged for mandatory pre-G0 replacement by:

> What is the status of the conservative-Hamiltonian approximation for the tested low-amplitude regime?

Author-intended key: `PARTIAL`.

### C2 — J6 can favor the treatment by design

The Trias condition explicitly names relations; the generic control does not. Therefore localization accuracy (`J6`) is a legitimate **secondary manipulation-linked outcome**, but it must not be treated as independent evidence of practical utility if the primary unsupported-transfer outcome fails.

This is already compatible with the preregistration, where G5 cannot rescue G3.

### C3 — Card length has not yet passed a mechanical 10% test

The paired cards were authored for fact equivalence, not yet mechanically normalized for word count. G1 must count and revise wording before freeze. This is an editorial instrument issue, not a scientific result.

### C4 — Some status items are intentionally harder

`BB05`, `PI01–PI05`, and `ED01–ED05` include `PARTIAL` or `UNCERTAIN` rather than only `UNTESTED`. This is desirable for avoiding a trivial status task, but those items are expected to be the main source of expert disagreement. They should be dropped or clarified if 4/5 keying cannot be obtained.

### C5 — Domain knowledge must not leak into scoring

The vignettes use batteries, stars, fluids, climate, molecular simulation, plasma, hydrology, reaction systems, power grids, and other domains. Experts must judge only supplied facts. Any item that requires external domain assumptions fails the specialist-information guardrail.

## 5. Internal gate result

The author-side instrument-construction gate is:

```text
candidate quantity                = PASS
four-archetype balance            = PASS
paired renderings present         = PASS
author intended keys present      = PASS
transfer pool present             = PASS
primary falsifiability preserved  = PASS
G0 external expert agreement      = NOT RUN
G1 independent equivalence review = NOT RUN
------------------------------------------------
PU1 INTERNAL BUILD                = COMPLETE
PU1 EXIT GATE                     = NOT YET PASSED
```

This distinction is essential. The project must not label PU1 itself `PASS` until independent G0 and G1 are actually completed.

## 6. Files produced

```text
practical_utility/pu1_vignette_bank_A_v0_1.md
practical_utility/pu1_vignette_bank_B_v0_1.md
practical_utility/pu1_transfer_candidates_v0_1.md
practical_utility/pu1_author_intended_keys_v0_1.md
practical_utility/pu1_expert_keying_selection_protocol_v0_1.md
practical_utility/pu1_external_reviewer_instructions_v0_1.md
practical_utility/pu1_expert_rating_sheet_template.csv
practical_utility/pu1_g1_equivalence_sheet_template.csv
```

## 7. Required next dependency

The next scientific step cannot be completed by the project authors alone. It requires external review:

### PU1-B — G0 expert keying

Recruit five experts meeting the frozen panel composition and obtain independent round-1 classifications.

### PU1-C — G1 information-equivalence review

Recruit two independent reviewers and audit paired card content/length.

Only after those ratings are locked should the project select the final three cases per archetype and two transfer cases under the prespecified ranking rule.

## 8. Recommendation

**Accept the internal PU1 candidate bank as READY_FOR_EXTERNAL_KEYING, not as a completed valid instrument.**

Do not implement PU2 yet.

The next useful author task, if external reviewers are not immediately available, is only logistical: prepare a reviewer packet/export and identify the five G0 + two G1 reviewers. No survey participant recruitment should start before G0/G1 pass.