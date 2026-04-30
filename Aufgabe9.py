import math

from Aufgabe5 import bisektion                      # Importiert den Bisektionssolver aus Aufgabe 5
from Aufgabe6 import regula_falsi                   # Importiert das Regula-falsi-Verfahren aus Aufgabe 6


def leitung_länge(radius: float) -> float:
    """Berechnet die Länge der durchhängenden Leitung."""
    return 2 * radius * math.sinh(100 / (2 * radius))    # Formel für die Leitungslänge


def aufgabe9() -> None:
    """Löst Aufgabe 9 mit den Verfahren aus Aufgabe 5 und 6."""

    try:
        funktion = "x * math.cosh(50 / x) - x - 10"      # Gleichung zur Berechnung des Krümmungsradius
        n = 0                                            # n wird hier nicht benötigt
        a = 100                                          # Linke Grenze des Intervalls
        b = 150                                          # Rechte Grenze des Intervalls

        print("--------------------------------")
        print("Aufgabe 9: Durchhängende Leitung")
        print("Gleichung: x * cosh(50 / x) - x - 10 = 0")
        print("Intervall: [100, 150]")

        exponent = int(input("Geben Sie die Hochzahl für epsilon ein, also 10^: "))  # Eingabe z.B. -5
        epsilon = 10 ** exponent                                                    # Berechnet epsilon aus der Hochzahl

        if epsilon <= 0:                                    # Prüft, ob epsilon positiv ist
            print("Fehler: epsilon muss positiv sein.")
            return

        ergebnis_bisektion = bisektion(a, b, n, epsilon, funktion)       # Berechnet den Radius mit Bisektion
        ergebnis_regula = regula_falsi(a, b, n, epsilon, funktion)       # Berechnet den Radius mit Regula falsi

        if ergebnis_bisektion is not None:                  # Prüft, ob Bisektion ein Ergebnis geliefert hat
            radius, iterationen = ergebnis_bisektion        # Speichert Radius und Iterationen
            laenge = leitung_länge(radius)                  # Berechnet die Leitungslänge

            print("--------------------------------")
            print("Aufgabe 9 mit Bisektion")
            print("Krümmungsradius:", radius, "m")
            print("Leitungslänge:", laenge, "m")
            print("Iterationen:", iterationen)

        if ergebnis_regula is not None:                     # Prüft, ob Regula falsi ein Ergebnis geliefert hat
            radius, iterationen = ergebnis_regula           # Speichert Radius und Iterationen
            laenge = leitung_länge(radius)                  # Berechnet die Leitungslänge

            print("--------------------------------")
            print("Aufgabe 9 mit Regula falsi")
            print("Krümmungsradius:", radius, "m")
            print("Leitungslänge:", laenge, "m")
            print("Iterationen:", iterationen)

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige ganze Zahl ein.")     # Fehler bei falscher Eingabe


if __name__ == "__main__":
    aufgabe9()                                            # Startet Aufgabe 9