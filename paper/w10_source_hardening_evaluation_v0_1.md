# W10 — Source-Hardening Evaluation v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D039, `paper/manuscript_source_hardened_v0_3.md`, `paper/references_v0_3.bib`, W9

## 1. Prüfziel

W10 prüft, ob die W9-Quellenregeln vollständig in eine journal-neutrale, source-clean Manuskriptfassung integriert wurden, ohne P3 zu verändern.

Geprüft werden:

```text
W9-R1…R8 integration
citation-key consistency
bibliography coverage
publication-status accuracy
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

## 2. Gesamturteil

```text
OVERALL = PASS_TO_JOURNAL_SELECTION
```

Die Source-Hardening-Stufe ist vollständig genug, um nun ein Zieljournal festzulegen. Es gibt keinen blockierenden bibliographischen Gap und keine quellenbedingte Änderung des Principal Claim P3.

## 3. W9-R1…R8 Integration

```text
W9-R1 Schlesinger/Sargent terminology = PASS
W9-R2 Zhai preprint status            = PASS
W9-R3 Sundman 1912 + no term-count    = PASS
W9-R4 W3C PROV core terminology       = PASS
W9-R5 identifiability boundary        = PASS
W9-R6 Naser wording precision         = PASS
W9-R7 ASME domain-specific boundary   = PASS
W9-R8 absence-claim restriction       = PASS
```

### R1

Section 2 trennt jetzt explizit:

```text
Schlesinger 1979 -> model qualification / model verification / model validation
Sargent 2013    -> conceptual-model validity / model verification / operational validity
```

Das R/T/C-Mapping bleibt ausdrücklich genealogisch und approximativ.

### R2

Zhai–Lucarini–Lai wird ausschließlich als

```text
Zhai et al. (2025), arXiv preprint, arXiv:2509.03769
```

geführt. Keine peer-reviewte 2026-Publikation wird impliziert.

### R3

Sundman wird konsistent als 1912 zitiert. Die praktische Ineffizienz wird qualitativ formuliert; keine spektakuläre Termzahl wird verwendet.

### R4

Section 7 beschreibt W3C PROV über `Entity`, `Activity`, `Agent` sowie Usage/Generation/Derivation. Parameter werden nicht als eigene PROV-Kernklasse behauptet.

### R5

Villaverde et al. wird auf parametrische structural identifiability begrenzt. Modellform-/Strukturambiguität wird zusätzlich über Hadaegh–Bekey sowie SINDy/SINDy-PI kontextualisiert.

### R6

Naser wird als konkretes P.E.D.U.D.-Framework formuliert, nicht als alleiniger Beleg eines Feldkonsenses.

### R7

ASME V&V 40 wird ausdrücklich als domain-specific medical-device standard bezeichnet.

### R8

Der stärkste verbleibende Abwesenheitssatz lautet nun sinngemäß:

> no direct analogue was identified in our documented audits

und wird ausdrücklich als audit-relative, nicht universelle Nicht-Existenzbehauptung begrenzt.

## 4. Citation-key consistency

**PASS.**

Das Manuskript nutzt einen journal-neutralen Pandoc-/BibTeX-Key-Stil. Alle im Manuskript verwendeten externen Keys sind in

`paper/references_v0_3.bib`

vorhanden.

Standardisierte Hauptkeys:

```text
schlesinger1979
sargent2013
nasa7009b2024
nasahdbk7009b2026
asmevv402018
jakeman2026
naser2025
vinuesa2026
karniadakis2021
kramer2026
zhai2025preprint
sundman1912
belorizky1930
henkel2001
chenciner2007
musielak2014
w3cprov2013
khan2019
goodenough2012
gsn2021
villaverde2016
hadaegh1985
brunton2016
kaheman2020
```

## 5. Bibliography coverage

**PASS.**

Die zentrale externe Claimstruktur ist jetzt bibliographisch abgedeckt:

```text
classical model credibility        -> Schlesinger / Sargent
modern credibility                 -> NASA / ASME / Jakeman
ML epistemic functions             -> Naser
ML roles by theory availability    -> Vinuesa et al.
PIML                               -> Karniadakis et al.
automated/equation discovery       -> Kramer et al. / Brunton et al.
Zhai bridge                        -> 2025 arXiv preprint
Sundman control                    -> Sundman + Belorizky/Henkel/Chenciner/Musielak-Quarles
provenance                         -> W3C PROV / CWLProv
assurance                          -> Goodenough et al. / GSN v3
parameter identifiability          -> Villaverde et al.
model-form near-equivalence        -> Hadaegh & Bekey
sparse discovery robustness        -> Brunton et al. / Kaheman et al.
```

## 6. Project-internal evidence

**STRONG PASS.**

Die drei project-specific empirical branches bleiben externen Literaturquellen klar getrennt:

```text
Figure-eight      -> project-internal positive/use-dependent control
Lorenz/SINDy      -> INFORMATIVE_NEGATIVE
ML provenance v0.1-> INCONCLUSIVE_LEARNER_ERROR
```

Externe Quellen werden nicht als Quelle dieser Zahlen oder Klassifikationen benutzt. Der lineare inverse Seed-2-Fall bleibt explorativ.

## 7. P3 consistency

**PASS.**

Source Hardening ändert den Principal Claim nicht. Weiterhin gilt:

```text
framework novelty     = NO
triangle novelty      = NO
individual AI role novelty = NO
residual contribution = MODERATE CROSS-DOMAIN SYNTHESIS
practical usefulness = UNTESTED
```

Die source-hardened Fassung formuliert den Rest als

> genealogically grounded evidence-localization vocabulary

und nicht als neue Credibility-Theorie.

## 8. Journal-neutral source cleanliness

**PASS.**

Die v0.3-Fassung ist bewusst noch nicht auf einen Journalstil festgelegt. Offen für den nächsten Pass bleiben daher nur format- und venue-spezifische Punkte:

```text
citation style / bibliography style
US vs UK spelling
AI for Science vs AI-for-Science house style
heading depth
table formatting
figure requirements
word-limit targeting
abstract length / keywords
supplement / repository citation format
```

Diese Punkte sind kein Quellenproblem.

## 9. Verbleibende bibliographische Kleinrisiken

Keine blockierenden Gaps. Vor finaler Submission sollte beim journal-spezifischen Pass noch maschinell bzw. manuell geprüft werden:

- finaler BibTeX-Import im gewählten LaTeX-/Word-Workflow;
- Journalnamen-/Capitalization-Konventionen;
- offizielle URLs/Dokumentnummern für Standards, falls das Zieljournal sie verlangt;
- vollständige Author-Metadaten aus dem gewählten Citation Export;
- Repository-/Supplement-DOI oder archivierter Release für die project-internal runs.

## 10. Gesamtklassifikation

```text
W9-R1…R8 integration         = PASS
citation consistency         = PASS
bibliography coverage        = PASS
publication-status accuracy  = PASS
project evidence preservation= STRONG PASS
P3 consistency               = PASS
blocking gap                 = NO
-----------------------------------
OVERALL                      = PASS_TO_JOURNAL_SELECTION
```

## 11. Nächste Abhängigkeit

Empfehlung: **W10 = PASS_TO_JOURNAL_SELECTION akzeptieren.**

Danach soll kein weiterer generischer Manuskriptpass erfolgen. Nächster Schritt ist eine explizite Venue-Entscheidung mit realistischen Optionen, voraussichtlich:

```text
A. European Journal for Philosophy of Science
B. Synthese
C. Minds and Machines
D. Studies in History and Philosophy of Science
E. Philosophy of Science (stretch)
```

Nach der Autorentscheidung wird ausschließlich der gewählte journal-spezifische Style-/Submission-Pass ausgeführt.
