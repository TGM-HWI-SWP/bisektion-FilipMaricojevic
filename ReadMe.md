[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rJS_cvW3)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23213378&assignment_repo_type=AssignmentRepo)
# Bisektion Vorlage

## Beschreibung
Dieses Projekt dient als Vorlage für ein kleines Softwareentwicklungs- und Projektmanagement-Projekt. Es enthält verschiedene Aufgaben, die jeweils in separaten Dateien bearbeitet werden.

## Aufgaben
- Aufgabe5.py: [In Aufgabe 5 wird ein Solver mit dem Bisektionsverfahren programmiert.  
Der Benutzer kann eine Funktion, einen Wert für n, ein Intervall und eine Genauigkeit eingeben. Das Programm berechnet dann schrittweise eine Nullstelle der Funktion.  
Getestet wird der Solver mit der Wurzelfunktion x**2 - n für n = 25, 81 und 144]
- Aufgabe6.py: [In Aufgabe 6 wird ein zweites Verfahren umgesetzt, und zwar Regula falsi.  
Es funktioniert ähnlich wie die Bisektion, aber der neue Näherungswert wird nicht mit der Mitte des Intervalls berechnet, sondern mit einer Sekante.  
Auch dieses Verfahren wird mit der Wurzelfunktion x**2 - n getestet und mit der echten Wurzel verglichen.]
- Aufgabe7.py: [In Aufgabe 7 wird die Bisektion mit matplotlib grafisch dargestellt.  
Das Programm zeigt die Funktion, den aktuellen Näherungswert, die Genauigkeit pro Iteration und die aktuelle Lösung pro Iteration.  
Dadurch sieht man, wie sich der Solver Schritt für Schritt der Nullstelle nähert.]
- Aufgabe8.py: [In Aufgabe 8 wird der Solver mit dem Polynom 2*x + x**2 + 3*x**3 - x**4 getestet. Es wird ein passendes Intervall [3, 4] verwendet, um die Nullstelle bei ungefähr 3,45.. zu finden.  
Danach wird geprüft, wie viele Iterationen für 10^-2 und 10^-8 benötigt werden.]
- Aufgabe9.py: [In Aufgabe 9 wird der Solver auf ein reales Problem angewendet.  
Es geht um eine Leitung zwischen zwei Masten, die in der Mitte 10 m durchhängt.  
Zuerst wird der Krümmungsradius mit dem Solver berechnet. Danach wird mit diesem Wert die Länge der Leitung berechnet.]

## Voraussetzungen
- Python 3.x

## Ausführung
Jede Aufgabe kann einzeln ausgeführt werden:


## Projektstruktur
- `Aufgabe5.py` bis `Aufgabe9.py`: Implementierungen der einzelnen Aufgaben
- `ReadMe.md`: Diese Datei
- `__init__.py`: Initialisierungsdatei für das Paket