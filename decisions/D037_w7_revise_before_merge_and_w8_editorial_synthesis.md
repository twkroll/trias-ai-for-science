# D037 — W7 `REVISE_BEFORE_MERGE` akzeptiert; W8 Editorial Synthesis freigegeben

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D036, `paper/w7_whole_manuscript_audit_v0_1.md`, Sections 1–9 v0.1

## Entscheidung

Der Whole-Manuscript-Audit W7 wird mit der Klassifikation

```text
REVISE_BEFORE_MERGE
```

akzeptiert.

Diese Klassifikation ist ausdrücklich **redaktionell**, nicht wissenschaftlich negativ. Akzeptiert bleiben:

```text
scientific/conceptual survival = PASS
P3 consistency                 = PASS
novelty boundary               = STRONG PASS
evidence-status discipline     = STRONG PASS
descriptive/normative boundary = PASS
paper mode                      = Perspective / Conceptual Synthesis
framework novelty               = NO
residual contribution           = MODERATE CROSS-DOMAIN SYNTHESIS
```

## Verbindliche Revisionsregeln

Die integrierte Manuskriptfassung v0.2 muss die W7-Home-Section-Regel anwenden:

```text
Genealogie / keine Topologie-Novelty       -> Section 2
R/T/C-Semantik + Nichttransfer             -> Section 3
vier AI-for-Science-Rollenkonfigurationen  -> Section 4
negative vs inconclusive evidence          -> Section 6
Comparator-/Contribution-Boundary          -> Section 7
kein globaler Score / kein Trade-off-Gesetz-> Section 8
```

Introduction und Conclusion dürfen diese Punkte nur komprimiert rahmen.

## Freigegebener nächster Schritt

Writing Goal W8:

> **Editorial Synthesis v0.2 — compress Sections 1–9 into a single integrated manuscript while preserving P3 and all accepted evidence classes.**

W8 darf:

- Wiederholungen entfernen;
- Terminologie vereinheitlichen;
- numerische Details reduzieren;
- Tabellen 1–3 beibehalten;
- den Haupttext auf ungefähr `7,000–8,300` Wörter zielen;
- technische Details für spätere Supplement-/Appendix-Auslagerung markieren.

W8 darf **nicht**:

- neue wissenschaftliche Claims einführen;
- negative oder inconclusive Evidenz umklassifizieren;
- neue Experimente starten;
- eine neue freie Novelty-Suche durchführen;
- die Trias als Ersatz für V&V, Provenance, Assurance, Identifiability oder SciML positionieren.

## Gate nach W8

Nach der integrierten Fassung erfolgt ein Editorial-Integration-Gate mit mindestens:

```text
claim consistency
length/proportionality
repetition reduction
terminology consistency
evidence-status preservation
section balance
submission-readiness before source audit
```

Erlaubte Urteile:

```text
PASS_TO_SOURCE_AUDIT
REVISE_INTEGRATED_DRAFT
SHORTEN_TO_PERSPECTIVE
```
