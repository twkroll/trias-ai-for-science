# D013 — ML v0.1 Review und v0.2 Resolvability-Richtung

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D010–D012

## Entscheidung A — v0.1 wissenschaftlich klassifiziert

Der wissenschaftliche ML Full Run v0.1 wird endgültig als

```text
INCONCLUSIVE_LEARNER_ERROR
```

klassifiziert.

Der Reference-Separation-Test und die gepaarte Initialisierung bestanden, das vorregistrierte Learner-Resolvability-Gate scheiterte jedoch klar. Der Lernfehler auf dem gehaltenen Phasenblock liegt ungefähr fünf Größenordnungen über der zu untersuchenden RK4-vs.-DOP853-Teacher-Differenz.

Daraus folgt:

1. C07 wird aus v0.1 weder akzeptiert noch verworfen.
2. One-Step- oder Rollout-Unterschiede der beiden Modellgruppen werden nicht als Teacher-Provenance-Effekt interpretiert.
3. Innerhalb v0.1 findet kein Rescue-Sweep, Architektur-Sweep, Teacher-Wechsel oder nachträgliches Split-Tuning statt.
4. Die vorregistrierten Gates gelten als wissenschaftlich produktiv, weil sie eine nicht tragfähige positive Interpretation verhindert haben.

## Entscheidung B — v0.2 Resolvability Repair

Ein separat preregistrierter v0.2-Test wird als nächste Richtung akzeptiert. Er repariert ausschließlich die in v0.1 diagnostizierte fehlende Signalauflösung.

### Akzeptierte Änderungen gegenüber v0.1

1. **Phase-stratifizierter Blocksplit:** Die 1000 geordneten Phasenpunkte werden in 200 zusammenhängende Fünferblöcke geteilt. Über einen deterministischen Fünferzyklus werden 60 % der Blöcke Training, 20 % Validation und 20 % Test zugeordnet. Alle Splits decken damit die gesamte Figure-eight-Phase ab. v0.2 ist ausdrücklich ein same-orbit interpolation/provenance test, kein neue-Orbit-Generalisationstest.
2. **Gemeinsamer teacher-unabhängiger Target-Scaler:** Ein einziger komponentenweiser Scaler wird ausschließlich aus den Trainingsinkrementen beider Teacher gemeinsam bestimmt und für beide Modelle identisch verwendet. Evaluation, Gates und Provenance-Zerlegung erfolgen nach Rücktransformation in den ursprünglichen dimensionslosen Koordinaten.

### Unverändert

- Figure-eight-Zielsystem;
- `N=1000`;
- DOP853 primary/tight als Reference teacher;
- coarse RK4 mit exakt einem Schritt `h=T_pub/50`;
- identische Inputzustände für beide Teacher;
- Residual-MLP `12-128-128-128-12`, `tanh`, float64 CPU;
- Seeds `{0,1,2}` und bitgleiche Paarinitialisierung;
- Adam, Lernrate und Trainingsbudget;
- Reference-, Teacher- und Learner-Resolvability-Gates;
- keine Physics-Regularisierung, neuen Orbits oder zusätzlichen Teacher;
- kein automatischer Sweep bei erneutem Scheitern.

## Wissenschaftliche Schutzregel

Teacher-Provenance wird in v0.2 nur interpretiert, wenn weiterhin gilt:

```text
G1: D_ref <= 0.01 * D_teacher
G2: paired inputs/splits/scalers/initialization identical
G3: median_seed(RMSE_own_teacher_test) < D_teacher_test
```

Scheitert G3 erneut, endet v0.2 wieder als `INCONCLUSIVE_LEARNER_ERROR`. Danach ist nicht automatisch ein v0.3-Tuning vorgesehen; stattdessen muss grundsätzlich entschieden werden, ob das Teacher-Signal für diesen Demonstrator zu klein gewählt ist oder ein anderer kontrollierter AI-for-Science-Fall geeigneter wäre.

## Nächste Abhängigkeit

Vor jeder Implementierung wird ein exakter `ML Implementation Contract v0.2` akzeptiert.