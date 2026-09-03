# W5 — Case-Coherence / Evidence-Status Evaluation v0.1

**Status:** COMPLETE / PENDING AUTHOR DECISION  
**Stand:** 2026-09-03  
**Depends on:** D034, `paper/manuscript_sections_5_6_v0_1.md`, W1–W4 PASS

## 1. Prüfziel

W5 prüft nicht erneut die Novelty des Projekts. Geprüft werden ausschließlich:

```text
case coherence
evidence-status discipline
manuscript proportionality
```

Erlaubte Urteile:

```text
PASS
REVISE
SHORTEN
```

## 2. Ergebnis

**Klassifikation: PASS — mit späterer redaktioneller Straffung.**

Die vier Fälle lassen sich kohärent in die Manuskriptlogik integrieren, ohne ihre akzeptierten Evidenzklassen zu verändern. Insbesondere bleiben positiver Kontrollbefund, informative negative Evidenz und inconclusive Evidenz klar getrennt.

## 3. Case coherence

**PASS.**

Die Fälle erfüllen vier unterschiedliche Funktionen und werden nicht künstlich als gemeinsame empirische Bestätigung der Trias behandelt:

```text
Sundman        -> conceptual T-C control
Figure-eight   -> standard V&V control
Lorenz/SINDy   -> inverse INFORMATIVE_NEGATIVE stress test
ML v0.1        -> INCONCLUSIVE_LEARNER_ERROR resolvability stress test
```

### 3.1 Sundman

Der Fall bleibt eng auf

```text
formal analytical availability != practical computational availability
```

beschränkt. Die W5-Prosa sagt ausdrücklich, dass die Reihen unter den Bedingungen des Theorems konvergieren und dass der methodologisch relevante Punkt die praktische Langsamkeit/Evaluierbarkeit ist.

Keine unzulässige Aussage zu Divergenz, geschlossener Form, Chaos oder numerischer Instabilität wird eingeführt.

### 3.2 Figure-eight

Der Fall funktioniert als Kontrollgruppe, weil das Manuskript offen zugibt, dass Standard Numerical Analysis, geometric integration und V&V den Befund bereits gut erklären.

Die zentralen akzeptierten Resultate bleiben korrekt gewichtet:

```text
short horizon -> RK4 deutlich trajectory-genauer
long horizon  -> Verlet kleinerer secular energy drift + roundoff-nahe Lz-Erhaltung
no global solver winner
```

Damit wird der Fall nicht als künstlicher Trias-Novelty-Beleg missbraucht.

### 3.3 Lorenz/SINDy

Der inverse Fall bleibt exakt als

```text
INFORMATIVE_NEGATIVE
```

geschrieben. Die technische Validität der Baseline wird von der nicht bestandenen seed-robusten structural-effect Hypothese getrennt.

Der einzige strukturell abweichende Fall `linear / seed 2` bleibt explorativ und wird nicht nachträglich zum Hauptergebnis hochgestuft.

### 3.4 ML v0.1

Der ML-Fall bleibt exakt

```text
INCONCLUSIVE_LEARNER_ERROR
```

und wird nicht als negative Evidenz gegen den Teacher-Provenance-Claim interpretiert.

Die Prosa macht den entscheidenden Unterschied explizit:

```text
teacher signal was cleanly separated
but learner error >> teacher difference
therefore downstream provenance claim not assessable
```

Dies ist der stärkste W5-Beleg dafür, dass `inconclusive` nicht dasselbe wie `negative` ist.

## 4. Evidence-status discipline

**STRONG PASS.**

W5 hält die folgenden Kategorien auseinander:

```text
positive / supported
informative negative
inconclusive / unresolved
untested
not applicable
```

Die wichtigste Definition im geschriebenen Abschnitt lautet funktional:

```text
negative:
  der Test war entscheidungsfähig, aber das vorregistrierte Kriterium wurde nicht erfüllt

inconclusive:
  eine notwendige Resolvability-/Messvoraussetzung wurde nicht erfüllt, daher kann der Zielclaim nicht entschieden werden

untested:
  die relevante Relation wurde nicht geprüft

not applicable:
  die Relation gehört nicht zum spezifizierten Claim
```

Diese Trennung ist mit Section 3 konsistent und wird durch reale Projektfälle illustriert, ohne eine neue allgemeine Evidenztheorie zu beanspruchen.

## 5. Kein post-hoc Upgrading

**PASS.**

W5 führt keine nachträgliche Umdeutung ein:

```text
Lorenz linear seed 2 -> bleibt explorativ
cubic seed 2 long-time threshold failure -> wird nicht globalisiert
ML rollout failure -> wird nicht als teacher-provenance effect gelesen
Figure-eight -> kein globaler solver winner
Sundman -> keine Divergenzbehauptung
```

Damit bleibt die vorab akzeptierte Claim-Disziplin erhalten.

## 6. Manuscript proportionality

**PASS, aber redaktionelle Straffung empfohlen.**

Die W5-v0.1-Fassung ist für einen Gate-Draft etwas ausführlicher als die spätere Endfassung sein sollte.

Empfohlener Zielumfang:

```text
Section 5 controls:      ca. 600–750 Wörter
Section 6 stress tests:  ca. 700–900 Wörter
```

Für die Endrevision können vor allem folgende Teile gekürzt werden:

```text
- numerische Detailwerte bei Figure-eight auf 2–3 exemplarische Zahlen reduzieren;
- Lorenz technische Gates nur einmal kompakt nennen;
- ML-Setup kürzer beschreiben, Resolvability-Verhältnis aber behalten;
- Cross-case ledger/table behalten, weil es die evidence-status discipline sichtbar macht.
```

Die Fälle sollen nicht zum numerischen Hauptteil des Perspective-Papers anwachsen.

## 7. Verhältnis zur Paper-Contribution

W5 stärkt P3 nicht durch neue positive Evidenz. Seine Funktion ist enger und methodologisch sinnvoll:

> Die vorgeschlagene Evidence-Localization-Sprache kann klassische, negative und inconclusive Fälle beschreiben, ohne deren Evidenzstatus zu homogenisieren.

Dieser Befund ist **case-coherence evidence**, keine Framework-Validierung.

Besonders wichtig ist, dass der inverse negative Fall und der ML-inconclusive Fall die Story nicht beschädigen. Im Gegenteil: Würde das Paper diese Resultate positiv umdeuten müssen, wäre Survival-Kriterium S5 `overclaim pressure` nachträglich verletzt. Das ist in W5 nicht der Fall.

## 8. Gesamturteil

```text
W5 case coherence            = PASS
W5 evidence-status discipline= STRONG PASS
manuscript proportionality   = PASS / later tighten
paper mode                    = CONTINUE PERSPECTIVE
new novelty claim             = NO
```

## 9. Empfehlung für die nächste Abhängigkeit

**ACCEPT W5 = PASS.**

Danach Writing Goal W6 sollte nicht sofort die Introduction schreiben, sondern zunächst:

> **Section 8 — Discussion: scientific success without global success.**

Begründung: Nach W1–W5 stehen Genealogie, Semantik, AI-Archetypen, Comparator-Boundary und Evidenzdisziplin. Die Discussion muss daraus nun den eigentlichen philosophischen Ertrag formulieren, ohne aus der deskriptiven Analyse einen normativen All-three-edges-Imperativ oder eine notwendige Trade-off-Theorie zu machen.

Nach Section 8 sollte ein letzter `descriptive-vs-normative`- und `global-success`-Check erfolgen. Erst danach sollten Introduction, Conclusion und Abstract geschrieben werden.