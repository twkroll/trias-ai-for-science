# Current Status

## Phase

**Week 1 — Claim and Scope / Frozen ML Full Run**

Das Claim-and-Scope-Fundament, der reine numerische Minimaldemonstrator und der vollständige numerische v0.1-Lauf sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeitigen Trias-Mehrwert auf Integrations-/Provenance-Funktion. Der minimale AI-for-Science-Provenance-Demonstrator ist als D010, sein ML Implementation Contract als D011 und der getestete ML Code Skeleton als D012 eingefroren.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation.
- **C04 / D004:** Konvergenz, operative Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, implementiert und getestet.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance.
- **AFS-DMO / D010:** minimaler ML-Provenance-Test mit DOP853-vs.-coarse-RK4-Teacher und gepaarten Residual-MLPs akzeptiert.
- **ML-IC / D011:** Dataset-, Netzwerk-, Optimierungs-, Gate-, Rollout- und Scope-Entscheidungen vor dem wissenschaftlichen ML-Run eingefroren.
- **ML-SKEL / D012:** getesteter Dataset-/Training-/Rollout-Skeleton als faithful implementation von D011 akzeptiert.

## Aktuelle Aufgabe

### Wissenschaftlicher ML Full Run v0.1
**Status:** RUN NEXT / FROZEN

Auszuführen sind unverändert:

- `N=1000` Figure-eight-Phaseninputs;
- DOP853 primary/tight und coarse RK4 als gepaarte Teacher;
- Seeds `{0,1,2}` mit bitgleicher Paarinitialisierung;
- Residual-MLP `12-128-128-128-12`, `tanh`, float64 CPU;
- maximal 5000 Epochen, vorregistriertes Early Stopping;
- One-Step own-teacher/common-reference Metriken;
- Reference- und Learner-Resolvability-Gates;
- Provenance-Fehlerzerlegung;
- MU1 = 1 Periode, MU2 = 10 Perioden;
- 3/3-Seed-Regel für robuste Hauptbefunde.

## Noch nicht entschieden

- Ergebnisstatus des ML Full Runs;
- möglicher neuer Claim zu simulationsgenerierten Labels und zielsystemrelativer Surrogatgüte;
- Originalität gegenüber starken Standard-ML-Provenance-/Credibility-Frameworks.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Spezifikationsdokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.