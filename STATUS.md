# Current Status

## Phase

**Week 1 — Claim and Scope / ML Full Run v0.1 Review**

Das Claim-and-Scope-Fundament, der numerische Minimaldemonstrator und dessen Full Run sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeitigen Trias-Mehrwert auf Integrations-/Provenance-Funktion. Der minimale AI-for-Science-Provenance-Test, sein Contract und sein getesteter Skeleton sind als D010–D012 eingefroren. Der wissenschaftliche ML Full Run v0.1 wurde nun ausgeführt.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation.
- **C04 / D004:** Konvergenz, operative Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, implementiert und getestet.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance.
- **AFS-DMO / D010:** minimaler ML-Provenance-Test akzeptiert.
- **ML-IC / D011:** Dataset-, Netzwerk-, Optimierungs-, Gate-, Rollout- und Scope-Entscheidungen eingefroren.
- **ML-SKEL / D012:** getesteter ML-Skeleton akzeptiert.

## ML Full Run v0.1

**Status:** COMPLETE — `INCONCLUSIVE_LEARNER_ERROR`

### Gates

- Reference separation: **PASS**.
  - test `D_teacher = 1.3035448186e-05`;
  - test `D_ref = 5.8302465944e-14`.
- Paired initialization: **PASS**, 3/3 Seeds.
- Learner resolvability: **FAIL**.
  - median own-teacher RMSE, ref-trained: `0.7187268`;
  - median own-teacher RMSE, rk4-trained: `0.7171894`.

Damit ist der Lern-/Held-out-Phasenfehler ungefähr fünf Größenordnungen größer als die numerische Teacher-Differenz. D011 verbietet deshalb eine Provenance-Interpretation des Runs.

Die exakte Fehlerzerlegung funktioniert technisch, aber der Teacher-Beitrag (`~2e-09` als mean squared vector term) wird von Modellfehlerbeiträgen von Ordnung `1–10` überdeckt. MU1/MU2 laufen formal ohne den Paarabstands-Abbruch, sind jedoch mit extrem großen Trajektorien-/Strukturfehlern und starker OOD-Akkumulation wissenschaftlich nicht als Teacher-Provenance-Evidenz interpretierbar.

Details: [`demonstrator/ml_full_run_v0_1_results.md`](demonstrator/ml_full_run_v0_1_results.md).

## C07

**Status:** NOT ASSESSABLE FROM v0.1.

Der Kandidat zu simulationsgenerierten Labels und zielsystemrelativer Surrogatgüte wird weder akzeptiert noch verworfen. Das Experiment ist wegen fehlender Learner-Resolvability nicht entscheidungsfähig.

Siehe [`claims/claim_07.md`](claims/claim_07.md).

## Nächste Entscheidung

Zu entscheiden ist, ob der v0.1-Status `INCONCLUSIVE_LEARNER_ERROR` als korrekte wissenschaftliche Schlussfolgerung akzeptiert wird und anschließend ein separat preregistrierter v0.2-Resolvability-Test entworfen werden soll. Innerhalb v0.1 findet kein Rescue-Sweep statt.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Spezifikationsdokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.