# Directed Trias v0.1 — gerichtete, nichtinvertierbare epistemische Transformationen

**Status:** WORKING THEORY REVISION / PENDING CLAIM REVIEW  
**Stand:** 2026-09-02  
**Auslöser:** Verbindung des bisherigen Trias-Programms mit Zhai, Lucarini & Lai (2025/2026) und der Frage nach Identifizierbarkeit in datengetriebener Dynamik.

## 1. Kernrevision

Die Trias `Realität/Zielsystem — Theorie — Berechnung/Umsetzung` wird nicht aufgegeben. Die drei Pole bleiben funktionale Audit-Rollen. Neu ist die stärkere These, dass der methodologisch interessante Gehalt primär in **gerichteten Transformationen zwischen diesen Rollen** liegt.

Die zentrale Arbeitsidee lautet:

> Wissenschaftliche Übersetzungen zwischen Zielsystem, Theorie und operativer Repräsentation sind im Allgemeinen weder verlustfrei noch eindeutig noch invertierbar. Deshalb muss ein Audit nicht nur die Pole, sondern Richtung, Provenance, Informationsverlust, Nicht-Eindeutigkeit und Zweckrelativität der Übergänge dokumentieren.

Dies ist eine projektinterne theoretische Synthese und noch kein akzeptierter Originalitätsclaim.

## 2. Zwei Hauptrichtungen

### Forward-Richtung

Von einer theoretischen Beschreibung zu einem operativen Output:

```text
T -> C_forward -> R_hat
```

Beispiele:

- analytische Repräsentation -> praktische Auswertung;
- Newtonsche Gleichungen -> numerischer Integrator -> Trajektorie;
- Theorie -> Simulationsdatengenerator -> ML-Surrogat -> Vorhersage.

Die zentrale Frage lautet nicht nur, ob gerechnet werden kann, sondern welche theoretischen Strukturen, Fehlerprofile und Rechtfertigungsbedingungen durch die Operationalisierung entstehen.

### Inverse-Richtung

Vom Zielsystem bzw. seinen Beobachtungen zu einer inferierten theoretischen Repräsentation:

```text
R -> C_observation -> D -> C_inference -> T_hat
```

Hier umfasst die operative Vermittlung unter anderem Messung, Sampling, Missingness, Imputation, Feature-/Library-Wahl, Optimierung und Modellselektion.

Die zentrale Frage lautet, ob und in welchem Sinn aus einer bestimmten Beobachtungs- und Inferenzpipeline eine eindeutige theoretische Struktur identifizierbar ist.

## 3. Berechnung als Familie operativer Vermittlungen

Der `C`-Pol wird nicht mehr nur als numerischer Forward-Solver verstanden. Für Auditzwecke wird er funktional in mehrere operative Rollen zerlegt:

```text
C_obs      Observation / Datafication
C_pre      preprocessing / imputation / reconstruction
C_infer    inference / equation discovery / model fitting
C_forward  numerical realization / simulation
C_ML       learned surrogate / learned operator
C_compare  comparison / validation / credibility assessment
```

Diese Unterteilung erzeugt keine neuen ontologischen Pole. Sie macht lediglich sichtbar, welche operative Transformation an einer gerichteten Kante stattfindet.

## 4. Formale Minimalstruktur

Sei `R*` das intendierte Zielsystem und `T*` eine zugehörige theoretische Dynamik. Eine Beobachtungspipeline `p` erzeuge Daten

```text
D_p = O_p(R*)
```

und eine Inferenzpipeline `q` daraus

```text
T_hat_(p,q) = I_q(D_p).
```

Eine Forward-Operationalisierung `k` erzeugt aus einer Theorie

```text
Y_(T,k) = F_k(T).
```

Im Allgemeinen ist nicht vorauszusetzen, dass

```text
I_q(O_p(R*)) = T*
```

oder dass verschiedene Forward-Operationalisierungen

```text
F_k1(T*) = F_k2(T*)
```

liefern.

Damit werden zwei Nicht-Eindeutigkeiten getrennt:

1. **Forward non-equivalence:** gleiche Theorie, unterschiedliche Operationalisierung, unterschiedliche wissenschaftliche Profile.
2. **Inverse non-identifiability:** ähnliche beobachtbare Dynamik oder gleiche Datenbasis, aber mehrere mögliche theoretische Repräsentationen.

## 5. Zweckrelative operative Äquivalenz

Für eine Menge wissenschaftlich relevanter Observablen `O` und eine Toleranz `epsilon` definieren wir projektintern:

```text
T1 ~_(O,epsilon) T2
```

falls die aus `T1` und `T2` erzeugten Outputs bezüglich der gewählten Observablen innerhalb der festgelegten Toleranz praktisch nicht unterschieden werden.

Wichtig:

```text
T1 ~_(O,epsilon) T2
```

impliziert **keine strukturelle Identität der Gleichungen**.

Damit werden vier Ebenen explizit getrennt:

```text
predictive adequacy
!= dynamical/statistical adequacy
!= structural equation fidelity
!= physical interpretability
```

Die Äquivalenzrelation ist zweck- und observable-relativ. Zwei Modelle können für Attraktorstatistiken äquivalent und für mechanistische Interpretation nicht äquivalent sein.

## 6. Verbindung der bisherigen Fälle

### Sundman

```text
formale/analytische Verfügbarkeit
not=> operative Verfügbarkeit
```

Der Bruch liegt primär auf der Forward-Kante `T -> C_forward`.

### Figure-eight Solverfall

```text
gleiche Theorie + gleiches Zielsystem
not=> gleiches operatives epistemisches Profil
```

Der Bruch liegt in der konkreten Operationalisierung `T -> C_forward -> R_hat`.

### Zhai–Lucarini–Lai

```text
ähnliche dynamische/statistische Outputs
not=> eindeutig identifizierte Gleichungsstruktur
```

Der Bruch liegt auf der inversen Kette `R -> C_obs/pre -> C_infer -> T_hat`.

### ML-Provenance-Zweig

```text
T/R -> C_sim -> D -> C_ML -> R_hat
```

Hier können mehrere operative Ebenen hintereinanderliegen. Das bisherige v0.1-Experiment blieb wegen fehlender Learner-Resolvability unentschieden.

## 7. Identifizierbarkeit als neue querliegende Auditdimension

Die bestehende sechs-stufige Lösungsleiter bleibt unverändert:

```text
Existenz -> analytische Repräsentation -> praktische Evaluierbarkeit -> numerische Simulation -> Vorhersage -> wissenschaftliche Nutzbarkeit
```

**Theoretische Identifizierbarkeit wird nicht als zusätzliche lineare Stufe eingefügt.** Analog zu Stabilität, Machbarkeit und Systemsensitivität wird sie als querliegende Auditdimension behandelt.

Auditfragen:

- Welche theoretischen Freiheitsgrade sind aus den verfügbaren Beobachtungen überhaupt unterscheidbar?
- Welche Nicht-Eindeutigkeit ist strukturell, welche praktisch/datenbedingt?
- Welche Teile der inferierten Struktur hängen von Messung, Imputation, Library oder Optimierung ab?
- Welche Observablen definieren die behauptete Äquivalenz?
- Welche wissenschaftliche Schlussfolgerung verlangt strukturelle Identität und welche nur operative Adäquanz?

## 8. Novelty Guardrail

Nicht behauptet wird:

- dass Nichtidentifizierbarkeit neu ist;
- dass observational equivalence/equifinality neu ist;
- dass System Identification bisher Messprozeduren ignoriert hat;
- dass Zhai–Lucarini–Lai die Trias beweisen;
- dass verschiedene Gleichungen generell physikalisch gleichwertig sind;
- dass erfolgreiche Prediction mechanistische Interpretation grundsätzlich ausschließt.

Structural/practical identifiability, observability, equifinality und model non-uniqueness sind etablierte Felder. Ein möglicher eigenständiger Trias-Beitrag kann daher nur in einer **durchgängigen gemeinsamen Auditierung von Forward- und Inverse-Transformationen** liegen.

## 9. Mögliche stärkere Synthese von C03–C06

Die bisherige Evidenz lässt sich nun symmetrischer lesen:

```text
Sundman:
T verfügbar not=> C praktikabel

Solverfall:
T fix not=> C1 und C2 epistemisch äquivalent

Inverse equation discovery:
ähnliche R-/Output-Eigenschaften not=> T eindeutig
```

Die gemeinsame methodologische Hypothese lautet damit:

> Die Abbildungen zwischen Zielsystem, Theorie und operativer Vermittlung besitzen im Allgemeinen keine garantierte Eindeutigkeit oder Invertierbarkeit. Wissenschaftliche Validität muss deshalb relativ zur Richtung der Transformation, zur Provenance der Zwischenrepräsentationen und zum intendierten Gebrauch beurteilt werden.

Diese Fassung ist derzeit **Arbeitsrevision**, nicht akzeptierter Hauptclaim.

## 10. Konsequenz für den aktuellen ML-v0.2-Zweig

D014 und der technisch fertige v0.2-Skeleton werden **nicht widerrufen**. Der wissenschaftliche Full Run wird jedoch vorläufig **pausiert**, weil der neue inverse Identifizierbarkeitsfall möglicherweise einen stärkeren und direkt messbaren Test von C06-R bietet als die Auflösung einer sehr kleinen DOP853-vs.-RK4-Teacher-Differenz.

Die Pause ist strategisch, kein negatives Urteil über v0.2.

## 11. Neue Abhängigkeitsreihenfolge

```text
C07-L Bridge Claim audit
-> Vergleich mit Identifiability / Observability / Equifinality / System Identification
-> Entscheidung, ob Directed Trias C06-R substanziell schärft
-> Minimaler inverse-direction Demonstrator spezifizieren
-> danach entscheiden: ML-v0.2 Full Run fortsetzen, sekundär stellen oder ersetzen
-> erst später ggf. chaotischer Drei-Körper-Fall
```

Der nächste Schritt ist daher kein Training, sondern die vollständige Claim-/Evidence-Prüfung von C07-L.