import math

def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n, "math": math})   # Führt die Funktion aus und berechnet den Funktionswert für die gegebenen Werte von x und n

def regula_falsi( a: float, b: float, n: float, epsilon: float, funktion: str ) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Regula-falsi-Verfahren."""

    fa = f(a, n, funktion)
    fb = f(b, n, funktion)

    if fa == 0:
        return a, 0

    if fb == 0:
        return b, 0

    if fa * fb > 0:
        print("Fehler: Kein gültiges Intervall.")
        return None

    iterationen = 0

    while True:
        fa = f(a, n, funktion)
        fb = f(b, n, funktion)

        c = b - fb * (b - a) / (fb - fa)    # Berechnet den neuen Schätzwert c basierend auf den Funktionswerten an den Endpunkten a und b.
        fc = f(c, n, funktion)
        iterationen += 1

        if abs(fc) < epsilon:
            return c, iterationen

        if fa * fc < 0:
            b = c
        else:
            a = c

def ausgabe( funktion: str, n: float, a: float, b: float, epsilon: float, nullstelle: float, iterationen: int ) -> None:
    """Gibt die Ergebnisse übersichtlich aus."""

    print("--------------------------------")
    print("Funktion:", funktion)
    print("n =", n)
    print("Intervall: [", a, ",", b, "]")
    print("Epsilon =", epsilon)
    print("Nullstelle:", nullstelle)
    print("Iterationen:", iterationen)
    print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))


def teste_wurzelfunktion(epsilon: float) -> None:
    """Testet Regula falsi mit n = 25, 81 und 144."""

    funktion = "x**2 - n"

    for n in [25, 81, 144]:
        a = 0
        b = n if n > 1 else 1
        ergebnis = regula_falsi(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis
            analytisch = math.sqrt(n)   # Berechnet die analytische Lösung der Wurzel von n, um die Genauigkeit des Regula-falsi-Verfahrens zu überprüfen.

            ausgabe(funktion, n, a, b, epsilon, nullstelle, iterationen)
            print("Analytische Lösung:", analytisch)
            print("Abweichung zur Wurzel:", abs(nullstelle - analytisch))


def solver2() -> None:
    """Fragt Benutzereingaben ab und startet Regula falsi."""

    try:
        print("Beispiel: x**2 - n")
        funktion = input("Funktion f(x): ")
        n = float(input("Wert für n: "))
        epsilon = float(input("Genauigkeit epsilon: "))

        if epsilon <= 0:
            print("Fehler: epsilon muss positiv sein.")
            return

        a = float(input("Linker Intervallwert a: "))
        b = float(input("Rechter Intervallwert b: "))

        ergebnis = regula_falsi(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis
            ausgabe(funktion, n, a, b, epsilon, nullstelle, iterationen)

    except ValueError:
        print("Fehler: Bitte gültige Zahlen eingeben.")
    except NameError:
        print("Fehler: Ungültige Variable in der Funktion.")
    except SyntaxError:
        print("Fehler: Die Funktion ist syntaktisch falsch.")
    except ZeroDivisionError:
        print("Fehler: Division durch 0 im Regula-falsi-Verfahren.")

if __name__ == "__main__":
    print("Automatische Tests für Aufgabe 6:")
    teste_wurzelfunktion(0.00001)       # Führt automatische Tests für die Wurzelfunktion mit einer Genauigkeit von 0.00001 durch, um die Funktionalität des Regula-falsi-Verfahrens zu überprüfen.

    print("\nEigener Regula-falsi-Solver:")
    solver2()