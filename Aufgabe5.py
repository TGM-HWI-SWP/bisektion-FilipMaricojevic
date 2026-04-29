import math

def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n, "math": math})   # Führt die Funktion aus und berechnet den Funktionswert für die gegebenen Werte von x und n

def bisektion( a: float, b: float, n: float, epsilon: float, funktion: str) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Bisektionsverfahren."""

    fa = f(a, n, funktion)
    fb = f(b, n, funktion)

    if fa == 0:
        return a, 0

    if fb == 0:
        return b, 0

    if fa * fb > 0:
        print("Fehler: Kein gültiges Intervall.")
        return None         # Überprüft, ob die Funktion an den Endpunkten des Intervalls liegt. 
                            #Wenn beide Funktionswerte das gleiche Vorzeichen haben, wird eine Fehlermeldung ausgegeben und None zurückgegeben.

    iterationen = 0

    while True:
        c = (a + b) / 2         
        fc = f(c, n, funktion)
        iterationen += 1

        if abs(fc) < epsilon:
            return c, iterationen

        if f(a, n, funktion) * fc < 0:
            b = c
        else:
            a = c

def ausgabe( funktion: str, n: float, a: float, b: float, epsilon: float, nullstelle: float, iterationen: int) -> None:
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
    """Testet den Solver mit n = 25, 81 und 144."""

    funktion = "x**2 - n"

    for n in [25, 81, 144]:
        a = 0
        b = n if n > 1 else 1
        ergebnis = bisektion(a, b, n, epsilon, funktion)

        if ergebnis is not None:    # Wenn das Verfahren eine Nullstelle gefunden hat, werden die Ergebnisse mit der analytischen Lösung verglichen, um die Genauigkeit zu bewerten.
            nullstelle, iterationen = ergebnis
            analytisch = math.sqrt(n)   # Berechnet die analytische Lösung, die Quadratwurzel von n, um die Genauigkeit der numerischen Lösung zu überprüfen

            ausgabe(funktion, n, a, b, epsilon, nullstelle, iterationen)
            print("Analytische Lösung:", analytisch)
            print("Abweichung zur Wurzel:", abs(nullstelle - analytisch))   # Berechnet die Abweichung zwischen der numerischen Lösung und der analytischen Lösung, um die Genauigkeit des Verfahrens zu bewerten.

def solver() -> None:
    """Fragt Benutzereingaben ab und startet den Solver."""

    try:
        print("Beispiel: x**2 - n")
        funktion = input("Funktion f(x): ")
        n = float(input("Wert für n: "))
        epsilon = float(input("Genauigkeit epsilon: "))

        if epsilon <= 0:
            print("Fehler: epsilon muss positiv sein.")
            return  # Überprüft, ob die eingegebene Genauigkeit epsilon positiv ist. Wenn nicht, wird eine Fehlermeldung ausgegeben und die Funktion wird mit return verlassen.

        a = float(input("Linker Intervallwert a: "))
        b = float(input("Rechter Intervallwert b: "))

        ergebnis = bisektion(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis
            ausgabe(funktion, n, a, b, epsilon, nullstelle, iterationen)    

    except ValueError:
        print("Fehler: Bitte gültige Zahlen eingeben.")
    except NameError:
        print("Fehler: Ungültige Variable in der Funktion.")
    except SyntaxError:
        print("Fehler: Die Funktion ist syntaktisch falsch.")

if __name__ == "__main__":
    print("Automatische Tests für Aufgabe 5:")
    teste_wurzelfunktion(0.00001)   # Führt automatische Tests für die Wurzelfunktion mit einer Genauigkeit von 0.00001 durch, um die Funktionalität des Bisektionsverfahrens zu überprüfen.

    print("\nEigener Solver:")
    solver()