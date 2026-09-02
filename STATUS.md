# Current Status

## Phase

**Directed Trias / Inverse-Direction Implementation Contract v0.1 Review**

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
- **D016:** starke C07-L-Neuheitsfassung verworfen; C07-L-R als moderate Arbeitsfassung akzeptiert; inverser MVP als nächste Abhängigkeit.
- **D017:** Minimal Inverse-Direction Demonstrator v0.1 akzeptiert und eingefroren.

## Directed Trias

Die drei Pole bleiben funktionale Rollen. Der Audit unterscheidet explizit gerichtete Transformationen:

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
```

Die sechs-stufige Lösungsleiter bleibt unverändert. Theoretische Identifizierbarkeit ist eine querliegende Auditdimension.

## C07-L-R

**ACCEPTED AS WORKING CLAIM — D016.**

Zhai–Lucarini–Lai dient als externer chaotischer Equation-Discovery-Fall. Der Trias-Anteil bleibt ausschließlich die zu testende Hypothese einer gemeinsamen richtungssensitiven Integrations-/Zuordnungsgrammatik.

## ML v0.2

**Status:** TECHNICALLY READY / SCIENTIFIC FULL RUN PAUSED.

D014 und der getestete v0.2-Skeleton bleiben gültig. Nach dem inversen MVP wird entschieden, ob der Branch fortgesetzt, sekundär gestellt oder ersetzt wird.

## Inverser MVP

**Status:** SPECIFICATION ACCEPTED — D017.

Eingefrorener Minimalfall:

```text
Lorenz-63 synthetic target
-> common DOP853 latent trajectory
-> P0 complete observations
-> P1 20% paired missingness + linear reconstruction
-> P2 same missingness + cubic-spline reconstruction
-> same 5-point derivative estimator
-> same quadratic SINDy/STLSQ pipeline
-> structural equation assessment
-> autonomous dynamical/statistical assessment
```

Drei vorregistrierte Missingness-Seeds `{0,1,2}` verhindern die Interpretation einer einzelnen Zufallsmaske. P0 muss vor jeder Provenance-Deutung das Structural-Recovery-Gate bestehen.

## Aktuelle Aufgabe

### Inverse-Direction Implementation Contract v0.1
**Status:** PENDING REVIEW

Der Contract friert unter anderem ein:

- Lorenz `x0=(1,1,1)`, DOP853 primary/tight reference, `dt_obs=0.01`;
- Discovery `[10,50]`, held-out vector-field assessment `(50,60]`;
- exakt 800 maskierte Zeitpunkte pro Seed bei Seeds `{0,1,2}` und bitgleicher P1/P2-Maske;
- lineare vs. not-a-knot CubicSpline-Rekonstruktion;
- gemeinsame zentrale Fünfpunktableitung vierter Ordnung;
- Feature-Library `[1,x,y,z,x^2,xy,xz,y^2,yz,z^2]`;
- STLSQ-Threshold `0.05`, Ridge `1e-8`, maximal 20 Iterationen;
- striktes P0-Gate: exakter Support und max. 5% Koeffizientenfehler;
- substantieller Structural-Effekt: Supportänderung oder >=20% Koeffizientenabweichung gegenüber P0;
- dynamische Äquivalenz über held-out vector-field error, Langzeitmittel/-varianz, Korrelation und normierte Wasserstein-Distanzen;
- vorregistrierte Resultatklassen und verpflichtenden post-hoc Comparator-Test.

Details: [`demonstrator/inverse_direction_implementation_contract_v0_1.md`](demonstrator/inverse_direction_implementation_contract_v0_1.md).

## Nächste Entscheidung

Zu entscheiden ist, ob der Implementation Contract akzeptiert und eingefroren wird. Bei GO darf anschließend **nur** ein Code-Skeleton implementiert, technisch getestet und in einem nichtwissenschaftlichen Smoke Run geprüft werden. Der wissenschaftliche Full Run benötigt danach ein weiteres GO.

## Projektkommando `PDF`

`PDF` erzeugt aus dem aktuellen Repository- und Entscheidungsstand ohne Rückfrage ein neues ausführliches Kooperationsbriefing als PDF plus LaTeX-Quelle. Directed Trias, C07-L-R, der pausierte ML-v0.2-Zweig und der inverse MVP werden berücksichtigt.

## Arbeitsregel

`GO` = aktuelle wissenschaftliche Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.

`PDF` = aktuellen detaillierten Kooperationsstand neu synthetisieren und als PDF bereitstellen.
