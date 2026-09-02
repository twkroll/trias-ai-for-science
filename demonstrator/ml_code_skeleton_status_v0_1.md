# ML Code Skeleton Status v0.1

**Status:** ACCEPTED — D012  
**Depends on:** D010–D011  
**Scientific claims:** none yet; ML-Provenance-Claim bleibt unbewertet.

## Entscheidung

Der getestete ML Code Skeleton v0.1 wird als faithful implementation des eingefrorenen ML Implementation Contract v0.1 akzeptiert. Der wissenschaftliche Full Run darf nun mit exakt den vorregistrierten Einstellungen ausgeführt werden.

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
- MU1/MU2-Rollout-Pipeline;
- Checkpoint-Speicherung für jedes Teacher-/Seed-Modell;
- maschinenlesbare Config-, Dataset-, Teacher-, Training-, One-Step-, Rollout-, Provenance- und Summary-Artefakte;
- Full-Run-Figure-Pipeline;
- nichtwissenschaftlicher `--smoke`-Modus.

## Technische Validierung vor Akzeptanz

```text
PYTHONPATH=src pytest -q
4 passed
```

Der nichtwissenschaftliche Smoke Run (`N=60`, Seed 0, maximal 20 Epochen) lief vollständig durch. Er erfüllte das Reference-Gate, bestätigte bitgleiche Paarinitialisierung und schloss die Provenance-Fehleridentität bis ungefähr `3.6e-15`. Diese Smoke-Werte sind keine wissenschaftliche Evidenz.

## Mitakzeptierte Grenzen

1. Der Full Run verwendet unverändert `N=1000`, Seeds `{0,1,2}`, maximal 5000 Epochen und die in D011 registrierten Gates.
2. Vor Sichtung der Full-Run-Ergebnisse werden keine Splits, Teacher, Architektur-, Optimierungs-, Seed- oder Normalisierungsentscheidungen verändert.
3. Ein nichtinformativer oder negativer Full Run löst keinen Hyperparameter-Sweep aus.
4. Ein möglicher ML-Provenance-Claim wird erst nach Gate-Prüfung, MU1/MU2-Auswertung und erneutem Vergleich mit einem starken Standard-ML-Provenance-/Credibility-Rahmen entschieden.

## Nächste Abhängigkeit

Den eingefrorenen wissenschaftlichen ML Full Run ausführen und zunächst ausschließlich die vorregistrierten Gates und Resultate auswerten.