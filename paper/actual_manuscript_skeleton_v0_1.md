# Actual Manuscript Skeleton v0.1

**Working title:** *From Model Credibility to AI for Science: A Descriptive Trias of Target, Theory, and Computation*  
**Status:** PENDING REVIEW  
**Stand:** 2026-09-03  
**Depends on:** D029 / C08-D-R3 / P3

## 1. Zweck

Dieses Dokument ist die unmittelbare Schreibvorlage für das Manuskript. Es enthält noch keinen ausformulierten Papertext. Jeder Absatz erhält eine argumentative Funktion, einen lokalen Claim, Literatur-/Evidenzbedarf, Guardrails und einen vorgesehenen Übergang.

Zielumfang Haupttext:

```text
6.000–8.000 Wörter
```

Fallback:

```text
4.000–5.000 Wörter Short Perspective
```

Der Principal Claim bleibt P3. Das Manuskript darf dessen Boundary nicht während des Schreibens stillschweigend verstärken.

---

# 2. Titel- und Abstract-Strategie

## 2.1 Arbeitstitel

Primärer Titel:

> **From Model Credibility to AI for Science: A Descriptive Trias of Target, Theory, and Computation**

Alternative, falls `Trias` im Titel zu projektspezifisch wirkt:

> **From Model Credibility to AI for Science: Claim-Relative Epistemic Roles for Target, Theory, and Computation**

Empfehlung: zunächst Primärtitel; final nach Section-4-Test entscheiden.

## 2.2 Abstract — Absatzfunktion

Der Abstract soll fünf Sätze/Funktionen enthalten:

1. **Genealogie:** klassische Model-Credibility-Trennung anerkennen.
2. **Problemverschiebung:** AI verändert die Rolle von computation.
3. **Vorschlag:** R/T/C als claimspezifische Rollen reinterpretieren.
4. **Demonstration:** vier AI-Archetypen + klassische Kontrollen + negative/inconclusive Stress Tests.
5. **Boundary:** Synthese, keine neue V&V-Theorie, keine Überlegenheitsbehauptung.

Keine Aussage wie `we introduce a new triangle`.

---

# 3. Section 1 — Introduction: When “the model works” is epistemically incomplete

**Zielumfang:** 700–900 Wörter.

## Absatz 1 — Konkreter AI-for-Science-Aufhänger

**Funktion:** Problem anschaulich machen, bevor Begriffe eingeführt werden.

**Beispielkern:** Zwei Modelle haben dieselbe niedrige RMSE. Modell A wird gegen reale Held-out-Messdaten geprüft; Modell B gegen Ausgaben eines Simulators/Teachers.

**Lokaler Claim:**

> Derselbe numerische Performancewert kann unterschiedliche wissenschaftliche Aussagen stützen, je nachdem, gegen welchen Referenten und für welchen Claim er erhoben wurde.

**Evidenzbedarf:** keine starke Literaturbehauptung nötig; konzeptionelles Beispiel. Später Anschluss an SciML/surrogate credibility.

**Guardrail:** Nicht behaupten, RMSE-Kontextabhängigkeit sei neu.

**Übergang:** Von der Metrik zur allgemeineren Frage: Was bedeutet `the model works`?

## Absatz 2 — Pluralität computationaler Rollen in AI for Science

**Funktion:** Vier Archetypen motivieren.

Kurz nennen:

```text
prediction
surrogation
physics-informed/hybrid learning
equation discovery
```

**Lokaler Claim:** Computation ist in AI for Science nicht nur Implementierung eines vorgegebenen Modells; sie kann selbst Predictor, Emulator, Rekonstruktions-/Inferenzinstanz oder Generator eines Theorieclaims sein.

**Literaturanker:** Vinuesa et al.; Naser/P.E.D.U.D.; Karniadakis et al.; Kramer et al.

**Guardrail:** Alle Rollen sind etablierte Einzelpraktiken.

## Absatz 3 — Klassische Credibility-Genealogie früh anerkennen

**Funktion:** Hauptreviewer-Einwand vorwegnehmen.

**Lokaler Claim:** Reality/Problem Entity – Conceptual Model – Computerized Model und conceptual validity / verification / operational validity sind etablierte Vorläufer.

**Literaturanker:** Schlesinger et al. 1979; Sargent; moderne V&V/VVUQ.

**Schlüsselsatz:**

> The triangle is not new.

**Guardrail:** Keine rhetorische Abwertung von V&V.

## Absatz 4 — Das eigentliche Problem des Papers

**Funktion:** Delta definieren.

**Lokaler Claim:** Die klassische Struktur wird hier nicht ersetzt, sondern als claimspezifische Rollenstruktur gelesen, weil `T` und `C` in AI-Workflows ihre Position relativ zueinander wechseln können.

Schema kurz:

```text
T -> C
R -> C
R -> C -> T_hat
T + R-data -> C
```

## Absatz 5 — Contribution Statement

**Funktion:** P3 komprimiert formulieren.

**Muss enthalten:**

- genealogische Reinterpretation;
- R real/synthetic/hybrid;
- T present/partial/none/inferred;
- C numerical/learned/inferential;
- evidenzlokalisierte RT/TC/CR-Claims;
- keine globale Modellgüte.

## Absatz 6 — Paper map

Sehr knapp Sections 2–8 ankündigen.

---

# 4. Section 2 — Genealogy: From model credibility to the present problem

**Zielumfang:** 800–1.000 Wörter.

## Absatz 1 — Schlesinger-Terminologie

**Funktion:** historischen Ausgangspunkt sauber darstellen.

**Lokaler Claim:** Model credibility wurde explizit über Problem Entity/Reality, Conceptual Model und Computerized Model organisiert.

**Literatur:** Schlesinger et al. 1979.

**Keine Überdehnung:** historische Details nur soweit evidenziert.

## Absatz 2 — Sargent: die drei Bewertungsrelationen

**Funktion:** nahezu isomorphes Mapping zeigen.

Mapping:

```text
R-T ~ conceptual model validity / qualification
T-C ~ computerized model verification
C-R ~ operational validity / validation
```

**Lokaler Claim:** Das relationale Grundgerüst der Trias hat deshalb keine Topologie-Novelty.

## Absatz 3 — Moderne Fortsetzung

**Funktion:** zeigen, dass dies keine tote historische Terminologie ist.

**Literatur:** ASME/AIAA/NASA; VVUQ; intended use/context of use.

**Claim:** Verification, Validation, Scope und intended-use-relative Credibility sind modern stark ausgearbeitet.

## Absatz 4 — Warum dennoch weitergehen?

**Funktion:** Genealogie in Problemstellung verwandeln.

**Claim:** Klassische Credibility ist besonders natürlich für den Forward-Fall eines konzeptuell/mathematisch gegebenen Modells und seiner Implementierung. AI for Science macht zusätzliche Rollenbelegungen prominent.

**Guardrail:** Nicht behaupten, Sargent könne AI prinzipiell nicht behandeln. Nur sagen, dass die Rollenreinterpretation eine andere analytische Lesart motiviert.

## Absatz 5 — Übergang zur Rollenlesart

Schlusssatz:

> The relevant question is therefore not whether the classical triangle should be replaced, but how its elements should be interpreted when theory and computation are no longer fixed lifecycle stages.

**Figure 1 hier:** Genealogy, not invention.

---

# 5. Section 3 — From lifecycle stages to claim-relative epistemic roles

**Zielumfang:** 900–1.100 Wörter.

## Absatz 1 — Definition von R

**Funktion:** Referent claimspezifisch machen.

```text
R_REAL
R_SYNTHETIC
R_HYBRID
```

**Claim:** Ein Wechsel des Referenten ändert den wissenschaftlichen Claim, auch wenn dieselbe computational realization unverändert bleibt.

**Beispiel:** Teacher vs reale Messung.

## Absatz 2 — Definition von T

```text
PRESENT
PARTIAL
NONE_CLAIMED
INFERRED
```

**Claim:** `T` bezeichnet nicht jede interne Modellstruktur, sondern den tatsächlich beanspruchten wissenschaftlichen Theorie-/Mechanismus-/Erklärungsinhalt.

**Wichtig:** Black-box Predictor kann für engen Prediction-Use-Case `NONE_CLAIMED` haben, ohne Defizitwert.

## Absatz 3 — Definition von C

```text
solver
predictor
surrogate
reconstruction pipeline
inference/equation discovery
hybrid computational practice
```

**Claim:** C ist operative computational practice, nicht nur Computerhardware oder Code-Artefakt.

## Absatz 4 — Kanten als Claimtypen

Leitfragen:

```text
R-T: Was stützt den Theorieclaim über das Target?
T-C: Wie wird der Theorieinhalt operationalisiert/realisiert?
C-R: Was stützt den computational output gegenüber dem Target?
```

**Guardrail:** keine eindimensionalen Scores.

## Absatz 5 — Evidence Ledger Minimalform

Einführen:

```text
edge | facet | claim | evidence | use case | scope | status
```

Status:

```text
ESTABLISHED
PARTIAL
UNCERTAIN
UNTESTED
NOT_APPLICABLE
```

**Claim:** Status ist nicht Wahrheit, sondern dokumentierter Evidenzstatus im Scope.

## Absatz 6 — Nichttransitivität als Default

Formeln:

\[
A_{RT}+A_{TC}\not\Rightarrow A_{CR},
\]
\[
A_{TC}+A_{CR}\not\Rightarrow A_{RT},
\]
\[
A_{RT}+A_{CR}\not\Rightarrow A_{TC}.
\]

**Wichtig:** kein logischer Unmöglichkeitsclaim; nur kein stillschweigender Evidenztransfer.

## Absatz 7 — Bridge Claims

Kurzes Surrogate-Beispiel:

```text
teacher fidelity
+ validated simulator for same QoI/scope
+ controlled surrogate error
-> conditional support for real-target claim
```

**Guardrail:** Assurance/provenance/credibility haben starke Vorarbeit; Bridge-Schema ist Synthese.

**Table 1 hier:** Genealogy/comparator mapping.

---

# 6. Section 4 — Four AI-for-Science role configurations

**Zielumfang:** 1.700–2.100 Wörter. Dies ist der Haupttest des Papers.

**Figure 2 am Anfang:** vier Panels der Rollenbelegungen.

## 4.1 Predictive black-box: C-R without an explicit T claim

### Absatz 1 — Workflow

```text
R -> D -> C
T = NONE_CLAIMED
```

### Absatz 2 — Evidenzprofil

Real held-out prediction stützt primär `CR_PREDICTION`.

**Nichtimplikation:** keine automatische mechanistische/explanatory `R-T`-Stützung.

### Absatz 3 — Literaturvergleich

Naser/P.E.D.U.D.; prediction/explanation/understanding literature; Vinuesa.

**Boundary:** Trias erfindet Prediction ohne Erklärung nicht; sie lokalisiert den Claim.

### Absatz 4 — Nutzen der Rollenlesart

Ein `NOT_APPLICABLE` oder `NONE_CLAIMED` für T ist keine Abwertung. Das verhindert, dass das Framework heimlich Mechanismus als universelles Gütekriterium setzt.

## 4.2 Synthetic surrogate: same metric, different referent

### Absatz 1 — Workflow

```text
T -> C_sim -> D_syn -> C_surrogate
```

### Absatz 2 — Kernkontrast

Teacher-Holdout vs Real-Holdout.

\[
\mathrm{RMSE}_{\mathrm{teacher}}=\epsilon
\]

und

\[
\mathrm{RMSE}_{\mathrm{real}}=\epsilon
\]

können numerisch gleich sein, aber unterschiedliche Claims stützen.

### Absatz 3 — Referentenwechsel

`R_syn` und `R_real` explizit unterscheiden.

**Claim:** Ein Wechsel des Referenten erzeugt ein anderes Evidenzprofil.

### Absatz 4 — Comparator

Surrogate/metamodel credibility, SciML-V&V, Jakeman et al.

**Boundary:** sim-to-real nicht neu; der Beitrag ist gemeinsame Claimtypisierung.

**Figure 3 hier:** Same metric, different epistemic claim.

## 4.3 Physics-informed/hybrid ML: overlapping relations

### Absatz 1 — Workflow

```text
T + D(R) -> C
```

### Absatz 2 — drei unterschiedliche Fragen

```text
T-C: Constraint/Theorie implementiert?
R-T: Theorie für reales Regime adäquat?
C-R: Modelloutput empirisch erfolgreich?
```

### Absatz 3 — Warum `physics-informed` kein globaler Status ist

**Claim:** Physics-informed bezeichnet zunächst eine Konstruktions-/Operationalisierungsrelation, nicht automatisch reale Gültigkeit oder mechanistische Wahrheit.

### Absatz 4 — Literatur

Karniadakis et al.; SciML; Vinuesa et al.

**Guardrail:** keine Kritik, dass PIML dies grundsätzlich verwechselt; nur semantische Trennung der möglichen Claims.

## 4.4 Equation Discovery: C produces T

### Absatz 1 — Workflow

```text
R -> D -> C_infer -> T_hat
```

### Absatz 2 — Rollenverschiebung

Hier ist T epistemischer Output der computational practice, nicht vorausgesetzter Input.

**Claim:** Dies macht die Lifecycle-Lesart besonders unpassend und die Rollenlesart besonders anschaulich.

### Absatz 3 — zwei Erfolgsformen

```text
dynamical/statistical adequacy
structural/mechanistic fidelity
```

nicht automatisch gleichsetzen.

### Absatz 4 — Literatur

Kramer et al.; SINDy/Equation Discovery; Identifiability; Zhai–Lucarini–Lai.

### Absatz 5 — Zwischenfazit Section 4

Alle vier Fälle sind mit derselben kleinen Grammatik darstellbar, ohne die jeweiligen Fachliteraturen zu ersetzen.

**Survival-Test S2 hier durchführen:** Wenn der geschriebene Abschnitt keine zusätzliche begriffliche Kompression erzeugt, Paper kürzen/stoppen.

**Table 2 hier:** AI-for-Science role profiles.

---

# 7. Section 5 — Classical controls: where ordinary V&V already suffices

**Zielumfang:** 600–800 Wörter.

## 5.1 Sundman

### Absatz 1 — Historischer Fall

Korrekt formulieren: konvergente analytische Repräsentation nach Regularisierung; praktisch extrem langsam/evaluativ unattraktiv.

### Absatz 2 — Profilfunktion

Unterscheidung innerhalb T-C:

```text
formal representation/fidelity
vs
tractability/evaluability
```

**Claim:** analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.

**Guardrail:** keine falsche Aussage, Sundman-Reihe divergiere.

## 5.2 Figure-eight

### Absatz 1 — Warum Kontrollgruppe

Gleiches synthetisches Target + gleiche Theorie + verschiedene Solver.

### Absatz 2 — Befund

RK4 stärker bei Trajektoriengenauigkeit; Verlet stärker bei bestimmten Struktur-/Driftkriterien.

### Absatz 3 — epistemische Funktion

**Claim:** Standard Numerical Analysis/V&V erklärt diesen Fall bereits sehr gut.

**Wichtig:** Gerade dieses Nicht-Mehrleisten schützt das Paper vor Universalitätsanspruch.

---

# 8. Section 6 — Stress tests: negative and inconclusive evidence

**Zielumfang:** 600–800 Wörter.

## 6.1 Lorenz/SINDy — informative negative

### Absatz 1 — Forschungsfrage und Vorregistrierung

Kurz: 20% paired missingness; linear vs cubic reconstruction; fixed SINDy; seed consistency.

### Absatz 2 — Ergebnis

```text
G1-G3 PASS
linear structural perturbation: 1/3
cubic: 0/3
classification: INFORMATIVE_NEGATIVE
```

### Absatz 3 — Rolle im Paper

**Claim:** Die Trias liefert keine positive Provenance-Wirkung; sie lokalisiert korrekt, dass structural-effect evidence nicht robust etabliert wurde, obwohl andere dynamische Claims oft gut aussehen.

**Guardrail:** Seed 2 nur explorativ.

## 6.2 ML v0.1 — inconclusive

### Absatz 1 — Resolvability-Problem

Learner error >> teacher difference.

### Absatz 2 — epistemische Funktion

`TC_RESOLVABILITY` scheitert; damit ist der nachgelagerte Teacher-Provenance-Claim unentscheidbar.

**Status:** `INCONCLUSIVE_LEARNER_ERROR`, nicht negative Evidenz gegen C07.

### Absatz 3 — Meta-Punkt

Ein deskriptives Profil sollte `negative`, `inconclusive`, `untested` sauber auseinanderhalten.

**Table 3 hier:** Project evidence ledger.

---

# 9. Section 7 — What the Trias adds, and what adjacent frameworks already do better

**Zielumfang:** 900–1.100 Wörter.

## Absatz 1 — V&V/VVUQ

**Was es besser/tiefer macht:** Verification, Validation, UQ, acceptance criteria, context/intended use.

**Trias-Rest:** Rollen-/Claimlokalisierung über mehrere AI-Konfigurationen.

## Absatz 2 — Provenance

**Was es besser macht:** Herkunft/Transformation von Artefakten.

**Trias-Rest:** epistemische Rolle des Claims, nicht nur lineage.

## Absatz 3 — Assurance cases

**Was es besser macht:** Claim–Argument–Evidence-Beziehungen.

**Trias-Rest:** sehr kleine domänenübergreifende Rollenklassifikation.

## Absatz 4 — Identifiability/System ID

**Was sie besser machen:** formale/technische Recoverability und Robustheit inverser Modelle.

**Trias-Rest:** Verbindung zu Forward-/Predictive-/Surrogate-Fällen in einer gemeinsamen Sprache.

## Absatz 5 — Philosophy of ML / P.E.D.U.D. / Vinuesa

**Was sie besser machen:** epistemische Funktionen und Theory-Availability differenzierter analysieren.

**Trias-Rest:** Zuordnung konkreter Evidenz zu Referent–Theory–Computation-Relationen.

## Absatz 6 — Exakter Contribution Boundary

Muss sehr defensiv sein:

> The proposal is therefore best understood as a compact genealogical synthesis and evidence-localization vocabulary, not as a replacement for any of these frameworks.

## Absatz 7 — Gegen mögliche Trivialitätskritik

Reviewerfrage antizipieren:

> Ist das nur neue Notation?

Antwort darf nur lauten: Der Eigenwert besteht dann, wenn Section 4 tatsächlich verschiedene Fachfälle mit weniger begrifflichen Ad-hoc-Wechseln vergleichbar macht.

**Stop-Kriterien S1–S4 hier intern erneut prüfen.**

---

# 10. Section 8 — Discussion: scientific success without global success

**Zielumfang:** 600–800 Wörter.

## Absatz 1 — Keine globale Erfolgseigenschaft

**Claim:** `successful`, `validated`, `physics-informed`, `discovered` sind ohne Claim-/Scope-Angabe leicht überbreit.

## Absatz 2 — Kein normativer All-three-edges-Imperativ

**Claim:** Ein Predictor ohne T kann für seinen Zweck legitim sein; `NOT_APPLICABLE` ist kein Defizit.

## Absatz 3 — Keine notwendige Trade-off-Theorie

**Claim:** Kanten können in Spannung geraten, aber es wird keine Nullsummen-Geometrie behauptet.

## Absatz 4 — Deskriptiver Nutzen

Mögliche Funktion:

- transparentere Kommunikation;
- präzisere Interpretation von Performance Claims;
- Explikation offener Evidenzrelationen.

**Guardrail:** praktische Nützlichkeit nicht empirisch nachgewiesen.

## Absatz 5 — Future Work

Nur klar getrennt:

- Nutzerstudie / inter-rater coding;
- echte Case-study-Audit-Anwendung;
- mögliche normative Erweiterung später.

Keine neue Experimentspflicht für dieses Paper.

---

# 11. Section 9 — Conclusion

**Zielumfang:** 200–300 Wörter.

Nur drei Funktionen:

1. Genealogie anerkennen.
2. Rollenreinterpretation + Evidence Localization zusammenfassen.
3. Grenzen wiederholen.

Kein neuer Claim am Ende.

---

# 12. Figuren- und Tabellenplan

## Figure 1 — Genealogy, not invention

Links: Schlesinger/Sargent-Triade.  
Rechts: claim-relative R/T/C-Rollen.  
Pfeilbeschriftung: `genealogical reinterpretation / generalisation`.

## Figure 2 — Four AI-for-Science role configurations

Vier Panels:

```text
A black-box:       R -> D -> C      ; T absent
B surrogate:       T -> C1 -> Dsyn -> C2
C PIML:            T + D(R) -> C
D equation disc.:  R -> D -> C -> T_hat
```

**Wichtigste Abbildung.**

## Figure 3 — Same metric, different epistemic claim

Teacher RMSE vs real-target RMSE; gleiche Zahl, andere Claimrelation.

## Table 1 — Genealogy/comparator matrix

```text
Trias element | classical credibility | modern V&V/SciML | novelty status | paper role
```

## Table 2 — AI role profiles

```text
case | R type | T status | C role | evidence | supported relation | explicit non-implication
```

## Table 3 — Own project evidence

```text
Sundman       conceptual illustration
Figure-eight  positive standard-V&V control
Lorenz/SINDy  INFORMATIVE_NEGATIVE
ML v0.1       INCONCLUSIVE_LEARNER_ERROR
```

---

# 13. Quellenzuordnung nach Manuskriptteil

## Section 1

- Schlesinger/Sargent als Vorgriff;
- Vinuesa;
- Naser;
- Kramer;
- Karniadakis.

## Section 2

- Schlesinger et al. 1979;
- Sargent;
- ASME/AIAA/NASA;
- ggf. Oberkampf/Roy/Trucano für V&V-Hintergrund.

## Section 3

- eigene Edge-Semantics als projektspezifische Synthese;
- Parker für adequacy-for-purpose;
- Assurance/Provenance nur für Abgrenzung.

## Section 4

- 4.1 Naser, Vinuesa, Philosophy-of-ML;
- 4.2 Jakeman + surrogate/ROM credibility;
- 4.3 Karniadakis + moderne PIML/SciML;
- 4.4 Kramer + SINDy + Zhai–Lucarini–Lai + Identifiability.

## Section 5

- Sundman-historische Quellen;
- eigene Figure-eight-Ergebnisse + Numerical Analysis/V&V.

## Section 6

- eigene Results/Contracts;
- Zhai nur als externer Kontrast, nicht als Bestätigung.

## Section 7

- V&V/VVUQ;
- W3C PROV/workflow provenance;
- Assurance cases/GSN;
- Identifiability/observability;
- System ID;
- Naser/Vinuesa/Jakeman.

---

# 14. Empfohlene Schreibreihenfolge

Nicht linear von Introduction nach Conclusion schreiben.

Empfohlene Reihenfolge:

```text
1. Section 4 — vier AI-Archetypen
2. Section 2 — Genealogie
3. Section 3 — Rollen-/Evidence-Semantik
4. Section 7 — Comparator/Contribution Boundary
5. Section 5 — klassische Kontrollen
6. Section 6 — negative/inconclusive Stress Tests
7. Section 8 — Discussion
8. Section 1 — Introduction
9. Section 9 — Conclusion
10. Abstract
```

Begründung: **Section 4 ist der eigentliche Survival-Test.** Wenn dort die Synthese keinen begrifflichen Mehrwert erzeugt, soll das Paper gekürzt oder gestoppt werden, bevor viel Prosa geschrieben wird.

---

# 15. Granulare Schreibziele

## Schreibziel W1 — Section 4 v0.1

Erstelle nur die vier AI-Archetypen als Rohtext, jeweils 3–5 Absätze. Noch keine Introduction. Prüfe danach:

```text
- gleiche Grammatik ohne ad-hoc Ausnahmen?
- pro Fall mindestens ein präziser Evidenzunterschied?
- weniger Mehrdeutigkeit als globale Labels?
- Equation Discovery tatsächlich strukturell instruktiv?
```

**Decision Gate:** PASS / SHORTEN / STOP.

## Schreibziel W2 — Genealogy + Mapping

Section 2 schreiben und Table 1 erstellen. Jede Trias-Komponente gegen Prior Art annotieren.

## Schreibziel W3 — Formal minimal semantics

Section 3 schreiben; nur so viel Ledger-Semantik wie Section 4 tatsächlich benötigt.

## Schreibziel W4 — Boundary section

Section 7 schreiben. Wenn Beitrag hier nur Notation bleibt: STOP/STORT PERSPECTIVE.

## Schreibziel W5 — Controls + stress tests

Sections 5–6 integrieren, ohne zentrale Story zu überladen.

## Schreibziel W6 — Discussion + framing

Sections 8, 1, 9 und Abstract zuletzt.

---

# 16. Manuskript-Red-Flags

Beim Schreiben sofort markieren, wenn einer dieser Sätze sinngemäß auftaucht:

```text
“we introduce the first...”
“existing V&V cannot...”
“AI fundamentally breaks validation...”
“the three relations are independent...”
“all scientific models should maximize...”
“our Lorenz experiment demonstrates...” [positive provenance]
“our ML experiment shows...” [teacher effect]
```

Diese Formulierungen sind mit den akzeptierten Entscheidungen nicht vereinbar.

---

# 17. Entscheidungsempfehlung nach Skeleton

**Empfehlung: ACCEPT Actual Manuscript Skeleton v0.1.**

Danach nicht das gesamte Paper auf einmal schreiben. Nächste Abhängigkeit sollte ausschließlich **Writing Goal W1: Section 4 — Four AI-for-Science Role Configurations v0.1** sein.

Nach W1 wird explizit entschieden:

```text
PASS -> Manuskript fortsetzen
SHORTEN -> Short Perspective
STOP -> Standalone Paper beenden
```

Dieser Gate verhindert, dass die verbleibende Synthese nur aufgrund bereits investierter Arbeit weitergeschrieben wird.