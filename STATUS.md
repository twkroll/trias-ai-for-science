# Current Status

## Phase

**Directed Trias / Minimal Inverse-Direction Demonstrator v0.1 Specification Review**

Das Claim-and-Scope-Fundament und der numerische Drei-Körper-Demonstrator sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf eine Integrations-/Provenance-Funktion. Der ursprüngliche ML-Provenance-Test v0.1 blieb `INCONCLUSIVE_LEARNER_ERROR`; die v0.2-Resolvability-Reparatur ist technisch vorbereitet, ihr wissenschaftlicher Full Run jedoch strategisch pausiert. Der aktuelle Fokus liegt auf der inversen Richtung `target/observation -> data -> preprocessing -> inference -> theory`.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; die sechs-stufige Lösungsleiter bleibt erhalten.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, implementiert, getestet und vollständig ausgeführt.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance/Mapping.
- **AFS-DMO / D010, ML-IC v0.1 / D011, ML-SKEL v0.1 / D012:** minimaler ML-Provenance-Test vorregistriert und implementiert.
- **D013:** ML v0.1 endgültig `INCONCLUSIVE_LEARNER_ERROR`; C07 bleibt unentschieden; v0.2 als separate Resolvability-Reparatur erlaubt.
- **D014:** v0.2 ändert ausschließlich phase-stratifizierten Blocksplit und gemeinsamen teacher-unabhängigen Target-Scaler; übrige wissenschaftliche Einstellungen eingefroren.
- **D015:** Directed Trias als Arbeitsrevision akzeptiert; ML-v0.2-Full-Run pausiert; C07-L gegen starke Comparatoren geprüft.
- **D016:** starke C07-L-Neuheitsfassung verworfen; C07-L-R als moderate Arbeitsfassung akzeptiert; inverser MVP ist die nächste Abhängigkeit.

## Directed Trias

Die drei Pole bleiben funktionale Rollen. Der Audit unterscheidet jetzt explizit gerichtete Transformationen:

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
```

Die sechs-stufige Lösungsleiter bleibt unverändert. Theoretische Identifizierbarkeit ist eine querliegende Auditdimension.

Details: [`theory/directed_trias_v0_1.md`](theory/directed_trias_v0_1.md).

## C07-L / C07-L-R

Der Comparator-Audit ist abgeschlossen. Nichtidentifizierbarkeit, observational equivalence/equifinality, structural error/near-identifiability, pipelineabhängige Inferenz und allgemeine Provenance sind etablierte Themen. Daher ist die starke C07-L-Fassung als Neuheitsclaim verworfen.

**C07-L-R ist ACCEPTED AS WORKING CLAIM — D016.**

Zhai–Lucarini–Lai dient als externer chaotischer Equation-Discovery-Fall. Der Trias-Anteil bleibt ausschließlich die zu testende Hypothese einer gemeinsamen richtungssensitiven Integrations-/Zuordnungsgrammatik.

Details:

- [`claims/claim_07_lucarini_bridge_revised.md`](claims/claim_07_lucarini_bridge_revised.md)
- [`literature/c07_l_comparator_audit.md`](literature/c07_l_comparator_audit.md)

## ML v0.2

**Status:** TECHNICALLY READY / SCIENTIFIC FULL RUN PAUSED.

D014 und der getestete v0.2-Skeleton bleiben gültig. Nach dem inversen MVP wird entschieden, ob der Branch fortgesetzt, sekundär gestellt oder ersetzt wird.

## Aktuelle Aufgabe

### Minimal Inverse-Direction Demonstrator v0.1
**Status:** PENDING REVIEW

Vorgeschlagener Minimalfall:

```text
Lorenz-63 synthetic target
-> common high-accuracy latent trajectory
-> P0 complete observations
-> P1 20% paired missingness + linear reconstruction
-> P2 same missingness + cubic-spline reconstruction
-> same derivative estimator
-> same quadratic SINDy/STLSQ pipeline
-> structural equation assessment
-> autonomous dynamical/statistical assessment
```

Drei vorregistrierte Missingness-Seeds sollen verhindern, dass der Befund an einer einzelnen Maske hängt. Die vollständige Beobachtung P0 muss zunächst ein Structural-Recovery-Gate bestehen.

Die zentrale Trennung lautet:

```text
structural equation fidelity
vs.
dynamical/statistical adequacy
```

Ein positiver inverser Provenance-Fall erfordert strukturelle Unterschiede bei gleichzeitig vorregistriert hinreichend ähnlicher Dynamik; triviale `bad model`-Fälle zählen nicht.

Details: [`demonstrator/inverse_direction_spec_v0_1.md`](demonstrator/inverse_direction_spec_v0_1.md).

## Nächste Entscheidung

Zu entscheiden ist, ob `inverse_direction_spec_v0_1.md` akzeptiert und eingefroren wird. Bei GO wird **nur** ein exakter Inverse-Direction Implementation Contract v0.1 erstellt. Vor dessen weiterem GO wird kein Code geschrieben und kein wissenschaftlicher Run gestartet.

## Projektkommando `PDF`

`PDF` erzeugt aus dem aktuellen Repository- und Entscheidungsstand ohne Rückfrage ein neues ausführliches Kooperationsbriefing als PDF plus LaTeX-Quelle. Directed Trias, C07-L-R, der pausierte ML-v0.2-Zweig und der inverse MVP werden berücksichtigt.

## Arbeitsregel

`GO` = aktuelle wissenschaftliche Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.

`PDF` = aktuellen detaillierten Kooperationsstand neu synthetisieren und als PDF bereitstellen.
