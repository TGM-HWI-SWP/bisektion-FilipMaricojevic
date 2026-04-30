import math

from Aufgabe5 import solver, bisektion
from Aufgabe6 import solver2, regula_falsi
from Aufgabe7 import plotter


def leitung_länge(radius: float) -> float:
    """Berechnet die Länge der durchhängenden Leitung."""
    return 2 * radius * math.sinh(100 / (2 * radius))


def aufgabe9() -> None:
    """Löst Aufgabe 9 mit den Verfahren aus Aufgabe 5 und 6."""

    try:
        funktion = "x * math.cosh(50 / x) - x - 10"
        n = 0
        a = 100
        b = 150
        
        print("--------------------------------")
        print("Aufgabe 9: Durchhängende Leitung")
        print("Gleichung: x * cosh(50 / x) - x - 10 = 0")
        print("Intervall: [100, 150]")

        exponent = int(input("Geben Sie die Hochzahl für epsilon ein, also 10^: "))
        epsilon = 10 ** exponent

        if epsilon <= 0:
            print("Fehler: epsilon muss positiv sein.")
            return

        ergebnis_bisektion = bisektion(a, b, n, epsilon, funktion)
        ergebnis_regula = regula_falsi(a, b, n, epsilon, funktion)

        if ergebnis_bisektion is not None:
            radius, iterationen = ergebnis_bisektion
            laenge = leitung_länge(radius)

            print("--------------------------------")
            print("Aufgabe 9 mit Bisektion")
            print("Krümmungsradius:", radius, "m")
            print("Leitungslänge:", laenge, "m")
            print("Iterationen:", iterationen)

        if ergebnis_regula is not None:
            radius, iterationen = ergebnis_regula
            laenge = leitung_länge(radius)

            print("--------------------------------")
            print("Aufgabe 9 mit Regula falsi")
            print("Krümmungsradius:", radius, "m")
            print("Leitungslänge:", laenge, "m")
            print("Iterationen:", iterationen)

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige ganze Zahl ein.")


if __name__ == "__main__":
    solver()
    solver2()
    plotter()
    aufgabe9()