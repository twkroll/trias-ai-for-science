# Paper Contribution Boundary + Outline v0.1

**Status:** PENDING AUTHOR-INTENT CLARIFICATION  
**Stand:** 2026-09-02  
**Depends on:** D021 / C06-R2

## 1. Zweck dieses Dokuments

Dieses Dokument friert noch **nicht** den endgültigen Paper-Claim ein. Es legt zunächst die engste Contribution fest, die durch den bisherigen Projektstand sicher getragen wird, und markiert anschließend explizit jene Stellen, an denen die ursprüngliche Trias-Idee möglicherweise stärker gemeint war als sie im bisherigen Comparator-Audit operationalisiert wurde.

Der nächste wissenschaftliche Schritt ist daher keine weitere Simulation, sondern eine Präzisierung der Autorenintention.

---

## 2. Sicher tragfähige Contribution Boundary

Der bisher sicher tragfähige Beitrag lautet:

> Die Directed Trias ist eine kompakte fachübergreifende Audit-Linse, mit der unterschiedliche Praktiken der Computational Science als gerichtete Transformationen zwischen den funktionalen Rollen Zielsystem, Theorie und operative Vermittlung beschrieben und miteinander verglichen werden können. Die bisherigen Fallstudien zeigen zugleich, dass diese Linse keine neue Fehler-, Validierungs-, Provenance- oder Identifiability-Theorie ersetzt oder begründet. Ihr derzeit belegbarer Beitrag ist die gemeinsame Darstellung und begriffliche Verbindung von Forward- und Inverse-Problemen, die sonst typischerweise in getrennten Fachsprachen behandelt werden.

Diese Fassung beansprucht **Synthese**, nicht exklusive Diagnosefähigkeit.

---

## 3. Vorgeschlagener Paper-Hauptclaim v0.1

> **Principal Claim P1:** Computational Science kann methodologisch als System gerichteter Transformationen zwischen einem intendierten Zielsystem, theoretischen Repräsentationen und operativen Vermittlungen analysiert werden. Eine explizite Directed-Trias-Darstellung bietet dafür eine einheitliche, leichtgewichtige Sprache, in der formale Lösbarkeit, numerische Operationalisierung, datengetriebene inverse Inferenz und gelernte Surrogate vergleichbar gemacht werden. Der Beitrag besteht in dieser fachübergreifenden Synthese und in der expliziten Begrenzung dessen, was aus den jeweiligen Outputs gerechtfertigt folgt; nicht in neuen mathematischen Validierungs- oder Identifizierbarkeitskriterien.

### Evidenzstatus

- gemeinsame Darstellbarkeit der Projektfälle: direkt demonstrierbar;
- begriffliche Anschlussfähigkeit: hoch;
- Überlegenheit gegenüber bestehenden Frameworks: **nicht gezeigt**;
- praktische Verbesserung wissenschaftlicher Entscheidungen: **nicht gezeigt**;
- Originalität der Synthese: nur moderat und weiter literaturkritisch zu prüfen.

---

## 4. Explizite Non-Claims

Das Paper sollte nicht behaupten:

1. Berechnung sei in Wissenschaftsphilosophie oder Computational Science bisher epistemisch übersehen worden.
2. Realität, Theorie und Berechnung seien ontologisch drei unabhängige Entitäten.
3. Die Trias entdecke neue numerische Fehlertypen oder ersetze Verification & Validation.
4. Gerichtete Provenance sei neu.
5. Claim-to-evidence traceability sei neu.
6. Nichtidentifizierbarkeit, Equifinality oder observational equivalence seien neue Folgen der Trias.
7. Dynamische Adäquanz impliziere oder widerlege strukturelle Gleichungswahrheit.
8. Der inverse Lorenz/SINDy-Demonstrator bestätige einen robusten Provenance-Effekt; sein vorregistriertes Ergebnis ist `INFORMATIVE_NEGATIVE`.
9. Der ML-v0.1-Demonstrator bestätige den ML-Provenance-Claim; sein Ergebnis ist `INCONCLUSIVE_LEARNER_ERROR`.
10. Die Directed Trias sei bereits empirisch als nützlicher, verständlicher oder effizienter als etablierte Frameworks validiert.

---

## 5. Comparator-Coverage-Matrix für das Paper

| Directed-Trias-Frage | Starker bestehender Comparator | Abdeckung | verbleibende mögliche Trias-Rolle |
|---|---|---:|---|
| Welche numerische Operationalisierung ist für einen Use Case geeignet? | Numerical Analysis / V&V / Credibility | sehr hoch | gemeinsame Einordnung mit nicht-numerischen Fällen |
| Wie beeinflusst Preprocessing Equation Discovery? | System Identification / SINDy robustness | sehr hoch | Einordnung als inverse Transformationskante |
| Ist eine Theorie/Parameterstruktur eindeutig rekonstruierbar? | Identifiability / Observability / structural error | sehr hoch | Verbindung mit Forward-Problemen |
| Woher stammt ein Daten-/Modellartefakt? | Workflow/Data Provenance / W3C PROV | sehr hoch | epistemische Typisierung der Artefakte |
| Welche Evidenz rechtfertigt welchen Claim? | V&V + Assurance Cases / CAE / GSN | sehr hoch | Bezug der Claims auf R/T/C-Rollen und Transformationsrichtung |
| Formale Lösbarkeit vs. praktische Verfügbarkeit | Computability/traktability/numerical practice + philosophy of simulation | hoch | Verbindung mit späteren daten-/ML-basierten Fällen |
| Eine einzige Sprache über Sundman, Solver, inverse Inferenz und ML | kein einzelner projektspezifisch getesteter Comparator | offen | wahrscheinlich stärkster verbleibender Synthese-Claim |

Der letzte Tabellenpunkt ist der derzeit interessanteste Rest, aber noch kein belegter Überlegenheitsclaim.

---

## 6. Rolle der vier Projektfälle

### 6.1 Sundman — analytische Verfügbarkeit ist nicht operative Verfügbarkeit

Funktion im Paper:

```text
T_formal -> C_evaluation
```

Kernaussage:

```text
konvergente analytische Repräsentation
not=> praktische Berechenbarkeit/Nutzbarkeit
```

Sundman liefert den historischen Einstieg und motiviert die Unterscheidung zwischen mathematischer Existenz/Repräsentation und operativer Verfügbarkeit. Er ist kein Beweis für die Originalität der Trias.

### 6.2 Figure-eight — Forward-Operationalisierung

Funktion:

```text
same target + same T -> C_RK4 / C_Verlet -> different profiles
```

Der Demonstrator zeigt empirisch, dass eine einzige globale Genauigkeitsmetrik wissenschaftliche Eignung nicht vollständig repräsentiert. RK4 und Velocity-Verlet erzeugen unterschiedliche Trajektorien-/Strukturprofile. Dies stützt C05, ist aber etablierter numerical-analysis/V&V-Stoff.

### 6.3 Lorenz/SINDy — inverser, vorregistrierter negativer Test

Funktion:

```text
R -> D -> C_pre -> D_reconstructed -> C_infer -> T_hat
```

Der interessante Provenance-Effekt tritt nicht seed-robust auf. Gerade deshalb eignet sich der Fall als methodologischer Stress-Test: Die Audit-Linse muss auch ein negatives Ergebnis korrekt lokalisieren können und darf den explorativen Seed-2-Einzelfall nicht zum Haupteffekt machen.

### 6.4 ML v0.1 — inconclusive Provenance-Test

Funktion:

```text
T/R -> C_sim -> D -> C_ML -> R_hat
```

Der Learner-Fehler war wesentlich größer als die Teacher-Differenz. Der Fall illustriert, dass eine epistemische Hypothese nicht bewertet werden kann, wenn die operative Methode das zu untersuchende Signal nicht auflöst. Empfohlen: Appendix oder kurzer Haupttextkasten, nicht zentrales Resultat.

---

## 7. Empfohlene Haupttext-/Appendix-Verteilung

### Haupttext

1. Problem und Contribution Boundary.
2. Directed-Trias-Minimalnotation.
3. Sundman als historischer Motivationstest.
4. Figure-eight als Forward-Fall.
5. Lorenz/SINDy als inverser negativer Stress-Test.
6. Comparator-Matrix.
7. Diskussion: Synthesewert, Grenzen, AI-for-Science-Relevanz.

### Appendix / Supplement

- vollständige Figure-eight-Implementation/Gates;
- vollständige inverse Vorregistrierung und Metriken;
- ML-v0.1-Inconclusive-Experiment;
- detaillierte Literatur-/Comparator-Tabellen;
- Audit-Templates und maschinenlesbare Beispiele.

---

## 8. Vorgeschlagene Paperstruktur

### 1. Introduction — The problem is not another error metric

Motivation: Computational Science enthält mehrere gerichtete Übersetzungen, und unterschiedliche Literaturen behandeln einzelne Abschnitte dieser Übersetzungen sehr gut. Das Paper fragt, ob eine minimale gemeinsame Audit-Sprache nützlich ist, ohne sie als neue Credibility-Theorie zu verkaufen.

### 2. The Directed Trias as a lightweight synthesis

Definition der funktionalen Rollen:

```text
R = intended target system
T = theoretical representation
C = operational mediation
```

sowie gerichtete Ketten:

```text
Forward: T -> C_forward -> R_hat
Inverse: R -> C_obs -> D -> C_pre -> C_infer -> T_hat
Hybrid/ML: T/R -> C_sim -> D -> C_ML -> R_hat
```

### 3. Formal availability and operational availability: Sundman

Historischer Fall + Lösungsleiter; keine Neuheitsüberdehnung.

### 4. Forward operationalization: the Figure-eight demonstrator

Use-case-relative Solverprofile, C05, Vergleich mit V&V.

### 5. Inverse transformation: pre-registered Lorenz/SINDy stress test

Negative Resultatklasse als wissenschaftlich relevanter Befund; keine Seed-2-Überinterpretation.

### 6. Where the Trias is not novel

Explizite Comparatoren: System ID, identifiability, V&V/Credibility, provenance, assurance cases.

### 7. What the synthesis may still contribute

Nur fachübergreifender Vergleich, epistemische Typisierung und gemeinsame Darstellung. Praktische Nützlichkeit als offene Evaluationsfrage.

### 8. Implications for AI for Science

Besonders relevant bei mehrstufigen Pipelines aus Simulation, Daten, Rekonstruktion, Lernen und wissenschaftlichem Gebrauch. Keine Behauptung, dass dies nur mit Trias analysierbar sei.

### 9. Conclusion

Präziser Claim + Grenzen + offene Frage, ob die Synthese als eigenständiges Framework den Namen `Trias` verdient.

---

## 9. Vorgeschlagene Kernabbildungen/-tabellen

1. **Figure 1:** Directed Trias mit Forward-, Inverse- und Hybrid/ML-Pfad.
2. **Figure 2:** Lösungsleiter + querliegende Auditdimensionen.
3. **Figure 3:** Figure-eight: Trajektoriengenauigkeit vs. Struktur-/Invariantenerhaltung.
4. **Figure 4:** Lorenz/SINDy: `reconstruction error -> equation structure -> dynamical adequacy`, inklusive negativem Robustheitsergebnis.
5. **Table 1:** Comparator-Coverage-Matrix.
6. **Table 2:** Claim ledger: welcher Fall stützt welchen Claim und welchen ausdrücklich nicht.
7. **Box 1:** Reusable Directed-Trias Audit Template.

---

## 10. Empfohlenes Paperformat

Primär geeignet erscheint derzeit ein:

```text
conceptual / methodological synthesis paper
oder
perspective with computational case studies
```

Nicht empfohlen als Hauptpositionierung:

```text
new V&V framework
new AI-for-Science validation theory
new identifiability framework
new provenance standard
```

Eine konkrete Journalentscheidung sollte erst erfolgen, nachdem die Autorenintention im folgenden Abschnitt geklärt wurde.

---

## 11. Wo die bisherige Interpretation der ursprünglichen Idee scheitern könnte

Der bisherige Audit hat hauptsächlich folgende starke Lesart getestet:

> Die Trias erzeugt eine **neue diagnostische/validierende Fähigkeit**, die etablierte Frameworks nicht besitzen.

Genau diese Lesart wird durch die Comparatoren stark geschwächt.

Es ist jedoch möglich, dass die ursprüngliche Autorenintuition etwas anderes meint. Vier alternative Kerne müssen unterschieden werden:

### Interpretation A — `Computation is a third irreducible epistemic role`

Behauptung: Theorie–Experiment ist als Grundschema kategorial unzureichend; Berechnung besitzt eine eigenständige epistemische Rolle, die nicht sinnvoll in Theorie oder Experiment aufgeht.

Bisheriges Problem: Philosophie der Simulation und Computational Science behandeln Berechnung/Simulation längst als epistemisch eigenständig relevant. Der bisherige Demonstrator zeigt zudem noch nicht, in welchem **präzisen Sinn irreduzibel** gemeint ist.

Was zur Rettung nötig wäre: ein klares Irreduzibilitätskriterium. Beispiel: Welche Erklärung, Rechtfertigung oder Abhängigkeit kann prinzipiell nicht ohne separaten C-Typ formuliert werden?

### Interpretation B — `The key object is the transformation, not the poles`

Behauptung: Die eigentliche Theorie betrifft gerichtete, verlustbehaftete oder nichtinvertierbare Transformationen zwischen epistemischen Objekten.

Bisheriges Problem: Provenance, system identification, numerical analysis und information-loss/measurement frameworks behandeln solche Transformationen bereits. `Nichtinvertierbar` ist zudem bisher nur metaphorisch bzw. methodologisch und nicht mathematisch präzisiert.

Was zur Rettung nötig wäre: spezifizieren, welche Struktur der Transformationskomposition neu analysiert wird — z.B. Typen von Nicht-Kommutativität, Verlusten oder ungültigem Evidenztransport über mehrere Kanten.

### Interpretation C — `The novelty is epistemic typing`

Behauptung: Entscheidend ist nicht Provenance allein, sondern die explizite Typisierung jedes Artefakts als `target`, `theory`, `operational representation`, `data`, `prediction`, etc.; dadurch werden Kategorienfehler beim Evidenztransfer sichtbar.

Bisheriges Problem: Domänenspezifische Provenance plus Assurance Cases können ebenfalls Typen, Kontexte, Claims und Evidenzbeziehungen annotieren.

Was zur Rettung nötig wäre: ein konkreter Kategorienfehler, der in Standard-Provenance/CAE typischerweise unentdeckt bleibt, aber durch R/T/C-Typisierung systematisch ausgeschlossen wird.

### Interpretation D — `The key claim is about solution/knowledge levels, not framework novelty`

Behauptung: Das eigentliche philosophische Argument ist, dass Begriffe wie `solved`, `known`, `predicted`, `simulated` und `scientifically usable` verschiedene epistemische Ebenen markieren und Computational Science diese Ebenen systematisch auseinanderziehen muss.

Bisheriges Problem: Auch Traktabilität, numerical analysis, verification/validation und Wissenschaftsphilosophie unterscheiden viele dieser Ebenen. Wir haben noch nicht geprüft, ob **genau unsere Kombination/Lösungsleiter** einen eigenständigen philosophischen Beitrag liefert.

Was zur Rettung nötig wäre: den Hauptclaim von `Trias is a new audit framework` zu `computational solution is stratified and use-relative` verschieben und diesen gegen Literatur zu solution concepts, computability, tractability, simulation und prediction separat prüfen.

---

## 12. Autor-Intent-Entscheidung vor dem nächsten GO

Bevor der Paper-Hauptclaim eingefroren wird, sollte der Autor sagen, welche Aussage der ursprünglichen Idee am nächsten kommt:

```text
A = Berechnung ist als epistemische Rolle irreduzibel neben Realität und Theorie.
B = Entscheidend sind gerichtete/nichtinvertierbare Transformationen und ihr Informations-/Rechtfertigungsverlust.
C = Entscheidend ist die epistemische Typisierung der Zwischenobjekte und die Verhinderung ungültigen Evidenztransfers.
D = Entscheidend ist die Staffelung von „Lösung/Wissen/Nutzbarkeit“ in Computational Science.
E = Kombination aus A–D; bitte Priorität angeben.
F = etwas anderes; in eigenen Worten formulieren.
```

Bis diese Intention geklärt ist, sollte `Principal Claim P1` als konservative Synthese-Fassung behandelt werden und **nicht** als endgültiger Claim des Papers.

---

## 13. Nächster Schritt nach Autorenklärung

Nach der Klärung wird genau **eine** der folgenden Arbeiten durchgeführt:

- Claim neu formulieren und gezielten Comparator-Audit nur gegen die tatsächlich gemeinte starke These durchführen;
- oder konservative Synthese-Paperstruktur akzeptieren;
- oder das eigenständige Trias-Paper beenden und einzelne empirische Branches separat weiterführen.

Keine neue Simulation ist vor dieser begrifflichen Entscheidung notwendig.
