# D034 — W4 PASS akzeptiert; Writing Goal W5 Controls + Stress Tests freigegeben

**Datum:** 2026-09-03  
**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Depends on:** D033, `paper/manuscript_section_7_v0_1.md`, `paper/w4_contribution_boundary_evaluation_v0_1.md`

## Entscheidung

Die W4-Contribution-Boundary-/Residual-Compression-Evaluation wird mit der Klassifikation

```text
PASS
```

akzeptiert.

Der PASS gilt ausschließlich für eine **Perspective / Conceptual Synthesis**. Er erzeugt keine technische oder methodologische Framework-Novelty.

## Akzeptierte W4-Befunde

Die direkte Gegenüberstellung mit V&V/VVUQ, Provenance, Assurance Cases, Identifiability/System Identification, Philosophy of ML und SciML lässt einen begrenzten, aber kohärenten Rest übrig:

> eine genealogisch verankerte, claimspezifische Evidence-Localization-Sprache, die über heterogene computational scientific workflows sichtbar macht, welchen Referenten, welchen Theorieclaim und welche computational practice konkrete Evidenz verbindet.

Die zentrale Arbeitsteilung bleibt:

```text
Trias                -> wo / welcher Typ von wissenschaftlichem Claim?
Spezialframework     -> wie wird dieser Claim fachlich tief geprüft?
```

Akzeptiert ist außerdem:

```text
S2 no residual explanatory compression = NOT TRIGGERED
S3 notation only                       = NOT TRIGGERED
S5 overclaim pressure                  = NOT TRIGGERED
residual contribution                  = MODERATE CROSS-DOMAIN SYNTHESIS
practical superiority                  = UNTESTED
```

Equation Discovery und Synthetic Surrogates bleiben die stärksten konzeptionellen Träger; Black-box Prediction und PIML dienen stärker der cross-case Vergleichbarkeit.

## Freigegebener nächster Schritt

Als nächste Abhängigkeit wird ausschließlich **Writing Goal W5** ausgeführt:

> **Sections 5–6 — Classical controls and negative/inconclusive stress tests.**

W5 muss vier Projektfälle in die Manuskriptlogik integrieren:

```text
Sundman          -> klassischer T-C-Grenzfall / conceptual illustration
Figure-eight     -> positive standard-V&V control
Lorenz/SINDy     -> INFORMATIVE_NEGATIVE
ML v0.1          -> INCONCLUSIVE_LEARNER_ERROR
```

## W5 Guardrails

1. Sundmans Reihen dürfen nicht als divergent beschrieben werden; relevant ist die extrem langsame praktische Konvergenz/Evaluierbarkeit.
2. Figure-eight darf nicht als Beleg neuer Trias-Numerik dargestellt werden; Standard Numerical Analysis/V&V erklärt den Fall gut.
3. Lorenz/SINDy bleibt exakt `INFORMATIVE_NEGATIVE`; linear seed 2 bleibt explorativ.
4. ML v0.1 bleibt exakt `INCONCLUSIVE_LEARNER_ERROR`; der Teacher-Provenance-Claim wird weder unterstützt noch widerlegt.
5. `negative`, `inconclusive`, `untested` und `not applicable` dürfen nicht semantisch vermischt werden.
6. Keine neuen Experimente, keine Schwellenrevision, keine post-hoc Rettung eines positiven Effekts.

## Gate nach W5

Nach dem Schreiben wird nur geprüft:

```text
case coherence
evidence-status discipline
manuscript proportionality
```

Erlaubte Urteile:

```text
PASS
REVISE
SHORTEN
```

Kein neuer allgemeiner Novelty-Audit. Introduction und Abstract bleiben weiterhin zurückgestellt.