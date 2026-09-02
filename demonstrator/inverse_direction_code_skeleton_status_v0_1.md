# Inverse-Direction Code Skeleton v0.1

**Status:** READY FOR REVIEW  
**Stand:** 2026-09-02  
**Depends on:** D018  
**Scientific full run:** NOT EXECUTED

## Implementierter Scope

Der Skeleton implementiert die im akzeptierten Inverse-Direction Implementation Contract benötigten technischen Kernbausteine, ohne den wissenschaftlichen Full Run auszuführen:

- Lorenz-63 RHS und exaktes Vektorfeld in `float64`;
- DOP853-Referenzintegration und primary/tight reference gap;
- PCG64-Missingness-Masken mit geschützten zwei Randpunkten;
- SHA-256-Mask-Hashes zur Pairing-/Provenance-Kontrolle;
- lineare und `not-a-knot` CubicSpline-Rekonstruktion ohne Extrapolation;
- gemeinsame zentrale Fünfpunktableitung vierter Ordnung;
- feste quadratische Feature-Library `[1,x,y,z,x^2,xy,xz,y^2,yz,z^2]`;
- wahre Lorenz-Support-/Koeffizientenmatrix;
- STLSQ-artige sparse regression mit Threshold/Ridge/Iterationsparametern aus D018;
- Structural precision/recall, spurious/missing terms, Support-Jaccard und Koeffizientenfehler;
- held-out Vector-Field-NRMSE;
- Forward-Integration inferierter ODEs;
- normierter Short-Horizon-Zustandsfehler;
- Langzeitmittel, Standardabweichung, Korrelationsmatrix und normierte 1-Wasserstein-Distanzen;
- technische Dynamic-validity- und operative-Äquivalenzfunktionen mit den vorregistrierten D018-Toleranzen;
- CLI-Einstieg `trias-inverse-demo`.

Neue Module:

```text
src/trias_demo/inverse_data.py
src/trias_demo/inverse_sindy.py
src/trias_demo/inverse_validation.py
src/trias_demo/inverse_experiment.py
```

Neue Tests:

```text
tests/test_inverse_skeleton.py
tests/test_inverse_validation.py
```

## Technische lokale Prüfung

Die neu implementierten inversen Tests wurden in einer lokalen Python-Umgebung mit NumPy/SciPy ausgeführt:

```text
python -m pytest -q
......
6 passed
```

Die Tests prüfen insbesondere:

1. exakte Repräsentierbarkeit des Lorenz-Vektorfelds durch die eingefrorene Feature-Library;
2. Masken- und Rekonstruktionsintegrität;
3. die 5-Punkt-Ableitung an Polynomen bis Grad vier;
4. STLSQ-Recovery des exakten Lorenz-Supports aus exakten Vektorfeldwerten;
5. gepaarte P1/P2-Mask-Hashes im Smoke-Pfad;
6. numerische Äquivalenz von wahrer Lorenz-Dynamik und Forward-Modell mit den exakten Lorenz-Koeffizienten.

Diese Prüfung ist technisch, nicht wissenschaftlich. Sie ist keine Ausführung des eingefrorenen Full Contracts.

## Nichtwissenschaftlicher Smoke Run

Ausgeführt wurde ausschließlich ein verkürzter Pipeline-Test mit:

```text
dt = 0.02
t_end = 12
discovery = [2,8]
holdout = (8,12]
missing_count = 60
mask_seed = 0
```

Damit werden die wissenschaftlichen Full-Parameter aus D018 ausdrücklich **nicht** benutzt.

Technische Resultate:

```text
reference G1 = True
max normalized primary/tight gap ~= 4.77e-12
paired linear/cubic mask hash = identical
G2 mask integrity = True for both paths
linear reconstruction RMSE ~= 1.02e-1
cubic reconstruction RMSE ~= 3.88e-3
```

Im verkürzten Smoke Run war das Full-Contract-P0-G3 nicht erfüllt (`precision=0.875`, `recall=1.0`, ein spurious term). Dieser Befund wird **nicht wissenschaftlich interpretiert**, weil der Smoke Run ein anderes Zeitfenster, gröberes Sampling und nur einen Seed verwendet. Er dient ausschließlich dazu zu bestätigen, dass die Pipeline G3 berechnet und ein Scheitern korrekt sichtbar macht.

## Guardrail

Es wurde **kein** wissenschaftlicher Run mit

```text
dt=0.01
Discovery [10,50]
Holdout (50,60]
800 missing points
mask seeds {0,1,2}
```

ausgeführt. Insbesondere wurden keine Resultate zu `INFORMATIVE_POSITIVE`, `INFORMATIVE_NEGATIVE`, C07-L-R oder dem methodologischen Mehrwert der Directed Trias erzeugt.

## Nächste Entscheidung

Empfehlung: **ACCEPT den Code Skeleton als technische Umsetzung von D018.**

Erst bei weiterem `GO` darf der wissenschaftliche inverse Full Run mit den vollständig eingefrorenen D018-Parametern ausgeführt werden. Die Interpretation beginnt danach strikt mit G1–G3 und erst anschließend mit Structural-vs.-Dynamical-Adequacy und dem verpflichtenden Comparator-Audit.