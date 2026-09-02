# Claim Registry

Das Register enthält die wissenschaftlich relevanten Claims und Demonstratorentscheidungen des Projekts in Abhängigkeitsreihenfolge.

| ID | Kurzbezeichnung | Status | Evidenzstatus | Entscheidung |
|---|---|---|---|---|
| C01 | Diagnostischer Mehrwert der Trias | ACCEPTED / UNDER TEST | Reiner Solverfall stützt nur schwache integrative Fassung; Directed-Trias-Schärfung wird geprüft | D001 |
| C02 | Synthetisches Zielsystem als Realitäts-Pol | ACCEPTED | begrifflich anschlussfähig; konkrete Trias-Rolle methodologische Setzung | D002 |
| C03 | Sundman / analytische vs operative Verfügbarkeit | ACCEPTED | mathematisch-historischer Kern gestützt | D003 |
| C04 | Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ Nutzbarkeit | ACCEPTED | Identifizierbarkeit als querliegende Auditdimension | D004 |
| DMO | Numerischer Minimaldemonstrator | ACCEPTED / COMPLETE | Figure-eight Full Run abgeschlossen | D005–D007 |
| C05 | Implementierungswahl erzeugt use-case-relative Profile | ACCEPTED | numerischer Full Run stützt moderate Fassung | D008 |
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | ACCEPTED / UNDER REFINEMENT | starke Neuheitsform gegenüber V&V verworfen | D009 |
| AFS-DMO | ML-Provenance-Demonstrator | ACCEPTED | v0.1 ausgeführt; v0.2 technisch vorbereitet | D010 |
| ML-IC-v0.1 | ML Implementation Contract v0.1 | ACCEPTED | eingefroren | D011 |
| ML-SKEL-v0.1 | ML Skeleton v0.1 | ACCEPTED | technische Tests/Smoke bestanden | D012 |
| ML-RUN-v0.1 | ML Provenance Full Run | COMPLETE / INCONCLUSIVE | Learner-Resolvability verletzt | D013 |
| C07 | ursprünglicher ML-Provenance-Claim | NOT ASSESSABLE | v0.1 entscheidet den Claim nicht | — |
| ML-v0.2 | Resolvability Repair | ACCEPTED / PAUSED | technisch vorbereitet; Full Run strategisch pausiert | D013–D015 |
| ML-IC-v0.2 | ML Implementation Contract v0.2 | ACCEPTED | eingefroren | D014 |
| ML-SKEL-v0.2 | ML Skeleton v0.2 | READY / PAUSED | technische Tests bestanden | — |
| DT-v0.1 | Directed Trias | ACCEPTED AS WORKING REVISION | Forward/Inverse-Auditgrammatik; Originalität ungeklärt | D015 |
| C07-L | starke Lucarini-Bridge als Novelty | REJECTED / SUPERSEDED | Comparator-Audit zeigt etablierte Vorläufer | D016 |
| C07-L-R | moderate Equation-Discovery-Bridge | ACCEPTED AS WORKING CLAIM | externer Zhai–Lucarini–Lai-Fall; Trias-Anteil Integrationshypothese | D016 |
| INV-DMO-v0.1 | Minimal Inverse-Direction Demonstrator | ACCEPTED | Lorenz-63 + gepaarte Missingness/Reconstruction + feste SINDy-Pipeline | D017 |
| INV-IC-v0.1 | Inverse-Direction Implementation Contract | ACCEPTED | Reference-, Mask-, Reconstruction-, Derivative-, SINDy-, Gate- und Äquivalenzparameter eingefroren | D018 |
| INV-SKEL-v0.1 | Inverse-Direction Code Skeleton | READY FOR REVIEW | neue gezielte Tests: 6 passed; nichtwissenschaftlicher Smoke Run vollständig | — |

## Aktueller Evidenzstand

Der numerische Demonstrator stützt C05, nicht aber eine starke Originalitätsbehauptung gegenüber V&V. Der ML-v0.1-Zweig blieb wegen fehlender Learner-Resolvability unentschieden und v0.2 bleibt pausiert.

D015–D016 verschieben den aktuellen Test auf die Directed Trias und die inverse Equation-Discovery-Kette. D017 friert den minimalen Lorenz/SINDy-Demonstrator ein; D018 friert dessen exakte technische Vorregistrierung ein.

Der Code Skeleton implementiert inzwischen die technischen Kernbausteine von Referenzintegration über Missingness/Reconstruction, Derivative Estimation und STLSQ bis zu Structural Metrics sowie Forward-/Langzeitvalidierungsfunktionen. Gezielte lokale Tests ergeben `6 passed`. Ein absichtlich verkürzter Smoke Run bestätigt Reference-/Mask-/Pairing-Integrität; seine SINDy-Ergebnisse werden nicht wissenschaftlich interpretiert.

## Abhängigkeitslogik

```text
C01–C06-R
-> ML v0.1 inconclusive
-> D013/D014 ML v0.2 vorbereitet
-> D015 Directed Trias + ML-v0.2 pause
-> D016 C07-L-R
-> D017 inverse MVP spec
-> D018 inverse implementation contract
-> INV-SKEL-v0.1 review
-> inverse scientific full run
-> comparator audit
-> decision: resume ML v0.2 vs secondary vs replace
-> renewed originality test
```

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; Directed Trias, C07-L-R und der inverse MVP werden berücksichtigt.
