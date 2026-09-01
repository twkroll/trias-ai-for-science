# Code Skeleton Status v0.1

**Status:** READY FOR REVIEW  
**Depends on:** D006 accepted Implementation Contract v0.1  
**Scientific claims:** none yet; C05/C06 remain unassessed.

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

## Local validation performed before repository write

Environment used for the local validation:

```text
Python: container runtime
NumPy: 2.3.5
SciPy: 1.17.0
Matplotlib: 3.10.8
pytest: 9.0.2
```

Test command:

```text
python -m pytest -q
```

Result:

```text
4 passed
```

Covered gates:

1. Figure-eight initial center of mass approximately zero;
2. initial total linear momentum approximately zero;
3. initial total angular momentum approximately zero;
4. internal pair-force antisymmetry via vanishing net internal force;
5. U1 RK4 and Verlet runs finite at `n=50,100`;
6. U1 endpoint position error decreases from `n=50` to `n=100` for both methods;
7. primary/tight DOP853 U1 reference discrepancy is small (`<1e-8` test bound).

## Quick pipeline smoke run

Executed successfully with:

```text
python -m trias_demo.experiment --quick --output-dir run_quick
```

Quick mode generated all eight required artifact types:

```text
results/reference_check.json
results/metrics.csv
results/summary.json
results/trias_audit.md
figures/u1_trajectory_error.png
figures/u2_energy_error.png
figures/error_vs_cost.png
figures/refinement_u1.png
```

Quick mode is not the frozen scientific experiment and its numerical values are not used as evidence for C05/C06.

## Deliberately not yet claimed

- full 100-period run validated;
- all five frozen refinements valid over U2;
- reference adequacy over U2;
- textbook convergence orders over the full usable refinement range;
- a scientific ranking between RK4 and Verlet;
- diagnostic added value of the Trias.

## Next dependency

Review this skeleton. If accepted, execute the frozen full v0.1 experiment and evaluate the scientific gates before interpreting C05.