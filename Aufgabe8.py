def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n})


def bisektion(a: float,b: float,n: float,epsilon: float,funktion: str) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Bisektionsverfahren."""

    if f(a, n, funktion) * f(b, n, funktion) > 0:
        print("Fehler: Kein gültiges Intervall.")
        return None

    iterationen = 0

    while True:
        c = (a + b) / 2
        iterationen += 1

        if abs(f(c, n, funktion)) < epsilon:
            return c, iterationen

        if f(a, n, funktion) * f(c, n, funktion) < 0:
            b = c
        else:
            a = c


def solver() -> None:
    """Startet den Solver für Aufgabe 8."""

    try:
        funktion = "2*x + x**2 + 3*x**3 - x**4"
        n = 0
        a = 3
        b = 4

        print("Aufgabe 8: Polynom P4(x) = 2x + x² + 3x³ - x⁴")
        print("Passendes Intervall: [3, 4]")

        epsilon = float(input("Geben Sie die gewünschte Genauigkeit epsilon ein: "))

        if epsilon <= 0:
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return

        ergebnis = bisektion(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis

            print("--------------------------------")
            print("Funktion:", funktion)
            print("Intervall: [", a, ",", b, "]")
            print("Epsilon:", epsilon)
            print("Nullstelle:", nullstelle)
            print("Iterationen:", iterationen)
            print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige Zahl ein.")


if __name__ == "__main__":
    solver()