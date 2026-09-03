# Paper Contribution Boundary v0.2 — From Model-Credibility Triangle to Descriptive Trias for AI for Science

**Status:** PENDING REVIEW  
**Stand:** 2026-09-03  
**Depends on:** D026 / C08-D-R2 / `literature/relational_profile_novelty_audit_v0_1.md`

## 1. Zweck

Dieses Dokument ersetzt die v0.1-Paper-Boundary als aktuellen Mainline-Entwurf. Es setzt den Beitrag genealogisch neu auf: Die Trias wird **nicht** als originäre Dreieckstopologie von Realität, Theorie und Berechnung eingeführt. Ausgangspunkt ist die etablierte Model-Credibility-/V&V-Tradition mit `Reality/Problem Entity`, `Conceptual Model` und `Computerized Model` sowie den Relationen conceptual model validity/qualification, verification und validation.

Die Forschungsfrage lautet nun:

> **Was muss an dieser klassischen Credibility-Triade verändert oder generalisiert werden, wenn die computational practice in AI for Science nicht mehr nur ein gegebenes conceptual model implementiert, sondern selbst vorhersagt, approximiert, rekonstruiert oder wissenschaftliche Theorie erzeugt?**

Der Paper-Beitrag darf nur in dieser Generalisierung liegen.

---

## 2. Genealogischer Ausgangspunkt

### 2.1 Klassische Model-Credibility-Triade

Der historische Ausgangspunkt wird im Paper explizit dargestellt als:

```text
Problem Entity / Reality
        | \
        |  \ operational validity / validation
        |   \
conceptual validity       Computerized Model
        |                  /
        |                 / verification
        |                /
        Conceptual Model
```

Semantisch:

```text
Reality <-> Conceptual Model
    conceptual model validity / qualification

Conceptual Model <-> Computerized Model
    verification

Computerized Model <-> Reality
    operational validity / validation
```

Diese Struktur ist der historische Vorläufer und wird nicht als Gegner des Projekts behandelt.

### 2.2 Warum trotzdem eine Generalisierung untersucht wird

Die klassische Struktur ist primär auf einen Workflow zugeschnitten, in dem ein conceptual/mathematical model vorliegt und anschließend computational implementiert wird. In AI-for-Science-Pipelines treten dagegen zusätzliche Konfigurationen auf:

```text
1. C ohne expliziten T-Claim
   R -> data -> learned predictor C

2. T als Output von C
   R -> observation/data -> inference C -> T_hat

3. C approximiert einen synthetischen Referenten
   T/simulator -> synthetic data -> learned surrogate C

4. T und C werden partiell gemeinsam operationalisiert
   theory constraints + data -> physics-informed C

5. mehrere computational Ebenen liegen übereinander
   T -> simulator C1 -> synthetic data -> surrogate C2 -> scientific use
```

Die Trias v0.2 fragt deshalb nicht, ob Verification/Validation ersetzt werden müssen, sondern ob die klassischen Rollen für diese Fälle **epistemisch neu typisiert und dynamischer gelesen** werden sollten.

---

## 3. Vorgeschlagener Principal Claim P2

> **P2 — Genealogical Generalisation Claim:** Die klassische Model-Credibility-Triade aus Problem Entity, Conceptual Model und Computerized Model liefert einen wesentlichen historischen Vorläufer für die Trennung von Zielsystem, Modell und Berechnung. Für AI for Science schlagen wir keine neue Dreieckstopologie vor, sondern eine wissenschaftsphilosophische Generalisierung ihrer Rollen vor: `T` bezeichnet den expliziten wissenschaftlichen Theorie-, Mechanismus- oder Erklärungsclaim und kann fehlen oder selbst Ergebnis computationaler Inferenz sein; `C` bezeichnet eine konkrete computational practice und kann neben Implementierung auch Lernen, Surrogation, Rekonstruktion oder Equation Discovery umfassen; `R` bezeichnet den für den jeweiligen Claim explizit fixierten realen, synthetischen oder hybriden Referenten. Evidenz wird anschließend danach profiliert, welche Relation und welchen Claim sie tatsächlich stützt. Dadurch lassen sich verschiedene Arten wissenschaftlichen Erfolgs in AI for Science beschreiben, ohne Prediction, Theorietreue und Realitätsgrounding global gleichzusetzen.

### Status von P2

```text
historische Genealogie: stark gestützt
klassische Topologie als Vorläufer: stark gestützt
analytische Diskriminationsleistung der erweiterten Profilierung: positiv in Projektfällen
AI-for-Science-Generalisation: plausibel
Einzigartigkeit der Generalisation: noch zu härten
praktische Überlegenheit: nicht getestet
```

P2 ist damit ein **wissenschaftsphilosophischer Synthese-/Generalisierungsclaim**, kein technischer V&V-Claim.

---

## 4. Exakter behaupteter Delta gegenüber klassischer Simulation Credibility

Der Delta wird in fünf Punkten begrenzt.

### Delta 1 — Von `Conceptual Model` zu claim-typisiertem `T`

`T` ist nicht lediglich die konzeptionelle Spezifikation eines Simulationsmodells. `T` ist der theoretische Inhalt, dessen wissenschaftlicher Status behauptet wird, z. B.:

```text
mechanistic law
symbolic equation structure
explanatory mechanism
formal mathematical representation
scope/idealisation claim
```

Entscheidend ist:

```text
T can be PRESENT
T can be NONE_CLAIMED
T can be INFERRED_BY_C
```

Diese Unterscheidung wird im Paper als stärkster semantischer Delta behandelt.

### Delta 2 — Von `Computerized Model` zu pluralen computational practices

`C` wird nicht nur als Computerimplementierung eines vorgegebenen Modells gelesen, sondern als operative wissenschaftliche Praxis:

```text
numerical realization
learned predictor
surrogate / emulator
reconstruction pipeline
inverse inference
symbolic equation discovery
hybrid physics-ML realization
```

Damit kann C sowohl downstream als auch upstream von T liegen.

### Delta 3 — Expliziter Target-Typ

`R` wird pro Claim typisiert als:

```text
REAL
SYNTHETIC
HYBRID
```

Dies ist keine neue V&V-Idee, aber in der Trias-Generalisation wird ein Referentenwechsel als **neues epistemisches Profil** behandelt. Eine Güteaussage relativ zu einem Teacher/Simulator und eine Güteaussage relativ zu einem realen Target sind dadurch nicht sprachlich austauschbar.

### Delta 4 — Deskriptive Typisierung von wissenschaftlichem Erfolg

Der primäre Zweck ist nicht die Zertifizierung eines Modells, sondern die Beschreibung:

```text
Welche Art von Erfolg wurde gezeigt?
Welche Relation wird durch die Evidenz gestützt?
Welche Art von Erfolg bleibt offen?
```

Beispiele:

```text
real-data predictive success     -> primär C-R
surrogate/teacher fidelity       -> primär T-C bzw. C-R_syn
mechanistic support              -> primär R-T
physics-constraint satisfaction  -> primär T-C
```

### Delta 5 — Claimgebundene Kanten und Bridge-Explizitheit

Das akzeptierte Ledger bindet jeden Eintrag an:

```text
edge + facet + claim + evidence + use case + scope + status
```

und behandelt Evidenztransfer zwischen Kanten als expliziten Bridge-Claim. Dies ist eine Synthese aus Credibility-, Assurance- und Provenance-Ideen; es wird nicht als jeweils neue Einzeltechnik beansprucht.

---

## 5. Was das Paper ausdrücklich NICHT behaupten darf

1. `Reality / Theory / Computation` sei als Dreieck neu.
2. Die drei Paarrelationen seien erstmals durch die Trias erkannt worden.
3. Verification und Validation seien unzureichend oder würden ersetzt.
4. Conceptual model validity, intended use oder scope-relative adequacy seien neue Ideen.
5. Synthetic-to-real gaps oder Prediction-vs.-Understanding seien neue AI-Probleme.
6. Claim-Evidence-Traceability, Provenance oder Assurance Cases seien neue Trias-Erfindungen.
7. Die drei Kanten seien unabhängig, eindimensional oder als globale Scores messbar.
8. Zwischen den Kanten bestehe notwendig ein Nullsummen-Trade-off.
9. Ein Black-box-Modell ohne expliziten Theorieclaim sei epistemisch minderwertig.
10. Ein Modell müsse auf allen drei Relationen hohe Adäquanz erreichen.
11. Die Trias sei bereits empirisch als nützlicher oder verständlicher als etablierte Credibility-Frameworks validiert.
12. Der Lorenz/SINDy-Run habe einen robusten positiven Provenance-Effekt gezeigt.
13. Der ML-v0.1-Run habe den Teacher-Provenance-Claim entschieden.

---

## 6. Warum der Beitrag trotz historischem Vorläufer potenziell relevant ist

Die stärkste Motivation ist nicht `V&V forgot AI`, sondern eine Verschiebung der Rollenlogik.

Im klassischen Forward-Fall gilt näherungsweise:

```text
R -> conceptual T -> computerized C -> comparison with R
```

In AI for Science kann die Richtung dagegen variieren:

```text
black-box prediction:
R -> data -> C

surrogate learning:
T -> simulator/data -> C

equation discovery:
R -> data -> C -> T_hat

physics-informed learning:
T + data(R) -> C

multi-level synthetic pipeline:
T -> C1 -> data_syn -> C2 -> claim about R
```

Die neue philosophische Frage ist daher:

> Sind `theory`, `computation` und `target` in AI for Science noch sinnvoll als feste Workflow-Stufen zu lesen, oder sollten sie als **epistemische Rollen** verstanden werden, die in unterschiedlichen Richtungen und Kombinationen auftreten?

Die Trias beansprucht die zweite Lesart als Generalisierung.

---

## 7. Rolle der Projektfälle im neuen Paper

### 7.1 Schlesinger/Sargent — kein Related Work, sondern Section-2-Fundament

Funktion:

```text
historical ancestor
+
novelty boundary
+
terminological comparator
```

Das Paper sollte früh zeigen, dass die Autoren den Vorläufer kennen und die Genealogie absichtlich fortsetzen.

### 7.2 Sundman — Minimalfall für T-C ohne AI

Sundman bleibt ein kompakter historischer Motivationsfall:

```text
formal theoretical availability
!=
practical computational availability
```

Seine Funktion ist nicht Novelty, sondern zu zeigen, dass `T-C` selbst mehrere Facetten besitzt: formale Treue und praktische Traktabilität können auseinanderfallen.

Empfehlung: kurze Haupttext-Box oder 1–1.5 Seiten, nicht eigener großer Ergebnisteil.

### 7.3 Figure-eight — klassische V&V-Kontrollgruppe

Der Figure-eight-Fall sollte nun explizit als **Kontrollgruppe** gelesen werden:

> In einem klassischen Forward-Simulationsfall leistet die Trias kaum mehr als etablierte Numerical Analysis/V&V.

Das ist im Paper wertvoll, weil es die Grenze der Generalisierung demonstriert.

Empfehlung: stark komprimierter Haupttext oder Supplement; kein zentraler Novelty-Beleg.

### 7.4 Black-box Predictor — erster zentraler AI-Archetyp

Dieser Fall ist theoretisch wichtiger geworden:

```text
C is scientifically useful
T may be NONE_CLAIMED
```

Damit wird sichtbar, dass das klassische `Conceptual Model -> Computerized Model`-Verhältnis für einen engen Prediction-Claim nicht einfach vorausgesetzt werden sollte.

Dieser Fall kann rein konzeptionell mit Literaturbeispielen behandelt werden; kein neues Training nötig.

### 7.5 Synthetic-data Surrogate — zweiter zentraler AI-Archetyp

Kern:

```text
high fidelity to simulator/teacher
!= automatically evidence about R_real
```

Neu ist nicht der sim-to-real-Gedanke. Der Fall demonstriert die claim- und referentenabhängige Profilierung der Trias.

Empfehlung: zentrale Abbildung oder Tabelle.

### 7.6 Physics-informed ML — Rollenüberlagerung

Kernfragen:

```text
T-C: is theory encoded/satisfied?
R-T: is that theory adequate for the real regime?
C-R: does the resulting model work on the real target?
```

Dieser Archetyp zeigt besonders anschaulich, dass `physics-informed` keine globale epistemische Gütebezeichnung ist.

### 7.7 Equation Discovery — stärkster Inversionsfall

Hier liegt der wichtigste strukturelle Unterschied zur klassischen Forward-Genealogie:

```text
R -> data -> C_infer -> T_hat
```

`T` ist nicht Input des computerized model, sondern epistemischer Output einer computational practice.

Der externe Zhai–Lucarini–Lai-Fall kann den Archetyp illustrieren. Der eigene vorregistrierte Lorenz/SINDy-Run bleibt als negativer Stress-Test wichtig: Er zeigt, dass die Trias nicht voraussetzt, dass jede Pipeline tatsächlich strukturelle Nicht-Eindeutigkeit erzeugt.

Empfehlung: zentraler Haupttextfall.

### 7.8 ML-v0.1 — Appendix als Resolvability-Beispiel

Der `INCONCLUSIVE_LEARNER_ERROR`-Fall ist kein Hauptresultat. Er eignet sich als Appendix-Beispiel dafür, dass ein TC-Resolvability-Problem einen nachgelagerten wissenschaftlichen Claim unentscheidbar machen kann, ohne ihn zu widerlegen.

---

## 8. Empfohlene Paper-Architektur v0.2

### 1. Introduction — From credibility of simulations to epistemic roles in AI for Science

Problemstellung:

- klassische Simulation besitzt ausgereifte Credibility-Terminologie;
- AI-for-Science-Workflows verändern die Rolle von computation;
- Ziel ist Generalisierung, nicht Ersatz.

### 2. The model-credibility triangle: genealogy and boundary

Schlesinger/Sargent, conceptual validity, verification, operational validity; moderne V&V-/VVUQ-Fortsetzung.

Am Ende dieser Section explizit:

```text
Our triangle is not new.
```

### 3. From lifecycle stages to epistemic roles

Definition:

```text
R = claim-relative target
T = theory/mechanism/explanation claim, possibly absent or inferred
C = concrete computational practice
```

Hier Edge Semantics und Target-Typen in Minimalform einführen.

### 4. Descriptive profiles: what kind of scientific success has been shown?

Evidence Ledger, keine Scores, Facets, Scope, Nichttransitivität als Default.

Zentrale Vergleichsbeispiele:

```text
same RMSE against real data vs simulator
physics-informed vs real-world validated
predictive C without T
```

### 5. Where the classical forward reading still suffices

Sundman + Figure-eight als Grenz-/Kontrollfälle. Ergebnis: klassische V&V deckt den traditionellen Forward-Fall stark ab.

### 6. Where AI for Science changes the role structure

Drei Unterfälle:

```text
6.1 black-box prediction: T absent
6.2 surrogate / physics-informed ML: layered and hybrid relations
6.3 equation discovery: T inferred by C
```

### 7. Stress tests and negative evidence

Lorenz/SINDy `INFORMATIVE_NEGATIVE`; ML-v0.1 `INCONCLUSIVE_LEARNER_ERROR` kurz einordnen. Ziel: zeigen, dass das Profil Resultatstatus lokalisiert, nicht positive Effekte erzwingt.

### 8. Comparison with adjacent frameworks

Nicht defensiv, sondern modular:

```text
V&V/VVUQ -> credibility evidence
provenance -> artifact lineage
assurance cases -> claim-evidence argumentation
identifiability/system ID -> inverse uniqueness/robustness
Descriptive Trias -> role/edge typing across these practices
```

### 9. What is actually contributed — and what remains open

Contribution Boundary, Falsifikationskriterien, praktische Nützlichkeit ungetestet.

### 10. Conclusion

Keine neue Triade; Vorschlag einer genealogisch transparenten AI-for-Science-Generalisation.

---

## 9. Vorgeschlagene Kernabbildungen

### Figure 1 — Genealogy figure

Links klassische Credibility-Triade:

```text
Problem Entity — Conceptual Model — Computerized Model
```

rechts generalized epistemic roles:

```text
R — T — C
```

mit explizitem Label:

```text
not a new topology; semantic generalisation
```

### Figure 2 — Role configurations in AI for Science

Vier kleine Panels:

```text
Forward simulation: T -> C
Black-box:        R -> C
Surrogate:        T/C_teacher -> C_ML
Equation discovery: R -> C_infer -> T_hat
```

Diese Abbildung ist vermutlich die wichtigste des Papers.

### Figure 3 — Same metric, different epistemic relation

Beispiel `RMSE = 0.01`:

```text
against real holdout      -> CR_PREDICTION
against simulator teacher -> TC_SURROGATE / CR_SYN
```

### Figure 4 — Evidence Ledger

Kompakte claimgebundene Tabelle mit Edge, Facet, Evidence, Scope, Status und Non-Implication.

### Table 1 — Classical credibility vs Descriptive Trias generalisation

Spalten:

```text
classical concept | Trias mapping | identical/preceded | generalisation | example
```

### Table 2 — Case contribution ledger

Zeigt für jeden Projektfall ausdrücklich:

```text
what it supports
what it does not support
role in paper
```

---

## 10. Paperformat und realistische Positionierung

Der aktuelle Beitrag trägt am ehesten ein:

```text
philosophy-of-science / methodology paper
oder
conceptual perspective on AI for Science with computational case studies
```

Nicht geeignet als:

```text
new V&V framework paper
new validation methodology
new AI algorithm paper
new mathematical theory of model credibility
```

Eine publikationsfähige Version muss den historischen Model-Credibility-Vorläufer zentral und detailliert rekonstruieren. Ohne diesen genealogischen Teil wäre der Beitrag angreifbar.

---

## 11. Harte Survival Criteria vor Manuskript-Freeze

Der eigenständige Trias-Begriff soll nur beibehalten werden, wenn die Paper-Ausarbeitung mindestens folgende vier Punkte überzeugend trägt:

### S1 — Role generalisation

Mindestens zwei zentrale AI-for-Science-Archetypen müssen zeigen, dass `T` und `C` nicht sinnvoll nur als feste Stufen `conceptual model -> computerized model` gelesen werden, sondern als Rollen mit variabler Richtung.

Zielkandidaten:

```text
black-box prediction
Equation Discovery
```

### S2 — Descriptive gain

Die relationale Typisierung muss mindestens einen klaren Kategorienunterschied explizieren, den ein globales Label verdeckt, z. B.:

```text
teacher accuracy != real-target prediction evidence
physics-constrained != theory-validated != real-world validated
```

Dieser Punkt ist im Profile Test bereits analytisch positiv, muss aber paperfähig formuliert werden.

### S3 — Genealogical honesty

Das Paper muss Schlesinger/Sargent so zentral behandeln, dass keine Leserinterpretation möglich ist, die Autoren beanspruchten deren Dreieck neu.

### S4 — No single-framework collapse

Wenn bei der Paper-Ausarbeitung ein einzelner etablierter AI-for-Science-Credibility-Rahmen gefunden wird, der bereits explizit

```text
T absent / T inferred
learned and inverse C
claim-relative target typing
cross-case descriptive success profiles
```

in praktisch derselben Semantik behandelt, muss der Trias-Eigenbegriff weiter abgeschwächt werden.

---

## 12. Entscheidungspunkte

### Option A — Genealogical Descriptive Trias Paper

Akzeptiere P2 als Paper-Hauptclaim-Boundary und entwickle das Manuskript entlang der obigen Architektur.

**Stärke:** entspricht der präzisierten Autorenintention; historische Prior Art wird zur Grundlage statt zum Problem; AI-for-Science-Fälle liefern plausible Generalisierung.

**Risiko:** Beitrag bleibt primär interpretative Synthese; Journalfit muss entsprechend gewählt werden.

### Option B — Nur klassische Credibility + AI-for-Science Review/Perspective

Eigenbegriff `Trias` stark zurücknehmen. Fokus auf Review der Veränderung von Verification/Validation unter AI for Science.

**Stärke:** sehr defensible.

**Risiko:** deutlich weniger eigenständiger konzeptioneller Beitrag.

### Option C — Projekt als eigenständiges Paper stoppen

Wenn eine eigenständige neue Theorie oder technische Methodik zwingende Zielbedingung ist, reicht die aktuelle Evidenz nicht.

---

## 13. Empfehlung

**Option A weiterverfolgen, aber P2 noch als Paper-Boundary und nicht als endgültigen Publikationsclaim behandeln.**

Vor dem Manuskriptschreiben sollte als nächster Schritt ein kompakter `AI-for-Science Delta Audit v0.1` nur für die vier vermeintlich generalisierten Konfigurationen durchgeführt werden:

```text
1. T = NONE_CLAIMED / black-box prediction
2. T = inferred by C / equation discovery
3. layered synthetic surrogate pipelines
4. hybrid physics-informed T+C configurations
```

Der Audit soll nicht mehr die Dreieckstopologie testen, sondern ausschließlich prüfen, ob genau diese **Rollenveränderungen** bereits explizit in einem einzelnen etablierten Credibility-/philosophy-of-AI-for-science-Rahmen synthetisiert sind.

Wenn dieser Delta-Audit trägt, kann anschließend der Manuskript-Hauptclaim eingefroren werden. Wenn nicht, wird auf Option B oder C zurückgestuft.