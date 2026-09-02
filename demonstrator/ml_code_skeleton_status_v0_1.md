# ML Code Skeleton Status v0.1

**Status:** READY FOR REVIEW  
**Depends on:** D010–D011  
**Scientific claims:** none yet; ML-Provenance-Claim bleibt unbewertet.

## Implementiert

- deterministische Figure-eight-Phaseninputs;
- gemeinsame paired-teacher Datengenerierung ab exakt denselben gespeicherten Inputs;
- DOP853 primary/tight one-step labels;
- coarse RK4 one-step labels mit `h=T_pub/50`;
- zusammenhängender Train/Validation/Test-Split;
- training-only Inputnormalisierung;
- Residual-MLP `12-128-128-128-12`, `tanh`, float64 CPU;
- gepaarte Seeds mit bitgleicher Initialisierung;
- full-batch Adam und vorregistriertes Early Stopping;
- own-teacher versus common-reference One-Step-Metriken;
- quantitative Provenance-Fehlerzerlegung;
- MU1/MU2-Rollout-Pipeline für den späteren Full Run;
- Checkpoint-Speicherung für jedes Teacher-/Seed-Modell;
- maschinenlesbare Config-, Dataset-, Teacher-, Training-, One-Step-, Rollout-, Provenance- und Summary-Artefakte;
- Full-Run-Figure-Pipeline für Teacher-Differenz, One-Step-Vergleich und MU1/MU2;
- nichtwissenschaftlicher `--smoke`-Modus.

## Lokale technische Validierung vor Repository-Write

Ausgeführt wurde:

```text
PYTHONPATH=src pytest -q
```

Resultat:

```text
4 passed
```

Die Tests prüfen mindestens:

1. endliche paired-teacher Datenerzeugung;
2. Reference-tight-Differenz klar unter der coarse-teacher-Differenz auf einem kleinen Testdatensatz;
3. Normalisierungsstatistiken ausschließlich aus dem Trainingssplit;
4. bitgleiche Initialparameter innerhalb eines Seed-Paares;
5. endliches Tiny-Training und endliche Vorhersagen.

## Smoke Run

Nichtwissenschaftlicher Pipeline-Smoke-Test:

```text
python -m trias_demo.ml_experiment --smoke --output-dir smoke
```

Smoke-Konfiguration verkürzt den Datensatz auf `N=60`, verwendet nur Seed `0` und höchstens 20 Epochen. Diese Einstellungen gehören **nicht** zum eingefrorenen wissenschaftlichen Experiment.

Der Smoke Run lief erfolgreich durch. Er erzeugte Checkpoints sowie Config-, Dataset-, Teacher-, Training-, One-Step-, Provenance-, Rollout- und Audit-Artefakte. Technische Checks:

```text
status = SMOKE_ONLY
reference_gate = True
paired_initialization = True
D_teacher_test = 1.3045e-05
D_ref_test = 7.2859e-14
rollout primary/tight reference max position gap = 6.6867e-10
provenance identity residual ≈ -3.55e-15
```

Die hohen ML-Fehler des absichtlich extrem kurzen Smoke-Trainings werden nicht interpretiert und sind keine Evidenz für oder gegen den Provenance-Claim.

## Noch nicht wissenschaftlich ausgeführt/entschieden

- Dataset `N=1000` als wissenschaftlicher Full Run;
- alle drei Seeds mit bis zu 5000 Epochen;
- Learner-Resolvability-Gate im eingefrorenen Experiment;
- MU1/MU2 über alle sechs Modelle;
- 3/3-Seed-Robustheit;
- Ergebnisstatus des Full Runs;
- Vergleich gegen starken Standard-ML-Provenance-/Credibility-Rahmen;
- neuer wissenschaftlicher ML-Provenance-Claim.

## Review-Empfehlung

Der ML Code Skeleton v0.1 ist technisch ausreichend, um nach Akzeptanz den eingefrorenen wissenschaftlichen Full Run auszuführen. Es werden vor diesem Run keine wissenschaftlichen Einstellungen, Splits, Teacher, Architektur-, Optimierungs- oder Seed-Entscheidungen mehr verändert.
