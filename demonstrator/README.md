# Drei-Körper-Demonstratoren

## Numerischer Minimaldemonstrator

**Scientific scope:** D005  
**Technical contract:** D006  
**Code skeleton:** D007  
**Scientific result:** Full v0.1 complete; C05 accepted as D008; strong C06 form rejected and C06-R accepted as D009.

Der numerische Demonstrator prüft nicht, welcher Solver allgemein „der beste“ ist. Er untersucht, ob dieselbe synthetische Figure-eight-Zielinstanz und dieselbe Newtonsche Theorie unter verschiedenen numerischen Operationalisierungen unterschiedliche wissenschaftlich relevante Bewertungsprofile erzeugen.

### Frozen comparison

- target: planare gleichmassige Figure-eight-Choreographie;
- reference: DOP853 with primary/tight tolerances;
- baseline: fixed-step classical RK4;
- structural contrast: velocity-Verlet / kick-drift-kick;
- U1: one nominal period, trajectory-oriented use;
- U2: 100 nominal periods, structure-oriented use;
- refinement: `n = {50, 100, 200, 400, 800}` with `h=T_pub/n`.

Details:

- [`minimal_spec_v0_1.md`](minimal_spec_v0_1.md)
- [`implementation_contract_v0_1.md`](implementation_contract_v0_1.md)
- [`full_run_v0_1_results.md`](full_run_v0_1_results.md)
- [`c06_comparison_v0_1.md`](c06_comparison_v0_1.md)

### Kernergebnis

RK4 ist im getesteten Bereich trajectory-genauer; Velocity-Verlet zeigt ein anderes Langzeit-Strukturprofil mit deutlich kleinerem fitted secular energy drift und Drehimpulserhaltung nahe Rundungsniveau. Dies stützt einen use-case-relativen C05-Claim, aber keinen globalen Solverwinner.

Der harte C06-Vergleich zeigt zugleich, dass diese numerischen Befunde mit etablierter numerischer Analysis und V&V/Credibility vollständig beschreibbar sind. Die Trias wird deshalb nicht als Ersatz für V&V behandelt; ihr derzeitiger Restmehrwert ist integrativ/provenance-orientiert.

## Minimaler ML / AI-for-Science Provenance Demonstrator

**Scientific scope:** D010 accepted  
**ML Implementation Contract:** PENDING REVIEW  
**ML code/training:** not started by design

Der nächste Test führt genau eine zusätzliche Ebene ein:

`Zielsystem/Theorie → numerischer Datengenerator → Trainingsdaten → Residual-MLP → Rollout/wissenschaftlicher Gebrauch`.

Akzeptiert sind:

- unverändertes Figure-eight-Zielsystem;
- DOP853 versus coarse RK4 `h=T_pub/50` als Teacher;
- identische Inputs, nur unterschiedliche Teacher-Labels;
- ein Residual-MLP;
- drei gepaarte Seeds;
- generatorrelative versus gemeinsame Referenzbewertung;
- MU1 = 1 Periode, MU2 = 10 Perioden;
- kein Architektur-/Hyperparameter-Sweep und kein Physics-informed Training.

Details:

- [`ml_epistemic_spec_v0_1.md`](ml_epistemic_spec_v0_1.md)
- [`ml_implementation_contract_v0_1.md`](ml_implementation_contract_v0_1.md)

Vor Akzeptanz des ML Implementation Contract wird weder Dataset-/Training-Code geschrieben noch ein Training gestartet.

## Epistemische Guardrails

- DOP853 wird nie als exakte Ground Truth bezeichnet.
- Gerundete Figure-eight-Anfangsdaten implizieren keine exakte Periodizität.
- Gute `ML ↔ Teacher`-Metriken dürfen nicht automatisch als `ML ↔ Zielsystem`-Validierung interpretiert werden.
- Ein positiver ML-Befund wäre noch kein Originalitätsnachweis gegenüber etablierten Dataset-Provenance-/ML-Credibility-Ansätzen.
- Negative und nichtinformative Ergebnisse sind zulässig und führen nicht automatisch zu Scope- oder Tuning-Erweiterungen.