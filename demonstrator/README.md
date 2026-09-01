# Drei-Körper-Minimaldemonstrator

**Scientific scope:** D005  
**Technical contract:** D006  
**Code status:** minimal tested skeleton implemented; full v0.1 scientific run not yet interpreted.

Der Demonstrator prüft nicht, welcher Solver allgemein „der beste“ ist. Er untersucht, ob dieselbe synthetische Figure-eight-Zielinstanz und dieselbe Newtonsche Theorie unter verschiedenen numerischen Operationalisierungen unterschiedliche wissenschaftlich relevante Bewertungsprofile erzeugen.

## Frozen comparison

- target: planare gleichmassige Figure-eight-Choreographie;
- reference: DOP853 with primary/tight tolerances;
- baseline: fixed-step classical RK4;
- structural contrast: velocity-Verlet / kick-drift-kick;
- U1: one nominal period, trajectory-oriented use;
- U2: 100 nominal periods, structure-oriented use;
- refinement: `n = {50, 100, 200, 400, 800}` with `h=T_pub/n`.

Details: [`minimal_spec_v0_1.md`](minimal_spec_v0_1.md) and [`implementation_contract_v0_1.md`](implementation_contract_v0_1.md).

## Install and test

```bash
cd demonstrator
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
```

## Quick smoke run

```bash
trias-demo --quick --output-dir run_quick
```

Quick mode is explicitly **not** the frozen scientific experiment: it shortens U2 to five nominal periods, uses `n={50,100,200}`, and performs one timing repeat. Its purpose is only to check the execution pipeline.

## Frozen v0.1 run

```bash
trias-demo --output-dir run_v0_1
```

This produces the contract artifacts under `run_v0_1/results` and `run_v0_1/figures`.

## Epistemic guardrails

- The DOP853 reference is never called exact ground truth.
- Rounded published Figure-eight initial data do not imply exact periodic closure.
- Long-time position error alone is not a solver-quality ranking.
- `trias_audit.md` is generated from fixed rules and deliberately does not declare C05/C06 successful.
- C05 and C06 are evaluated only after the full run passes reference and refinement checks.

## Scope exclusions

No ML, chaotic case, Sundman-series evaluation, high-precision arithmetic, softening, collision regularization, or expanded parameter sweep is included in v0.1.