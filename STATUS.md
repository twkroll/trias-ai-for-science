# Current Status

## Phase

**Directed Trias / Inverse-Direction Code Skeleton v0.1 Review**

Der numerische Drei-Körper-Demonstrator ist abgeschlossen. C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf eine Integrations-/Provenance-Funktion. Die Directed Trias ist als Arbeitsrevision akzeptiert. Der ML-v0.2-Full-Run bleibt strategisch pausiert. Aktuell wird die inverse Kette `target/observation -> data -> preprocessing -> inference -> theory` mit einem minimalen Lorenz/SINDy-Demonstrator geprüft.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** numerischer Figure-eight-Demonstrator und C05 abgeschlossen/akzeptiert.
- **D009:** starke Trias-Neuheitsbehauptung gegenüber V&V verworfen; C06-R = Integrations-/Provenance-Fassung.
- **D010–D014:** ML-Provenance-Zweig v0.1 ausgeführt (`INCONCLUSIVE_LEARNER_ERROR`), v0.2 technisch vorbereitet.
- **D015:** Directed Trias als Arbeitsrevision akzeptiert; ML-v0.2-Full-Run pausiert.
- **D016:** starke C07-L-Neuheitsfassung verworfen; C07-L-R als moderate Equation-Discovery-Bridge akzeptiert.
- **D017:** Minimal Inverse-Direction Demonstrator v0.1 akzeptiert und eingefroren.
- **D018:** Inverse-Direction Implementation Contract v0.1 akzeptiert und eingefroren.

## Directed Trias

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
```

Die drei Pole bleiben funktionale Rollen; Daten sind Zwischenartefakte. Theoretische Identifizierbarkeit bleibt eine querliegende Auditdimension, keine neue Stufe der sechs-stufigen Lösungsleiter.

## Inverser MVP

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

P0 muss vor jeder Provenance-Interpretation das Structural-Recovery-Gate bestehen. Structural equation fidelity und dynamical/statistical adequacy werden getrennt bewertet. Der spätere Comparator-Test gegen System Identification, Identifiability/Observability, SciML V&V und Workflow/Data Provenance bleibt verpflichtend.

## Code Skeleton v0.1

**Status: READY FOR REVIEW. Scientific full run: NOT EXECUTED.**

Implementiert wurden:

- Lorenz-Referenz, Missingness, Pairing/Mask-Hashes und Reconstruction;
- 5-Punkt-Derivative Estimation;
- feste quadratische Feature-Library und STLSQ;
- Structural Metrics und held-out Vector-Field-NRMSE;
- Forward-Integration inferierter ODEs;
- Short-Horizon-Fehler, Langzeitstatistik, Korrelation und Wasserstein-Metriken;
- Dynamic-validity- und operative-Äquivalenzfunktionen;
- CLI `trias-inverse-demo`;
- technische Tests und ein verkürzter, ausdrücklich nichtwissenschaftlicher Smoke Run.

Lokale gezielte Tests:

```text
6 passed
```

Smoke-Pipeline: Reference-Gate und Mask-Integrität bestanden; P1/P2 verwendeten denselben Mask-Hash. Das P0-Full-Gate wurde im absichtlich verkürzten Smoke-Setup nicht erfüllt und wird ausdrücklich nicht wissenschaftlich interpretiert.

Details: [`demonstrator/inverse_direction_code_skeleton_status_v0_1.md`](demonstrator/inverse_direction_code_skeleton_status_v0_1.md).

## ML v0.2

**TECHNICALLY READY / SCIENTIFIC FULL RUN PAUSED.** D014 und der v0.2-Skeleton bleiben gültig.

## Nächste Entscheidung

Zu entscheiden ist, ob der Inverse-Direction Code Skeleton v0.1 als faithful technische Umsetzung von D018 akzeptiert wird. Erst bei weiterem `GO` darf der wissenschaftliche inverse Full Run mit den eingefrorenen D018-Parametern ausgeführt werden.

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; Directed Trias, C07-L-R, inverser MVP und pausierter ML-v0.2-Zweig werden berücksichtigt.
