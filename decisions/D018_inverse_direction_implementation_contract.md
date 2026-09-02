# D018 — Inverse-Direction Implementation Contract v0.1 akzeptiert

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D017

## Entscheidung

Der `demonstrator/inverse_direction_implementation_contract_v0_1.md` wird als exakte Vorregistrierung des inversen Lorenz/SINDy-Demonstrators akzeptiert und eingefroren.

Damit sind insbesondere Referenzintegration, Zeitfenster, 20%-Missingness mit Seeds `{0,1,2}`, gepaarte P1/P2-Masken, lineare bzw. not-a-knot-CubicSpline-Rekonstruktion, gemeinsame 5-Punkt-Ableitung, quadratische Feature-Library, STLSQ-Parameter, das harte P0-Structural-Recovery-Gate, Structural-Perturbation-Kriterien, held-out Vector-Field-Metrik, vorregistrierte Langzeitobservablen, operative Äquivalenztoleranzen und Resultatklassen festgelegt.

## Erlaubter nächster Schritt

Nach D018 darf ausschließlich ein **Inverse-Direction Code Skeleton v0.1** implementiert werden. Zulässig sind technische Unit-Tests und ein explizit nichtwissenschaftlicher verkürzter Smoke Run zur Pipeline-Integrität.

Nicht zulässig vor weiterem GO sind:

- der wissenschaftliche Full Run mit dem eingefrorenen Full-Contract;
- Änderung von Thresholds, Toleranzen, Missingness-Rate oder Seeds nach Sichtung wissenschaftlicher Resultate;
- wissenschaftliche Interpretation eines Smoke Runs;
- Fortsetzung des pausierten ML-v0.2-Full-Runs.

## Nächste Entscheidung

Review des Code-Skeletons und seiner technischen Tests/Smoke-Ergebnisse. Erst ein weiteres GO erlaubt den wissenschaftlichen inversen Full Run.