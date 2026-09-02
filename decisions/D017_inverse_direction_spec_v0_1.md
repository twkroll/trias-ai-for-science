# D017 — Minimal Inverse-Direction Demonstrator v0.1 akzeptiert

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D016

## Entscheidung

Die Spezifikation `demonstrator/inverse_direction_spec_v0_1.md` wird als wissenschaftliche Arbeitsgrundlage akzeptiert und eingefroren.

Der inverse MVP verwendet ausschließlich Lorenz-63 als synthetisches Zielsystem und vergleicht drei kontrollierte Datenpfade:

```text
P0: vollständige Beobachtung -> gemeinsame Derivative Estimation -> gemeinsame SINDy-Pipeline
P1: 20% gepaarte Missingness -> lineare Rekonstruktion -> dieselbe Derivative Estimation -> dieselbe SINDy-Pipeline
P2: dieselbe Missingness -> kubische Rekonstruktion -> dieselbe Derivative Estimation -> dieselbe SINDy-Pipeline
```

Für P1 und P2 werden exakt dieselben Missingness-Masken verwendet. Vorgesehen sind die drei vorregistrierten Mask-Seeds `{0,1,2}`. Die quadratische SINDy-Library muss die wahre Lorenz-Struktur enthalten; condition-spezifisches Hyperparameter-Tuning ist ausgeschlossen.

## Wissenschaftliche Bewertungslogik

Der Demonstrator trennt explizit:

```text
structural equation fidelity
vs.
dynamical/statistical adequacy
```

P0 muss vor jeder Provenance-Interpretation ein Structural-Recovery-Gate bestehen. Ein informativer positiver inverser Provenance-Fall erfordert reproduzierbare strukturelle Unterschiede unter mindestens einer Rekonstruktionspipeline bei gleichzeitig vorregistriert hinreichender dynamisch/statistischer Adäquanz. Triviale `bad model`-Fälle zählen nicht als positiver Befund.

Die Directed Trias wird nicht als neue Identifiability-Theorie interpretiert. Der spätere Comparator-Test gegen System Identification, Identifiability/Observability, SciML V&V und Workflow/Data Provenance bleibt verpflichtend.

## Scope Freeze

Nicht Bestandteil von v0.1 sind insbesondere Three-body chaos, Neural Networks, der pausierte ML-v0.2-Teacher-Provenance-Run, große SINDy-/Hyperparameter-Sweeps, zusätzliche Measurement Noise, mehrere Missingness-Raten, Block-Missingness, alternative Systeme oder verpflichtende Koopman-Spektren.

## Strategische Folge

D014 und der technisch vorbereitete ML-v0.2-Zweig bleiben gültig, aber der wissenschaftliche Full Run bleibt pausiert.

Als nächste Abhängigkeit wird ausschließlich ein **Inverse-Direction Implementation Contract v0.1** erstellt. Vor dessen weiterem GO wird kein Code geschrieben und kein wissenschaftlicher inverser Run gestartet.