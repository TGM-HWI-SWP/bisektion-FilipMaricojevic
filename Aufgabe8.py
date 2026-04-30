def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n})      # Wertet die Funktion mit x und n aus


def bisektion(a: float, b: float, n: float, epsilon: float, funktion: str) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Bisektionsverfahren."""

    if f(a, n, funktion) * f(b, n, funktion) > 0:       # Prüft den Vorzeichenwechsel
        print("Fehler: Kein gültiges Intervall.")
        return None

    iterationen = 0                                     # Zählt die Durchläufe

    while True:
        c = (a + b) / 2                                 # Berechnet den Mittelpunkt
        iterationen += 1

        if abs(f(c, n, funktion)) < epsilon:            # Prüft die Genauigkeit
            return c, iterationen

        if f(a, n, funktion) * f(c, n, funktion) < 0:   # Nullstelle liegt links
            b = c
        else:
            a = c                                       # Nullstelle liegt rechts


def ausgabe(a: float, b: float, n: float, epsilon: float, funktion: str, exponent: int | None = None) -> None:
    """Gibt das Ergebnis für eine Genauigkeit aus."""

    ergebnis = bisektion(a, b, n, epsilon, funktion)

    if ergebnis is not None:
        nullstelle, iterationen = ergebnis

        print("--------------------------------")
        print("Funktion:", funktion)
        print("Intervall: [", a, ",", b, "]")

        if exponent is not None:
            print("Epsilon: 10^", exponent, "=", epsilon)
        else:
            print("Epsilon:", epsilon)

        print("Nullstelle:", nullstelle)
        print("Iterationen:", iterationen)
        print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))


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
        ausgabe(a, b, n, 10**-2, funktion, -2)
        ausgabe(a, b, n, 10**-8, funktion, -8)

        print("\nEigener Test:")
        exponent = int(input("Geben Sie die Hochzahl für epsilon ein, also 10^: "))
        epsilon = 10 ** exponent

        if epsilon <= 0:
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return

        ausgabe(a, b, n, epsilon, funktion, exponent)

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige ganze Zahl ein.")


if __name__ == "__main__":
    solver()