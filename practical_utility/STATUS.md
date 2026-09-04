# TPUT Side-Project Status

## Phase

**TPUT v0.1 / PU1 Candidate Bank Built / External G0+G1 Pending**

**Date:** 2026-09-04

## Decision state

D040 accepts the Trias Practical Utility Test as a side project and freezes the v0.1 design choices:

```text
primary comparator   = strong generic structured claim/evidence/scope/limitations control
design               = randomized parallel arm
minimum useful effect= Delta_overclaim* = -0.10
no-harm margin       = Delta_supported* = -0.05
feasibility cap      = 80 analyzable participants
expert key threshold = 4/5
final instrument     = 12 main + 2 transfer vignettes
```

The side project remains independent of the current Perspective manuscript. Main-paper practical usefulness remains:

```text
UNTESTED
```

until a preregistered TPUT result exists.

## PU1 internal build

Complete author-side artifacts:

```text
pu1_vignette_bank_A_v0_1.md          5 black-box + 5 surrogate candidates
pu1_vignette_bank_B_v0_1.md          5 PIML/hybrid + 5 equation-discovery candidates
pu1_transfer_candidates_v0_1.md      4 unformatted transfer candidates
pu1_author_intended_keys_v0_1.md     blinded author key
pu1_expert_keying_selection_protocol_v0_1.md
pu1_external_reviewer_instructions_v0_1.md
pu1_expert_rating_sheet_template.csv
pu1_g1_equivalence_sheet_template.csv
pu1_candidate_bank_evaluation_v0_1.md
```

Pool:

```text
20 main candidates = 5 per archetype
4 transfer candidates
```

Internal classification:

```text
PU1-A candidate construction = COMPLETE
G0 expert keying             = NOT RUN
G1 information equivalence   = NOT RUN
PU1 exit gate                = NOT YET PASSED
PU2 survey implementation    = NOT AUTHORIZED
```

## Mandatory pre-G0 correction

Replace `PI03-J5` by:

> What is the status of the conservative-Hamiltonian approximation for the tested low-amplitude regime?

Intended author status: `PARTIAL`.

This correction must be made in the blind expert packet before G0 round 1.

## Next dependency

Obtain independent external review:

```text
G0: 5 keying experts; >=2 philosophy/methodology, >=2 computational/SciML, >=3 external to Trias development
G1: 2 independent information-equivalence reviewers
```

After G0/G1, select exactly:

```text
3 black-box
3 surrogate
3 PIML/hybrid
3 equation-discovery
2 transfer
```

using the prespecified selection protocol and without participant outcome data.

## Stop condition

No participant recruitment, survey implementation, or pilot starts until G0/G1 pass. Failure to obtain a stable expert key is an instrument result, not permission for silent post-hoc rewriting.