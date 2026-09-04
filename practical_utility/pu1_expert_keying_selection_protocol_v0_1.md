# TPUT PU1 Expert-Keying + Selection Protocol v0.1

**Status:** READY AS PROCEDURE / NOT EXECUTED  
**Date:** 2026-09-04  
**Decision:** D040  
**Purpose:** operationalize G0, G1, and selection of 12 main + 2 transfer vignettes without outcome-driven cherry-picking.

## 1. Current candidate pool

Main candidates:

```text
BB01–BB05  black-box prediction            = 5
SS01–SS05  synthetic surrogate             = 5
PI01–PI05  physics-informed / hybrid ML    = 5
ED01–ED05  equation discovery              = 5
------------------------------------------------
total main candidates                      = 20
```

Transfer candidates:

```text
TR01–TR04 = 4
```

Target confirmatory instrument after G0/G1:

```text
12 main vignettes = 3 per archetype
2 unformatted transfer vignettes
```

No participant outcome data may be used for this selection.

---

## 2. Mandatory pre-panel correction

Before sending the blind packet, replace `PI03-J5` with:

> **What is the status of the conservative-Hamiltonian approximation for the tested low-amplitude regime?**

The current draft wording about an “exact-conservativity claim” does not map cleanly to the five status options. No other facts in PI03 change.

This correction is author-side and occurs before any external G0 ratings.

---

## 3. Expert panel G0

### Composition

Target exactly five independent keying experts for v0.1:

```text
>= 2 philosophy of science / methodology / epistemology of modeling
>= 2 computational science / numerical modeling / Scientific ML
>= 3 experts not involved in developing the Trias project
```

One person may satisfy more than one expertise descriptor, but the externality criterion is counted by individual.

### Independence

Experts complete round 1 independently. They must not discuss cases with each other before submitting their first classifications.

### Blinding

Experts receive:

```text
canonical fact sheet
claim item text
short response-category definitions
```

They do **not** receive:

```text
author-intended keys
which items are supposed to be unsupported transfers
which cases the authors consider “strongest”
condition-specific participant hypotheses
```

For keying scientific warrant, experts should preferably judge the canonical fact sheet rather than either experimental rendering.

---

## 4. Expert response form

For each `J1–J4`, select exactly one:

```text
DIRECTLY_SUPPORTED
PARTIALLY_SUPPORTED
UNSUPPORTED_TRANSFER
UNTESTED
UNCERTAIN
NOT_APPLICABLE
```

For each `J5`, select one status:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

For each `J6`, record:

```text
principal relation: R-T / T-C / C-R / MULTIPLE / AMBIGUOUS
referent type: REAL / SYNTHETIC / HYBRID / NOT_APPLICABLE / AMBIGUOUS
```

Experts also answer:

```text
Does answering this item require specialist information not supplied in the vignette? YES / NO
Is the wording ambiguous enough that two scientifically reasonable answers are possible? YES / NO
Free-text reason if either answer is YES.
```

---

## 5. G0 item-validity rule

A scored item passes round 1 only if:

```text
>= 4 of 5 experts choose the same intended scoring category
AND
<= 1 of 5 flags missing specialist information
AND
<= 1 of 5 flags substantive wording ambiguity
```

For `J1–J4`, the intended primary distinction is whether the claim is directly warranted versus an unsupported transfer. If 4/5 agree only at a coarser level but disagree between `PARTIALLY_SUPPORTED` and `DIRECTLY_SUPPORTED`, the item can remain as a secondary item only after explicit revision; it cannot silently enter the primary binary pool.

### Vignette-level pass

A main candidate is G0-eligible only if:

```text
both intended directly-supported items pass
both intended unsupported-transfer items pass
J5 status item passes
J6 localization item passes or is retained as secondary after revision
```

At minimum, all primary `J3/J4` unsupported-transfer items and at least one supported item must pass for a vignette to remain in contention.

---

## 6. Revision round

If an item fails G0 round 1:

1. Inspect expert comments without examining any participant data (none should exist yet).
2. Revise only wording or exposition of facts already present in the canonical sheet.
3. Do not add a new scientific premise merely to force the author-intended key.
4. Produce `v0.2` of the affected vignette.
5. Send the revision to a second blinded keying round.

Preferred second round: the same five experts re-key the revised item without seeing the group vote. If availability makes that impossible, replacement experts must satisfy the same panel-composition rules and be documented.

An item that still fails 4/5 after the allowed revision round is dropped.

---

## 7. Information-equivalence gate G1

G1 is distinct from G0. Use two reviewers who did not author the vignettes and were not responsible for the author-intended keys.

For each main vignette, reviewers compare:

```text
canonical fact sheet
Condition A generic card
Condition B Trias card
```

They mark every canonical proposition as:

```text
present in A / absent in A
present in B / absent in B
same numerical value in both / mismatch
same limitation in both / mismatch
```

### G1 hard requirements

```text
all scientific facts represented in both arms
all numerical values identical
all limitations present in both arms
no empirical result added only to Trias
no negative fact omitted from control
no scope expansion in either arm
```

### Length / density target

Before final freeze, target:

```text
word-count ratio B/A between 0.90 and 1.10
similar number of visual fields / bullets after rendering
same font size and display width
```

The conceptual labels (`R`, `T`, `C`, relation, status) are the treatment and therefore need not have lexical analogues in Condition A. The underlying facts that those labels summarize must, however, be available in A.

A main vignette is not eligible for the confirmatory instrument until both G1 reviewers sign off.

---

## 8. Selection of the final 12 main vignettes

Selection occurs **after G0 and G1, before participant pilot data**.

Exactly three cases are selected from each archetype.

### Hard eligibility

```text
G0 passed
G1 passed
no unresolved specialist-knowledge flag
both primary unsupported-transfer items retained
at least one directly-supported item retained
```

### Selection score among eligible candidates

Use this prespecified score only to break ties / rank more than three eligible cases per archetype:

```text
+2  unanimous 5/5 agreement on both primary UT items
+1  5/5 agreement on at least one supported item
+1  J5 status item passes 5/5
+1  J6 localization passes >=4/5 without AMBIGUOUS votes
+1  final A/B word-count ratio in [0.95, 1.05]
+1  no expert specialist-knowledge flags
-1  required wording revision after round 1
-2  any retained primary item only passes 4/5 rather than 5/5
```

If candidates tie, prefer diversity in the *kind* of unsupported transfer within that archetype rather than choosing three near-duplicates.

Examples of desired diversity:

```text
black-box: mechanism transfer / domain extrapolation / subgroup weakness
surrogate: teacher->real transfer / simulator-credibility transfer / out-of-domain transfer
PIML: residual->theory transfer / overall prediction->regime transfer / closure->mechanism transfer
equation discovery: dynamics->structure / bootstrap instability / reduced-model->full-mechanism transfer
```

If still tied, resolve by preregistered random selection with logged seed.

### Forbidden selection criteria

Do not use:

```text
which vignette “looks most favorable” to Trias
pilot condition difference
main-study condition difference
which item gives the largest observed overclaim rate difference
post-hoc topic preference
```

---

## 9. Selection of two transfer cases

Transfer candidates must pass 4/5 keying for every scored item and must not require specialist knowledge outside the text.

Choose two cases that:

```text
cover at least two different archetypes
are not close paraphrases of selected main vignettes
contain at least one supported and one unsupported item
have no explicit R/T/C labels in participant form
```

If more than two remain equally eligible, prefer one case involving referent transfer and one involving mechanism/structure transfer. If still tied, randomize with logged seed.

---

## 10. Required artifacts after external review

Create:

```text
pu1_expert_ratings_round1.csv
pu1_expert_comments_round1.md
pu1_revision_log.md
pu1_expert_ratings_round2.csv        (if needed)
pu1_g0_decision_table.md
pu1_g1_equivalence_review.csv
pu1_final_vignette_selection_v0_1.md
pu1_final_main_cards_v0_1.md
pu1_final_transfer_cards_v0_1.md
```

The expert identities do not need to be public in the open repository if confidentiality or ethics requires otherwise; expertise categories, externality status, and anonymized panel IDs should still be documented.

---

## 11. PU1 exit gate

PU1 is complete only when:

```text
12 main cases selected = 3 per archetype
2 transfer cases selected
all final primary items G0 >= 4/5
all final paired cards G1 passed
final canonical sheets + claim items frozen
no participant outcome data have been viewed
```

If fewer than 10 main cases survive overall or any archetype has fewer than two valid cases after the revision round:

```text
classification = INCONCLUSIVE_INSTRUMENT
```

and PU2 participant-study implementation is not authorized.

If 10–11 survive or one archetype has only two, the instrument must be redesigned and re-keyed; it may not simply reduce the confirmatory coverage without a new design decision.