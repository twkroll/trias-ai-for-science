# C03 — Sundmans Reihenlösung: Konvergenz und praktische Traktabilität

**Status:** PENDING REVIEW  
**Evidenzstatus:** mathematischer Kern gut gestützt; bibliographische Datierung und genaue Formulierungsdetails weiter dokumentieren  
**Stand:** 2026-09-01

## Vorgeschlagene Claim-Fassung

> Sundmans klassisches Resultat liefert für das Newtonsche Drei-Körper-Problem unter der Voraussetzung nichtverschwindenden Gesamtdrehimpulses nach Regularisierung binärer Kollisionen und Einführung einer geeigneten neuen Zeitvariablen Potenzreihen, die für die entsprechende regularisierte Variable konvergieren und die Bewegung für alle reellen Zeiten repräsentieren. Der methodologisch relevante Punkt ist daher nicht fehlende mathematische Konvergenz, sondern die extrem geringe praktische Konvergenzgeschwindigkeit der resultierenden Reihen. Die Existenz einer konvergenten analytischen Repräsentation garantiert somit weder eine praktikable Bahnberechnung noch wissenschaftliche Nutzbarkeit.

## Was als gut gestützt gilt

### 1. Es handelt sich um ein Konvergenzresultat

Die Standarddarstellungen von Sundmans Theorem beschreiben eine Regularisierung der binären Kollisionen sowie eine Transformation der Zeitvariable. Unter der klassischen Voraussetzung, dass der Gesamtdrehimpuls nicht null ist, werden die Koordinaten, die gegenseitigen Abstände und die Zeit als analytische Funktionen einer regularisierten Variablen dargestellt. Nach einer konformen Abbildung entstehen Potenzreihen, die im Einheitskreis konvergieren und die Bewegung für alle reellen Zeiten erfassen.

### 2. Binäre und totale Kollisionen müssen getrennt werden

Für nichtverschwindenden Gesamtdrehimpuls kann eine totale Dreifachkollision nicht auftreten. Binäre Kollisionen können in Sundmans Konstruktion regularisiert werden. Deshalb ist die verkürzte Formulierung „Sundmans Lösung gilt nur kollisionsfrei“ irreführend.

### 3. Praktische Ineffizienz ist historisch dokumentiert

Belorizky untersuchte 1930 die praktische Anwendung von Sundmans Methode auf einen speziellen Drei-Körper-Fall und zeigte eine extrem langsame Konvergenz. Spätere mathematische und astronomische Darstellungen charakterisieren die Reihen deshalb als für praktische Ephemeriden- oder Bahnberechnung ungeeignet. Für unser Paper genügt zunächst die qualitative Aussage „extrem langsam / praktisch ungeeignet“; spektakuläre Zahlen zur notwendigen Termanzahl sollen nur verwendet werden, wenn sie direkt und kontextgetreu aus Belorizkys Rechnung rekonstruiert werden.

## Wichtige Präzisierungen

### „Analytische Lösung“ vorsichtig verwenden

Die Formulierung „Sundman löste das allgemeine Drei-Körper-Problem analytisch“ ist historisch verbreitet, aber ohne Zusatz zu stark. Für das Projekt sollte präziser von einer **global konvergenten Reihenrepräsentation in einer regularisierten Variablen unter den Voraussetzungen des Sundman-Theorems** gesprochen werden.

### Keine Behauptung einer geschlossenen Form

Sundmans Resultat ist keine geschlossene Formel im üblichen Sinne. Es ist eine konvergente Potenzreihendarstellung nach nichttrivialen Variablentransformationen.

### Keine Gleichsetzung von Konvergenz und praktischer Berechenbarkeit

Dass die Reihe konvergiert, beantwortet nur die mathematische Konvergenzfrage. Die benötigte Anzahl von Termen bzw. der Aufwand zur Erreichung einer praktisch relevanten Genauigkeit ist eine davon getrennte operative Frage.

### Keine Gleichsetzung mit numerischer Stabilität

Aus der langsamen Konvergenz der Sundman-Reihe folgt nicht unmittelbar eine Aussage über die numerische Stabilität moderner Integratoren. Diese Begriffe werden in C04 ausdrücklich getrennt.

## Datierungsnotiz

Die Literatur zitiert das Mémoire teils als 1912, teils als 1913. Das Werk erschien in *Acta Mathematica*, Band 36, S. 105–179, DOI 10.1007/BF02422379. Das Projekt sollte in der Bibliographie eine einheitliche Datierung nach dem tatsächlich verwendeten bibliographischen Datensatz wählen und die 1907/1909 erschienenen Vorarbeiten von der späteren zusammenfassenden Fassung unterscheiden. Bis zur endgültigen Bibliographieprüfung soll im Fließtext bevorzugt „Sundmans Mémoire“ bzw. „Sundmans klassisches Resultat“ verwendet werden, wenn das genaue Publikationsjahr nicht argumentativ relevant ist.

## Quellenbasis für die Arbeitsfassung

1. K. F. Sundman, *Mémoire sur le problème des trois corps*, Acta Mathematica 36, 105–179, DOI: 10.1007/BF02422379.
2. D. Belorizky, *Application pratique des méthodes de M. Sundman à un cas particulier du problème des trois corps*, Bulletin astronomique 6 (1930), 417–434, DOI: 10.3406/bastr.1930.14038.
3. M. Henkel, *Sur la solution de Sundman du problème des trois corps*, Philosophia Scientiae 5(2) (2001), 161–184.
4. A. Chenciner, *Three body problem*, Scholarpedia 2(10):2111 (2007).
5. *Encyclopedia of Mathematics*, Eintrag „Three-body problem“.
6. Q. D. Wang, Überblick/Arbeiten zur globalen Lösung des n-body problem, als moderne mathematische Einordnung der Sundman-Konstruktion.

## Explizite Nicht-Claims

Das Projekt behauptet nicht:

- dass Sundmans Reihe divergiert,
- dass das Drei-Körper-Problem damit in einer praktisch brauchbaren Form „gelöst“ ist,
- dass Sundmans Resultat eine geschlossene Lösung liefert,
- dass jede Null-Drehimpuls-Konfiguration zwangsläufig eine Dreifachkollision besitzt,
- dass die langsame Konvergenz der Reihe dasselbe wie numerische Instabilität ist,
- dass Sundmans Resultat allein die Eigenständigkeit des Berechnungs-Pols beweist.

## Methodologische Rolle im Trias-Projekt

Sundman ist kein alleiniger Beweis für die Trias. Der Fall dient als besonders klare Illustration für eine Trennung, die später allgemeiner gefasst wird:

**mathematische Existenz / analytische Repräsentierbarkeit ≠ operative Evaluierbarkeit.**

Er liefert damit den Übergang zu C04, in dem mathematische Konvergenz, rechnerische Machbarkeit, numerische Stabilität und wissenschaftliche Nutzbarkeit systematisch getrennt werden.

## Revisionsbedingung

C03 muss revidiert werden, wenn die Primärquellenprüfung zeigt, dass die hier zugeschriebenen Konvergenz- oder Geltungsbedingungen unzutreffend formuliert sind. Insbesondere dürfen Aussagen über Kollisionsfälle, Gesamtdrehimpuls und globale Zeitabdeckung nur in der durch die Quellen gedeckten Form erhalten bleiben.

## Entscheidungsempfehlung

**ACCEPT mit vorsichtiger Formulierung.**

Die für das Paper zentrale Aussage soll lauten: Sundmans Resultat ist ein Beispiel für eine mathematisch konvergente, aber praktisch extrem ineffiziente Reihenrepräsentation; nicht für eine divergente Reihe.

Nach `GO` folgt C04: Konvergenz ≠ Machbarkeit ≠ Stabilität ≠ wissenschaftliche Nutzbarkeit.