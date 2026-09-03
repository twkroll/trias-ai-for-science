# W7 — Whole-Manuscript Claim-Consistency / Length / Repetition Audit v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D036, Sections 1–9 v0.1, W1–W6 PASS

## 1. Prüfziel

W7 prüft erstmals den bisher getrennt geschriebenen Manuskriptbogen als Ganzes. Geprüft werden:

```text
claim consistency
novelty-boundary consistency
negative/inconclusive evidence discipline
descriptive-vs-normative discipline
terminology consistency
section ordering
length / proportionality
repetition
remaining survival criteria S1-S6
```

Erlaubte Gesamturteile:

```text
PASS_TO_MERGE
REVISE_BEFORE_MERGE
SHORTEN
STOP
```

## 2. Gesamturteil

**Klassifikation: REVISE_BEFORE_MERGE.**

Dies ist **kein wissenschaftliches oder konzeptionelles Scheitern**. Die Claim-Boundary, Evidenzdisziplin und philosophische Positionierung bestehen den Whole-Manuscript-Test. Der aktuelle Satz einzelner Gate-Drafts ist jedoch deutlich zu lang und wiederholt seine zentralen Schutzbehauptungen zu oft, um bereits als zusammenhängendes Perspective-Manuskript gemerged zu werden.

Der Paper-Status bleibt:

```text
scientific/conceptual survival = PASS
paper mode                     = Perspective / Conceptual Synthesis
framework novelty              = NO
residual contribution          = MODERATE CROSS-DOMAIN SYNTHESIS
whole-manuscript editorial gate= REVISE_BEFORE_MERGE
```

## 3. Claim consistency

**PASS.**

Section 1, Abstract und Conclusion führen keinen Claim ein, der über P3/C08-D-R3 hinausgeht. Der gesamte Manuskriptbogen bleibt bei der akzeptierten Fassung:

> Die klassische Model-Credibility-Struktur wird für AI-for-Science als claimspezifische Rollen-/Evidenzgrammatik gelesen; der Restbeitrag liegt in cross-domain Evidence Localization, nicht in neuen V&V-, Provenance-, Assurance-, Identifiability- oder ML-Kategorien.

Insbesondere bleibt durchgängig erhalten:

```text
triangle topology = not new
individual AI roles = not new
claim-relative evidence localization = residual synthesis contribution
practical utility = untested
```

### Ergebnis

```text
P3 consistency = PASS
C08-D-R3 consistency = PASS
new hidden claim introduced in W7 = NO
```

## 4. Novelty-boundary consistency

**STRONG PASS.**

Die stärksten potenziellen Overclaims werden im aktuellen Bogen mehrfach und konsistent ausgeschlossen:

```text
new triangle                           -> NO
new verification/validation categories -> NO
new sim-to-real distinction            -> NO
new provenance directionality          -> NO
new claim-evidence method               -> NO
new identifiability theory              -> NO
first prediction-without-explanation    -> NO
first computational equation discovery  -> NO
AI breaks classical V&V                 -> NO
```

Das empfohlene W7-Titelstatement

> **From Model Credibility to AI for Science: Claim-Relative Evidence Across Target, Theory, and Computation**

ist mit dieser Boundary besser kompatibel als ein Titel, der `new framework`, `new theory` oder eine eigenständige `Trias`-Architektur suggeriert.

## 5. Evidence-status discipline

**STRONG PASS.**

Die akzeptierten Projektresultate bleiben im gesamten Manuskript korrekt getrennt:

```text
Figure-eight -> positive / use-case-relative control
Lorenz/SINDy -> INFORMATIVE_NEGATIVE
ML v0.1      -> INCONCLUSIVE_LEARNER_ERROR
real-target surrogate validity without real test -> UNTESTED
absent theory claim in narrow prediction case    -> NOT_APPLICABLE
```

Es findet kein post-hoc Upgrading statt. Insbesondere:

- linear Lorenz seed 2 bleibt explorativ;
- das negative inverse Ergebnis wird nicht als positiver Trias-Beleg umgedeutet;
- ML v0.1 wird nicht als negative Evidenz gegen den Provenance-Claim gelesen;
- Figure-eight erzeugt keinen globalen Solverwinner;
- Sundman wird nicht als divergente Reihe beschrieben.

## 6. Descriptive-vs-normative discipline

**PASS.**

Die Introduction, Discussion und Conclusion bleiben kompatibel mit W6:

```text
no global scalar model-quality score
no obligation to maximize all three relations
no ideal center of the triangle
no necessary zero-sum/Pareto trade-off law
NOT_APPLICABLE is not a penalty
higher-level credibility judgments remain legitimate
```

Der Satz `scientific success without global success` wird im Manuskript als Kritik an undifferenzierten globalen Labels verstanden, nicht als Behauptung, dass globale scientific judgments prinzipiell unmöglich seien.

## 7. Terminology consistency

**PASS WITH REVISION.**

Die Kernterminologie ist konzeptionell stabil:

```text
R = claim-relative target/referent
T = theory/mechanism/structure/explanation-level claim
C = concrete computational practice
```

Vor dem Merge sollten aber vier sprachliche Konventionen vereinheitlicht werden:

1. Im Haupttext bevorzugt `role profile` oder `evidence-localization vocabulary`; `descriptive Trias` nur als Name des Vorschlags, nicht in jedem Absatz.
2. `computational practice` als Standard für `C`; `computational realization` nur dort, wo Implementierung/Fidelity gemeint ist.
3. `target` und `referent` nicht beliebig austauschbar: `referent` für das konkrete Vergleichsobjekt einer Evidenzrelation, `target` für das wissenschaftlich intendierte System.
4. `theory-level claim` als Oberbegriff; `mechanistic`, `structural`, `explanatory` als Facetten, nicht als Synonyme.

## 8. Section ordering

**PASS.**

Die Reihenfolge ist argumentativ sinnvoll:

```text
1 problem + contribution
2 genealogy / novelty boundary
3 minimal semantics
4 four AI role configurations
5 classical controls
6 negative/inconclusive stress tests
7 comparator / exact contribution boundary
8 philosophical discussion
9 conclusion
```

Es besteht kein zwingender Grund, die Reihenfolge vor dem ersten Merge zu ändern. Sections 5–6 dürfen jedoch nicht so lang werden, dass die Projektentwicklung das konzeptionelle Zentrum Section 4 verdrängt.

## 9. Length / proportionality

**FAIL in current draft form -> editorial revision required.**

Die einzelnen W1–W7-Dateien sind bewusst ausführliche Gate-Drafts. Aus ihren aktuellen Dateigrößen und der Textdichte ergibt sich grob ein Haupttext im Bereich von **ca. 13.000–15.000 Wörtern** vor finaler Bibliographie. Das ist deutlich oberhalb des ursprünglich akzeptierten Perspective-Ziels von ca. `6.000–8.000` Wörtern.

Die Überschreitung ist nicht überraschend: W2–W6 wurden absichtlich vollständig genug geschrieben, um die Survival-Gates zu testen. Für ein Paper müssen diese Prüftexte jetzt in einen deutlich kompakteren Argumentbogen überführt werden.

### Empfohlene Zielverteilung für v0.2

```text
Section 1  Introduction                         750–850
Section 2  Genealogy                            750–900 + Table 1
Section 3  Role/evidence semantics               850–1,000
Section 4  Four AI configurations               1,700–1,900 + Table 2
Section 5  Classical controls                    500–650
Section 6  Negative/inconclusive stress tests    650–800 + Table 3
Section 7  Comparator / contribution boundary    850–1,000
Section 8  Discussion                            800–950
Section 9  Conclusion                            200–250
--------------------------------------------------------
Target main text                              ca. 7,050–8,300
Abstract                                      ca. 180–220
```

Damit bleibt eine vollwertige Perspective möglich, ohne auf die 4.000–5.000-Wörter-Short-Perspective zurückzugehen.

## 10. Repetition audit

**REVISE.**

Der aktuell größte Manuskriptfehler ist nicht Inkonsistenz, sondern Wiederholung derselben Boundary-Sätze. Besonders häufig wiederholt werden:

```text
- the triangle is not new
- Trias does not replace V&V / provenance / assurance / identifiability
- evidence is relation-specific
- no global model-quality score
- teacher fidelity is not real validation
- equation discovery can make T an output of C
- practical usefulness is untested
```

Diese Wiederholungen waren für die getrennten Gate-Drafts sinnvoll, würden im zusammenhängenden Paper aber defensiv und schwerfällig wirken.

### Verbindliche Home-Section-Regel für die Revision

Jeder Kernpunkt erhält eine Haupt-Heimat:

```text
triangle/genealogy novelty boundary  -> Section 2
role definitions + non-transfer      -> Section 3
four AI distinctions                 -> Section 4
negative vs inconclusive             -> Section 6
adjacent-framework boundary          -> Section 7
no global score / no trade-off       -> Section 8
```

Introduction und Conclusion dürfen diese Punkte nur komprimiert ankündigen bzw. zusammenfassen. Sections 4–8 sollen nicht jeweils erneut die gesamte Novelty-Boundary rekonstruieren.

## 11. Specific compression instructions

### Section 1

Current W7 draft is conceptually consistent but too comprehensive. Kürzen durch:

```text
- literature landscape to one compact paragraph;
- contribution boundary to one paragraph;
- project stress-test preview to 2–3 sentences;
- paper map to one sentence.
```

### Section 2

Table 1 behalten. Prosa deutlich kürzen. Keine wiederholte moderne V&V-Liste nach der Tabelle.

### Section 3

Die stärkste Kürzung ist hier möglich. Behalten:

```text
R/T/C definitions
R_REAL/R_SYNTHETIC/R_HYBRID
T PRESENT/PARTIAL/NONE_CLAIMED/INFERRED
minimal status semantics
non-transfer default
one bridge example
```

Facet-Kataloge und ausführliche Ledger-Regeln in Appendix/Supplement verschieben.

### Section 4

Konzeptionelles Zentrum behalten. Jeder Archetyp nur:

```text
workflow
one principal evidence distinction
one non-implication
one comparator/boundary sentence
```

Equation Discovery und Synthetic Surrogate dürfen länger bleiben als Black-box und PIML.

### Sections 5–6

Numerische Details stark reduzieren. Cross-case evidence table behalten. Vollständige Zahlen bleiben in Project/Supplementary material.

### Section 7

Comparatoren nicht als Mini-Reviews. Je Comparator maximal:

```text
what it does better
what Trias cannot claim
what residual role remains
```

### Section 8

W6-Gate-Draft auf die fünf unverzichtbaren Punkte reduzieren:

```text
claim-relative success
no all-three-edges imperative
no necessary trade-off
higher-level global judgments still allowed
practical usefulness remains untested
```

### Section 9

Auf etwa 200–250 Wörter kürzen; keine erneute vollständige Liste der vier AI-Fälle nötig.

## 12. Remaining survival criteria S1–S6

Nach W7:

```text
S1 direct isomorph         -> NOT TRIGGERED; reopen only for concrete new source
S2 no residual compression -> NOT TRIGGERED; moderate residual survives
S3 notation only           -> NOT TRIGGERED
S4 genealogy dominates     -> NOT TRIGGERED / active but controllable by compression
S5 overclaim pressure      -> NOT TRIGGERED
S6 case incoherence        -> NOT TRIGGERED
```

Kein wissenschaftliches Stop-Kriterium wird durch den Whole-Manuscript-Bogen ausgelöst.

## 13. W7 verdict

```text
scientific claim consistency  = PASS
novelty boundary              = STRONG PASS
evidence-status discipline    = STRONG PASS
descriptive/normative boundary= PASS
section ordering              = PASS
terminology                    = PASS WITH REVISION
length                         = REVISE
repetition                     = REVISE
-------------------------------------------
OVERALL                        = REVISE_BEFORE_MERGE
```

## 14. Empfehlung für die nächste Abhängigkeit

**ACCEPT W7 = REVISE_BEFORE_MERGE.**

Danach Writing Goal W8:

> **Editorial Synthesis v0.2 — compress Sections 1–9 into a single integrated manuscript while preserving P3 and all accepted evidence classes.**

W8 soll keine neue Literatur- oder Novelty-Suche und keine neuen Experimente enthalten. Es soll ausschließlich:

1. die oben festgelegte Home-Section-Regel anwenden;
2. Wiederholungen entfernen;
3. Haupttext auf ca. `7.000–8.300` Wörter bringen;
4. Tabellen 1–3 behalten und numerische Details in Appendix/Supplement auslagern;
5. Terminologie vereinheitlichen;
6. einen integrierten Manuskriptentwurf v0.2 erzeugen.

Erst danach sollte eine finale Quellen-/Bibliographieprüfung und ein journal-spezifischer Stilpass erfolgen.