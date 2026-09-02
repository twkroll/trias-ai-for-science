# Inverse-Direction Scientific Full Run v0.1

**Status:** COMPLETE / PENDING SCIENTIFIC REVIEW  
**Stand:** 2026-09-02  
**Depends on:** D018, D019  
**Pre-registered result class:** `INFORMATIVE_NEGATIVE`

## 1. Gate results

### G1 — reference

**PASS.** Der maximale normierte Abstand zwischen DOP853 primary und tight reference auf `[0,10]` beträgt

```text
4.7727891186720604e-12
```

und liegt damit klar unter `1e-8`.

### G2 — mask integrity

**PASS.** Für Seeds `{0,1,2}` wurden jeweils exakt 800 zulässige Missingness-Indizes erzeugt. P1/P2 desselben Seeds verwenden dieselbe Maske; die Mask-Hashes stimmen paarweise überein. Alle Rekonstruktionen sind endlich.

### G3 — P0 structural baseline

**PASS.** P0 rekonstruiert exakt den wahren Lorenz-Termsupport:

```text
precision = 1.0
recall = 1.0
spurious terms = 0
missing true terms = 0
max relative coefficient error = 5.295715025790404e-04
RMS relative coefficient error = 2.0427400056911374e-04
```

Held-out Vector-Field-NRMSE von P0:

```text
2.9566884198731605e-05
```

Damit sind die Baseline-Gates erfüllt und P1/P2 dürfen nach dem vorregistrierten Contract interpretiert werden.

## 2. Rekonstruktionsfehler an maskierten Punkten

Linear:

```text
seed 0: 8.428153969334459e-02
seed 1: 7.401823203269979e-02
seed 2: 8.152003704538022e-02
```

Cubic spline:

```text
seed 0: 1.9449610812077662e-03
seed 1: 1.6268375289569628e-03
seed 2: 1.7864887029666874e-03
```

Kubische Rekonstruktion ist im eingefrorenen Setup also deutlich genauer als lineare Rekonstruktion; dies ist zunächst nur eine Pipeline-Diagnose.

## 3. Structural equation fidelity

### Linear reconstruction

Seed 0:

```text
support Jaccard vs P0 = 1.0
max relative coefficient deviation vs P0 = 2.2698275577701404e-02
```

Seed 1:

```text
support Jaccard vs P0 = 1.0
max relative coefficient deviation vs P0 = 1.3970314938312208e-02
```

Seed 2:

```text
support Jaccard vs P0 = 0.875
max relative coefficient deviation vs P0 = 2.9768512631671348e-03
```

Nur Seed 2 erzeugt eine Supportänderung. Der zusätzliche Term ist ein konstanter Term in `dz/dt` mit Koeffizient ungefähr

```text
-0.09676111875926846
```

Damit zeigt der lineare Pfad nur in **1/3 Seeds** eine substantielle strukturelle Perturbation.

### Cubic reconstruction

Alle drei Seeds besitzen denselben Support wie P0:

```text
support Jaccard vs P0 = 1.0
```

Die maximalen relativen Koeffizientenabweichungen gegenüber P0 liegen deutlich unter der vorregistrierten 20%-Schwelle. Damit zeigt der kubische Pfad in **0/3 Seeds** eine substantielle strukturelle Perturbation.

## 4. Held-out Vector-Field-NRMSE

```text
P0              2.9566884198731605e-05
linear seed 0   1.6117399500201295e-03
cubic  seed 0   5.6709521993148916e-05
linear seed 1   1.0115844028435600e-03
cubic  seed 1   3.6421776881056610e-05
linear seed 2   1.2998655267752205e-03
cubic  seed 2   4.0895739862571295e-05
```

Alle Werte liegen weit unter dem eingefrorenen Gate `0.20`.

## 5. Short-horizon forward test

Median / Maximum des normierten RMS-Zustandsfehlers über die fünf vorregistrierten Anchors:

```text
P0             7.4340e-05 / 1.6316e-04
linear seed 0  3.3856e-03 / 2.1242e-02
cubic  seed 0  1.6092e-04 / 6.4135e-04
linear seed 1  1.8474e-03 / 1.0747e-02
cubic  seed 1  8.9386e-05 / 2.0369e-04
linear seed 2  1.7250e-03 / 8.4594e-03
cubic  seed 2  9.4956e-05 / 1.8577e-04
```

Diese Metrik ist berichtspflichtig, aber nicht Bestandteil der vorregistrierten operativen Äquivalenzentscheidung.

## 6. Autonomous long-time test

Alle sechs inferierten P1/P2-ODEs bleiben im eingefrorenen 100-Zeiteinheiten-Test endlich und unter dem technischen Norm-Grenzwert `100`.

Nach den eingefrorenen operativen Äquivalenztoleranzen bestehen:

```text
linear seed 0  PASS
cubic  seed 0  PASS
linear seed 1  PASS
cubic  seed 1  PASS
linear seed 2  PASS
cubic  seed 2  FAIL
```

Cubic seed 2 scheitert vor allem an den finite-window Langzeit-Mittelwert-/Wasserstein-Schwellen (`mean_scaled_max ~= 0.426`, `wasserstein_scaled_max ~= 0.434`), obwohl seine Gleichungs- und Vector-Field-Fehler sehr klein sind. Wegen der chaotischen Dynamik wird dieser Einzelbefund nicht als strukturelles Scheitern umgedeutet; die Schwellen bleiben dennoch gemäß Vorregistrierung unverändert.

## 7. Vorregistrierte Klassifikation

Ein `INFORMATIVE_POSITIVE` verlangt für mindestens einen Rekonstruktionspfad eine seed-konsistente substantielle strukturelle Perturbation in mindestens `2/3` Seeds und gleichzeitig operative Äquivalenz in mindestens `2/3` derselben Seeds.

Ergebnis:

```text
linear: structural perturbation 1/3; structural + operational equivalence 1/3
cubic:  structural perturbation 0/3; structural + operational equivalence 0/3
```

Daher lautet die durch D018 vorregistrierte Klassifikation:

```text
INFORMATIVE_NEGATIVE
```

## 8. Wissenschaftliche Bedeutung

Der eingefrorene Minimalfall reproduziert **nicht robust** den interessierenden Befund `structural disagreement + dynamical similarity`. Es gibt einen einzelnen diagnostisch interessanten Fall (linear, seed 2), der eine zusätzliche Gleichungskomponente bei weiterhin bestandener operativer Äquivalenz erzeugt; nach den vorregistrierten Robustheitsregeln darf dieser Einzelbefund jedoch nicht als positiver Provenance-Fall gewertet werden.

Das Ergebnis widerlegt weder klassische Nichtidentifizierbarkeit noch die Befunde von Zhai–Lucarini–Lai. Es sagt enger: **Die konkrete Minimalisierung auf 20% zufällige punktweise Missingness, lineare vs. kubische Rekonstruktion und die eingefrorene SINDy-Pipeline erzeugt keinen seed-robusten strukturellen Provenance-Effekt.**

## 9. Konsequenz für Directed Trias

Der numerische Befund selbst stärkt C07-L-Rc nicht positiv. Er zeigt aber, dass der Directed-Trias-Audit die negative Diagnose sauber lokalisieren kann:

```text
R -> sampled D -> C_pre -> reconstructed D -> C_infer -> T_hat
```

Die Rekonstruktionsoperation beeinflusst Fehlergrößen deutlich, aber unter diesem Scope nicht robust die inferierte Struktur im vorregistrierten Sinn.

Der verpflichtende nächste Schritt bleibt daher ein **Comparator-Audit auf genau diesem negativen Resultat**. Erst danach sollte entschieden werden, ob

1. der inverse Branch mit einer begründeten stärkeren Observation-/Missingness-Störung revidiert wird,
2. der pausierte ML-v0.2-Branch wieder aufgenommen wird,
3. oder der Originalitätsanspruch der Directed Trias weiter abgeschwächt wird.

Keine dieser Optionen wird durch dieses Ergebnis automatisch gewählt.