# Minimal ML / AI-for-Science Provenance Demonstrator v0.1

**Status:** PENDING REVIEW  
**Depends on:** D001–D009  
**Purpose:** kleinstmöglicher Test der nach C06-R verbleibenden Integrations-/Provenance-Hypothese  
**Rule:** noch keine Implementierung und kein Architektur-/Performance-Sweep vor Akzeptanz.

## ML-DMO-01 — Wissenschaftliche Leitfrage

> Kann ein gelerntes Surrogat auf üblichen ML-Metriken überzeugend erscheinen, obwohl seine Trainingsziele bereits von einer konkreten numerischen Operationalisierung geprägt sind, und lässt sich die daraus entstehende Rechtfertigungslücke durch eine explizite Provenance-Kette `Zielsystem/Theorie → Datengenerator → Trainingsdaten → Lernmodell → wissenschaftlicher Gebrauch` transparent lokalisieren?

Der Demonstrator soll **nicht** zeigen, dass schlechte Trainingsdaten schlechte Modelle erzeugen. Das wäre trivial. Er soll kontrolliert testen, ob generatorrelative ML-Güte und zielsystemrelative wissenschaftliche Güte auseinanderfallen können und welche zusätzliche Disziplin eine durchgängige Herkunftszuordnung liefert.

## ML-DMO-02 — Kein neues physikalisches Zielsystem

Das synthetische Zielsystem bleibt die bereits akzeptierte planare equal-mass Figure-eight-Konfiguration mit `G=1`, den publizierten gerundeten Anfangsdaten und `T_pub=6.32591398`.

Es wird bewusst **kein** chaotischer oder perturbierter Drei-Körper-Fall ergänzt. Dadurch bleibt die neue Variable des Experiments möglichst isoliert: die zusätzliche Daten-/Lernkette.

## ML-DMO-03 — Zwei kontrollierte Datengeneratoren

Es werden zwei Teacher-/Datengeneratoren verwendet:

1. **Reference teacher `G_ref`:** DOP853 mit der bereits akzeptierten primären Referenzeinstellung; die engere DOP853-Rechnung bleibt Cross-Check und wird nicht als exakte Ground Truth bezeichnet.
2. **Coarse teacher `G_rk4`:** der bereits implementierte klassische RK4 mit einem bewusst gröberen, aber im bisherigen Demonstrator validierten Schritt `h = T_pub/50`.

Es wird kein neuer numerischer Solver eingeführt.

### Kontrollprinzip

Die Eingaben beider Trainingsdatensätze sind **identisch**. Startzustände `x_j` werden aus der DOP853-Referenz entlang einer nominellen Figure-eight-Periode gesampelt. Für jeden identischen Startzustand wird dann ein Schritt der Länge

```text
Delta_t = T_pub / 50
```

mit beiden Teacher-Operationalisierungen erzeugt:

```text
x_j -> y_ref,j
x_j -> y_rk4,j
```

Damit unterscheiden sich die beiden Datensätze ausschließlich in der Herkunft der Trainingslabels, nicht in der Input-Verteilung.

Der primäre Lerngegenstand ist der Zustandsinkrement-Operator

```text
Delta x = y - x.
```

## ML-DMO-04 — Datensatz und Split-Logik

Vorgesehen sind `1000` gleichmäßig über eine nominelle Periode verteilte Startphasen. Die genaue numerische Erzeugung und Cross-Check-Logik wird erst im Implementation Contract eingefroren.

Der Split erfolgt nach **zusammenhängenden Phasenblöcken**, nicht durch zufälliges Mischen einzelner benachbarter Zeitpunkte:

- 60 % Training,
- 20 % Validation,
- 20 % Test.

Damit wird verhindert, dass nahezu identische Nachbarzustände gleichzeitig in Train und Test auftauchen.

Dieser v0.1-Test beansprucht ausdrücklich **keine Generalisierung auf neue Orbits oder neue Anfangsbedingungen**. Er ist ein kontrollierter Provenance-Test auf derselben Zielinstanz.

## ML-DMO-05 — Gelerntes Modell

Es wird genau eine einfache Modellklasse verwendet:

**Residual MLP one-step surrogate**

```text
x_hat_(k+1) = x_k + f_theta(x_k)
```

mit 12-dimensionalem Zustand und 12-dimensionalem Inkrementoutput.

Vorgesehen ist ein kleines vollverbundenes Netz mit identischer Architektur, Normalisierung, Optimierung und Trainingsbudget für beide Teacher-Datensätze. Die exakten Layerbreiten, Aktivierung, Lernrate, Epochenzahl und Early-Stopping-Regel werden erst im Implementation Contract festgelegt.

### Wichtige Kontrollentscheidung

Für jedes Random Seed werden die beiden Modelle mit **identischer Initialisierung** gestartet. Der einzige systematische Unterschied zwischen dem Modellpaar ist der Teacher, dessen Labels gelernt werden.

Minimal `3` Seeds; kein Hyperparameter-Sweep.

## ML-DMO-06 — Kein Physics-Informed Training in v0.1

Nicht verwendet werden:

- PINN-Loss;
- Hamiltonian Neural Network;
- Neural ODE;
- Symplectic Network;
- explizite Energie-/Drehimpulsregularisierung;
- Multi-step training loss.

Begründung: Der erste Test soll die Provenance des Datengenerators isolieren. Eine physikalische Induktionsbias würde eine zweite methodologische Variable einführen.

## ML-DMO-07 — Zwei Arten von ML-Güte

Der zentrale Audit-Kontrast ist die Trennung von **generatorrelativer** und **ziel-/referenzrelativer** Bewertung.

### A. Generatorrelative Güte

Für jedes Modell wird auf seinem eigenen Testdatensatz gemessen:

```text
MSE_own_teacher
```

Frage:

> Wie gut reproduziert das Netz genau den numerischen Teacher, von dem seine Labels stammen?

### B. Gemeinsame Referenzbewertung

Beide Modelle werden auf denselben gehaltenen Testinputs zusätzlich gegen `G_ref` bewertet:

```text
MSE_vs_ref
```

Für das RK4-trainierte Modell wird zusätzlich dokumentiert:

```text
MSE_vs_rk4_teacher
MSE_vs_ref
```

Dadurch wird sichtbar, ob ein Modell einen numerischen Teacher gut approximiert, ohne im gleichen Maß die stärkere numerische Referenz zu approximieren.

## ML-DMO-08 — Rollout-Gebrauchsfragen

Ein One-Step-MSE ist nicht die wissenschaftliche Zielgröße des Surrogats. Deshalb werden zwei einfache Verwendungen definiert.

### MU1 — one-period surrogate use

> Kann das Surrogat aus dem publizierten Anfangszustand eine nominelle Periode lang als Ersatz für den numerischen Fluss verwendet werden?

Rollout:

```text
50 learned steps = 1*T_pub
```

Primäre Auswertung:

- normalisierter Positionsfehler gegen DOP853-Referenz;
- Energiefehler;
- Drehimpulsfehler.

### MU2 — short long-horizon use

> Wie verändert sich das wissenschaftlich relevante Profil bei wiederholter Anwendung des gelernten diskreten Operators?

Rollout:

```text
500 learned steps = 10*T_pub
```

MU2 ist bewusst deutlich kürzer als der numerische U2-100-Perioden-Test. Ziel ist nicht ein Langzeit-ML-Benchmark, sondern die Sichtbarkeit von Fehlervererbung und Akkumulation.

## ML-DMO-09 — Pairwise-Provenance-Diagnostik

Für jeden Seed werden die beiden Modelle als Paar ausgewertet:

```text
same inputs
same split
same architecture
same initialization
same optimizer/budget
only teacher labels differ
```

Zusätzlich wird die direkte Teacher-Differenz

```text
||y_rk4 - y_ref||
```

auf Train/Validation/Test dokumentiert.

Damit entsteht eine kontrollierte Kette:

```text
Teacher difference
    -> label difference
    -> learned-model difference
    -> rollout/scientific-use difference
```

Diese Kette ist der eigentliche Gegenstand des Experiments.

## ML-DMO-10 — Baseline-ML-View versus Trias-Provenance-View

Jeder Lauf wird zweimal interpretiert.

### Baseline ML view

- train/validation/test loss;
- own-teacher test MSE;
- eventuell one-period rollout error;
- Seed-Streuung.

### Trias provenance view

Zusätzlich explizit:

1. Was ist das synthetische Zielsystem?
2. Welche theoretische Dynamik wird vorausgesetzt?
3. Welcher numerische Datengenerator erzeugt die Labels?
4. Welche numerischen Approximationseigenschaften dieses Teachers können in die Daten eingehen?
5. Welche Relation wird mit `test MSE` tatsächlich validiert: `ML ↔ Teacher` oder `ML ↔ Zielsystem`?
6. Welche Struktur geht im Schritt `Theorie → Simulation → Daten → ML` verloren oder bleibt nur indirekt geprüft?
7. Welcher wissenschaftliche Schluss ist für MU1/MU2 tatsächlich gerechtfertigt?

Die Trias darf dabei nicht behaupten, Dataset Provenance oder Model Cards erfunden zu haben. Getestet wird die **durchgängige Verknüpfung** der Ebenen.

## ML-DMO-11 — Minimal positiver Befund

Der Demonstrator ist für die Integrationshypothese informativ, wenn mindestens eines der folgenden robust über Seeds auftritt:

1. Beide Modelle haben gute bzw. ähnliche own-teacher Testfehler, unterscheiden sich aber deutlich in `MSE_vs_ref` oder Rollout-/Strukturmetriken.
2. Das RK4-trainierte Modell reproduziert `G_rk4` klar besser als `G_ref`, sodass eine niedrige Test-MSE ohne Teacher-Provenance eine zu starke Aussage über das Zielsystem nahelegen würde.
3. Eine Rangfolge nach One-Step-Test-MSE stimmt nicht mit der Rangfolge für MU1/MU2 überein.
4. Eine beobachtete ML-Abweichung lässt sich quantitativ bis zu einem Teacher-/Label-Unterschied zurückverfolgen, statt unspezifisch als „Modellfehler“ etikettiert zu werden.

Ein positiver Befund stärkt nur den **Provenance-/Integrationsnutzen**. Er beweist noch nicht, dass keine etablierte ML-Credibility-Methode dieselbe Diagnose leisten kann.

## ML-DMO-12 — Negativer Befund

Der Test gilt als negativ oder nicht informativ, wenn beispielsweise:

- die Teacher-Differenz gegenüber der ML-Approximation praktisch irrelevant ist;
- beide Modelle unter gemeinsamer Referenzbewertung ununterscheidbar sind;
- ML-Optimierungsrauschen den Teacher-Effekt dominiert;
- die behauptete Herkunft nicht robust über Seeds ist;
- ein starker Standard-ML-/V&V-Provenance-Audit dieselbe Zuordnung ebenso transparent liefert und die Trias keine zusätzliche Integrationsdisziplin demonstriert.

Ein negatives Ergebnis führt zu keiner nachträglichen Erweiterung des Sweeps, nur um einen positiven Effekt zu erzeugen.

## ML-DMO-13 — Scope Freeze

Nicht Bestandteil von v0.1:

- neue Anfangsbedingungsfamilien;
- chaotische Generalisierung;
- Architekturvergleich;
- Hyperparameteroptimierung;
- Physics-informed Losses;
- symplektische NNs;
- probabilistische UQ;
- externe/experimentelle Daten;
- Vergleich vieler Teacher-Solver;
- Behauptung eines allgemein besseren ML-Modells.

## Kandidat für einen späteren Claim

Noch **nicht akzeptiert**:

> Gute ML-Güte relativ zu simulationsgenerierten Trainingslabels rechtfertigt nicht automatisch eine gleich starke Aussage über das wissenschaftliche Zielsystem; die epistemische Bewertung eines Surrogats muss die Provenance des Datengenerators berücksichtigen.

Ob dieser Satz im Projekt einen eigenständigen Trias-Beitrag oder nur etablierte Dataset-/Model-Credibility-Prinzipien ausdrückt, wird erst nach dem Experiment entschieden.

## Entscheidungsempfehlung

Akzeptiere den Minimal ML Epistemic Demonstrator v0.1 mit:

- unverändertem Figure-eight-Zielsystem;
- zwei Teachers `DOP853` und `RK4 h=T_pub/50`;
- identischen Inputzuständen und nur unterschiedlichen Labels;
- einem einfachen Residual-MLP;
- drei gepaarten Seeds;
- eigener Teacher-MSE versus gemeinsamer Referenzbewertung;
- MU1 = 1 Periode und MU2 = 10 Perioden;
- explizitem Baseline-ML-vs.-Trias-Provenance-Vergleich.

Nach Akzeptanz folgt **noch kein Training**, sondern ein kleiner ML Implementation Contract mit exakten Netzwerk-, Split-, Optimierungs-, Normalisierungs-, Seed- und Gate-Definitionen.