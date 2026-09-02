# Current Status

## Phase

**Week 1 — Claim and Scope / C06 Originality Stress Test**

Das Claim-and-Scope-Fundament, der Minimaldemonstrator, der Implementation Contract und der getestete Code-Skeleton sind eingefroren. Der vollständige v0.1-Lauf wurde ausgeführt und C05 ist akzeptiert. Aktuell wird der mögliche zusätzliche diagnostische Wert der Trias gegen etablierte numerische Analysis, Verification & Validation und Simulationsphilosophie geprüft.

## Akzeptierte Entscheidungen

- **C01 / D001:** Trias als methodologisches Audit-Framework; diagnostischer Mehrwert ist die zentrale Hypothese.
- **C02 / D002:** synthetisches Zielsystem als funktionaler Realitäts-Pol; keine notwendige ontologische Trennung der Pole.
- **C03 / D003:** Sundman als konvergente, praktisch extrem ineffiziente Reihenrepräsentation; formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.
- **C04 / D004:** Konvergenz, operative Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit werden getrennt; V&V bleibt Vergleichsrahmen.
- **Minimal Demonstrator / D005:** Figure-eight + DOP853 + RK4 + Velocity-Verlet, U1/U2, kein ML/chaotischer Fall in v0.1.
- **Implementation Contract / D006:** v0.1-Konfiguration, Referenzlogik, Schrittweiten, Metriken, Gates und Artefakte eingefroren.
- **Code Skeleton / D007:** minimaler getesteter Skeleton als faithful implementation von D006 akzeptiert.
- **C05 / D008:** unterschiedliche numerische Operationalisierungen können bei gleichem Zielsystem/Theorie verschiedene wissenschaftlich relevante Fehler- und Strukturprofile erzeugen; Bewertung ist use-case-relativ.

## Full Demonstrator v0.1

**Status:** COMPLETE

Reference gates und U1-Refinement-Gates sind erfüllt. Der Hauptbefund ist ein mehrdimensionales Implementierungsprofil: RK4 ist im getesteten Bereich trajectory-genauer, während Velocity-Verlet deutlich geringeren fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau zeigt. Daraus folgt keine globale Solver-Rangfolge.

Details: [`demonstrator/full_run_v0_1_results.md`](demonstrator/full_run_v0_1_results.md).

## Aktuelle Aufgabe

### C06 — zusätzlicher diagnostischer Wert des Trias-Audits
**Status:** IN PROGRESS / STRONG FORM UNDER PRESSURE

Der harte Vergleich wird mit denselben Demonstratorresultaten durchgeführt:

1. gewöhnliche numerische Analysis / Verification & Validation / Credibility Assessment;
2. Trias-Audit mit Zielsystem, Theorie, Berechnung und Übergangskanten.

Vorläufiger Befund: Die starke Form von C06 — dass die Trias im numerischen Figure-eight-Fall neue Fehler- oder Validierungsfragen erzeugt — ist derzeit nicht ausreichend gestützt. Etablierte V&V-/Credibility-Frameworks decken bereits Code/Solution Verification, intended use, uncertainty, sensitivity, model assumptions und Ergebnis-Credibility ab. Ein möglicher verbleibender Mehrwert liegt eher in der expliziten integrativen Zuordnung über Zielsystem–Theorie–Berechnung hinweg und in der Verbindung von analytischer Traktabilität (Sundman) mit operativer Umsetzung.

Siehe [`claims/claim_06.md`](claims/claim_06.md) und [`demonstrator/c06_comparison_v0_1.md`](demonstrator/c06_comparison_v0_1.md).

## Nächste Entscheidung

Zu entscheiden ist, ob C06 in einer **revidierten schwachen/integrativen Form** akzeptiert wird und die starke Neuheitsbehauptung verworfen wird.

Falls diese Revision akzeptiert wird, ist der nächste sinnvolle Test eine minimale AI-for-Science-Erweiterung, weil der reine Solverfall den Neuheitsanspruch gegenüber etabliertem V&V nicht trägt.

## Arbeitsregel

`GO` im Forschungsdialog = aktuelle Empfehlung akzeptiert; Decision-/Status-/Claim-Dokumentation aktualisieren; anschließend zum nächsten abhängigen Schritt übergehen.