# Projektbriefing: Trias — Zielsystem, Theorie, Berechnung und AI-for-Science-Provenance

**Zielgruppe:** promovierte Physikerin mit wissenschaftsphilosophischem Hintergrund  
**Status:** internes Diskussions- und Einladungsdokument  
**Stand:** 2026-09-02

## 1. Projektidee

Das Projekt untersucht, ob die explizite Trennung von **Zielsystem/Realität, theoretischer Beschreibung und Berechnung/Umsetzung** als methodologisches Audit-Framework für Computational Science und AI for Science einen eigenständigen diagnostischen Nutzen besitzt.

Die Trias wird nicht als universale Ontologie verstanden. Der mögliche Beitrag liegt vielmehr in einer durchgängigen Provenance- und Rechtfertigungsstruktur: Für ein wissenschaftliches Resultat soll explizit sichtbar bleiben,

1. was am Zielsystem festgelegt oder vorausgesetzt wurde,
2. was die Theorie tatsächlich lizenziert,
3. welche Transformationen durch konkrete Berechnung, Diskretisierung, Datengenerierung oder ML hinzukommen,
4. und welcher wissenschaftliche Gebrauch dadurch tatsächlich gerechtfertigt ist.

Das Newtonsche Drei-Körper-Problem dient als kontrollierter Leitfall. Es erlaubt, analytische Repräsentation, praktische Auswertbarkeit, numerische Operationalisierung und lernbasierte Surrogation voneinander zu trennen, ohne sofort empirische Messunsicherheit als zusätzliche Variable einzuführen.

## 2. Methodologischer Status der Trias

Der erste akzeptierte Kernclaim ist bewusst moderat:

> Im Drei-Körper-Fall kann die explizite Trennung von Zielsystem, theoretischer Beschreibung und operativer Umsetzung diagnostische Unterschiede sichtbar machen, die in einer bloßen Theorie–Experiment-Beschreibung unterbestimmt bleiben. Der beanspruchte Mehrwert besteht nicht darin, Berechnung erstmals als epistemisch relevante Praxis zu identifizieren, sondern darin, entsprechende Einsichten in ein explizites Audit-Schema zu überführen.

Inzwischen hat der Demonstrator diesen Claim zugleich gestützt und eingeschränkt. Der reine Solverfall zeigt tatsächlich implementationsabhängige wissenschaftliche Profile; ein harter Vergleich mit etablierter numerischer Analysis, Verification & Validation und Credibility-Frameworks zeigt jedoch, dass die Trias dort keine eindeutig neuen numerischen Fehlertypen oder Validierungsfragen liefert.

Der aktuell verteidigungsfähige Mehrwert ist daher schwächer: **integrative Zuordnung, Mapping und epistemische Provenance** über mehrere Übergangsebenen hinweg.

## 3. Synthetisches Zielsystem

Der erste Pol der Trias wird funktional als **Zielsystem** verstanden. Im kontrollierten Drei-Körper-Fall ist dies ein synthetisches Zielsystem: eine konkrete Instanziierung der idealisierten Newtonschen Dynamik mit Zustandsraum, Massen, Anfangsdaten und betrachteter Zeitspanne.

Projektintern kann dies schematisch als

```text
S_syn = (X, F, theta, x0)
```

notiert werden.

Die Unterscheidung zwischen Theorie und Zielsystem ist funktional, nicht notwendig ontologisch. Das Zielsystem ist durch Theorie mitkonstituiert, bleibt aber von jeder konkreten numerischen oder gelernten Repräsentation zu unterscheiden. Eine berechnete Trajektorie ist nicht das Zielsystem selbst.

## 4. Lösungsleiter und operative Verfügbarkeit

Ein zentraler Gedanke des Projekts lautet, dass das Wort „Lösung“ mehrere nichtäquivalente Ebenen verdecken kann. Relevant sind unter anderem:

- mathematische Existenz,
- analytische Repräsentation,
- mathematische Konvergenz,
- operative rechnerische Machbarkeit,
- numerische Simulation und Stabilität,
- Vorhersage,
- wissenschaftliche Nutzbarkeit.

C04 trennt insbesondere mathematische Konvergenz, operative Machbarkeit, numerische Stabilität, Systemsensitivität und wissenschaftliche Nutzbarkeit. Diese Kategorien werden nicht als vollständig unabhängig verstanden, dürfen aber nicht gleichgesetzt werden.

Wissenschaftliche Nutzbarkeit ist zweckrelativ: Ein numerischer Output kann für eine kurzfristige Trajektorienfrage geeignet und für eine langfristige Strukturfrage unzureichend sein oder umgekehrt.

## 5. Sundman als historisch-mathematischer Leitfall

Sundmans klassisches Resultat ist für das Projekt gerade kein Beispiel fehlender Konvergenz. Unter den klassischen Voraussetzungen wird nach Regularisierung und geeigneter Zeittransformation eine global konvergente Reihenrepräsentation erhalten.

Der methodologische Punkt lautet:

> **Formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.**

Die Reihe ist mathematisch konvergent, aber für praktische Bahnberechnung extrem langsam. Daraus folgt nicht, dass sie numerisch instabil sei, und die praktische Ineffizienz wird nicht einfach auf Chaos zurückgeführt.

Sundman trägt den methodologischen Bogen, beweist die Trias aber nicht allein.

## 6. Numerischer Minimaldemonstrator

Als kontrollierte Zielinstanz wurde die planare equal-mass Figure-eight-Choreographie in dimensionslosen Einheiten gewählt. Verglichen wurden:

- DOP853 als hochgenaue adaptive Referenz mit zusätzlicher engerer Cross-Check-Rechnung,
- klassischer Fixed-Step-RK4,
- Velocity-Verlet als symplektischer strukturerhaltender Kontrast.

Zwei Use Cases wurden getrennt:

- **U1:** kurzfristige Trajektoriengenauigkeit über eine nominelle Periode;
- **U2:** langfristige Strukturdiagnostik über 100 nominelle Perioden.

Die Referenzunsicherheit wurde explizit überprüft und nicht als exakte Ground Truth behandelt.

### Hauptresultat

RK4 war im getesteten Bereich deutlich trajectory-genauer. Velocity-Verlet zeigte dagegen wesentlich geringeren fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau. Gleichzeitig hatte RK4 teilweise kleinere maximale Energiefehleramplituden.

Daraus folgt keine globale Rangfolge. Das Resultat unterstützt den moderaten Claim C05:

> Verschiedene numerische Operationalisierungen können bei identischem Zielsystem und identischer Theorie verschiedene wissenschaftlich relevante Fehler- und Strukturprofile erzeugen; welche Operationalisierung vorzuziehen ist, hängt vom spezifizierten wissenschaftlichen Gebrauch ab.

## 7. Der entscheidende negative Originalitätstest

Ein nachgeschalteter Vergleich fragte, ob die Trias diese Befunde besser diagnostiziert als etablierte numerische Analysis, V&V und Credibility Assessment.

Das Ergebnis war negativ für die starke Fassung. Code Verification, Solution Verification, intended use, uncertainty, sensitivity, model assumptions und Ergebnis-Credibility decken den Solverfall bereits sehr weitgehend ab.

Deshalb wurde C06 revidiert:

> Der Trias-Audit erzeugt im gegenwärtigen Drei-Körper-Demonstrator keine eindeutig neuen numerischen Validierungsfragen. Sein derzeit belegbarer Mehrwert liegt in einer expliziten durchgängigen Zuordnung von Annahmen, Transformationen und Rechtfertigungsanforderungen zu Zielsystem, Theorie, Berechnung und ihren Übergängen.

Die Trias wird ausdrücklich **nicht als Ersatz für V&V** positioniert.

## 8. Warum anschließend AI for Science?

Im reinen Solverfall besteht im Wesentlichen die Kette

```text
Zielsystem/Theorie -> numerische Operationalisierung -> Output.
```

Bei AI for Science kommen zusätzliche Übersetzungen hinzu:

```text
Zielsystem/Theorie
-> numerischer Datengenerator
-> Trainingsdaten
-> gelerntes Modell
-> Rollout/Prediction
-> wissenschaftlicher Schluss.
```

Damit wird eine neue Provenance-Frage kontrollierbar: Eine kleine Test-MSE kann zunächst nur zeigen, dass ein Modell einen numerischen Teacher gut reproduziert. Daraus folgt nicht automatisch, dass es das wissenschaftliche Zielsystem im gleichen Maß repräsentiert.

## 9. ML-Provenance-Demonstrator v0.1

Der erste ML-Test hielt das Figure-eight-Zielsystem fest und verwendete zwei Teacher:

- DOP853 primary/tight als Reference teacher,
- coarse RK4 mit genau einem Schritt `h=T_pub/50`.

Beide Trainingsdatensätze verwendeten exakt dieselben Inputzustände; nur die Labels unterschieden sich. Gelernt wurde mit einem einfachen Residual-MLP `12-128-128-128-12`, drei gepaarten Seeds und bitgleicher Initialisierung innerhalb jedes Teacher-Paars.

Ein wichtiger Bestandteil war die exakte Fehlerzerlegung

```text
e_total = e_model + e_teacher
```

mit

```text
e_model   = y_hat_rk4model - y_rk4
e_teacher = y_rk4 - y_ref
e_total   = y_hat_rk4model - y_ref.
```

Damit sollte eine gemeinsame Referenzabweichung quantitativ in Learner- und Datengeneratorbeitrag zerlegt werden.

## 10. Ergebnis von ML v0.1: bewusst inconclusive

Der Full Run bestand das Reference-Gate sehr deutlich:

```text
D_teacher_test ≈ 1.3035e-05
D_ref_test     ≈ 5.83e-14
```

Die numerische Unsicherheit des Reference teachers war also nicht das Problem.

Das vorregistrierte Learner-Resolvability-Gate scheiterte jedoch klar. Die medianen own-teacher Test-RMSEs lagen bei etwa

```text
ref-trained ≈ 0.7187
rk4-trained ≈ 0.7172
```

und damit ungefähr fünf Größenordnungen über dem Teacher-Signal.

Das Experiment wird daher korrekt als

```text
INCONCLUSIVE_LEARNER_ERROR
```

klassifiziert. Der mögliche ML-Provenance-Claim C07 wird weder akzeptiert noch verworfen.

Methodologisch ist dies wichtig: Die vorregistrierten Gates verhinderten, dass kleine Differenzen zwischen Modellgruppen nachträglich als scheinbar interessanter Provenance-Effekt interpretiert wurden.

## 11. Diagnose des v0.1-Fehlers

Zwei Probleme dominierten:

1. Der rohe Inkrement-Lernfehler blieb bereits im Training deutlich über der sehr kleinen RK4-vs.-DOP853-Teacher-Differenz.
2. Der ursprüngliche zusammenhängende 60/20/20-Phasensplit machte aus dem vorgesehenen Provenance-Test teilweise eine starke Phasenextrapolationsaufgabe: Training auf den ersten 60 % der Orbitphase, Test auf einem späteren zusammenhängenden Bereich.

MU1/MU2-Rollouts wurden deshalb nicht als Provenance-Evidenz interpretiert; sie zeigten vor allem Surrogat-/OOD-Fehlerakkumulation.

## 12. v0.2 — Resolvability Repair

D013 akzeptiert einen separat preregistrierten v0.2-Test. Er vergrößert nicht künstlich das Teacher-Signal und führt keinen Architektur-Sweep durch. Geändert werden nur zwei Punkte:

### Phase-stratifizierter Blocksplit

Die 1000 Phasenpunkte werden in 200 zusammenhängende Fünferblöcke geteilt. Ein deterministischer Fünferzyklus weist 60 % der Blöcke Training, 20 % Validation und 20 % Test zu. Damit decken alle Splits die gesamte Figure-eight-Phase ab, ohne einzelne benachbarte Punkte zufällig zu mischen.

Der Test wird ausdrücklich als **same-orbit interpolation/provenance test** interpretiert, nicht als neue-Orbit-Generalisation.

### Gemeinsamer Target-Scaler

Die Trainingstargets beider Teacher werden gemeinsam und ausschließlich auf dem Trainingssplit skaliert. Beide Modelle verwenden denselben Target-Scaler. Alle wissenschaftlichen Metriken und die Provenance-Zerlegung werden nach Rücktransformation in Rohkoordinaten berechnet.

Das entscheidende Gate bleibt:

```text
median_seed(RMSE_own_teacher_test) < D_teacher_test.
```

Scheitert auch v0.2 daran, wird nicht automatisch weitergetunt.

## 13. Aktueller Originalitätsstatus

Der gegenwärtige Stand rechtfertigt keine Behauptung, die Trias habe neue numerische oder ML-Credibility-Kategorien erfunden.

Der interessante Restclaim ist vielmehr:

- durchgängige Provenance über analytische, numerische, datenbasierte und lernbasierte Übergänge;
- explizite Lokalisierung, an welchem Übergang eine Annahme, Approximation oder Rechtfertigung entsteht;
- Verknüpfung von formaler Lösbarkeit, operativer Berechenbarkeit und zweckrelativer wissenschaftlicher Nutzung in einem gemeinsamen Audit.

Ob diese Integrationsleistung gegenüber starken bestehenden V&V-, Credibility-, Dataset-Provenance- und Model-Documentation-Ansätzen hinreichend eigenständig ist, bleibt eine offene Forschungsfrage und soll nicht vorzeitig positiv beantwortet werden.

## 14. Besonders offene philosophische Fragen

- Ist „Realität“ als Name des ersten Pols noch sinnvoll, oder sollte die endgültige Terminologie stärker auf „Target/Zielsystem“ setzen?
- Sind die Übergangskanten methodologisch wichtiger als die drei Pole?
- Wann ist eine Integrationsleistung wissenschaftsphilosophisch eigenständig genug, wenn ihre Einzelkomponenten bereits in existierenden Frameworks vorkommen?
- Was zählt als relevante epistemische Provenance in hybriden Simulation-ML-Ketten?
- Wie lässt sich vermeiden, dass ein Audit lediglich zusätzliche Dokumentation produziert, ohne wissenschaftliche Schlussfolgerungen zu verändern?
- Ist ein synthetischer Drei-Körper-Fall ausreichend, oder braucht der spätere Hauptbeitrag zusätzlich einen empirischeren AI-for-Science-Fall?

## 15. Mögliche Rolle einer Kooperationspartnerin

Besonders wertvoll wäre keine primäre Implementierungsrolle, sondern kritische Mitarbeit an:

1. **Begriffsarchitektur:** Target, Theorie, Modell, Simulation, Daten, Surrogat und wissenschaftlicher Gebrauch sauber trennen, ohne künstliche Ontologien zu erzeugen.
2. **Novelty-Stresstest:** Trias systematisch gegen V&V, Credibility, Simulation Philosophy, Model/Dataset Provenance und verwandte Frameworks halten.
3. **Physikalische Relevanz:** entscheiden, welche numerischen/strukturellen Größen wissenschaftlich bedeutsam und welche bloß technische Diagnostik sind.
4. **Interpretation negativer Resultate:** verhindern, dass inconclusive oder negative Tests nachträglich in eine positive Framework-Story umgedeutet werden.
5. **Fallwahl nach v0.2:** beurteilen, ob der Drei-Körper-Fall weiterhin genügend epistemische Spannung trägt oder ein ergänzender empirischer AI-for-Science-Fall nötig wird.

## 16. Nächste Abhängigkeit

Aktuell steht der **ML Implementation Contract v0.2** zur Review. Erst nach Akzeptanz werden Codeänderungen, technische Tests und ein nichtwissenschaftlicher Smoke Run vorgenommen. Danach folgt erneut ein Review vor dem wissenschaftlichen Full Run.

Die Abhängigkeitslogik ist derzeit:

```text
C01–C04
-> numerischer Demonstrator
-> C05
-> harter C06-V&V-Vergleich
-> C06-R
-> ML-Provenance v0.1
-> INCONCLUSIVE_LEARNER_ERROR
-> D013 / v0.2 Resolvability Repair
-> v0.2 Contract Review
-> v0.2 Skeleton
-> v0.2 Full Run
-> erneuter Originalitätstest
-> möglicher C07
```

## 17. Leitidee in einem Satz

> Das Projekt fragt nicht, ob Berechnung oder AI „wichtig“ sind, sondern ob eine explizite Provenance von Zielsystem, Theorie, numerischer Operationalisierung, Daten, gelerntem Modell und wissenschaftlichem Gebrauch Rechtfertigungslücken sichtbar macht und Fehlzuordnungen verhindert, die in aggregierten Erfolgsmetriken leicht verschwinden.

---

**Repository:** `trias-ai-for-science`  
**Arbeitsmodus:** Claims und Demonstratoren werden preregistriert, mit Gates und Revisionskriterien versehen und erst nach explizitem `GO` als aktuelle Forschungsgrundlage akzeptiert. Die Projektregel `PDF` erzeugt aus dem jeweils aktuellen Stand ein neues ausführliches Kooperationsbriefing.