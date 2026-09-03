# Claim 08 — Descriptive Relational Profile v2 (C08-D-R2)

**Status:** PENDING REVIEW  
**Stand:** 2026-09-03  
**Depends on:** D024, D025, `literature/relational_profile_novelty_audit_v0_1.md`

## Vorgeschlagene Arbeitsfassung

> **C08-D-R2:** Die Descriptive Trias wird nicht als neue Dreieckstopologie von Realität, Theorie und Berechnung beansprucht; eine strukturell sehr ähnliche Triade aus Reality/Problem Entity, Conceptual Model und Computerized Model mit den Relationen qualification/conceptual validity, verification und validation ist in der klassischen Model-Credibility-Literatur etabliert. Der mögliche Beitrag der Trias liegt in einer wissenschaftsphilosophischen Generalisierung dieser Struktur für Computational Science und AI for Science: `T` wird als expliziter theoretischer, mechanistischer oder erklärender Claim typisiert und kann fehlen oder datengetrieben inferiert werden; `C` umfasst numerische, gelernte und inferierende computational realizations; und Evidenz wird claimspezifisch danach profiliert, welche Relation sie tatsächlich stützt. Diese Generalisierung ist als interpretative Synthese zu positionieren, nicht als neue V&V-Theorie.

## Warum C08-D-R revidiert werden muss

Der finale direkte Novelty-Audit identifiziert einen historischen Vorläufer, der der bisherigen R/T/C-Struktur topologisch nahezu isomorph ist:

```text
Reality / Problem Entity
Conceptual Model
Computerized Model
```

mit:

```text
Reality <-> Conceptual Model      = qualification / conceptual model validity
Conceptual Model <-> Computerized = verification
Computerized Model <-> Reality    = validation / operational validity
```

Damit ist die Dreieckstopologie selbst kein tragfähiger Neuheitsclaim.

## Möglicher verbleibender Delta

Die Trias könnte gegenüber der klassischen Simulation-V&V-Lesart Folgendes generalisieren:

1. `T` ist nicht nur ein Simulations-Conceptual-Model, sondern der explizite wissenschaftliche Theorie-/Mechanismus-/Erklärungsclaim.
2. `T` kann `NONE_CLAIMED` sein, etwa bei enger Black-box Prediction.
3. `T` kann Ergebnis einer computational inference sein, etwa bei Equation Discovery.
4. `C` umfasst neben klassischen numerischen Implementierungen auch Surrogate, learned operators, Inferenz- und Rekonstruktionspipelines.
5. Ein identischer Performancewert wird danach typisiert, welchen epistemischen Claim er tatsächlich stützt.
6. Synthetic/real target switching wird als Änderung des Claimprofils explizit gemacht.
7. Die Struktur wird als deskriptive wissenschaftsphilosophische Profilierung verschiedener Arten wissenschaftlichen Erfolgs gelesen, nicht primär als normatives Credibility-Verfahren.

## Non-Claims

C08-D-R2 behauptet nicht:

- dass `Reality / Conceptual Model / Computerized Model` neu sei;
- dass Verification, Validation oder Conceptual Model Validity neu seien;
- dass die drei Paarrelationen erstmals durch die Trias unterschieden würden;
- dass Intended Use oder Scope-Relativität neu seien;
- dass synthetische Referenten und reale Validation erstmals unterschieden würden;
- dass Bridge-Claims oder Claim-Evidence-Strukturen neu seien;
- dass die AI-for-Science-Generalisation bereits als praktisch überlegen erwiesen sei.

## Evidenzstatus

```text
R/T/C topology novelty: REJECTED
edge distinction novelty: REJECTED
analytical discrimination across project cases: POSITIVE
AI-for-Science reinterpretation/generalisation: PLAUSIBLE
practical utility: UNTESTED
unique originality of the generalisation: NOT YET ESTABLISHED
```

## Entscheidungsempfehlung

**ACCEPT C08-D-R2 and rebase the paper genealogy.**

Danach kein weiteres Experiment. Nächster Schritt: `Paper Contribution Boundary v0.2 — From Model-Credibility Triangle to Descriptive Trias for AI for Science`.