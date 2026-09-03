# D039 — W9 `PASS_TO_SOURCE_INTEGRATION` akzeptiert; W10 Source Hardening freigegeben

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D038, `paper/w9_source_bibliography_audit_v0_1.md`, `paper/manuscript_integrated_v0_2.md`

## Entscheidung

Der W9 Source & Bibliography Audit wird mit

```text
PASS_TO_SOURCE_INTEGRATION
```

akzeptiert.

Akzeptiert bleiben:

```text
source coverage             = PASS
bibliographic resolvability = PASS
central claim support       = PASS
blocking source gap         = NO
P3                          = UNCHANGED
```

## Verbindliche W9-Regeln

W10 muss alle acht Quellenregeln integrieren:

```text
W9-R1  Schlesinger 1979: model qualification; conceptual-model validity Sargent zuordnen.
W9-R2  Zhai–Lucarini–Lai nur als 2025 arXiv preprint zitieren.
W9-R3  Sundman konsistent als 1912 führen; keine spektakulären Termzahlclaims.
W9-R4  W3C PROV: Entity/Activity/Agent + Usage/Generation/Derivation; parameters nicht als core class.
W9-R5  Villaverde auf parametrische structural identifiability begrenzen; Strukturclaims zusätzlich Hadaegh/System-ID/Equation Discovery stützen.
W9-R6  Naser als konkretes Framework, nicht als alleinigen Feldkonsens-Anker formulieren.
W9-R7  ASME V&V 40 nur als domain-specific medical-device credibility standard verwenden.
W9-R8  Abwesenheitsclaim nur als `no direct analogue identified in our documented audits` formulieren.
```

## Freigegebener Schritt W10

> **Source-Hardened Manuscript v0.3 — integrate W9-R1…R8, attach verified citations/BibTeX, standardize citation keys, and produce a source-clean manuscript without changing P3.**

W10 darf keine neue Novelty-Suche, keine neuen Experimente und keine Stärkung von P3 enthalten.

## Gate nach W10

Geprüft werden:

```text
W9-R1…R8 integration
citation-key consistency
bibliography completeness for cited external claims
preprint/standard status accuracy
project-internal evidence preservation
P3 consistency
journal-neutral source cleanliness
```

Erlaubte Urteile:

```text
PASS_TO_JOURNAL_SELECTION
REVISE_SOURCE_HARDENING
BLOCKED_BY_BIBLIOGRAPHIC_GAP
```
