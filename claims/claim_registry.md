# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; AI-for-Science-Test bleibt offen | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich gut anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | Mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | Numerisch gut gestützt; Machbarkeit/Nutzbarkeit projektinterne Auditbegriffe | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Scope D005/D006, Skeleton D007, Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full numerical v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED | Starke Neuheitsform im Solverfall verworfen; schwache integrative Fassung bleibt prüfbar | D009 |
| AFS-DMO | Minimaler ML/AI-for-Science-Provenance-Demonstrator | ACCEPTED | Testdesign eingefroren | D010 |
| ML-IC-v0.1 | ML Implementation Contract v0.1 | ACCEPTED | technische Vorregistrierung eingefroren | D011 |
| ML-SKEL-v0.1 | ML Dataset-/Training-Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | Wissenschaftlicher ML-Provenance-Run | COMPLETE / INCONCLUSIVE | Reference gate bestanden; Learner-Resolvability-Gate klar verletzt | D013 |
| C07 | ML-Provenance-Claim-Kandidat | NOT ASSESSABLE | v0.1 entscheidet den Claim wegen fehlender Signalauflösung nicht; v0.2 ausstehend | — |
| ML-v0.2 | Resolvability Repair | ACCEPTED | nur Splitgeometrie + gemeinsamer Target-Scaler geändert | D013–D014 |
| ML-IC-v0.2 | Implementation Contract v0.2 | ACCEPTED | v0.2-Reparatur vor Implementierung eingefroren | D014 |
| ML-SKEL-v0.2 | v0.2 Dataset-/Training-Skeleton | READY FOR REVIEW | technische Tests bestanden; Smoke-Pipeline erfolgreich; noch kein wissenschaftlicher Full Run | — |

## Arbeitsregel

Ein wissenschaftlicher Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet nicht endgültig bewiesen, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der numerische Demonstrator stützt C05, nicht aber eine starke Originalitätsbehauptung gegenüber V&V. C06-R beschränkt den derzeit belegbaren Mehrwert auf durchgängige Integrations-/Provenance-Zuordnung.

ML v0.1 hat das Reference-Gate sehr deutlich bestanden, aber das Learner-Resolvability-Gate verletzt. D013 akzeptiert diesen inconclusive Ausgang. D014 friert den separat preregistrierten v0.2-Test ein: Teacher, Target, `Delta_t`, Architektur, Seeds und Optimierung bleiben unverändert; geändert werden ausschließlich ein phase-stratifizierter Fünferblock-Split und ein gemeinsamer training-only Target-Scaler.

Der v0.2-Skeleton implementiert diese beiden Änderungen und besteht die technischen Split-, Scaler-, Pairing- und Tiny-Training-Tests. Ein nichtwissenschaftlicher Smoke Run ist vollständig durchgelaufen. C07 bleibt bis zum eingefrorenen v0.2-Full-Run und anschließendem Standard-Framework-Vergleich unentschieden.

## Abhängigkeitslogik

C01 → C02 → C03 → C04 → D005 → D006 → D007 → numerical full run → C05/D008 → C06-R/D009 → AFS-DMO/D010 → ML-IC-v0.1/D011 → ML-SKEL-v0.1/D012 → ML Full Run v0.1 → D013 → ML-IC-v0.2/D014 → ML-SKEL-v0.2 review → v0.2 full run → erneuter Originalitätstest → möglicher C07.

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; siehe `collaboration/PDF_WORKFLOW.md`.
