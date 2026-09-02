# D011 — ML Implementation Contract v0.1

**Datum:** 2026-09-02  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D010

## Entscheidung

Der vorregistrierte `ML Implementation Contract v0.1` wird in der vorgelegten Form akzeptiert und für den minimalen AI-for-Science-Provenance-Test eingefroren.

Damit sind insbesondere Datengenerierung, Teacher-Maps, Split, Normalisierung, Residual-MLP, gepaarte Seeds, Optimierung, One-Step-Metriken, Provenance-Fehlerzerlegung, Teacher-/Reference-Gates, MU1/MU2-Rollouts, Seed-Robustheit, Ergebnisstatus und Scope-Grenzen vor dem wissenschaftlichen Full Run festgelegt.

## Mitakzeptierte Konsequenzen

1. `N=1000` Startphasen und der zusammenhängende 60/20/20-Split werden nicht nach Sichtung der Resultate verändert.
2. Beide Teacher erhalten exakt dieselben gespeicherten Inputzustände.
3. Reference teacher ist DOP853 primary/tight; coarse teacher ist exakt ein RK4-Schritt mit `h=T_pub/50`.
4. Es gibt eine gemeinsame trainingsbasierte Inputnormalisierung und kein teacherabhängiges Target-Scaling.
5. Das einzige Netz ist `12-128-128-128-12`, `tanh`, Residualausgabe, float64 CPU.
6. Seeds `{0,1,2}` werden gepaart mit bitgleicher Initialisierung verwendet.
7. Kein Architektur-, Lernraten-, Seed- oder Hyperparameter-Sweep ist zulässig, wenn der Test negativ oder nicht informativ ausfällt.
8. Ein Teacher-Provenance-Effekt wird nur interpretiert, wenn Referenz- und Learner-Resolvability-Gates erfüllt sind.
9. Die exakte Zerlegung `e_total = e_model + e_teacher` ist verpflichtender Bestandteil der Auswertung.
10. Der wissenschaftliche Full Run wird erst nach Review des getesteten ML-Code-Skeletons gestartet.

## Revisionsbedingung

D011 wird nur revidiert, wenn die Implementierung einen technischen Widerspruch zur gepaarten Kontrolllogik oder eine Verletzung der vorregistrierten Gates offenlegt. Änderungen werden als neue Entscheidung dokumentiert.

## Nächste Abhängigkeit

Dataset-/ML-Code-Skeleton implementieren, technische Tests und einen nichtwissenschaftlichen Smoke Run ausführen; anschließend Skeleton reviewen, bevor der eingefrorene Full Run gestartet wird.
