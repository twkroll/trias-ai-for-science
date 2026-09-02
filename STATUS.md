# Current Status

## Phase

**Directed Trias / Inverse Scientific Full Run v0.1 Review**

Der numerische Drei-Körper-Demonstrator ist abgeschlossen. C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf eine Integrations-/Provenance-Funktion. Die Directed Trias ist als Arbeitsrevision akzeptiert. Der ML-v0.2-Full-Run bleibt strategisch pausiert. Der wissenschaftliche inverse Lorenz/SINDy-Full-Run wurde nun nach dem eingefrorenen D018-Contract ausgeführt.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** numerischer Figure-eight-Demonstrator und C05 abgeschlossen/akzeptiert.
- **D009:** starke Trias-Neuheitsbehauptung gegenüber V&V verworfen; C06-R = Integrations-/Provenance-Fassung.
- **D010–D014:** ML-Provenance-Zweig v0.1 ausgeführt (`INCONCLUSIVE_LEARNER_ERROR`), v0.2 technisch vorbereitet.
- **D015:** Directed Trias als Arbeitsrevision akzeptiert; ML-v0.2-Full-Run pausiert.
- **D016:** starke C07-L-Neuheitsfassung verworfen; C07-L-R als moderate Equation-Discovery-Bridge akzeptiert.
- **D017:** Minimal Inverse-Direction Demonstrator v0.1 akzeptiert und eingefroren.
- **D018:** Inverse-Direction Implementation Contract v0.1 akzeptiert und eingefroren.
- **D019:** Inverse-Direction Code Skeleton v0.1 akzeptiert; wissenschaftlicher Full Run freigegeben.

## Directed Trias

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
```

Die drei Pole bleiben funktionale Rollen; Daten sind Zwischenartefakte. Theoretische Identifizierbarkeit bleibt eine querliegende Auditdimension, keine neue Stufe der sechs-stufigen Lösungsleiter.

## Wissenschaftlicher inverse Full Run v0.1

**Status:** COMPLETE / PENDING SCIENTIFIC REVIEW  
**Pre-registered classification:** `INFORMATIVE_NEGATIVE`

Eingefrorener Full-Contract:

```text
Lorenz-63, x0=(1,1,1)
DOP853 primary/tight reference
dt_obs=0.01
Discovery [10,50]
Holdout (50,60]
P0 complete
P1 20% paired missingness + linear reconstruction
P2 same masks + not-a-knot cubic reconstruction
mask seeds {0,1,2}
common 5-point derivative estimator
common quadratic SINDy/STLSQ pipeline
```

### Gates

```text
G1 reference: PASS
max normalized primary/tight gap [0,10] = 4.7727891186720604e-12

G2 mask integrity: PASS for seeds {0,1,2}

G3 P0 structural baseline: PASS
precision = 1.0
recall = 1.0
spurious terms = 0
missing true terms = 0
max relative true-coefficient error = 5.295715025790404e-04
```

### Structural result

```text
linear reconstruction: substantial structural perturbation in 1/3 seeds
cubic reconstruction:  substantial structural perturbation in 0/3 seeds
required for seed-consistency: >=2/3
```

Der einzige Supportwechsel tritt bei linearer Rekonstruktion, Seed 2, auf: ein zusätzlicher konstanter Term in `dz/dt` mit Koeffizient ungefähr `-0.0967611`. Dieses Modell besteht zugleich die eingefrorenen operativen Äquivalenzkriterien, bleibt aber ein 1/3-Einzelfall.

### Dynamical/statistical result

Alle sechs P1/P2-ODEs bleiben im 100-Zeiteinheiten-Test endlich und beschränkt. Fünf von sechs erfüllen sämtliche eingefrorenen operativen Äquivalenztoleranzen. Cubic seed 2 scheitert an finite-window Langzeit-Mittelwert-/Wasserstein-Gates trotz sehr kleinem Gleichungs-/Vector-Field-Fehler.

Da kein Rekonstruktionspfad eine seed-konsistente strukturelle Perturbation in mindestens 2/3 Seeds zeigt, erzwingt D018 die Klassifikation:

```text
INFORMATIVE_NEGATIVE
```

Details: [`demonstrator/inverse_full_run_v0_1_results.md`](demonstrator/inverse_full_run_v0_1_results.md).

## Wissenschaftliche Bedeutung

Der eingefrorene Minimalfall reproduziert **nicht robust** den interessierenden Effekt `structural disagreement + dynamical similarity`. Der einzelne lineare Seed-2-Fall ist diagnostisch interessant, darf nach Vorregistrierung aber nicht als positiver Provenance-Fall gewertet werden.

Das Ergebnis widerlegt weder Nichtidentifizierbarkeit noch die Befunde von Zhai–Lucarini–Lai. Es begrenzt ausschließlich die Evidenz des konkreten Minimaldesigns mit 20% zufälliger punktweiser Missingness und linearer/kubischer Rekonstruktion.

## ML v0.2

**TECHNICALLY READY / SCIENTIFIC FULL RUN PAUSED.** D014 und der v0.2-Skeleton bleiben gültig.

## Nächste Entscheidung

Zu entscheiden ist, ob `INFORMATIVE_NEGATIVE` als wissenschaftlicher Projektbefund akzeptiert wird. Empfehlung: **ACCEPT** und danach zuerst den verpflichtenden Comparator-Audit auf genau diesem negativen Resultat durchführen. Vor diesem Audit keine Änderung von Missingness, SINDy-Thresholds oder ML-v0.2.

Erst danach wird entschieden zwischen:

```text
A. begründete Revision des inversen Demonstrators
B. Resume des pausierten ML-v0.2-Branches
C. weitere Abschwächung/Neupositionierung des Directed-Trias-Originalitätsclaims
```

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; Directed Trias, C07-L-R, inverser MVP und pausierter ML-v0.2-Zweig werden berücksichtigt.
