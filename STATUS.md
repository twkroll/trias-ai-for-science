# Current Status

## Phase

**Claim and Scope / AI-for-Science Provenance v0.2 Skeleton Review**

Das Claim-and-Scope-Fundament, der numerische Minimaldemonstrator und dessen Full Run sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeit belegbaren Trias-Mehrwert auf eine Integrations-/Provenance-Funktion. Der ML-Provenance-Test v0.1 ist abgeschlossen und als `INCONCLUSIVE_LEARNER_ERROR` akzeptiert. Die separat preregistrierte v0.2-Resolvability-Reparatur ist nun technisch implementiert und wartet auf Skeleton-Review.

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
- **ML v0.1 Review + v0.2 Direction / D013:** v0.1 endgültig als `INCONCLUSIVE_LEARNER_ERROR` akzeptiert; C07 bleibt unentschieden; v0.2 repariert ausschließlich Signalauflösung.
- **ML-IC v0.2 / D014:** phase-stratifizierter Fünferblock-Split und gemeinsamer teacher-unabhängiger Target-Scaler als einzige wissenschaftliche Änderungen gegenüber v0.1 akzeptiert und eingefroren.

## Numerischer Demonstrator

**Status:** COMPLETE.

Der reine Solverfall zeigt ein mehrdimensionales Implementierungsprofil: RK4 ist im getesteten Bereich trajectory-genauer, Velocity-Verlet zeigt deutlich geringeren fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau. Daraus folgt keine globale Solver-Rangfolge; wissenschaftliche Bewertung ist use-case-relativ.

Der anschließende harte Vergleich mit Standard-Numerik/V&V/Credibility zeigte, dass diese Befunde dort bereits vollständig diagnostizierbar sind. Die Trias wird deshalb nicht als Ersatz oder nachweislich überlegener V&V-Rahmen positioniert.

## ML Full Run v0.1

**Status:** COMPLETE — `INCONCLUSIVE_LEARNER_ERROR`.

Reference separation und paired initialization bestanden; Learner resolvability scheiterte klar. Der Lernfehler lag ungefähr fünf Größenordnungen über der RK4-vs.-DOP853-Teacher-Differenz. C07 wird daher aus v0.1 weder akzeptiert noch verworfen.

Details: [`demonstrator/ml_full_run_v0_1_results.md`](demonstrator/ml_full_run_v0_1_results.md).

## ML v0.2 Code Skeleton

**Status:** READY FOR REVIEW.

Implementiert wurden ausschließlich die in D014 zugelassenen Änderungen:

1. `phase_block_split`: 200 zusammenhängende Fünferblöcke bei `N=1000`, deterministischer 3/1/1-Zyklus für exakt 600/200/200 Samples; kein Block wird über Splits geteilt;
2. ein gemeinsamer Target-Scaler aus `delta_ref_train` und `delta_rk4_train`, identisch für beide Teacher-Modelle; alle wissenschaftlichen Metriken bleiben in rücktransformierten Rohkoordinaten.

Die v0.1-Teachererzeugung und das bestehende Residual-MLP werden wiederverwendet. Neu sind die versionierten Module `ml_v0_2_data.py`, `ml_v0_2_model.py` und `ml_experiment_v0_2.py` sowie technische Tests.

Lokale technische Prüfung:

```text
pytest -q tests/test_ml_v0_2_skeleton.py
3 passed
```

Nichtwissenschaftlicher Smoke Run (`N=100`, Seed 0, 30 Epochen) lief vollständig durch. G1 war auf allen Splits erfüllt, G2 war erfüllt, Target-Scale/Inverse-Scale schloss auf Rundungsniveau. Smoke-G3/G3a werden ausdrücklich nicht wissenschaftlich interpretiert.

Details: [`demonstrator/ml_v0_2_code_skeleton_status.md`](demonstrator/ml_v0_2_code_skeleton_status.md).

## C07

**Status:** NOT ASSESSABLE.

Der Kandidat zu simulationsgenerierten Labels und zielsystemrelativer Surrogatgüte bleibt bis zu einem auflösbaren v0.2-Full-Run und anschließendem Vergleich mit starken Standard-ML-Provenance-/Credibility-Ansätzen offen.

## Nächste Entscheidung

Zu entscheiden ist, ob der ML-v0.2-Code-Skeleton als faithful implementation von D014 akzeptiert wird. Erst nach diesem GO darf der eingefrorene wissenschaftliche v0.2-Full-Run mit `N=1000`, Seeds `{0,1,2}` und dem unveränderten Full-Budget gestartet werden.

## Projektkommando `PDF`

Im Forschungsdialog bedeutet die alleinige oder sinngemäße Nachricht **`PDF`**: Aus dem jeweils aktuellen Repository- und Entscheidungsstand wird ohne weitere Rückfrage ein neues ausführliches Kooperationsbriefing als PDF plus LaTeX-Quelle erzeugt. Details: `collaboration/PDF_WORKFLOW.md`.

## Arbeitsregel

`GO` = aktuelle wissenschaftliche Empfehlung akzeptieren, dokumentieren und zum nächsten abhängigen Schritt übergehen.

`PDF` = aktuellen detaillierten Kooperationsstand neu synthetisieren und als PDF bereitstellen.
