# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; AI-for-Science-Test läuft | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | Begrifflich gut anschlussfähig; konkrete Trias-Rolle ist methodologische Setzung | D002 |
| C03 | Sundmans konvergente Reihenlösung und praktische Traktabilität | ACCEPTED | Mathematisch-historischer Kern gut gestützt; methodologische Lesart projektintern | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit | ACCEPTED | Numerisch gut gestützt; Machbarkeit/Nutzbarkeit projektinterne Auditbegriffe | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Scope D005/D006, Skeleton D007, Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl kann wissenschaftlich relevante Profile erzeugen | ACCEPTED | Full v0.1 run stützt moderate zweckrelative Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED | Starke Neuheitsform im Solverfall verworfen; schwache integrative Fassung bleibt prüfbar | D009 |
| AFS-DMO | Minimaler ML/AI-for-Science-Provenance-Demonstrator | ACCEPTED | Testdesign für zusätzliche daten-/lernbasierte Übersetzung eingefroren | D010 |
| ML-IC | ML Implementation Contract v0.1 | ACCEPTED | technische Vorregistrierung eingefroren; noch kein wissenschaftlicher ML-Run | D011 |
| ML-SKEL | ML Dataset-/Training-Skeleton v0.1 | READY FOR REVIEW | lokale Tests 4/4; Smoke-Pipeline erfolgreich; wissenschaftliche Evidenz noch ausstehend | — |
| C07? | ML-Provenance-Claim-Kandidat | NOT STARTED | erst nach ML Full Run und erneutem Vergleich mit Standard-ML-Credibility bewertbar | — |

## Arbeitsregel

Ein Claim erhält den Status `ACCEPTED`, wenn die vorgeschlagene Arbeitsfassung im Forschungsdialog durch `GO` bestätigt wurde. `ACCEPTED` bedeutet **nicht endgültig bewiesen**, sondern als aktuelle Forschungsgrundlage akzeptiert.

## Aktueller Evidenzstand

Der vollständige numerische v0.1-Demonstrator stützt C05. Der harte Vergleich gegen etablierte Numerik/V&V trägt keine starke Behauptung neuer numerischer Validierungsfragen; C06-R beschränkt den Mehrwert auf Integrations-/Provenance-Zuordnung.

D010 und D011 führen nun genau eine daten-/lernbasierte Übersetzung ein und registrieren deren technische Kontrolllogik vor dem Full Run. Der ML-Skeleton implementiert die gepaarte Teacher-Datengenerierung, das Residual-MLP, One-Step-Metriken, Provenance-Fehlerzerlegung und MU1/MU2-Pipeline. Die lokale Smoke-Prüfung ist rein technisch und wird nicht als wissenschaftliche Evidenz verwendet.

## Abhängigkeitslogik

C01 → C02 → C03 → C04 → D005 → D006 → D007 → Full v0.1 run → C05/D008 → C06-R/D009 → AFS-DMO/D010 → ML-IC/D011 → ML-SKEL review → ML Full Run → erneuter Originalitätstest → möglicher C07.

Die Reihenfolge kann revidiert werden, wenn die Evidenzprüfung eine frühere Annahme problematisch macht.
