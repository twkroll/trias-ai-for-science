# D012 — ML Code Skeleton v0.1

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D010–D011

## Entscheidung

Der getestete `ML Code Skeleton v0.1` wird als faithful implementation des eingefrorenen `ML Implementation Contract v0.1` akzeptiert.

## Mitakzeptierte Konsequenzen

1. Die paired-teacher Datengenerierung verwendet identische gespeicherte Figure-eight-Inputs für DOP853- und coarse-RK4-Labels.
2. Contiguous split, training-only Inputnormalisierung, Residual-MLP, gepaarte Seeds, Optimierung, One-Step-Metriken, Provenance-Fehlerzerlegung und MU1/MU2-Pipeline entsprechen D011.
3. Die lokalen technischen Tests (`4 passed`) und der verkürzte Smoke Run gelten ausschließlich als Implementierungsprüfung und nicht als wissenschaftliche Evidenz.
4. Der wissenschaftliche ML Full Run darf nun mit `N=1000`, Seeds `{0,1,2}` und allen in D011 eingefrorenen Gates ausgeführt werden.
5. Vor Sichtung der Full-Run-Ergebnisse werden keine wissenschaftlichen Einstellungen verändert.
6. Negative oder nicht informative Resultate führen nicht automatisch zu Architektur-, Hyperparameter-, Seed- oder Teacher-Sweeps.

## Revisionsbedingung

D012 wird revidiert, falls der Full Run einen Implementierungsfehler oder eine Verletzung der in D011 vorregistrierten gepaarten Kontrolllogik offenlegt.

## Nächste Abhängigkeit

Den eingefrorenen wissenschaftlichen ML Full Run ausführen, Reference- und Learner-Resolvability-Gates prüfen, One-Step- und MU1/MU2-Ergebnisse auswerten und erst danach einen möglichen ML-Provenance-Claim formulieren.