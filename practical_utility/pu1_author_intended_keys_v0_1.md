# TPUT PU1 Author-Intended Keys v0.1

**Status:** AUTHOR KEY / BLINDED FROM EXTERNAL G0 ROUND 1  
**Date:** 2026-09-04  
**Applies to:** `pu1_vignette_bank_A_v0_1.md`, `pu1_vignette_bank_B_v0_1.md`, `pu1_transfer_candidates_v0_1.md`

## Use rule

This file records the instrument designers’ intended classification. It is **not** the valid expert key. External G0 experts must classify candidate items independently without seeing this file. The author key may be compared with expert judgments only after round-1 responses are locked.

For `J1–J4`:

```text
DS = DIRECTLY_SUPPORTED by the vignette
UT = UNSUPPORTED_TRANSFER / not warranted by the vignette
```

For `J5`, the intended answer uses the descriptive status vocabulary:

```text
ESTABLISHED / PARTIAL / UNCERTAIN / UNTESTED / NOT_APPLICABLE
```

For `J6`, the intended answer identifies the principal relation(s) and referent. `C-R` means computational output relative to the specified target/referent; `T-C` means implementation/constraint/fidelity of theory-level content; `R-T` means theory/mechanism/structure adequacy relative to the target.

---

# 1. Black-box prediction

| ID | J1 | J2 | J3 | J4 | J5 intended status | J6 intended localization |
|---|---|---|---|---|---|---|
| BB01 | DS | DS | UT | UT | `UNTESTED` for other manufacturer + temperature protocol | `C-R`, `R=REAL` physical held-out cells |
| BB02 | DS | DS | UT | UT | `UNTESTED` for different instrument / extreme metallicity regime | `C-R`, `R=REAL` physical stars |
| BB03 | DS | DS | UT | UT | `UNTESTED` outside tested Reynolds interval | `C-R`, `R=REAL` wind-tunnel drag |
| BB04 | DS | DS | UT | UT | `UNTESTED` for unseen polymer family | `C-R`, `R=REAL` measured conductivity |
| BB05 | DS | DS | UT | UT | `PARTIAL` for strong >6 m storm claim because rare extreme cases occur but evidence is sparse | `C-R`, `R=REAL` buoy observations |

### Rationale pattern

The intended discrimination is deliberately not “black box = bad.” Prediction relative to real observations can be directly supported while mechanistic interpretation is `NONE_CLAIMED` or unsupported. Extrapolation beyond tested domains is not silently licensed.

---

# 2. Synthetic surrogates

| ID | J1 | J2 | J3 | J4 | J5 intended status | J6 intended localization |
|---|---|---|---|---|---|---|
| SS01 | DS | DS | UT | UT | `UNTESTED` real wind-tunnel accuracy | `C-R_SYNTHETIC`: surrogate vs RANS simulator outputs |
| SS02 | DS | DS | UT | UT | `UNTESTED` historical-observation validation | `C-R_SYNTHETIC`: emulator vs ESM-X outputs |
| SS03 | DS | DS | UT | UT | `UNTESTED` experimental spectroscopy/thermodynamics | `C-R_SYNTHETIC`: neural potential vs chosen DFT outputs |
| SS04 | DS | DS | UT | UT | `UNTESTED` real-discharge validation | `C-R_SYNTHETIC`: surrogate vs gyrokinetic simulator outputs |
| SS05 | DS | DS | UT | UT | `UNTESTED` outside permeability-prior family | `C-R_SYNTHETIC`: surrogate vs calibrated simulator outputs |

### Rationale pattern

The principal intended error is silent referent transfer: a numerical metric against a simulator supports fidelity to a synthetic referent, not automatically accuracy against a physical target. Prior simulator calibration/verification can be a bridge premise but is not equivalent to the surrogate’s own real-target validation.

---

# 3. Physics-informed / hybrid ML

| ID | J1 | J2 | J3 | J4 | J5 intended status | J6 intended localization |
|---|---|---|---|---|---|---|
| PI01 | DS | DS | UT | UT | `PARTIAL` adequacy of homogeneous heat model in defect regime | PDE residual -> `T-C`; withheld sensors -> `C-R_REAL` |
| PI02 | DS | DS | UT | UT | `PARTIAL` completeness during extremes because ungauged tributary is omitted | balance discrepancy -> `T-C`; gauge MAE -> `C-R_REAL` |
| PI03 | DS | DS | UT | UT | **REVISE BEFORE G0**; current “exact conservativity” wording does not map cleanly to the five-status vocabulary. Recommended J5: “What is the status of the conservative-Hamiltonian approximation for the tested low-amplitude regime?” Intended=`PARTIAL`. | energy drift -> `T-C`; physical rollout -> `C-R_REAL` |
| PI04 | DS | DS | UT | UT | `PARTIAL` complete-theory adequacy because constraints omit turbulence/stratification physics | continuity residual -> `T-C`; mast RMSE -> `C-R_REAL` |
| PI05 | DS | DS | UT | UT | `UNCERTAIN` unique chemical-pathway identification | held-out field RMSE -> `C-R_REAL`; pathway uniqueness -> `R-T` |

### Rationale pattern

Constraint satisfaction and empirical prediction are separate evidence channels. The intended utility test should catch a common globalizing inference: “physics constraint satisfied” does not automatically imply “the encoded theory is complete for the physical target.”

---

# 4. Equation discovery

| ID | J1 | J2 | J3 | J4 | J5 intended status | J6 intended localization |
|---|---|---|---|---|---|---|
| ED01 | DS | DS | UT | UT | `UNCERTAIN` unique structural recovery | frequency agreement -> target-relative dynamical `C-R_SYNTHETIC`; unique structure -> `R-T` |
| ED02 | DS | DS | UT | UT | `PARTIAL` seed-robust exact recovery: true term appears in 13/20, not 20/20 | support recovery -> structural `R-T` evidence; period -> dynamical `C-R_SYNTHETIC` |
| ED03 | DS | DS | UT | UT | `UNCERTAIN` unique mechanistic identification | reduced-coordinate held-out dynamics -> `C-R_REAL`; unique nonlinear mechanism -> `R-T` |
| ED04 | DS | DS | UT | UT | `UNCERTAIN` unique reaction pathway | held-out concentrations -> `C-R_REAL`; pathway uniqueness -> `R-T` |
| ED05 | DS | DS | UT | UT | `UNCERTAIN` weak extra couplings | known-coupling comparison -> structural `R-T`; held-out phase trajectories -> `C-R_REAL` |

### Rationale pattern

The intended discrimination is dynamical/statistical adequacy versus structural/mechanistic identification. `T` is an inference output here; good forward behavior does not by itself make the inferred structure unique.

---

# 5. Transfer candidates — author key

| ID | Item | Intended key | Rationale |
|---|---|---|---|
| TR01 | T1 | DS | direct surrogate-to-simulator held-out fidelity |
| TR01 | T2 | UT | teacher RMSE is not gauge RMSE |
| TR01 | T3 | DS | separate gauge comparison is direct real-target evidence |
| TR01 | T4 | UT | surrogate teacher fidelity does not validate simulator physics |
| TR02 | T1 | DS | held-out patient activation-time error directly reported |
| TR02 | T2 | UT | eikonal residual does not establish complete cellular mechanism |
| TR02 | T3 | DS | high-scar subgroup has larger reported error |
| TR02 | T4 | UT | prediction does not establish unique latent mechanism |
| TR03 | T1 | DS | both models pass selected held-out dynamical criteria |
| TR03 | T2 | UT | lower RMSE does not uniquely identify pathway |
| TR03 | T3 | DS | pathway-discriminating intermediate is unmeasured; targeted test absent |
| TR03 | T4 | UT | similar period does not imply physical equivalence in every respect |
| TR04 | T1 | DS | held-out fifth-batch baseline comparison is direct |
| TR04 | T2 | UT | saliency without intervention/assay does not establish causality |
| TR04 | T3 | DS | screening claim within original protocol is tested |
| TR04 | T4 | UT | different staining protocol untested |

---

# 6. Expected expert-key outcomes and permissible revisions

The external panel may reject these intended keys. That is the purpose of G0. The following rules apply:

1. If <4/5 experts agree on an item in round 1, it is not scored in the current form.
2. A wording revision may clarify information already present in the canonical fact sheet; it may not add a premise that makes the intended answer easier.
3. Revised items undergo a second blinded round.
4. If 4/5 agreement is still not achieved, drop the item/candidate rather than force the author key.
5. Any disagreement that reveals a conceptual ambiguity in `R/T/C` classification must be documented as an instrument finding, not hidden.

## Pre-G0 author correction required

`PI03-J5` should be reworded before the external packet is distributed:

> **Revised PI03-J5:** What is the status of the conservative-Hamiltonian approximation for the tested low-amplitude regime?

Author-intended status: `PARTIAL`, because conservative structure is empirically useful in the tested weak-damping regime while the physical apparatus is known not to be exactly conservative.

No other author-side item is currently flagged as requiring mandatory revision before round 1, but external reviewers are expected to identify further ambiguities.