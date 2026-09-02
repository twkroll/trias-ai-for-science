# C06 — Zusätzlicher diagnostischer Wert des Trias-Audits

**Status:** PENDING REVIEW — STRONG FORM NOT SUPPORTED  
**Evidence status:** direkter Vergleich mit etablierter numerischer Analysis, V&V/Credibility und Simulationsphilosophie spricht gegen eine starke Neuheitsbehauptung im reinen Solverfall  
**Stand:** 2026-09-02

## Ausgangsform / starke Fassung

Die ursprünglich intendierte starke Fassung war sinngemäß:

> Der Trias-Audit liefert gegenüber gewöhnlicher numerischer Analysis und Verification & Validation zusätzliche Fehlerzuordnungen oder Validierungsfragen, die für die wissenschaftliche Interpretation des Drei-Körper-Demonstrators wesentlich sind.

Diese starke Fassung wird auf Basis des aktuellen Vergleichs **nicht zur Akzeptanz empfohlen**.

## Warum die starke Fassung unter Druck steht

Etablierte V&V- und Credibility-Frameworks decken bereits zentrale Punkte ab, die der Trias-Demonstrator sichtbar macht:

- Code Verification: implementiert der Code den vorgesehenen Algorithmus korrekt?
- Solution Verification: ist der Diskretisierungs-/numerische Fehler ausreichend kontrolliert?
- Validation bzw. Credibility relativ zum intended/proposed use;
- Sensitivität und Unsicherheit;
- Modellannahmen, Abstraktionen und zulässige Nutzungen;
- Dokumentation der Evidenz, Grenzen und Risiken eines M&S-Ergebnisses.

Auch die Simulationsphilosophie behandelt Computer-Simulationen nicht bloß als Theorie–Experiment-Brücke. Breite Simulation-Study-Ansätze umfassen Modellwahl, Implementierung, Rechner, Interpretation und Rechtfertigung von Schlüssen; die Zuverlässigkeit wird explizit relativ zum intended purpose diskutiert.

Damit sind die numerischen C05-Befunde — Refinement, Referenzunsicherheit, Invariantenerhaltung, Drift, Ressourcen und Use-Case-Abhängigkeit — mit etabliertem V&V-/Numerik-Vokabular vollständig beschreibbar.

## Was die Trias im aktuellen Fall dennoch leistet

Der derzeit belegbare Mehrwert ist schwächer und eher **integrativ/organisatorisch**:

1. Sie erzwingt eine gemeinsame Darstellung von Zielsystem, Theorie und konkreter Berechnung, statt Validierung erst auf der Ebene eines fertigen Simulationsmodells zu beginnen.
2. Sie macht die Übergangskanten explizit: Zielsystem↔Theorie, Theorie↔Berechnung, Berechnung↔Zielsystem.
3. Sie verbindet den historischen Sundman-Fall — analytische Repräsentierbarkeit ohne operative Traktabilität — mit der späteren numerischen Operationalisierung in einem gemeinsamen Schema.
4. Sie zwingt dazu, eine Abweichung zunächst nach ihrer epistemischen Herkunft zu lokalisieren, bevor sie als „Modellfehler“, „numerischer Fehler“ oder „mangelnde wissenschaftliche Nutzbarkeit“ etikettiert wird.

Diese Punkte sind jedoch derzeit am besten als **Synthesis/Mapping-Vorteil**, nicht als neu entdeckte Validierungsdimensionen, formulierbar.

## Empfohlene revidierte Claim-Fassung C06-R

> Im gegenwärtigen Drei-Körper-Demonstrator erzeugt der Trias-Audit keine eindeutig neuen numerischen Validierungsfragen gegenüber etablierter numerischer Analysis und Verification & Validation. Sein derzeit belegbarer methodologischer Mehrwert liegt vielmehr in einer expliziten, durchgängigen Zuordnung von Annahmen, Transformationen und Rechtfertigungsanforderungen zu Zielsystem, Theorie, Berechnung und ihren Übergängen. Diese Integrationsleistung verbindet insbesondere formale bzw. analytische Verfügbarkeit mit operativer Berechnung und zweckrelativer wissenschaftlicher Nutzung. Ob diese Integrationsleistung einen hinreichend eigenständigen Beitrag für AI for Science darstellt, muss an einem Fall mit zusätzlicher daten- bzw. lernbasierter Ebene weiter geprüft werden.

## Status der einzelnen Teile

### Gut gestützt

- Standard-Numerik/V&V kann die C05-Ergebnisse bereits diagnostizieren.
- intended use, verification, uncertainty/sensitivity und Ergebnis-Credibility sind etablierte Bestandteile einschlägiger Frameworks.
- eine starke Aussage „Trias entdeckt neue Validierungsfragen“ wäre im aktuellen Fall überzogen.

### Projektinterne Interpretation

- die Trias besitzt einen nützlichen Integrations-/Provenance-Vorteil;
- die explizite Kantenstruktur erleichtert die Lokalisierung epistemischer Übergänge;
- Sundman + numerischer Demonstrator bilden zusammen einen breiteren methodologischen Bogen als ein isolierter V&V-Solververgleich.

Diese Interpretation ist plausibel, aber noch nicht stark genug, um allein eine große Originalitätsbehauptung zu tragen.

## Explizite Nicht-Claims

C06-R behauptet nicht:

- dass V&V Implementierungsdetails oder intended use ignoriert;
- dass die Trias neue numerische Fehlertypen entdeckt;
- dass NASA-/ASME-/AIAA-artige Credibility-Frameworks unzureichend sind;
- dass eine Dreiecksvisualisierung allein wissenschaftliche Originalität begründet;
- dass der reine Figure-eight-Solverfall bereits einen eigenständigen AI-for-Science-Beitrag demonstriert;
- dass eine spätere ML-Erweiterung zwangsläufig einen positiven Neuheitsbefund liefern wird.

## Revisions-/Widerlegungskriterium

Auch C06-R muss weiter abgeschwächt werden, wenn eine detailliertere Framework-Literatur zeigt, dass selbst die behauptete Integrations-/Mapping-Leistung bereits ohne relevante Differenz in etablierten Credibility- oder Simulation-Study-Schemata enthalten ist.

Umgekehrt kann C06 später stärker werden, wenn ein AI-for-Science-Fall zeigt, dass die explizite Trennung von physikalischem/synthetischem Ziel, theoretischer Struktur, simulationsgenerierten Daten, gelerntem Modell und Ausführungsartefakten eine konkrete Fehlzuordnung oder ungerechtfertigte Schlussfolgerung verhindert, die ein Standard-Audit nicht ebenso transparent lokalisiert.

## Entscheidungsempfehlung

**REVISE, nicht die starke Form akzeptieren.**

Empfohlen wird, C06-R als aktuelle Arbeitsfassung zu akzeptieren und die starke Form explizit zu verwerfen. Danach sollte ein minimaler ML/AI-for-Science-Kontrast spezifiziert werden, dessen einziger Zweck darin besteht, die verbleibende Integrationshypothese zu testen — nicht den Scope beliebig zu erweitern.