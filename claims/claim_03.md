# C03 — Sundmans Reihenlösung: Konvergenz und praktische Traktabilität

**Status:** ACCEPTED  
**Akzeptiert durch:** GO  
**Evidenzstatus:** mathematisch-historischer Kern gut gestützt; methodologische Interpretation ist projektinterne Lesart  
**Stand:** 2026-09-01

## C03a — mathematisch-historischer Claim

> Sundman konstruierte für das Newtonsche Drei-Körper-Problem unter der klassischen Voraussetzung nichtverschwindenden Gesamtdrehimpulses nach Regularisierung binärer Kollisionen und Einführung einer geeigneten neuen Zeitvariablen Potenzreihen, die für die entsprechende regularisierte Variable konvergieren und die Bewegung für alle reellen Zeiten repräsentieren.

Für die spätere Paperfassung soll dies vorsichtig und quellengetreu formuliert werden. Insbesondere sind die genaue Rolle des Gesamtdrehimpulses, die Behandlung binärer Kollisionen, der Ausschluss bzw. Sonderstatus totaler Dreifachkollisionen und die globale Zeitabdeckung direkt an Primär- und Fachsekundärquellen zu dokumentieren.

## C03b — methodologischer Claim

> Der methodologisch relevante Punkt ist nicht fehlende mathematische Konvergenz, sondern die extrem geringe praktische Konvergenzgeschwindigkeit der resultierenden Reihen. Die Existenz einer konvergenten analytischen Repräsentation garantiert somit weder eine praktikable Bahnberechnung noch wissenschaftliche Nutzbarkeit.

Der engere, für die Trias wichtige Befund lautet daher:

**formale analytische Verfügbarkeit impliziert nicht operative Verfügbarkeit.**

## Was als gut gestützt gilt

### 1. Es handelt sich um ein Konvergenzresultat

Die Standarddarstellungen von Sundmans Theorem beschreiben eine Regularisierung binärer Kollisionen sowie eine Transformation der Zeitvariable. Unter der klassischen Voraussetzung, dass der Gesamtdrehimpuls nicht null ist, werden relevante Größen als analytische Funktionen einer regularisierten Variablen dargestellt; über eine weitere Abbildung erhält man Potenzreihen mit globaler Bedeutung für die reale Bewegung.

### 2. Binäre und totale Kollisionen müssen getrennt werden

Die verkürzte Aussage „Sundmans Lösung gilt nur kollisionsfrei“ ist irreführend. Binäre Kollisionen werden in der Konstruktion regularisiert. Totale Dreifachkollisionen bilden einen gesonderten Grenzfall; für nichtverschwindenden Gesamtdrehimpuls treten sie nicht auf.

### 3. Praktische Ineffizienz ist historisch dokumentiert

Belorizky untersuchte 1930 die praktische Anwendung von Sundmans Methode auf einen speziellen Drei-Körper-Fall und zeigte eine extrem langsame Konvergenz. Spätere mathematische und astronomische Darstellungen charakterisieren die Reihen deshalb als für praktische Ephemeriden- oder Bahnberechnung ungeeignet. Für das Paper genügt die qualitative Aussage „extrem langsam / praktisch ungeeignet“; spektakuläre quantitative Angaben zur notwendigen Termanzahl werden nur verwendet, wenn sie direkt und kontextgetreu aus der Quelle rekonstruiert werden.

## Wichtige Präzisierungen

### „Analytische Lösung“ vorsichtig verwenden

Die Formulierung „Sundman löste das allgemeine Drei-Körper-Problem analytisch“ ist historisch verbreitet, aber ohne Zusatz zu stark. Für das Projekt soll präziser von einer **global konvergenten Reihenrepräsentation in einer regularisierten Variablen unter den Voraussetzungen des Sundman-Theorems** gesprochen werden.

### Keine Behauptung einer geschlossenen Form

Sundmans Resultat ist keine geschlossene Formel im üblichen Sinn, sondern eine konvergente Potenzreihendarstellung nach nichttrivialen Variablentransformationen.

### Keine Gleichsetzung von Konvergenz und praktischer Berechenbarkeit

Dass die Reihe konvergiert, beantwortet die mathematische Konvergenzfrage. Die Anzahl benötigter Terme und der Aufwand zur Erreichung wissenschaftlich relevanter Genauigkeit sind davon getrennte operative Fragen.

### Keine Gleichsetzung mit numerischer Stabilität

Aus der langsamen Konvergenz der Sundman-Reihe folgt nicht unmittelbar eine Aussage über numerische Stabilität moderner Integratoren. Diese Begriffe werden in C04 ausdrücklich getrennt.

## Philosophische Rolle im Trias-Projekt

Sundman ist **kein alleiniger Beweis für die Trias**. Das Resultat wird als besonders klarer Grenzfall verwendet, an dem analytische Repräsentierbarkeit und operative Evaluierbarkeit auseinanderfallen.

Die weitergehende philosophische Interpretation — dass deshalb die Bedingungen der Operationalisierung ausdrücklich auditiert werden sollten — ist eine Setzung des Projekts und darf nicht Sundman selbst zugeschrieben werden.

## Quellenbasis für die Arbeitsfassung

1. K. F. Sundman, *Mémoire sur le problème des trois corps*, Acta Mathematica 36, 105–179, DOI: 10.1007/BF02422379.
2. D. Belorizky, *Application pratique des méthodes de M. Sundman à un cas particulier du problème des trois corps*, Bulletin astronomique 6 (1930), 417–434, DOI: 10.3406/bastr.1930.14038.
3. M. Henkel, *Sur la solution de Sundman du problème des trois corps*, Philosophia Scientiae 5(2) (2001), 161–184.
4. A. Chenciner, *Three body problem*, Scholarpedia 2(10):2111 (2007).
5. *Encyclopedia of Mathematics*, Eintrag „Three-body problem“.
6. Moderne mathematische Einordnungen der Sundman-Konstruktion und ihrer Voraussetzungen.

## Explizite Nicht-Claims

Das Projekt behauptet nicht:

- dass Sundmans Reihe divergiert;
- dass das Drei-Körper-Problem damit in praktisch brauchbarer Form „gelöst“ ist;
- dass Sundmans Resultat eine geschlossene Lösung liefert;
- dass jede Null-Drehimpuls-Konfiguration zwangsläufig eine Dreifachkollision besitzt;
- dass langsame Konvergenz dasselbe wie numerische Instabilität ist;
- dass die praktische Schwierigkeit durch Chaos erklärt wird;
- dass Sundmans Resultat allein die Eigenständigkeit des Berechnungs-Pols beweist;
- dass spektakuläre Termzahl-Schätzungen ohne direkte Quellenprüfung als Kernargument verwendet werden dürfen.

## Revisionsbedingung

C03 muss revidiert werden, wenn die Primärquellenprüfung zeigt, dass die zugeschriebenen Konvergenz-, Kollisions- oder Geltungsbedingungen zu stark oder unpräzise formuliert sind. Der methodologische Teil C03b bleibt nur dann bestehen, wenn die praktische Ineffizienz der konvergenten Darstellung zuverlässig belegt werden kann.

## Nächste Abhängigkeit

C04 — Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit.