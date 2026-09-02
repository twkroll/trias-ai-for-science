# Code Skeleton Status v0.1

**Status:** ACCEPTED — D007  
**Akzeptiert durch:** GO  
**Depends on:** D006 accepted Implementation Contract v0.1  
**Scientific claims:** none accepted by this decision; C05/C06 require full-run interpretation.

## Implemented

- frozen Figure-eight constants and configuration;
- shared Newtonian acceleration/RHS;
- energy, linear momentum, center of mass, planar angular momentum, minimum pair distance and radial diagnostics;
- explicit fixed-step classical RK4;
- explicit kick-drift-kick velocity-Verlet;
- DOP853 primary/tight reference integrations;
- normalized RMS position error;
- relative energy error and descriptive drift slope;
- zero-angular-momentum-safe normalized angular-momentum error;
- force/RHS evaluation counting;
- U1 observed-order calculation;
- deterministic output artifacts and rule-based `trias_audit.md`;
- quick smoke mode and frozen full-run mode.

## Validation before acceptance

```text
python -m pytest -q
4 passed
```

Covered gates included initial center of mass, total linear momentum, total angular momentum, pair-force antisymmetry, finite U1 integrations, first refinement behavior and primary/tight DOP853 consistency.

A quick pipeline smoke run generated all contract artifact types. Quick-mode numerical values were not used as evidence for C05/C06.

## Accepted scope boundary

D007 accepts the implementation skeleton as a faithful minimal realization of D006. It does not accept a solver ranking or a claim of added epistemic value for the Trias.

## Subsequent execution

After D007, the frozen full v0.1 experiment is executed over U1 and U2 with all five refinements. Scientific results are documented separately and C05 is reviewed only after the reference/refinement gates are checked.