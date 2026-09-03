# W8 — Editorial Integration Evaluation v0.2

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D037, `paper/manuscript_integrated_v0_2.md`, W1–W7

## 1. Prüfziel

W8 prüft die erste zusammengeführte Manuskriptfassung nach der in D037 akzeptierten redaktionellen Revision. Geprüft werden:

```text
claim consistency
length / proportionality
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

## 2. Gesamturteil

**Klassifikation: PASS_TO_SOURCE_AUDIT.**

Die integrierte v0.2-Fassung behebt den zentralen W7-Fehler: Die getrennten Gate-Drafts sind nun zu einem einzelnen Argumentbogen komprimiert. Die wissenschaftliche Boundary bleibt unverändert.

```text
scientific/conceptual survival = PASS
P3 consistency                 = PASS
framework novelty              = NO
residual contribution          = MODERATE CROSS-DOMAIN SYNTHESIS
evidence-status discipline     = PASS
editorial integration          = PASS
next task                      = SOURCE / BIBLIOGRAPHY AUDIT
```

## 3. Claim consistency

**PASS.**

Die integrierte Fassung führt keinen neuen Hauptclaim ein. Der Paperclaim bleibt:

> Die klassische Model-Credibility-Struktur wird als claimspezifische Rollen-/Evidenzgrammatik für heterogene computational scientific workflows gelesen. Der Restbeitrag ist cross-domain Evidence Localization, nicht eine neue V&V-, Provenance-, Assurance-, Identifiability-, System-ID- oder Scientific-ML-Theorie.

Unverändert bleiben insbesondere:

```text
triangle topology = not new
individual AI roles = not new
claim-relative role occupation = synthesis device
cross-relation evidence transfer = requires explicit bridge argument
practical usefulness = untested
```

## 4. Home-Section-Regel

**PASS.**

Die W7-Home-Section-Regel ist im Wesentlichen umgesetzt:

```text
Section 2 -> Genealogie / Novelty Boundary
Section 3 -> R/T/C-Semantik / Status / Nichttransfer
Section 4 -> vier AI-Konfigurationen
Section 6 -> negative vs inconclusive evidence
Section 7 -> Comparatoren / exakte Contribution Boundary
Section 8 -> global-success / normative / trade-off Grenzen
```

Introduction und Conclusion rahmen diese Punkte deutlich knapper als in den getrennten Gate-Drafts.

## 5. Length / proportionality

**PASS.**

Die v0.2-Fassung liegt nach redaktioneller Kompression ungefähr im ursprünglich akzeptierten Bereich einer vollwertigen Perspective und nicht mehr im W7-Bereich von ca. 13k–15k Wörtern. Der Text ist nun grob im Zielkorridor von etwa `7k–8.3k` Haupttextwörtern, abhängig davon, ob Tabellen, Formeln und provisorische Reference Anchors mitgezählt werden.

Die Abschnittsgewichte sind jetzt plausibel:

```text
Section 4 = konzeptionelles Zentrum
Sections 2–3 = Genealogie + minimale Semantik
Sections 5–6 = bewusst kurze Kontrollen / Stress Tests
Section 7 = kompakte Comparator Boundary
Section 8 = philosophischer Ertrag
```

Kein numerischer Projektfall dominiert den Perspective-Charakter.

## 6. Repetition reduction

**PASS.**

Die problematischen W7-Wiederholungen wurden deutlich reduziert. Die Aussagen

```text
triangle is not new
Trias does not replace specialist frameworks
evidence is relation-specific
no global score
practical usefulness is untested
```

haben nun erkennbare Hauptpositionen. Restwiederholungen in Abstract, Introduction und Conclusion sind funktional und im üblichen Manuskriptmaß vertretbar.

Vor finaler Submission kann ein stilistischer Pass einzelne Boundary-Sätze noch weiter glätten, aber dafür ist keine weitere konzeptionelle Revision erforderlich.

## 7. Terminology consistency

**PASS WITH MINOR SOURCE-PASS CLEANUP.**

Die Standardterminologie ist jetzt weitgehend konsistent:

```text
R -> target / referent role
T -> theory-level claim
C -> computational practice
role profile / evidence-localization vocabulary -> bevorzugte Bezeichnung
```

Die integrierte Fassung verwendet `descriptive Trias` nur noch begrenzt als Projekt-/Vorschlagsname und nicht als ständige Ersatzbezeichnung für jedes Argument.

Beim Source-/Style-Pass sollte noch vereinheitlicht werden:

- `Scientific ML`, `Scientific-ML`, `SciML`;
- `AI for Science` vs `AI-for-Science` je nach Journalstil;
- Gedankenstriche in `R-T`, `T-C`, `C-R` und typografische Unicode-Varianten;
- explizite Beschriftung der Section-4-Cross-case-Tabelle als **Table 2**.

Diese Punkte sind redaktionell, nicht konzeptionell.

## 8. Evidence-status preservation

**STRONG PASS.**

Keine akzeptierte Evidenzklasse wurde im Merge verändert:

```text
Sundman        -> conceptual positive control
Figure-eight   -> positive / use-dependent V&V control
Lorenz/SINDy   -> INFORMATIVE_NEGATIVE
ML v0.1        -> INCONCLUSIVE_LEARNER_ERROR
untested real-target surrogate claim -> UNTESTED
NONE_CLAIMED theory role -> NOT_APPLICABLE where appropriate
```

Der einzelne inverse `linear / seed 2`-Fall wird weiterhin nicht als Haupteffekt aufgewertet. Das ML-v0.1-Ergebnis wird weiterhin nicht als negative Evidenz gegen den Provenance-Claim interpretiert.

## 9. Section balance

**PASS.**

Die zentrale Argumentationslast liegt nun richtig:

1. **Section 4 — strongest positive conceptual load**
   - synthetic referent switch;
   - `T` as output of `C` in equation discovery.
2. **Section 7 — exact defensive contribution boundary.**
3. **Section 8 — philosophical payoff without normative overreach.**

Sundman, Figure-eight und die Projektstress-tests fungieren nur noch als Kontrollen für Semantik und Evidenzdisziplin. Sie werden nicht als empirischer Beweis der Trias präsentiert.

## 10. Submission-readiness before source audit

**PASS, conditional on a dedicated source audit.**

Die integrierte Fassung ist jetzt strukturell nah genug an einem echten Manuskript, dass die nächste sinnvolle Arbeit nicht eine weitere konzeptionelle Revision ist, sondern eine systematische Quellenprüfung.

Noch **nicht submission-ready** sind insbesondere:

```text
- endgültige bibliographische Angaben;
- genaue Versionen/Editionen von Sargent;
- präzise NASA/ASME/AIAA-Zitationen;
- Naser- und Zhai-Publikations-/Versionsdaten;
- provenance / assurance / identifiability / system-ID reference set;
- quellengetreue historische Formulierungen zu Sundman;
- journal-spezifische Zitierweise;
- formale Table/Figure numbering.
```

Diese Punkte müssen nun einzeln gegen Originalquellen bzw. belastbare Fachquellen geprüft werden. Keine bloße Literaturanker-Liste darf in die Submission übernommen werden.

## 11. Survival criteria after integration

```text
S1 direct isomorph         -> NOT TRIGGERED; reopen only for concrete source
S2 no residual compression -> NOT TRIGGERED; residual remains moderate
S3 notation only           -> NOT TRIGGERED
S4 genealogy dominates     -> NOT TRIGGERED; controlled by compressed Section 2
S5 overclaim pressure      -> NOT TRIGGERED
S6 case incoherence        -> NOT TRIGGERED
```

## 12. W8 verdict

```text
claim consistency       = PASS
length/proportionality  = PASS
repetition reduction    = PASS
terminology             = PASS WITH MINOR CLEANUP
evidence preservation   = STRONG PASS
section balance         = PASS
-------------------------------------
OVERALL                  = PASS_TO_SOURCE_AUDIT
```

## 13. Empfehlung für die nächste Abhängigkeit

**ACCEPT W8 = PASS_TO_SOURCE_AUDIT.**

Danach Writing Goal W9:

> **Source & Bibliography Audit v0.1 — verify every externally grounded manuscript claim and build a submission-grade reference ledger.**

W9 soll noch **keinen journal-spezifischen Stilpass** durchführen. Zuerst muss für jede Literaturachse feststehen:

```text
exact source
exact supported claim
claim strength allowed by source
bibliographic data / DOI / publication status
primary vs secondary status
manuscript locations that use the source
```

Priorität:

1. Schlesinger / Sargent / classical credibility genealogy;
2. current V&V / VVUQ / SciML credibility;
3. Naser / Vinuesa / Kramer / Karniadakis;
4. Zhai–Lucarini–Lai;
5. Sundman / Belorizky / Henkel / Chenciner;
6. Provenance / Assurance / Identifiability / System ID comparator anchors.

Erst nach W9 sollte die integrierte v0.2-Fassung bibliographisch gehärtet und anschließend auf ein konkretes Zieljournal zugeschnitten werden.
