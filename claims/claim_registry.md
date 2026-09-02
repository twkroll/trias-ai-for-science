# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | begrifflich anschlussfähig; konkrete Trias-Rolle methodologische Setzung | D002 |
| C03 | Sundman / analytische vs operative Verfügbarkeit | ACCEPTED | mathematisch-historischer Kern gestützt | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ Nutzbarkeit | ACCEPTED | Identifizierbarkeit als querliegende Auditdimension | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Figure-eight Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl erzeugt use-case-relative Profile | ACCEPTED | numerischer Full Run stützt moderate Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED / SUPERSEDED CANDIDATE | weiterer Comparator-Audit empfiehlt engere Revision C06-R2 | D009 |
| C06-R2 | Directed Trias als konzeptionelle Synthese / Audit-Linse | PENDING REVIEW | keine neue Fehler-/V&V-/Provenance-/Identifiability-Kategorie gezeigt; möglicher Restwert = fachübergreifende Synthese | — |
| AFS-DMO | ML-Provenance-Demonstrator | ACCEPTED | v0.1 ausgeführt; v0.2 technisch vorbereitet | D010 |
| ML-IC-v0.1 | ML Implementation Contract v0.1 | ACCEPTED | eingefroren | D011 |
| ML-SKEL-v0.1 | ML Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | ML Provenance Full Run | COMPLETE / INCONCLUSIVE | Learner-Resolvability verletzt | D013 |
| C07 | ursprünglicher ML-Provenance-Claim | NOT ASSESSABLE | v0.1 entscheidet den Claim nicht | — |
| ML-v0.2 | Resolvability Repair | ACCEPTED / PAUSED | technisch vorbereitet; nicht Mainline | D013–D015 |
| ML-IC-v0.2 | ML Implementation Contract v0.2 | ACCEPTED | eingefroren | D014 |
| ML-SKEL-v0.2 | ML Skeleton v0.2 | READY / PAUSED | technische Tests bestanden | — |
| DT-v0.1 | Directed Trias | ACCEPTED AS WORKING REVISION | Forward/Inverse-Auditgrammatik; starke Originalität durch Comparator-Audit nicht gestützt | D015 |
| C07-L | starke Lucarini-Bridge als Novelty | REJECTED / SUPERSEDED | Comparator-Audit zeigt etablierte Vorläufer | D016 |
| C07-L-R | moderate Equation-Discovery-Bridge | ACCEPTED AS WORKING CLAIM | externer Zhai–Lucarini–Lai-Fall; eigener Minimalfall negativ | D016 |
| INV-DMO-v0.1 | Minimal Inverse-Direction Demonstrator | ACCEPTED | Lorenz-63 + gepaarte Missingness/Reconstruction + feste SINDy-Pipeline | D017 |
| INV-IC-v0.1 | Inverse-Direction Implementation Contract | ACCEPTED | Parameter/Gates eingefroren | D018 |
| INV-SKEL-v0.1 | Inverse-Direction Code Skeleton | ACCEPTED | gezielte Tests 6 passed; Smoke nichtwissenschaftlich | D019 |
| INV-RUN-v0.1 | Inverse scientific full run | COMPLETE / INFORMATIVE_NEGATIVE | G1–G3 PASS; structural perturbation linear 1/3, cubic 0/3 | D020 |
| INV-COMP-v0.1 | Comparator audit on inverse negative result | COMPLETE | starke Abdeckung durch System ID, Identifiability, V&V, Provenance und Assurance Cases | D020 follow-up |

## Aktueller Evidenzstand

Der Figure-eight-Demonstrator stützt C05, aber keine starke Trias-Neuheit gegenüber V&V. ML v0.1 blieb wegen fehlender Learner-Resolvability inconclusive. Der inverse Full Run ist nach D020 ein akzeptiertes `INFORMATIVE_NEGATIVE`: Der interessierende strukturell-andere-aber-dynamisch-ähnliche Effekt tritt im eingefrorenen Minimaldesign nicht seed-robust auf.

Der anschließende Comparator-Audit ist abgeschlossen. Er zeigt, dass die wesentlichen Diagnosefunktionen des Projekts stark durch etablierte Rahmen abgedeckt werden:

```text
System Identification / SINDy robustness
+ structural/practical identifiability / structural error
+ M&S / SciML V&V and credibility
+ workflow/data provenance
+ Claims–Arguments–Evidence / assurance cases
```

Damit ist derzeit keine neue Fehler-, Validierungs-, Provenance- oder Identifiability-Kategorie der Directed Trias belegt. Als möglicher Restbeitrag bleibt eine kompakte fachübergreifende Synthese, die Forward- und Inverse-Fälle in einer gemeinsamen Sprache ordnet. Dieser Rest ist als C06-R2 zur Entscheidung vorgelegt.

## Abhängigkeitslogik

```text
C01–C06-R
-> ML v0.1 inconclusive
-> D013/D014 ML v0.2 vorbereitet
-> D015 Directed Trias + ML-v0.2 pause
-> D016 C07-L-R
-> D017 inverse MVP spec
-> D018 inverse implementation contract
-> D019 inverse code skeleton
-> D020 inverse full run accepted: INFORMATIVE_NEGATIVE
-> comparator audit COMPLETE
-> C06-R2 review
-> recommended: paper contribution boundary + outline
-> only later decide whether any paused empirical branch deserves independent continuation
```

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; C06-R2-Status, Directed Trias, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
