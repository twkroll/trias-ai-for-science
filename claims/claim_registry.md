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
| C06-R | Integrations-/Provenance-Wert des Trias-Audits | SUPERSEDED | weiterer Comparator-Audit führte zu C06-R2 | D009 |
| C06-R2 | Directed Trias als konzeptionelle Synthese / Audit-Linse | ACCEPTED / FALLBACK BOUNDARY | keine neue Fehler-/V&V-/Provenance-/Identifiability-Kategorie gezeigt | D021 |
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
| PAPER-BOUND-v0.1 | Paper Contribution Boundary + Outline | PAUSED / FALLBACK | konservative Synthese-Fassung ausgearbeitet; Descriptive-Trias-Test vorgeschaltet | D021 follow-up |
| DT-DESCR-v0.1 | Descriptive Trias | WORKING THEORY | drei Rollen R/T/C + drei paarweise Adäquanzrelationen; keine notwendige Trade-off-These | D022 |
| DT-LIT-v0.1 | Descriptive Trias Literature Stress Test | ACCEPTED | starke Einzelneuheiten verworfen; kein Direktanalog der exakten Kantenprofilstruktur im v0.1-Test gefunden | D023 |
| DT-PROFILE-v0.1 | Descriptive Trias Profile Test | COMPLETE / PENDING CLAIM DECISION | sechs Falltypen zeigen positive analytische Diskriminationsleistung; Kanten benötigen Facet/Use/Evidence/Scope | D023 follow-up |
| C08-D | ursprünglicher Descriptive Relational Profile Claim | SUPERSEDED CANDIDATE | durch Profile Test zu C08-D-R präzisiert | — |
| C08-D-R | Descriptive Relational Profile, revised | PENDING REVIEW | analytische Diskriminationsleistung positiv; praktische Nützlichkeit untested; starke Originalität unverified | — |

## Aktueller Evidenzstand

Die bisherigen experimentellen und Comparator-Ergebnisse bleiben gültig. D021 setzt eine konservative Fallback-Boundary: Die Trias ist nach bisheriger Evidenz keine neue V&V-, Provenance- oder Identifiability-Theorie.

D022 präzisiert die Autorenintention als primär deskriptive Theorie dreier relationsspezifischer epistemischer Adäquanzen:

```text
A_RT = target/reality <-> theory
A_TC = theory <-> computation
A_CR = computation <-> target/reality
```

D023 akzeptiert den Literatur-Stress-Test. Nicht neu sind computation-as-third-pillar, models-as-mediators, Simulationsepistemologie, Modelltradeoff-Dreiecke, adequacy-for-purpose, prediction-vs-understanding, sim-to-real gaps sowie physics-informed/data-theory integration. Im v0.1-Stress-Test wurde jedoch kein klarer Direktanalog gefunden, der die drei R/T/C-Kanten als gemeinsames deskriptives relationales Profil eines konkreten Modells über Computational Science und AI for Science hinweg verwendet.

Der anschließende Profile Test zeigt nun einen positiven analytischen Effekt. Insbesondere kann derselbe Typ von Performancemetrik epistemisch Verschiedenes belegen:

```text
synthetic teacher accuracy -> primär A_TC
real held-out prediction   -> primär A_CR
physics constraint         -> primär A_TC
mechanistic adequacy       -> primär A_RT
```

Außerdem zeigt der Test, dass Target-Wechsel, Use Case und Claim-Facet explizit Teil des Profils sein müssen. Die drei Kanten dürfen deshalb nicht als drei skalare Gütekoordinaten verstanden werden.

C08-D-R liegt nun zur Review vor. Es beansprucht ausschließlich die gemeinsame deskriptive Profilgrammatik und nicht neue Einzelprobleme, notwendige Tradeoffs oder empirische Überlegenheit gegenüber etablierten Frameworks.

## Abhängigkeitslogik

```text
C01–C06-R
-> ML v0.1 inconclusive
-> D015 Directed Trias
-> D020 inverse run INFORMATIVE_NEGATIVE
-> D021 conservative synthesis boundary
-> D022 Descriptive Trias
-> D023 literature stress test accepted
-> Descriptive Trias Profile Test COMPLETE
-> C08-D-R review
-> recommended: Edge Semantics + Evidence Ledger v0.1
-> final literature/novelty test
-> paper contribution boundary revision
```

## Dialogkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen Projektstand als ausführliches Kooperationsbriefing neu synthetisieren und als PDF plus LaTeX-Quelle erzeugen; Descriptive Trias, C08-D-R, C06-R2-Fallback, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
