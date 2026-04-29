def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n})      # Wertet die Funktion mit den aktuellen Werten für x und n aus


def bisektion(a: float, b: float, n: float, epsilon: float, funktion: str) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Bisektionsverfahren."""

    if f(a, n, funktion) * f(b, n, funktion) > 0:       # Prüft, ob im Intervall ein Vorzeichenwechsel vorhanden ist
        print("Fehler: Kein gültiges Intervall.")
        return None                                     # Beendet die Funktion, wenn das Intervall ungültig ist

    iterationen = 0                                     # Zählt die Anzahl der Durchläufe

    while True:                                         # Wiederholt die Berechnung, bis die Genauigkeit erreicht ist
        c = (a + b) / 2                                 # Berechnet den Mittelpunkt des Intervalls
        iterationen += 1                                # Erhöht den Iterationszähler um 1

        if abs(f(c, n, funktion)) < epsilon:            # Prüft, ob f(c) nahe genug bei 0 liegt
            return c, iterationen                       # Gibt die Nullstelle und die Iterationsanzahl zurück

        if f(a, n, funktion) * f(c, n, funktion) < 0:   # Prüft, ob die Nullstelle im linken Teilintervall liegt
            b = c                                       # Setzt die rechte Grenze auf c
        else:
            a = c                                       # Setzt die linke Grenze auf c


def solver() -> None:
    """Startet den Solver für Aufgabe 8."""

    try:
        funktion = "2*x + x**2 + 3*x**3 - x**4"         # Polynom aus Aufgabe 8
        n = 0                                           # n wird hier nicht benötigt, bleibt aber wegen der allgemeinen f-Funktion erhalten
        a = 3                                           # Linke Intervallgrenze
        b = 4                                           # Rechte Intervallgrenze

        print("Aufgabe 8: Polynom P4(x) = 2x + x² + 3x³ - x⁴")
        print("Passendes Intervall: [3, 4]")

        exponent = int(input("Geben Sie die Hochzahl für epsilon ein, also 10^: "))   # Benutzer gibt z.B. -2 oder -8 ein
        epsilon = 10 ** exponent                                                     # Berechnet daraus epsilon, z.B. 10^-2

        if epsilon <= 0:                                  # Prüft, ob epsilon positiv ist
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return

        ergebnis = bisektion(a, b, n, epsilon, funktion)  # Startet das Bisektionsverfahren

        if ergebnis is not None:                          # Prüft, ob ein Ergebnis gefunden wurde
            nullstelle, iterationen = ergebnis            # Teilt das Ergebnis in Nullstelle und Iterationsanzahl auf

            print("--------------------------------")
            print("Funktion:", funktion)
            print("Intervall: [", a, ",", b, "]")
            print("Epsilon: 10^", exponent, "=", epsilon)
            print("Nullstelle:", nullstelle)
            print("Iterationen:", iterationen)
            print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))   # Zeigt, wie nahe f(x) bei 0 liegt

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige ganze Zahl ein.")     # Fehler bei ungültiger Eingabe


if __name__ == "__main__":
    solver()                                                           