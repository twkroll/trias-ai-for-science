# D024 — C08-D-R als Working Claim akzeptiert; Edge Semantics freigegeben

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D022, D023, `theory/descriptive_trias_profile_test_v0_1.md`

## Entscheidung

Die revidierte Fassung **C08-D-R** wird als aktueller Working Claim der Descriptive Trias akzeptiert:

> In Computational Science und AI for Science kann der Evidenzstatus eines Modells deskriptiv in drei relationsspezifische Bereiche zerlegt werden: Zielsystem–Theorie (`R–T`), Theorie–computational realization (`T–C`) und computational realization–Zielsystem (`C–R`). Dieselbe globale Erfolgsbezeichnung oder Performancemetrik kann je nach wissenschaftlichem Workflow Evidenz für unterschiedliche dieser Relationen darstellen; Evidenz auf einer Relation etabliert die anderen daher nicht automatisch. Ein relationales Profil macht diese Differenz explizit, sofern jeder Kantenstatus an einen konkreten wissenschaftlichen Claim/Facet, einen Use Case, Evidenz und Scope gebunden wird. Der beanspruchte Beitrag ist diese gemeinsame deskriptive Profilgrammatik, nicht ein neuer Fehlertyp, eine notwendige Trade-off-Theorie oder eine normative Rangordnung von Modellen.

## Evidenzstatus

Akzeptiert wird ausschließlich folgende begrenzte Lesart:

```text
analytische Diskriminationsleistung: POSITIVE
praktische Nutzer-/Entscheidungsnützlichkeit: UNTESTED
starker Literatur-Novelty-Nachweis: UNVERIFIED
```

C08-D-R ist damit **kein finaler Originalitätsclaim**.

## Mitakzeptierte Guardrails

1. `R`, `T` und `C` sind funktionale epistemische Rollen, keine notwendigerweise ontologisch unabhängigen Entitäten.
2. Die drei Kanten sind keine skalaren Qualitätskoordinaten.
3. Jeder Kantenstatus ist claim-, facet-, use-case-, evidenz- und scope-relativ.
4. Zwischen den Kanten wird keine notwendige Nullsummen-Trade-off-Struktur behauptet.
5. Evidenz darf nicht standardmäßig transitiv von einer Kante auf eine andere übertragen werden.
6. Synthetische und reale Targets müssen explizit unterschieden werden.
7. `NOT_APPLICABLE` ist kein negativer Qualitätsstatus, sondern bedeutet, dass die betreffende Relation für den spezifizierten wissenschaftlichen Claim nicht ausgebildet ist.
8. Der konservative C06-R2-Pivot bleibt als Fallback gültig, falls die präzisierte Profilgrammatik den finalen Literatur-/Novelty-Test nicht trägt.

## Freigegebener nächster Schritt

Es wird ausschließlich ein **Edge Semantics + Evidence Ledger v0.1** ausgearbeitet. Dieses Dokument muss mindestens festlegen:

- Semantik von `R`, `T`, `C`;
- Facetten der drei Kanten `R–T`, `T–C`, `C–R`;
- Evidenztypen, die eine jeweilige Kante direkt oder indirekt stützen können;
- Statusregeln für `ESTABLISHED`, `PARTIAL`, `UNCERTAIN`, `UNTESTED`, `NOT_APPLICABLE`;
- Regeln für synthetische versus reale Targets;
- explizite Nicht-Transitivität sowie zulässige Bridge-Argumente zwischen Kanten;
- ein minimales maschinen-/tabellenlesbares Ledger-Schema;
- Beispiele für AI-for-Science-Claims, die bei identischer Metrik auf unterschiedlichen Kanten liegen.

Noch kein neuer numerischer Versuch und noch kein finaler Paper-Hauptclaim.