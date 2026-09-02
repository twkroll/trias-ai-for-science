# Current Status

## Phase

**Week 1 — Claim and Scope / ML Code Skeleton Review**

Das Claim-and-Scope-Fundament, der reine numerische Minimaldemonstrator und der vollständige v0.1-Lauf sind abgeschlossen. C05 ist akzeptiert; C06-R beschränkt den derzeitigen Trias-Mehrwert auf Integrations-/Provenance-Funktion. Der minimale AI-for-Science-Provenance-Demonstrator ist als D010 und sein technischer ML Implementation Contract als D011 eingefroren.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework; diagnostischer Mehrwert ist die zentrale Hypothese.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation.
- **C04 / D004:** Konvergenz, operative Machbarkeit, Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt.
- **Numerischer Demonstrator / D005–D007:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, implementiert und getestet.
- **C05 / D008:** verschiedene numerische Operationalisierungen erzeugen use-case-relative Fehler-/Strukturprofile.
- **C06-R / D009:** starke Neuheitsbehauptung gegenüber V&V verworfen; verbleibender Mehrwert ist integrative Provenance.
- **AFS-DMO / D010:** minimaler ML-Provenance-Test mit DOP853-vs.-coarse-RK4-Teacher und gepaarten Residual-MLPs akzeptiert.
- **ML-IC / D011:** Dataset-, Netzwerk-, Optimierungs-, Gate-, Rollout- und Scope-Entscheidungen vor dem wissenschaftlichen ML-Run eingefroren.

## ML Code Skeleton v0.1

**Status:** READY FOR REVIEW

Implementiert sind:

- paired-teacher Dataset-Erzeugung ab identischen Figure-eight-Inputs;
- DOP853 primary/tight und ein coarse RK4-Schritt als Labelgeneratoren;
- contiguous split und training-only Inputnormalisierung;
- Residual-MLP `12-128-128-128-12`, `tanh`, float64 CPU;
- bitgleich gepaarte Seeds und deterministischer Trainingspfad;
- One-Step own-teacher/common-reference Metriken;
- quantitative Zerlegung `e_total=e_model+e_teacher`;
- MU1/MU2-Rollout-Pipeline;
- technischer `--smoke`-Modus.

Lokale technische Validierung vor Repository-Write:

```text
pytest -q
4 passed
```

Der Smoke Run (`N=60`, Seed 0, maximal 20 Epochen; ausdrücklich nicht wissenschaftlich) lief vollständig durch. Das Reference-Gate war erfüllt, die Initialisierung war bitgleich gepaart und die Provenance-Fehleridentität schloss bis ungefähr `3.6e-15`. Die ML-Güte des Smoke Runs wird nicht interpretiert.

Details: [`demonstrator/ml_code_skeleton_status_v0_1.md`](demonstrator/ml_code_skeleton_status_v0_1.md).

## Noch nicht wissenschaftlich ausgeführt/entschieden

- eingefrorener ML Full Run mit `N=1000` und Seeds `{0,1,2}`;
- Learner-Resolvability-Gate;
- MU1/MU2 über alle sechs Modelle;
- 3/3-Seed-Robustheit;
- Full-Run-Ergebnisstatus;
- starker Vergleich gegen etablierte ML-Provenance/Credibility-Frameworks;
- neuer Claim zu simulationsgenerierten Labels und zielsystemrelativer Surrogatgüte.

## Nächste Abhängigkeit

Review des ML Code Skeleton v0.1. Nach Akzeptanz werden fehlende reine Output-/Checkpoint-Protokollierungsdetails ergänzt, ohne wissenschaftliche Einstellungen zu ändern, und anschließend der eingefrorene wissenschaftliche ML Full Run ausgeführt.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Spezifikationsdokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.
