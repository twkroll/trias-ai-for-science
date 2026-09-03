# W2 — Genealogy-Dominance Evaluation v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D031, `paper/manuscript_section_2_v0_1.md`, W1 PASS

## 1. Prüfziel

W2 prüft Survival-Kriterium S4:

> Dominiert die klassische Schlesinger/Sargent-Genealogie den gesamten interessanten Inhalt so stark, dass die AI-for-Science-Trias nur noch eine Umbenennung oder Illustration bestehender V&V-Strukturen ist?

Erlaubte lokale Urteile:

```text
PASS
SHORTEN
STOP
```

Der Test bewertet den geschriebenen genealogischen Abschnitt, nicht die investierte Projektarbeit.

## 2. Ergebnis

**Klassifikation: PASS — mit harter Längen- und Funktionsbegrenzung der Genealogie.**

S4 wird in W2 **nicht ausgelöst**. Die Genealogie ist stark und nimmt der Trias die Topologie- und Kantenneuheit vollständig. Sie absorbiert aber nicht den gesamten in W1 gezeigten Rollenwechsel.

Der PASS gilt weiterhin nur für eine **Perspective / Conceptual Synthesis**.

## 3. Was die Genealogie tatsächlich absorbiert

Section 2 macht nun explizit, dass folgende Bestandteile vollständig oder nahezu vollständig klassische Vorarbeit sind:

```text
Reality / Problem Entity
Conceptual Model
Computerized Model

conceptual-model validity
computerized-model verification
operational validity / validation

intended use / scope
verification != validation
synthetic-reference fidelity != real-world validation
```

Damit sind folgende starke Lesarten endgültig nicht verfügbar:

```text
- new triangle
- new three-edge adequacy structure
- new distinction between implementation correctness and real validity
- new use-relative credibility logic
- new sim-to-real distinction
```

Die Tabelle in W2 ist deshalb nicht bloß Related Work, sondern eine explizite Novelty-Boundary.

## 4. Warum S4 trotzdem nicht ausgelöst wird

Der verbleibende Manuskriptbeitrag liegt nicht mehr in der Geometrie der Genealogie, sondern in einer Rollenreinterpretation, die Section 4 tatsächlich verwendet.

### 4.1 Equation Discovery bleibt nicht vollständig lifecycle-kompatibel

Der klassische Forward-Fall liest sich natürlich als

```text
problem entity -> conceptual model -> computerized model
```

Equation Discovery wird im Manuskript dagegen als

```text
R -> D -> C_infer -> T_hat
```

analysiert. Die klassische Credibility-Terminologie kann diesen Fall selbstverständlich erweitert behandeln; W2 zeigt aber keinen Grund, `T_hat` weiterhin primär als vorgängige Lifecycle-Stufe zu lesen. Die Rollenlesart erklärt hier mit derselben Semantik wie im Forward-Fall, warum der Theorieclaim ein Output computationaler Inferenz sein kann.

Dies ist kein neuer Equation-Discovery-Befund, aber ein realer cross-case Synthesegewinn.

### 4.2 Synthetic Surrogate behält einen cross-case Referentengewinn

Surrogate-Credibility kennt den Unterschied zwischen Teacher-/High-Fidelity-Referent und realer Validation bereits. Der Manuskriptgewinn ist daher nicht diese Unterscheidung selbst. Er liegt darin, denselben Referentenwechsel mit derselben Rollen-/Evidenzsprache zu beschreiben, die auch Black-box Prediction, PIML und Equation Discovery abdeckt.

Auch dies ist moderate Kompression, keine neue V&V-Idee.

### 4.3 PIML und Black-box werden von Genealogie stärker absorbiert

Hier ist das S4-Risiko am größten:

```text
PIML -> RT/TC/CR lässt sich sehr natürlich in V&V-Sprache lesen.
Black-box -> Prediction ohne Mechanismus ist stark in Philosophy of ML vorweggenommen.
```

Diese Fälle dürfen deshalb nicht die Neuheitslast tragen. Ihre Funktion ist nur zu zeigen, dass dieselbe kleine Grammatik auch dort ohne Defizitannahmen funktioniert.

## 5. Verhältnis von Section 2 zu Section 4

Das Paper bleibt nur lebensfähig, wenn die Gewichtung asymmetrisch bleibt:

```text
Section 2: genealogy + boundary          = necessary but compressed
Section 4: AI role configurations       = conceptual center
```

Empfohlene Endfassung:

```text
Section 2 prose: ca. 750–950 words
Table 1: retained
Section 4 prose: clearly longer and conceptually dominant
```

Die Genealogie sollte **nicht** zu einer ausführlichen Geschichte von V&V ausgebaut werden. Zusätzliche historische Details gehören nur ins Paper, wenn sie einen konkreten Boundary-Claim verändern.

## 6. S4-Urteil

### S4 — Genealogy dominates contribution

**NOT TRIGGERED, BUT ACTIVE RISK.**

Begründung:

1. Die klassische Genealogie erklärt die R/T/C-Topologie vollständig.
2. Sie erklärt auch viele Edge-Semantics bereits sehr tief.
3. W1 zeigt jedoch einen Rest, der gerade aus der gemeinsamen Rollenlesart über unterschiedlich gerichtete AI-Workflows entsteht.
4. Besonders Equation Discovery und Surrogate Learning erzeugen genug cross-case Unterschied, dass das Paper nicht auf reine V&V-Genealogie kollabiert.
5. Dieser Rest ist moderat und rechtfertigt Perspective, nicht Framework-Paper.

## 7. Weitere Survival-Kriterien nach W2

```text
S1 direct isomorph             -> nicht ausgelöst; weiter offen bei konkretem Literaturfund
S2 no residual compression     -> nicht ausgelöst; bleibt Hauptrisiko für Sections 3/7
S3 notation only               -> nicht ausgelöst, aber muss in Section 3 erneut geprüft werden
S4 genealogy dominates         -> nicht ausgelöst, aktives Risiko
S5 overclaim pressure          -> nicht ausgelöst
S6 case incoherence            -> W1 PASS
```

## 8. Revisionshinweise für Section 2

### W2-R1 — Mapping als „approximate“, nicht identisch

Das Mapping

```text
R-T ~ conceptual validity
T-C ~ verification
C-R ~ operational validity
```

sollte als starke strukturelle Entsprechung, nicht als semantische Identität formuliert bleiben. Insbesondere ist `T` im aktuellen Paper enger auf den tatsächlich beanspruchten wissenschaftlichen Theorie-/Mechanismus-/Erklärungsinhalt typisiert als ein beliebiges conceptual model.

### W2-R2 — Keine Behauptung, klassische V&V könne AI nicht behandeln

Die Manuskriptformulierung soll ausschließlich lauten, dass die Rollenlesart für variable Workflowrichtungen analytisch nützlich sein **kann**. Moderne SciML-V&V behandelt learned/hybrid models bereits ausdrücklich.

### W2-R3 — Table 1 ist zentraler Boundary-Beleg

Table 1 sollte im finalen Manuskript bleiben. Sie macht transparent, dass fast alle Einzelbestandteile `not new` oder `strongly preceded` sind und dass der verbleibende Claim nur in der gemeinsamen Synthese liegt.

## 9. Gesamturteil

W2 verschärft die Contribution Boundary, ohne das Standalone-Paper zu zerstören:

```text
W2 genealogy-dominance gate = PASS
paper mode                    = CONTINUE PERSPECTIVE
S4                            = ACTIVE RISK, NOT TRIGGERED
framework novelty             = NO
synthesis contribution        = still plausible / moderate
```

## 10. Empfehlung für die nächste Abhängigkeit

**ACCEPT W2 = PASS.**

Danach Writing Goal W3:

> **Section 3 — From lifecycle stages to claim-relative epistemic roles.**

W3 soll ausdrücklich nur die minimale Semantik schreiben, die Section 4 tatsächlich benötigt. Es muss einen lokalen **notation-only / semantic-load check** gegen S3 durchführen. Falls `R/T/C`, Statuswerte und Bridge-Claims dort keinen argumentativen Gehalt über neue Labels hinaus besitzen, ist auf `SHORTEN` oder `STOP` zurückzugehen.