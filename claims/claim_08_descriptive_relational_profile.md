# Claim 08 — Descriptive Relational Profile (C08-D-R)

**Status:** ACCEPTED AS WORKING CLAIM — D024  
**Stand:** 2026-09-03  
**Depends on:** D022, D023, D024, `theory/descriptive_trias_profile_test_v0_1.md`

## Akzeptierte Arbeitsfassung

> **C08-D-R:** In Computational Science und AI for Science kann der Evidenzstatus eines Modells deskriptiv in drei relationsspezifische Bereiche zerlegt werden: Zielsystem–Theorie (`R–T`), Theorie–computational realization (`T–C`) und computational realization–Zielsystem (`C–R`). Dieselbe globale Erfolgsbezeichnung oder Performancemetrik kann je nach wissenschaftlichem Workflow Evidenz für unterschiedliche dieser Relationen darstellen; Evidenz auf einer Relation etabliert die anderen daher nicht automatisch. Ein relationales Profil macht diese Differenz explizit, sofern jeder Kantenstatus an einen konkreten wissenschaftlichen Claim/Facet, einen Use Case, Evidenz und Scope gebunden wird. Der beanspruchte Beitrag ist diese gemeinsame deskriptive Profilgrammatik, nicht ein neuer Fehlertyp, eine notwendige Trade-off-Theorie oder eine normative Rangordnung von Modellen.

## Gestützt durch den Profile Test

Der Profile Test zeigt analytische Diskriminationsleistung in sechs Falltypen:

- Sundman;
- Figure-eight / numerische Solver;
- Black-box ML auf realen Daten;
- ML-Surrogat auf synthetischen Daten;
- Physics-informed ML;
- Equation Discovery.

Besonders stark ist die Unterscheidung zwischen:

```text
synthetic teacher accuracy -> primär T-C-Evidenz
real held-out prediction   -> primär C-R-Evidenz
physics constraint         -> primär T-C-Evidenz
mechanistic adequacy       -> primär R-T-Evidenz
```

## Wichtige Präzisierung

Die drei Kanten sind keine eindimensionalen Scores. Jeder Status muss mindestens relativ zu

```text
Use Case
Claim/Facet
Evidence
Scope
```

gelesen werden.

Die Topologie der Trias ist damit einfach, ihre Semantik aber absichtlich evidenz- und claimspezifisch.

D024 akzeptiert zusätzlich als Guardrail, dass Evidenz **nicht standardmäßig transitiv** von einer Kante auf eine andere übertragen werden darf. Jede solche Übertragung benötigt einen expliziten Bridge-Claim mit dokumentierten Prämissen und Scope.

## Non-Claims

C08-D-R behauptet nicht:

- eine notwendige Nullsummen-Trade-off-Struktur;
- Unabhängigkeit der drei Kanten;
- einen globalen Modellscore;
- neue V&V-, Provenance-, Identifiability- oder Assurance-Kategorien;
- dass Prediction ohne Understanding neu sei;
- dass sim-to-real gaps neu seien;
- dass practical/purpose-relative adequacy neu sei;
- empirische Überlegenheit des Profils gegenüber bestehenden Frameworks;
- endgültig bewiesene Originalität der exakten Profilstruktur.

## Evidenzstatus

```text
analytische Diskriminationsleistung: POSITIVE
praktische Nutzer-/Entscheidungsnützlichkeit: UNTESTED
vollständiger Literatur-Novelty-Nachweis: UNVERIFIED
```

## Nächste Abhängigkeit

Das `Edge Semantics + Evidence Ledger v0.1` präzisiert die Kanten in Facets, Evidence-Typen, Statusregeln, Target-Typen und Bridge-Claims. Nach dessen Review folgt ein letzter gezielter Novelty-Audit der präzisierten relationalen Profilgrammatik, bevor der Paper-Hauptclaim eingefroren wird.