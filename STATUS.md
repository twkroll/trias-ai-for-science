# Current Status

## Phase

**Genealogically Rebasing the Descriptive Trias / Paper Contribution Boundary v0.2 Review**

Mit D026 wurde der direkte Relational-Profile Novelty Audit akzeptiert. Die R/T/C-Dreieckstopologie und die drei Paarrelationen werden nicht mehr als originäre Trias-Neuheit beansprucht, weil die klassische Model-Credibility-/V&V-Tradition um Schlesinger/Sargent einen nahezu isomorphen historischen Vorläufer besitzt.

C08-D-R2 ist nun der aktuelle Working Claim. Das Paper wird genealogisch von der klassischen Credibility-Triade ausgehend neu aufgebaut.

## Akzeptierte Entscheidungen

- **D001–D004:** Claim-/Scope-Fundament, synthetisches Zielsystem, Sundman, Bewertungsdimensionen.
- **D005–D008:** Figure-eight-Demonstrator abgeschlossen; C05 akzeptiert.
- **D009:** starke Trias-Neuheit gegenüber V&V verworfen.
- **D010–D014:** ML-Provenance v0.1 `INCONCLUSIVE_LEARNER_ERROR`; v0.2 technisch vorbereitet und pausiert.
- **D015–D016:** Directed Trias als Arbeitsrevision; starke Lucarini-Neuheitsfassung verworfen; moderate Equation-Discovery-Bridge behalten.
- **D017–D020:** inverser Lorenz/SINDy-Zweig vorregistriert und als `INFORMATIVE_NEGATIVE` akzeptiert.
- **D021:** C06-R2 als konservative Fallback-Boundary akzeptiert.
- **D022:** Autorenintention als deskriptive R/T/C-Theorie präzisiert.
- **D023:** erster Descriptive-Trias-Literatur-Stress-Test akzeptiert.
- **D024:** C08-D-R als Working Claim akzeptiert; positive analytische Diskriminationsleistung.
- **D025:** Edge Semantics + Evidence Ledger akzeptiert; direkter Novelty Audit freigegeben.
- **D026:** direkter Novelty Audit akzeptiert; R/T/C-Topologie-Novelty verworfen; C08-D-R2 als Working Claim akzeptiert; Paper genealogisch auf Schlesinger/Sargent rebaset.

## Historischer Ausgangspunkt

Die klassische Model-Credibility-Triade lautet näherungsweise:

```text
Reality / Problem Entity
Conceptual Model
Computerized Model
```

mit:

```text
Reality <-> Conceptual Model      = conceptual model validity / qualification
Conceptual Model <-> Computerized = verification
Computerized Model <-> Reality    = operational validity / validation
```

Diese Struktur wird im Projekt nicht mehr als Rand-Comparator, sondern als **Genealogie des eigenen Ansatzes** behandelt.

## Aktueller Working Claim C08-D-R2

> Die Descriptive Trias wird nicht als neue Dreieckstopologie von Realität, Theorie und Berechnung beansprucht; eine strukturell sehr ähnliche Triade aus Reality/Problem Entity, Conceptual Model und Computerized Model mit den Relationen qualification/conceptual validity, verification und validation ist in der klassischen Model-Credibility-Literatur etabliert. Der mögliche Beitrag der Trias liegt in einer wissenschaftsphilosophischen Generalisierung dieser Struktur für Computational Science und AI for Science: `T` wird als expliziter theoretischer, mechanistischer oder erklärender Claim typisiert und kann fehlen oder datengetrieben inferiert werden; `C` umfasst numerische, gelernte und inferierende computational realizations; und Evidenz wird claimspezifisch danach profiliert, welche Relation sie tatsächlich stützt. Diese Generalisierung ist als interpretative Synthese zu positionieren, nicht als neue V&V-Theorie.

Evidenzstatus:

```text
R/T/C topology novelty: REJECTED
edge distinction novelty: REJECTED
analytical discrimination across project cases: POSITIVE
AI-for-Science reinterpretation/generalisation: PLAUSIBLE
practical utility: UNTESTED
unique originality of the generalisation: NOT YET ESTABLISHED
```

Details: [`claims/claim_08_descriptive_relational_profile_v2.md`](claims/claim_08_descriptive_relational_profile_v2.md).

## Akzeptierte Edge Semantics

Das Ledger aus D025 bleibt gültig:

```text
R = claim-relative target, REAL / SYNTHETIC / HYBRID
T = theory/mechanism/explanation claim, ggf. NONE_CLAIMED oder inferred
C = concrete computational realization/practice
```

Kantenstatus sind gebunden an:

```text
Use Case + Claim/Facet + Evidence + Scope
```

und Evidenztransfer benötigt explizite Bridge-Claims.

## Paper Contribution Boundary v0.2

**Status: PENDING REVIEW.**

Neues Dokument: [`paper/paper_contribution_boundary_v0_2.md`](paper/paper_contribution_boundary_v0_2.md).

Leitfrage:

> Was muss an der klassischen Credibility-Triade verändert oder generalisiert werden, wenn computation in AI for Science nicht mehr nur ein gegebenes conceptual model implementiert, sondern selbst vorhersagt, approximiert, rekonstruiert oder Theorie erzeugt?

Vorgeschlagener Delta:

```text
1. T als expliziter wissenschaftlicher Theorie-/Mechanismus-/Erklärungsclaim;
2. T kann NONE_CLAIMED sein;
3. T kann Output von C sein (Equation Discovery);
4. C umfasst learned/inferential practices, nicht nur Forward-Implementierung;
5. REAL/SYNTHETIC/HYBRID referent switching wird claimspezifisch profiliert;
6. primär deskriptive Typisierung von Arten wissenschaftlichen Erfolgs statt neue Credibility-Zertifizierung.
```

## Rolle der bisherigen Projektfälle im Paper v0.2

```text
Schlesinger/Sargent: genealogisches Fundament
Sundman: kompakter T-C-/Tractability-Motivationsfall
Figure-eight: klassische V&V-Kontrollgruppe; kein Novelty-Beleg
Black-box prediction: zentraler Fall T = NONE_CLAIMED
Synthetic surrogate: zentraler Target-/Evidence-Typing-Fall
Physics-informed ML: Rollenüberlagerung T/R/C
Equation Discovery: zentraler Inversionsfall T inferred by C
Lorenz/SINDy: negativer Stress-Test, kein positiver Provenance-Beleg
ML v0.1: Appendix, Resolvability-Inconclusive
```

## Strategischer Freeze

Keine neue numerische Mainline. ML-v0.2 und inverse v0.2 bleiben pausiert. C06-R2 bleibt konservative Fallback-Boundary.

## Nächste Entscheidung

`Paper Contribution Boundary v0.2` empfiehlt **Option A: genealogisches Descriptive-Trias-Paper weiterverfolgen**, aber den Principal Claim P2 noch nicht endgültig einfrieren.

Vor Manuskript-Freeze wird ein letzter eng begrenzter **AI-for-Science Delta Audit v0.1** empfohlen. Er prüft nur noch, ob die vier Rollenveränderungen

```text
T = NONE_CLAIMED
T = inferred by C
layered synthetic surrogate pipelines
hybrid physics-informed T+C configurations
```

bereits in einem einzelnen etablierten Credibility-/Philosophy-of-AI-for-Science-Rahmen in praktisch derselben Semantik synthetisiert sind.

Bei `GO` wird die Paper Contribution Boundary v0.2 akzeptiert und dieser Delta Audit als nächste Abhängigkeit ausgeführt. Noch kein Manuskriptschreiben und kein neues Experiment.

## Projektkommandos

- `GO`: aktuelle Empfehlung akzeptieren und zum nächsten abhängigen Schritt übergehen.
- `PDF`: aktuellen detaillierten Kooperationsstand als PDF plus LaTeX-Quelle neu synthetisieren; D026, Schlesinger/Sargent-Genealogie, C08-D-R2, Paper Boundary v0.2, negative/inconclusive Resultate und pausierte Branches werden berücksichtigt.
