# C07 — ML-Provenance und zielsystemrelative Surrogatgüte

**Status:** NOT ASSESSABLE FROM v0.1  
**Run status:** `INCONCLUSIVE_LEARNER_ERROR`  
**Stand:** 2026-09-02

## Kandidat

> Gute ML-Güte relativ zu simulationsgenerierten Trainingslabels rechtfertigt nicht automatisch eine gleich starke Aussage über das wissenschaftliche Zielsystem; die epistemische Bewertung eines Surrogats muss die Provenance des Datengenerators berücksichtigen.

Dieser Satz bleibt ein **Claim-Kandidat** und wird aus dem aktuellen Experiment weder akzeptiert noch verworfen.

## Warum v0.1 nicht entscheidet

Das numerische Teacher-Signal auf dem Testsplit beträgt

```text
D_teacher ≈ 1.3035e-05
```

während die mediane own-teacher Test-RMSE der trainierten Surrogate ungefähr

```text
ref-trained: 0.7187
rk4-trained: 0.7172
```

beträgt.

Damit ist der Lernfehler etwa fünf Größenordnungen größer als die zu unterscheidende Teacher-Differenz. Das in D011 vorregistrierte Learner-Resolvability-Gate scheitert eindeutig.

Auch die exakte Provenance-Zerlegung bestätigt die Skalenproblematik: der quadratische Teacher-Beitrag ist von Ordnung `2e-09`, der Modellbeitrag von Ordnung `1` bis `10`.

## Konsequenz

Keine seed-wise Rangfolge, keine One-Step-Differenz und kein MU1/MU2-Unterschied darf als Evidenz für einen Teacher-Provenance-Effekt interpretiert werden.

Der aktuelle Run ist deshalb **inconclusive**, nicht negativ gegenüber dem Claim und nicht positiv für die Trias.

## Erforderliche Bedingung vor erneuter Prüfung

Eine v0.2 darf C07 erst erneut testen, wenn bereits vor der eigentlichen Provenance-Interpretation demonstriert ist, dass der gemeinsame Learner die Teacher-Map auf einer nicht-leakenden gehaltenen Auswertung mit Fehler deutlich unterhalb von `D_teacher` approximieren kann.

Änderungen gegenüber v0.1 müssen separat preregistriert und als neue Entscheidung dokumentiert werden; es findet kein nachträglicher Sweep innerhalb v0.1 statt.