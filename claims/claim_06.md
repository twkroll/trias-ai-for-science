# C06 — Zusätzlicher diagnostischer Wert des Trias-Audits

**Status:** ACCEPTED IN REVISED FORM — D009  
**Strong form:** REJECTED / NOT SUPPORTED in the pure solver case  
**Evidence status:** direkter Vergleich mit etablierter numerischer Analysis, V&V/Credibility und Simulationsphilosophie spricht gegen eine starke Neuheitsbehauptung im reinen Solverfall  
**Stand:** 2026-09-02

## Verworfene starke Fassung

Die ursprünglich intendierte starke Fassung war sinngemäß:

> Der Trias-Audit liefert gegenüber gewöhnlicher numerischer Analysis und Verification & Validation zusätzliche Fehlerzuordnungen oder Validierungsfragen, die für die wissenschaftliche Interpretation des Drei-Körper-Demonstrators wesentlich sind.

Diese starke Fassung wird nach dem direkten Vergleich **nicht akzeptiert**.

## Akzeptierte revidierte Fassung C06-R

> Im gegenwärtigen Drei-Körper-Demonstrator erzeugt der Trias-Audit keine eindeutig neuen numerischen Validierungsfragen gegenüber etablierter numerischer Analysis und Verification & Validation. Sein derzeit belegbarer methodologischer Mehrwert liegt vielmehr in einer expliziten, durchgängigen Zuordnung von Annahmen, Transformationen und Rechtfertigungsanforderungen zu Zielsystem, Theorie, Berechnung und ihren Übergängen. Diese Integrationsleistung verbindet insbesondere formale bzw. analytische Verfügbarkeit mit operativer Berechnung und zweckrelativer wissenschaftlicher Nutzung. Ob diese Integrationsleistung einen hinreichend eigenständigen Beitrag für AI for Science darstellt, muss an einem Fall mit zusätzlicher daten- bzw. lernbasierter Ebene weiter geprüft werden.

## Warum die starke Fassung verworfen wird

Etablierte V&V- und Credibility-Frameworks decken bereits zentrale Punkte ab, die der Trias-Demonstrator sichtbar macht:

- Code Verification;
- Solution Verification;
- Validation/Credibility relativ zum intended use;
- Sensitivität und Unsicherheit;
- Modellannahmen, Abstraktionen und zulässige Nutzungen;
- Dokumentation von Evidenz, Grenzen und Risiken eines M&S-Ergebnisses.

Auch die Simulationsphilosophie behandelt Computer-Simulationen nicht bloß als Theorie–Experiment-Brücke. Die C05-Befunde — Refinement, Referenzunsicherheit, Invariantenerhaltung, Drift, Ressourcen und Use-Case-Abhängigkeit — sind mit etabliertem V&V-/Numerik-Vokabular vollständig beschreibbar.

## Der akzeptierte Restmehrwert

Der derzeit belegbare Mehrwert ist integrativ/organisatorisch:

1. gemeinsame Darstellung von Zielsystem, Theorie und konkreter Berechnung;
2. explizite Zuordnung von Annahmen und Verlusten zu den Übergangskanten;
3. Verbindung des Sundman-Falls — analytische Repräsentierbarkeit ohne operative Traktabilität — mit numerischer Operationalisierung und wissenschaftlichem Gebrauch;
4. epistemische Provenance: eine Abweichung soll zunächst nach ihrer Herkunft lokalisiert werden, bevor sie als Modellfehler, numerischer Fehler oder mangelnde wissenschaftliche Nutzbarkeit etikettiert wird.

Diese Punkte gelten als **Synthesis/Mapping-Vorteil**, nicht als neu entdeckte Validierungsdimensionen.

## Explizite Nicht-Claims

C06-R behauptet nicht:

- dass V&V Implementierungsdetails oder intended use ignoriert;
- dass die Trias neue numerische Fehlertypen entdeckt;
- dass etablierte Credibility-Frameworks unzureichend sind;
- dass eine Dreiecksvisualisierung allein wissenschaftliche Originalität begründet;
- dass der reine Figure-eight-Solverfall bereits einen eigenständigen AI-for-Science-Beitrag demonstriert;
- dass eine ML-Erweiterung zwangsläufig einen positiven Neuheitsbefund liefern wird.

## Revisions-/Widerlegungskriterium

C06-R muss weiter abgeschwächt werden, wenn eine detailliertere Framework-Literatur zeigt, dass auch die behauptete Integrations-/Mapping-Leistung ohne relevante Differenz bereits in etablierten Credibility- oder Simulation-Study-Schemata enthalten ist.

C06-R kann später nur dann gestärkt werden, wenn ein AI-for-Science-Fall zeigt, dass die explizite Trennung von Zielsystem, theoretischer Struktur, simulationsgenerierten Daten, gelerntem Modell und Ausführungsartefakten eine konkrete Fehlzuordnung oder ungerechtfertigte Schlussfolgerung verhindert oder transparent lokalisiert.

## Nächste Abhängigkeit

Nach D009 wird ein **minimaler ML/AI-for-Science-Provenance-Demonstrator** spezifiziert. Sein einziger Zweck ist, die verbleibende Integrationshypothese zu testen; er ist kein Performance- oder Architekturprojekt.