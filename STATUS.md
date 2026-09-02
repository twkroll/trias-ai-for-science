# Current Status

## Phase

**Week 1 — Claim and Scope / Minimal AI-for-Science Provenance Test**

Das Claim-and-Scope-Fundament, der reine numerische Minimaldemonstrator, der Implementation Contract, der Code-Skeleton und der vollständige v0.1-Lauf sind abgeschlossen. C05 ist akzeptiert. Der harte C06-Vergleich hat die starke Neuheitsbehauptung im reinen Solverfall nicht gestützt; C06-R ist als schwächere Integrations-/Provenance-Fassung akzeptiert.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework; diagnostischer Mehrwert ist die zentrale Hypothese.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol; keine notwendige ontologische Trennung der Pole.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; V&V bleibt Vergleichsrahmen.
- **Minimal Demonstrator / D005:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, U1/U2, kein ML/chaotischer Fall in v0.1.
- **Implementation Contract / D006:** v0.1-Konfiguration, Referenzlogik, Schrittweiten, Metriken, Gates und Artefakte eingefroren.
- **Code Skeleton / D007:** minimaler getesteter Skeleton als faithful implementation von D006 akzeptiert.
- **C05 / D008:** unterschiedliche numerische Operationalisierungen können bei gleichem Zielsystem/Theorie verschiedene wissenschaftlich relevante Fehler- und Strukturprofile erzeugen; Bewertung ist use-case-relativ.
- **C06-R / D009:** die starke Aussage neuer numerischer Validierungsfragen wird verworfen. Der derzeit belegbare Trias-Mehrwert ist eine explizite integrative Zuordnung/Provenance über Zielsystem, Theorie, Berechnung und wissenschaftliche Nutzung.

## Ergebnis des reinen Solverfalls

Der Figure-eight-Demonstrator erfüllt die Referenz-/Refinement-Gates und stützt C05. Gleichzeitig lassen sich seine numerischen Befunde ohne Informationsverlust in Standard-Numerik/V&V/Credibility-Sprache ausdrücken. Daher ist die Trias **nicht** als Ersatz oder nachweislich überlegener Rahmen gegenüber V&V zu behandeln.

Details:

- [`demonstrator/full_run_v0_1_results.md`](demonstrator/full_run_v0_1_results.md)
- [`demonstrator/c06_comparison_v0_1.md`](demonstrator/c06_comparison_v0_1.md)
- [`claims/claim_06.md`](claims/claim_06.md)

## Aktuelle Aufgabe

### Minimal ML / AI-for-Science Provenance Demonstrator v0.1
**Status:** PENDING REVIEW

Der nächste Test führt genau **eine** zusätzliche Übersetzungsebene ein:

`synthetisches Zielsystem / Theorie → numerischer Datengenerator → Trainingsdaten → gelerntes One-Step-Surrogat → Rollout / wissenschaftlicher Gebrauch`.

Ziel ist nicht ML-Performance, sondern die kontrollierte Frage, ob gute generatorrelative ML-Metriken zu einer ungerechtfertigten Aussage über das Zielsystem führen können und ob die explizite Provenance-Zuordnung der Trias diese Herkunft transparent macht.

Siehe [`demonstrator/ml_epistemic_spec_v0_1.md`](demonstrator/ml_epistemic_spec_v0_1.md).

## Noch nicht akzeptiert / implementiert

- konkrete ML-Spezifikation;
- ML-Code oder Training;
- neuer Claim zu Datenprovenance oder Surrogatgüte;
- chaotische/generalization-heavy Benchmarks;
- physik-informierte oder strukturerhaltende Netzwerkarchitekturen.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Spezifikationsdokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.