def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n})      # Wertet die Funktion mit x und n aus


def bisektion(a: float, b: float, n: float, epsilon: float, funktion: str) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Bisektionsverfahren."""

    if f(a, n, funktion) * f(b, n, funktion) > 0:       # Prüft, ob ein Vorzeichenwechsel im Intervall vorhanden ist
        print("Fehler: Kein gültiges Intervall.")
        return None                                     # Beendet die Funktion bei ungültigem Intervall

    iterationen = 0                                     # Zählt die Anzahl der Iterationen

    while True:                                         # Wiederholt die Bisektion bis zur gewünschten Genauigkeit
        c = (a + b) / 2                                 # Berechnet den Mittelpunkt des Intervalls
        iterationen += 1                                # Erhöht den Iterationszähler

        if abs(f(c, n, funktion)) < epsilon:            # Prüft, ob f(c) nahe genug bei 0 liegt
            return c, iterationen                       # Gibt Nullstelle und Iterationsanzahl zurück

        if f(a, n, funktion) * f(c, n, funktion) < 0:   # Prüft, ob die Nullstelle zwischen a und c liegt
            b = c                                       # Setzt c als neue rechte Grenze
        else:
            a = c                                       # Setzt c als neue linke Grenze


def ausgabe(a: float, b: float, n: float, epsilon: float, funktion: str, exponent: int | None = None) -> None:
    """Gibt das Ergebnis für eine Genauigkeit aus."""

    ergebnis = bisektion(a, b, n, epsilon, funktion)    # Startet die Bisektion mit den übergebenen Werten

    if ergebnis is not None:                            # Prüft, ob ein Ergebnis gefunden wurde
        nullstelle, iterationen = ergebnis              # Speichert Nullstelle und Iterationsanzahl

        print("--------------------------------")
        print("Funktion:", funktion)
        print("Intervall: [", a, ",", b, "]")

        if exponent is not None:                        # Ausgabe, wenn epsilon als 10^Exponent angegeben wurde
            print("Epsilon: 10^", exponent, "=", epsilon)
        else:
            print("Epsilon:", epsilon)

        print("Nullstelle:", nullstelle)
        print("Iterationen:", iterationen)
        print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))   # Zeigt, wie nahe f(x) bei 0 liegt


def solver() -> None:
    """Startet den Solver für Aufgabe 8."""

    try:
        funktion = "2*x + x**2 + 3*x**3 - x**4"         # Polynom aus Aufgabe 8
        n = 0                                           # n wird hier nicht benötigt
        a = 3                                           # Linke Intervallgrenze
        b = 4                                           # Rechte Intervallgrenze

        print("--------------------------------")
        print("Aufgabe 8: Polynom P4(x) = 2x + x² + 3x³ - x⁴")
        print("Passendes Intervall: [3, 4]")

        print("\nAutomatische Tests laut Angabe:")
        ausgabe(a, b, n, 10**-2, funktion, -2)          # Test mit epsilon = 10^-2
        ausgabe(a, b, n, 10**-8, funktion, -8)          # Test mit epsilon = 10^-8

        print("\nEigener Test:")
        
        while True:
            try:
                exponent = int(input("Geben Sie die Hochzahl für epsilon ein, also 10^: "))   # Benutzer gibt z.B. -2 oder -8 ein
                epsilon = 10 ** exponent                                                     # Berechnet daraus epsilon
                break
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige ganze Zahl ein.")                                                     # Berechnet daraus epsilon

        if epsilon <= 0:                                  # Prüft, ob epsilon positiv ist
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return

        ausgabe(a, b, n, epsilon, funktion, exponent)     # Führt den eigenen Test aus

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige ganze Zahl ein.")                 # Fehler bei ungültiger Eingabe


if __name__ == "__main__":
    solver()                                      # Startet das Programm