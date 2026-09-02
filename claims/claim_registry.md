# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; AI-for-Science-Test ausstehend | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich gut anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | Mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | Numerisch gut gestützt; Machbarkeit/Nutzbarkeit projektinterne Auditbegriffe | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Scope D005/D006, Skeleton D007, Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED | Starke Neuheitsform im Solverfall verworfen; schwache integrative Fassung bleibt prüfbar | D009 |
| AFS-DMO | Minimaler ML/AI-for-Science-Provenance-Demonstrator | ACCEPTED | Testdesign für zusätzliche daten-/lernbasierte Übersetzung eingefroren | D010 |
| ML-IC | ML Implementation Contract v0.1 | PENDING REVIEW | technische Vorregistrierung vor Dataset-Code und Training | — |
| C07? | ML-Provenance-Claim-Kandidat | NOT STARTED | erst nach ML-Run und erneutem Vergleich mit Standard-ML-Credibility bewertbar | — |

## Arbeitsregel

Ein Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet **nicht endgültig bewiesen**, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der vollständige numerische v0.1-Demonstrator stützt C05. Der anschließende harte Vergleich gegen etablierte numerische Analysis, V&V/Credibility und Simulationsphilosophie widerlegt nicht die Trias als Organisationsschema, trägt aber **keine starke Behauptung neuer numerischer Validierungsfragen**. C06-R beschränkt den derzeitigen Mehrwert daher auf durchgängige Integrations-/Provenance-Zuordnung.

D010 führt nun genau eine daten-/lernbasierte Übersetzung ein. Noch wird kein neuer ML-Claim akzeptiert. Vor jedem Training steht die Akzeptanz des `ML Implementation Contract v0.1`.

## Abhängigkeitslogik

C01 → C02 → C03 → C04 → D005 → D006 → D007 → Full v0.1 run → C05/D008 → C06-R/D009 → AFS-DMO/D010 → ML-IC review → ML skeleton → ML run → erneuter Originalitätstest.

Die Reihenfolge kann revidiert werden, wenn die Evidenzprüfung eine frühere Annahme problematisch macht.