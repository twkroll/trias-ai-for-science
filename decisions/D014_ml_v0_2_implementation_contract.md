# D014 — ML Implementation Contract v0.2: Resolvability Repair

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D013

## Entscheidung

Der vorregistrierte `ML Implementation Contract v0.2 — Resolvability Repair` wird in der vorgelegten Form akzeptiert und eingefroren.

v0.2 verändert den wissenschaftlichen Claim-Kandidaten nicht und vergrößert die Teacher-Differenz nicht künstlich. Gegenüber v0.1 werden ausschließlich zwei aus dem `INCONCLUSIVE_LEARNER_ERROR`-Befund begründete Änderungen zugelassen:

1. ein deterministischer phase-stratifizierter Fünferblock-Split mit weiterhin exakt 60/20/20 Prozent;
2. ein gemeinsamer teacher-unabhängiger Target-Scaler, ausschließlich aus den Trainingstargets beider Teacher gemeinsam berechnet.

## Unverändert eingefroren

- Figure-eight-Zielsystem und publizierte gerundete Anfangsdaten;
- `N=1000` und `Delta_t=T_pub/50`;
- DOP853 primary/tight als Reference teacher/Cross-Check;
- exakt ein klassischer RK4-Schritt als coarse teacher;
- identische Inputs für beide Teacher;
- Residual-MLP `12-128-128-128-12`, `tanh`, float64 CPU;
- Seeds `{0,1,2}` mit bitgleicher Paarinitialisierung;
- Adam, `lr=1e-3`, Full-Batch, `max_epochs=5000`, `patience=500`, `min_delta=1e-10`;
- keine Physics-Regularisierung, keine neuen Orbits und kein Hyperparameter-/Teacher-Sweep;
- G1 Reference separation, G2 paired-control integrity und G3 Learner resolvability als verpflichtende Gates;
- MU1 = 1 nominelle Periode und MU2 = 10 nominelle Perioden;
- Provenance-Zerlegung in den ursprünglichen Rohkoordinaten.

## Neue Schutzregeln

1. Kein Block darf über mehrere Splits verteilt werden.
2. Input-Scaler verwendet ausschließlich Trainingsinputs.
3. Der Shared Target-Scaler verwendet ausschließlich `delta_ref` und `delta_rk4` aus dem Trainingssplit und ist für beide Modelle identisch.
4. Alle wissenschaftlichen Metriken werden nach Rücktransformation in Rohkoordinaten berechnet.
5. `G3a` (Train-Resolvability) ist nur diagnostisch und ersetzt G3 auf dem Testsplit nicht.
6. Scheitert G3 erneut, endet v0.2 als `INCONCLUSIVE_LEARNER_ERROR`; es erfolgt kein automatischer Rescue-Sweep.

## Revisionsbedingung

D014 wird nur revidiert, wenn die Implementierung einen technischen Widerspruch zur kontrollierten Paar-/Scalerlogik zeigt. Änderungen werden als neue Entscheidung dokumentiert.

## Nächste Abhängigkeit

v0.2-Code-Skeleton implementieren, technische Tests und einen ausdrücklich nichtwissenschaftlichen Smoke Run durchführen. Erst nach Skeleton-Review darf der eingefrorene wissenschaftliche v0.2-Full-Run gestartet werden.
