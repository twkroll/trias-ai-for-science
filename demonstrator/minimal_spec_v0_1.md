# Minimal Demonstrator Specification v0.1

**Status:** PENDING REVIEW  
**Purpose:** kleinstmöglicher rechnerischer Test, ob die Trias mehr leistet als ein eindimensionaler Solververgleich  
**No implementation before acceptance.**

## DMO-01 — Wissenschaftliche Leitfrage

> Können bei identischem synthetischem Zielsystem, identischer Newtonscher Theorie und identischen Anfangsdaten unterschiedliche numerische Operationalisierungen verschiedene epistemische Profile erzeugen, so dass die Beurteilung eines Outputs vom wissenschaftlichen Zweck und nicht nur von einem einzelnen Trajektorienfehler abhängt?

Der Demonstrator soll **nicht** zeigen, dass numerische Verfahren unterschiedliche Fehler besitzen. Das ist bekannt. Er soll prüfen, ob die explizite Trennung von Zielsystem, Theorie, Implementierung und wissenschaftlichem Gebrauch eine präzisere Diagnose erzwingt.

## DMO-02 — Synthetisches Zielsystem

Empfohlen wird zunächst die planare gleichmassige Figure-eight-Lösung des Newtonschen Drei-Körper-Problems in dimensionslosen Einheiten (`G = 1`, `m_1=m_2=m_3=1`).

Begründung:

- kollisionsfrei im betrachteten Referenzregime;
- periodisch und strukturell reich genug für Langzeitvergleiche;
- kein chaotisches Regime als primäre Konfundierung;
- erlaubt die Trennung von algorithmischem Fehler und dynamischer Sensitivität;
- bekannte Anfangsdaten können später quellengeprüft übernommen werden.

Die exakten Anfangsdaten und die Periodendauer werden erst nach Quellenprüfung eingefroren.

## DMO-03 — Zwei wissenschaftliche Gebrauchsfragen

Um Zweckrelativität testbar zu machen, werden zwei minimale Use Cases unterschieden:

### U1 — Kurzfristige Trajektorienfrage

> Wie genau reproduziert der Solver die Referenzpositionen über einen begrenzten Zeithorizont?

Primäre Metrik: Trajektorienfehler gegenüber hochgenauer Referenz.

### U2 — Langfristige Strukturfrage

> Wie zuverlässig repräsentiert der Solver über viele Perioden zentrale theoretische Strukturen des gebundenen Systems?

Primäre Metriken: Energiefehler/-drift und qualitative Bahnstabilität; Drehimpuls wird als Kontrollinvariante geführt.

Ein diagnostisch interessantes Ergebnis liegt vor, wenn die Solverbewertung für U1 und U2 nicht identisch ist oder wenn ein einzelner Trajektorienfehler relevante Strukturunterschiede verdeckt.

## DMO-04 — Numerische Verfahren

Minimal drei Rollen:

1. **Referenz:** DOP853 oder vergleichbarer adaptiver Hochordnungs-Solver mit strengen Toleranzen.
2. **Baseline:** klassischer fester RK4.
3. **Strukturerhaltender Kontrast:** Velocity-Verlet / Leapfrog oder äquivalenter symplektischer Splitting-Integrator für den separablen Hamiltonian.

Kein ML-Modell in v0.1.

## DMO-05 — Referenzlogik

Die Referenz wird nicht als exakt bezeichnet.

Sie muss mindestens durch zwei der folgenden Checks abgesichert werden:

- strengere Toleranzstufe desselben Solvers;
- zweiter hochwertiger adaptiver Solver;
- Übereinstimmung zentraler Invarianten;
- interne Schrittverfeinerung.

Die Referenz ist ein **provisorisch stärker gerechtfertigter Rechenoutput**, nicht das synthetische Zielsystem selbst.

## DMO-06 — Minimale Metriken

Pflichtmetriken:

1. zeitabhängiger Trajektorienfehler gegen Referenz;
2. absoluter/skalierter Energiefehler und Driftcharakter;
3. Drehimpulsfehler als Invariantenkontrolle;
4. Schrittweiten-/Verfeinerungsstudie;
5. Laufzeit oder Zahl der Kraftauswertungen als Ressourcenindikator.

Nicht in v0.1: große Hyperparametersweeps, ML-Metriken, Unsicherheitsmodelle, umfassende Phasenraumstatistik.

## DMO-07 — Trennung Systemsensitivität vs. Numerik

Die erste Fallstudie verwendet bewusst ein reguläres/periodisches Regime. Dadurch soll vermieden werden, dass unterschiedliche Solvertrajektorien vorschnell mit chaotischer Sensitivität erklärt werden.

Ein sensitiver oder chaotischer zweiter Fall wird nur ergänzt, wenn der reguläre Fall nicht ausreicht oder wenn später C05/C06 explizit eine Sensitivitätsdiagnose benötigt.

## DMO-08 — Vergleichslogik

Der Demonstrator erzeugt zwei Ebenen der Auswertung:

### Baseline-Auswertung

- Trajektorienfehler;
- Laufzeit.

### Trias-Auswertung

Zusätzlich:

- welche theoretische Struktur wird erhalten/verletzt? (`T → C`)
- wie robust ist der Output gegenüber numerischer Verfeinerung? (`C → Zielsystem`)
- für welchen wissenschaftlichen Use Case ist der Output hinreichend gerechtfertigt?
- welche Abweichungen sind dem Zielproblem, der Theorie oder der Implementierung zuzuordnen?

Damit wird explizit geprüft, ob die Trias nur Metriken sammelt oder tatsächlich die Interpretation verändert.

## DMO-09 — Erfolgskriterium

### Minimaler positiver Befund

Der Demonstrator gilt als informativ, wenn mindestens eines der folgenden Muster robust auftritt:

1. Solver A ist nach kurzfristigem Trajektorienfehler besser, Solver B aber nach langfristiger Strukturerhaltung;
2. eine scheinbare Solver-Rangfolge ändert sich nach Schrittverfeinerung oder Ressourcenvergleich;
3. ein Rechenoutput sieht nach einer Standardmetrik gut aus, trägt aber einen spezifizierten wissenschaftlichen Schluss nicht;
4. die Trias-Auditfragen lokalisieren eine Annahme oder einen Verlust an einer konkreten Kante, die in der Baseline-Auswertung nicht explizit erscheint.

### Negativer Befund

Wenn alle relevanten Unterschiede vollständig durch gewöhnliche numerische Fehleranalyse/V&V beschrieben werden und die Trias keine zusätzliche Diagnose oder Interpretationsdisziplin erzeugt, wird dies als negatives Ergebnis für den Eigenständigkeitsanspruch dokumentiert.

## DMO-10 — Scope Freeze für v0.1

Nicht Bestandteil der ersten Implementierung:

- chaotischer Benchmark;
- Sundman-Reihe numerisch auswerten;
- ML-Surrogat;
- PINN/HNN/Neural ODE;
- umfassende Anfangsdatenfamilien;
- astrophysikalische Realitätsnähe;
- relativistische Korrekturen;
- Kollisionsregularisierung.

## Entscheidungsempfehlung

Akzeptiere v0.1 als Minimaldesign mit **Figure-eight + DOP853 + RK4 + symplektischem Kontrast + zwei Use Cases**.

Nach Akzeptanz folgt noch keine große Implementierung. Der nächste Schritt ist ein **Implementation Contract**: exakte Anfangsdaten, Zeithorizont, Toleranzen, Schrittweiten, Ausgabedateien und Tests werden eingefroren.