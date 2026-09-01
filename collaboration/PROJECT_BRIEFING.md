# Projektbriefing: Trias — Realität, Theorie, Berechnung

**Zielgruppe:** promovierte Physikerin mit wissenschaftsphilosophischem Hintergrund  
**Status:** internes Diskussions- und Einladungsdokument  
**Projektphase:** Woche 1 — Claim and Scope  
**Stand:** 2026-09-01

## 1. Worum es in dem Projekt geht

Das Projekt untersucht, ob die Trias **Realität — Theorie — Berechnung/Umsetzung** als methodologisches Audit-Framework für Computational Science und AI for Science einen eigenständigen diagnostischen Nutzen besitzt.

Die Ausgangsidee ist bewusst moderat. Es wird **nicht** behauptet, Wissenschaft bestehe ontologisch aus drei klar getrennten Sphären, und ebenso wenig, dass die Wissenschaftsphilosophie die epistemische Rolle von Modellen, Simulationen oder Berechnung bislang übersehen habe. Der mögliche Beitrag liegt vielmehr darin, einschlägige Einsichten in ein explizites Audit-Schema zu überführen, das für konkrete computational-science-Ergebnisse getrennt fragt:

1. Was wird über das Zielsystem vorausgesetzt?
2. Was wird durch die Theorie tatsächlich lizenziert?
3. Was entsteht erst durch die operative Umsetzung?
4. Welche Annahmen oder Verluste treten an den Übergängen zwischen diesen Rollen auf?

Das **Newtonsche Drei-Körper-Problem** dient als primärer Leitfall. Es ist methodologisch attraktiv, weil die physikalisch-mathematische Struktur explizit festgelegt werden kann, während analytische Repräsentation, praktische Auswertbarkeit, numerische Approximation und wissenschaftliche Nutzbarkeit dennoch auseinanderfallen können.

## 2. Der derzeit akzeptierte Kern

### Claim 1 — diagnostischer Mehrwert

> Im Drei-Körper-Fall kann die explizite Trennung von Zielsystem, theoretischer Beschreibung und operativer Umsetzung diagnostische Unterschiede sichtbar machen, die in einer bloßen Theorie–Experiment-Beschreibung unterbestimmt bleiben. Der beanspruchte Mehrwert besteht nicht darin, Berechnung erstmals als epistemisch relevante Praxis zu identifizieren, sondern darin, entsprechende Einsichten in ein explizites Audit-Schema zu überführen.

Diese Aussage ist als Forschungsgrundlage akzeptiert, aber noch nicht endgültig bewiesen. Sie muss durch Literaturvergleich und Demonstrator bestätigt werden.

### Claim 2 — synthetisches Zielsystem

Der Realitäts-Pol wird im Audit funktional als Rolle des **Zielsystems** verstanden. Im Drei-Körper-Fall kann diese Rolle durch ein explizit konstruiertes **synthetisches Zielsystem** eingenommen werden: eine konkrete Instanziierung der idealisierten Newtonschen Dynamik mit festgelegtem Zustandsraum, Parametern und Anfangsbedingungen.

Wichtig ist dabei:

- Das Zielsystem ist durch Theorie mitkonstituiert.
- Theorie und Zielsystem müssen deshalb nicht ontologisch unabhängig sein.
- Sie erfüllen dennoch verschiedene Audit-Funktionen.
- Eine numerisch erzeugte Trajektorie ist nicht mit diesem Zielsystem identisch, sondern eine konkrete operative Repräsentation bzw. Approximation.

Der technische Begriff **„synthetisches Zielsystem“** wird gegenüber „synthetischer Realität“ bevorzugt; „synthetische Modellwelt“ kann erläuternd verwendet werden.

## 3. Warum gerade das Drei-Körper-Problem?

Der Leitfall erlaubt eine ungewöhnlich kontrollierte Trennung verschiedener Ebenen, die im Wort „Lösung“ leicht zusammenfallen:

1. Festlegung eines physikalischen oder synthetischen Systems,
2. theoretische Gleichungen und Struktur,
3. formale analytische Resultate,
4. konvergente Reihendarstellungen,
5. praktische Evaluierbarkeit dieser Darstellungen,
6. numerische Integration,
7. Vorhersage- und Validierungsfragen,
8. optional später ein ML-Surrogat.

Besonders wichtig ist Sundmans Reihenlösung. Der relevante Punkt soll gerade **nicht** lauten, dass die Reihe „nicht konvergiert“. Zu prüfen ist präzise, unter welchen Voraussetzungen eine global konvergente Darstellung in einer regularisierten Variablen existiert und warum diese dennoch für praktische Bahnberechnungen keine geeignete operative Lösung darstellt. Dieser historische und mathematische Claim ist die nächste offene Evidenzaufgabe des Projekts.

## 4. Die drei Audit-Kanten

Der gegenwärtige Schwerpunkt liegt weniger auf den drei Substantiven als auf den Übergängen zwischen ihnen.

### Realität/Zielsystem ↔ Theorie

Welche Eigenschaften des intendierten Systems sind tatsächlich durch die theoretische Modellierung festgelegt, und welche werden durch Idealisierung ausgeschlossen oder stillschweigend vorausgesetzt?

### Theorie ↔ Berechnung

Welche theoretischen Strukturen bleiben bei der Operationalisierung erhalten, welche werden nur approximiert und welche gehen verloren? Im Drei-Körper-Fall betrifft dies beispielsweise Erhaltungsgrößen, kontinuierliche Zeitstruktur und qualitative Hamiltonsche Eigenschaften.

### Berechnung ↔ Realität/Zielsystem

Welche Evidenz rechtfertigt die Interpretation eines endlichen Rechenoutputs als verlässliche Aussage über das intendierte Zielsystem? Hier treten Solverwahl, Schrittweite, Präzision, Referenzkonstruktion, Robustheit und später gegebenenfalls Trainingsverteilung in den Vordergrund.

## 5. Geplanter Minimaldemonstrator

Der Demonstrator soll ausdrücklich **kein neues Lösungsverfahren für das Drei-Körper-Problem** entwickeln und zunächst auch kein großes ML-Projekt werden.

Die kleinste geplante Version verwendet ein kollisionsfreies planares, dimensionsloses Drei-Körper-System und vergleicht:

- eine hochgenaue adaptive Integration als vorläufige Referenz,
- eine einfache Fixed-Step-Baseline wie RK4,
- ein strukturerhaltendes Verfahren, etwa aus der Klasse symplektischer Integratoren.

Gemessen werden zunächst nur Trajektorienabweichung, Energie- und Drehimpulsdrift, Schrittweitensensitivität und Laufzeit. Die Referenz selbst soll durch Toleranzvariation oder einen zweiten hochwertigen Solver kreuzgeprüft werden.

Der entscheidende Erfolgstest ist nicht, ob Solver unterschiedliche Fehler besitzen — das wäre trivial. Relevant wäre erst ein Fall, in dem die Trias eine **spezifischere wissenschaftliche Diagnose oder Validierungsanforderung** erzeugt als die bloße Feststellung eines numerischen Fehlers.

## 6. Was philosophisch offen ist

Mehrere Punkte sind ausdrücklich noch nicht entschieden:

- Ist die Dreiteilung als Audit tatsächlich heuristisch produktiver als etablierte Begriffe aus Modell-, Simulations- und Fehlerphilosophie?
- Ist „Realität“ als Name des ersten Pols sinnvoll, wenn im kontrollierten Leitfall ein theoriegeprägtes synthetisches Zielsystem untersucht wird?
- Sind die drei Kanten methodologisch tragfähiger als die drei Pole selbst?
- Wie stark muss ein Audit über existierende Reproduzierbarkeits-, Validierungs- und UQ-Schemata hinausgehen, um einen eigenständigen Beitrag zu leisten?
- Was genau ist bei einem computational-science-Ergebnis die relevante epistemische Einheit: einzelne Trajektorie, qualitative Struktur, Invariantenerhaltung, Ensembleeigenschaft oder wissenschaftlicher Gebrauch?

Das Projekt ist so angelegt, dass ein negatives Ergebnis zulässig ist. Falls die Trias nur vorhandene Kategorien neu etikettiert, muss der zentrale Claim abgeschwächt oder aufgegeben werden.

## 7. Wo eine wissenschaftsphilosophisch geschulte Physikerin besonders wichtig wäre

Die gewünschte Rolle wäre nicht primär „zusätzliche Implementierung“, sondern kritische Mitentwicklung an der Physik–Philosophie-Schnittstelle. Besonders wertvoll wären Beiträge zu vier Punkten:

1. **Begriffsprüfung:** Sind Zielsystem, Theorie, Modell, Simulation und Implementierung sauber genug getrennt, ohne künstliche Ontologien zu erzeugen?
2. **Novelty-Stresstest:** Wo reproduziert die Trias bekannte Argumente aus Modell- und Simulationsphilosophie, und wo könnte tatsächlich ein auditierbarer Mehrwert entstehen?
3. **Physikalische Relevanz:** Welche numerischen Unterschiede sind wissenschaftlich relevant und welche lediglich technisch? Welche Invarianten oder qualitativen Strukturen sollten im Leitfall Priorität besitzen?
4. **Interpretation des Demonstrators:** Welche Schlussfolgerungen sind aus Solverunterschieden legitim, und wo würde das Projekt zu viel epistemische Bedeutung in normale numerische Analyse hineinlesen?

## 8. Sinnvoller Einstieg in die Zusammenarbeit

Für einen ersten kritischen Einstieg wäre keine vollständige Literaturrecherche nötig. Hilfreich wäre zunächst eine Bewertung der folgenden drei Fragen:

**A.** Ist der moderate Claim 1 stark genug, um ein Paper zu tragen, ohne eine überzogene Originalitätsbehauptung zu machen?

**B.** Ist die funktionale Verwendung eines synthetischen Zielsystems als Realitäts-Pol begrifflich vertretbar, oder sollte die Trias terminologisch bereits jetzt verändert werden?

**C.** Welche Art von Befund müsste der Drei-Körper-Demonstrator liefern, damit man wirklich von einem philosophisch-methodologischen Mehrwert und nicht bloß von bekannter numerischer Fehleranalyse sprechen kann?

Eine kritische Antwort auf diese drei Fragen wäre für die aktuelle Projektphase wertvoller als eine breite Mitarbeit an Details.

## 9. Nächste Projektabhängigkeiten

Aktuell sind C01 und C02 als Arbeitsgrundlage akzeptiert. Die nächste Aufgabe ist C03: die genaue historische und mathematische Prüfung von Sundmans Reihenlösung. Danach folgt die präzise begriffliche Trennung von mathematischer Konvergenz, rechnerischer Machbarkeit, numerischer Stabilität und wissenschaftlicher Nutzbarkeit. Erst danach wird der Minimaldemonstrator endgültig spezifiziert.

## 10. Leitidee in einem Satz

> Das Projekt fragt nicht, ob Berechnung „wichtig“ ist, sondern ob die explizite Auditierung von Zielsystem, Theorie, Implementierung und ihren Übergängen wissenschaftliche Begründungslücken sichtbar macht, die sonst leicht als bloße technische Details verschwinden.

---

**Repository:** `trias-ai-for-science`  
**Arbeitsmodus:** Claims werden einzeln ausgearbeitet, evidenziell geprüft, mit Revisionskriterien versehen und erst nach expliziter Entscheidung als aktuelle Forschungsgrundlage akzeptiert.