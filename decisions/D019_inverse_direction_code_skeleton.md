# D019 — Inverse-Direction Code Skeleton v0.1 akzeptiert

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D018

## Entscheidung

Der in `demonstrator/inverse_direction_code_skeleton_status_v0_1.md` dokumentierte Inverse-Direction Code Skeleton v0.1 wird als technische Umsetzung des eingefrorenen D018-Contracts akzeptiert.

Akzeptiert sind insbesondere die technischen Bausteine für Lorenz-63-Referenzintegration, gepaarte Missingness-Masken, lineare/kubische Rekonstruktion, gemeinsame 5-Punkt-Ableitung, feste quadratische SINDy-Library, STLSQ, Structural-Metriken, held-out Vector-Field-Metrik sowie Forward-/Langzeitvalidierung.

Der verkürzte Smoke Run bleibt ausdrücklich nichtwissenschaftlich. Sein P0-G3-Scheitern wird nicht als wissenschaftliche Evidenz interpretiert.

## Erlaubter nächster Schritt

Nach D019 darf der wissenschaftliche inverse Full Run exakt nach D018 ausgeführt werden. Die Auswertung muss strikt mit G1, G2 und G3 beginnen. Erst bei bestandenen Baseline-/Integritätsgates dürfen Structural-Perturbation und dynamisch/statistische Adäquanz interpretiert werden.

Nach der numerischen Klassifikation bleibt der Comparator-Test gegen System Identification, Identifiability/Observability, SciML-V&V und Workflow/Data-Provenance verpflichtend.

## Guardrail

D018-Thresholds, Toleranzen, Missingness-Rate, Seeds und Resultatlogik dürfen nach Sichtung des Full Runs nicht rückwirkend angepasst werden.