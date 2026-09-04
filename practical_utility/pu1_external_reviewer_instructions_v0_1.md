# TPUT PU1 External Reviewer Instructions v0.1

**Status:** REVIEW-PACKET TEMPLATE / NOT YET SENT  
**Date:** 2026-09-04

## A. Instructions for G0 keying experts

You are reviewing short synthetic scientific vignettes designed to test how readers interpret claims about computational and AI-based scientific models. Your task is **not** to evaluate the Trias proposal and not to guess the authors’ preferred answer. Judge each claim only from the canonical fact sheet supplied for that vignette.

For each `J1–J4`, choose the best category:

- `DIRECTLY_SUPPORTED`: the stated evidence directly warrants the claim within the stated scope.
- `PARTIALLY_SUPPORTED`: the claim is directionally supported but broader/stronger than the direct evidence.
- `UNSUPPORTED_TRANSFER`: the claim imports support from a different target, relation, mechanism, or scope without a warranted bridge.
- `UNTESTED`: the claim is relevant but the vignette reports no direct test.
- `UNCERTAIN`: the available evidence bears on the claim but does not discriminate it reliably.
- `NOT_APPLICABLE`: the claim is outside the scientific use being assessed.

For `J5`, choose `ESTABLISHED`, `PARTIAL`, `UNCERTAIN`, `UNTESTED`, or `NOT_APPLICABLE`.

For `J6`, identify the principal relation and referent type using the definitions below:

- `R-T`: evidence about whether a theory/mechanism/structure claim is adequate for the target.
- `T-C`: evidence about computational implementation, constraint satisfaction, fidelity, tractability, or resolvability of theory-level content.
- `C-R`: evidence about computational output relative to the specified target/referent.
- `REAL`: physical/empirical referent.
- `SYNTHETIC`: explicitly constructed or simulator-defined referent.
- `HYBRID`: referent that combines real and constructed components.

Also flag whether the item requires specialist information not given in the vignette or permits more than one scientifically reasonable answer because of wording ambiguity.

Please complete your first round independently and do not discuss the items with other panel members before submission.

## B. Instructions for G1 information-equivalence reviewers

For each candidate, compare the canonical fact sheet with the generic control card and the Trias card. Your task is not to judge scientific correctness. Check only whether both experimental renderings contain the same underlying scientific information.

Reject equivalence if either condition:

- adds or omits an empirical/numerical result;
- adds or omits a limitation;
- changes a numerical value;
- expands or narrows scope;
- adds a scientific premise needed to answer a claim item;
- presents a stronger scientific conclusion as a fact rather than as a label/organizational cue.

The `R/T/C`, relation, and status labels are the intended treatment and do not need literal counterparts in the control card. The scientific facts those labels summarize must nonetheless be available in both arms.

Record word counts and whether visual density is comparable. Final target is a Trias/control word-count ratio between 0.90 and 1.10.

## C. Independence note

A reviewer can serve in G0 or G1, but for v0.1 it is preferable to keep the two roles separate. Anyone who helped author the candidate bank should not serve as an independent G1 reviewer. At least three of the five G0 keying experts must be external to Trias development.

## D. Confidentiality / documentation

Public release need not identify reviewers by name. The project should retain a private mapping from reviewer identity to anonymized panel ID if required for audit, while publishing at minimum:

```text
panel ID
expertise category
external/internal status
round completed
all anonymized ratings
all wording-relevant comments
```
