# D010 — Minimal ML / AI-for-Science Provenance Demonstrator v0.1

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D001–D009

## Entscheidung

Der nächste Test des Trias-Projekts führt genau eine zusätzliche daten-/lernbasierte Übersetzungsebene ein. Das physikalische bzw. synthetische Zielsystem bleibt unverändert; getestet wird die Kette

`Zielsystem/Theorie → numerischer Datengenerator → Trainingsdaten → gelerntes One-Step-Surrogat → wissenschaftlicher Gebrauch`.

Der Zweck ist kein ML-Performance-Benchmark, sondern ein kontrollierter Test der nach C06-R verbleibenden Integrations-/Provenance-Hypothese.

## Eingefrorener Scope

- equal-mass Figure-eight als unverändertes synthetisches Zielsystem;
- Reference teacher: DOP853 mit der bereits akzeptierten primären Referenzeinstellung;
- Coarse teacher: klassischer RK4 mit `h = T_pub/50`;
- identische Inputzustände für beide Trainingsdatensätze; nur die Teacher-Labels unterscheiden sich;
- `1000` Startphasen über eine nominelle Periode;
- zusammenhängender 60/20/20 Train/Validation/Test-Split;
- ein Residual-MLP als einzige Modellklasse;
- drei gepaarte Seeds mit identischer Initialisierung innerhalb jedes Teacher-Paares;
- generatorrelative Testgüte versus gemeinsame DOP853-Referenzbewertung;
- MU1 = 50 learned steps = 1 nominelle Periode;
- MU2 = 500 learned steps = 10 nominelle Perioden;
- expliziter Baseline-ML-vs.-Trias-Provenance-Vergleich.

## Mitakzeptierte Grenzen

1. Kein Architektur- oder Hyperparameter-Sweep.
2. Kein PINN/HNN/Neural-ODE/symplektisches Netzwerk und keine Physik-Regularisierung in v0.1.
3. Keine neue Orbit- oder Anfangsbedingungsfamilie.
4. Keine Behauptung von Generalisierung auf neue Orbits.
5. Keine Behauptung, die Trias habe Dataset Provenance, Model Cards oder ML-Credibility erfunden.
6. Ein positiver ML-Befund würde zunächst nur einen Provenance-/Integrationsnutzen stützen; Originalität gegenüber starken bestehenden ML-Credibility-Ansätzen wäre danach separat zu testen.
7. Ein negativer oder nicht informativer Befund bleibt zulässig; der Scope wird nicht nachträglich erweitert, nur um einen positiven Effekt zu erzeugen.

## Noch nicht akzeptierter Claim-Kandidat

> Gute ML-Güte relativ zu simulationsgenerierten Trainingslabels rechtfertigt nicht automatisch eine gleich starke Aussage über das wissenschaftliche Zielsystem; die epistemische Bewertung eines Surrogats muss die Provenance des Datengenerators berücksichtigen.

Dieser Satz bleibt bis nach dem Experiment ein Testkandidat und ist nicht Bestandteil von D010 als wissenschaftlich bestätigter Claim.

## Revisionsbedingung

D010 wird nur geändert, wenn der ML Implementation Contract einen technischen Widerspruch zur kontrollierten Paarlogik offenlegt oder die Datengenerierung den Teacher-Effekt nicht isolieren kann. Änderungen werden explizit als neue Entscheidung dokumentiert.

## Nächste Abhängigkeit

Vor Implementierung und Training wird ein ML Implementation Contract v0.1 akzeptiert, der Datengenerierung, Netzwerk, Normalisierung, Optimierung, Seeds, Gates, Rolloutmetriken und Artefakte exakt einfriert.