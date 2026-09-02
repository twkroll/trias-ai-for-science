# Current Status

## Phase

**Claim and Scope / AI-for-Science Provenance v0.2 Contract Review**

Das Claim-and-Scope-Fundament, der numerische Minimaldemonstrator und dessen Full Run sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf eine Integrations-/Provenance-Funktion. Der minimale AI-for-Science-Provenance-Test v0.1, sein technischer Contract und sein getesteter Skeleton sind als D010–D012 eingefroren. Der wissenschaftliche ML Full Run v0.1 wurde ausgeführt und als nicht entscheidungsfähig klassifiziert.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, implementiert, getestet und vollständig ausgeführt.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance/Mapping.
- **AFS-DMO / D010:** minimaler ML-Provenance-Test akzeptiert.
- **ML-IC v0.1 / D011:** Dataset-, Netzwerk-, Optimierungs-, Gate-, Rollout- und Scope-Entscheidungen eingefroren.
- **ML-SKEL v0.1 / D012:** getesteter ML-Skeleton akzeptiert.
- **ML v0.1 Review + v0.2 Direction / D013:** v0.1 endgültig als `INCONCLUSIVE_LEARNER_ERROR` akzeptiert; v0.2 repariert ausschließlich Signalauflösung durch phase-stratifizierten Blocksplit und gemeinsamen teacher-unabhängigen Target-Scaler.

## Numerischer Demonstrator

**Status:** COMPLETE.

Der reine Solverfall zeigt ein mehrdimensionales Implementierungsprofil: RK4 ist im getesteten Bereich trajectory-genauer, Velocity-Verlet zeigt deutlich geringeren fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau. Daraus folgt keine globale Solver-Rangfolge; wissenschaftliche Bewertung ist use-case-relativ.

Der anschließende harte Vergleich mit Standard-Numerik/V&V/Credibility zeigte jedoch, dass diese Befunde dort bereits vollständig diagnostizierbar sind. Die Trias wird deshalb nicht als Ersatz oder nachweislich überlegener V&V-Rahmen positioniert.

## ML Full Run v0.1

**Status:** COMPLETE — `INCONCLUSIVE_LEARNER_ERROR`.

### Gates

- Reference separation: **PASS**.
  - test `D_teacher = 1.3035448186e-05`;
  - test `D_ref = 5.8302465944e-14`.
- Paired initialization: **PASS**, 3/3 Seeds.
- Learner resolvability: **FAIL**.
  - median own-teacher RMSE, ref-trained: `0.7187268`;
  - median own-teacher RMSE, rk4-trained: `0.7171894`.

Der Lernfehler liegt damit ungefähr fünf Größenordnungen über der numerischen Teacher-Differenz. Die exakte Provenance-Zerlegung funktioniert technisch, doch der Modellfehler dominiert den Teacher-Beitrag. MU1/MU2 werden daher nicht als Teacher-Provenance-Evidenz interpretiert.

Details: [`demonstrator/ml_full_run_v0_1_results.md`](demonstrator/ml_full_run_v0_1_results.md).

## C07

**Status:** NOT ASSESSABLE.

Der Kandidat

> Gute ML-Güte relativ zu simulationsgenerierten Trainingslabels rechtfertigt nicht automatisch eine gleich starke Aussage über das wissenschaftliche Zielsystem; die epistemische Bewertung eines Surrogats muss die Provenance des Datengenerators berücksichtigen.

wird aus v0.1 weder akzeptiert noch verworfen.

## Aktuelle Aufgabe

### ML Implementation Contract v0.2 — Resolvability Repair
**Status:** PENDING REVIEW

v0.2 behält Target, Teacher, `N=1000`, `Delta_t`, Architektur, Seeds und Optimierung bei. Geändert werden nur:

1. ein deterministischer phase-stratifizierter Fünfer-Blocksplit mit weiterhin exakt 60/20/20 %, der alle Splits über die gesamte Figure-eight-Phase verteilt;
2. ein gemeinsamer teacher-unabhängiger Target-Scaler, ausschließlich aus den Trainingstargets beider Teacher gemeinsam berechnet.

Teacher-Provenance darf weiterhin nur interpretiert werden, wenn `G1–G3` bestanden sind, insbesondere

```text
median_seed(RMSE_own_teacher_test) < D_teacher_test.
```

Siehe [`demonstrator/ml_implementation_contract_v0_2.md`](demonstrator/ml_implementation_contract_v0_2.md).

## Projektkommando `PDF`

Im Forschungsdialog bedeutet die alleinige Nachricht **`PDF`**: Aus dem jeweils aktuellen Repository- und Entscheidungsstand wird ein neues ausführliches Kooperationsbriefing als PDF erzeugt. Es soll für eine promovierte Physikerin mit wissenschaftsphilosophischem Hintergrund verständlich und kritisch lesbar sein und nicht lediglich alte Briefingtexte erneut ausgeben. Details sind in `collaboration/PDF_WORKFLOW.md` festgelegt.

## Arbeitsregel

`GO` = aktuelle wissenschaftliche Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.

`PDF` = aktuellen detaillierten Kooperationsstand neu synthetisieren und als PDF bereitstellen.