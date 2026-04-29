import math                                                     # Importiert die math-Bibliothek, um mathematische Funktionen wie sqrt zu verwenden


def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x) für eine gegebene Funktion."""
    return eval(funktion, {"x": x, "n": n, "math": math})       # Erlaubt die Verwendung von math-Funktionen in der Funktion, z.B. math.sqrt(n)


def bisektion(a: float,b: float,n: float,epsilon: float,funktion: str) -> tuple[float, int] | None:
    """Führt die Bisektionsmethode durch, um eine Nullstelle der Funktion f(x) = 0 zu finden."""

    if f(a, n, funktion) == 0:                  # Überprüft, ob a bereits eine Nullstelle ist
        return a, 0

    if f(b, n, funktion) == 0:                  # Überprüft, ob b bereits eine Nullstelle ist
        return b, 0

    if f(a, n, funktion) * f(b, n, funktion) > 0:   # Überprüft, ob f(a) und f(b) das gleiche Vorzeichen haben, was bedeutet, dass keine Nullstelle im Intervall liegt
        print("Fehler: Kein gültiges Intervall gefunden.")
        return None                                 # Gibt None zurück, wenn kein gültiges Intervall gefunden wird

    iterationen = 0

    while True:                 # Solange bis die gewünschte Genauigkeit erreicht ist
        c = (a + b) / 2
        iterationen += 1

        if abs(f(c, n, funktion)) < epsilon:        # Überprüft, ob die Funktion an der Stelle c nahe genug an 0 ist, um als Nullstelle betrachtet zu werden
            return c, iterationen

        if f(a, n, funktion) * f(c, n, funktion) < 0:   # Überprüft, ob die Nullstelle im Intervall [a, c] liegt
            b = c
        else:
            a = c


def teste_wurzelfunktion(epsilon: float) -> None:
    """Testet die Bisektionsmethode an der Funktion f(x) = x^2 - n für verschiedene Werte von n."""

    funktion = "x**2 - n"               # Definiert die Funktion, die getestet werden soll, in diesem Fall die Wurzelfunktion, die die Nullstelle bei sqrt(n) hat
    testwerte = [25, 81, 144]          
    for n in testwerte:                 # Für jeden Testwert n wird die Bisektionsmethode angewendet, um die Nullstelle der Funktion zu finden, und die Ergebnisse werden mit der analytischen Lösung (der Quadratwurzel von n) verglichen.
        a = 0
        b = n if n > 1 else 1

        ergebnis = bisektion(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis
            analytische_loesung = math.sqrt(n)      # Berechnet die analytische Lösung, die Quadratwurzel von n, um die Genauigkeit der numerischen Lösung zu überprüfen
            abweichung = abs(nullstelle - analytische_loesung)  # Berechnet die Abweichung zwischen der numerischen Lösung und der analytischen Lösung 

            
            print("n =", n)
            print("Funktion:", funktion)
            print("Intervall: [", a, ",", b, "]")
            print("Epsilon =", epsilon)
            print("Iterationen:", iterationen)
            print("Numerische Lösung:", nullstelle)
            print("Analytische Lösung:", analytische_loesung)
            print("Abweichung:", abweichung)


def solver() -> None:
    """Fragt Benutzereingaben ab und startet den Bisektionssolver."""

    try:
        print("Beispiel für die Wurzelfunktion: x**2 - n")
        funktion = input("Geben Sie die Funktion f(x) ein: ")

        n = float(input("Geben Sie den Wert für n ein: "))
        epsilon = float(input("Geben Sie die gewünschte Genauigkeit epsilon ein: "))

        if n < 0:
            print("Fehler: n muss eine nicht-negative Zahl sein.")
            return

        if epsilon <= 0:
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return

        a = float(input("Geben Sie den linken Intervallwert a ein: "))
        b = float(input("Geben Sie den rechten Intervallwert b ein: "))

        ergebnis = bisektion(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis

           
            print("Funktion:", funktion)
            print("n =", n)
            print("Epsilon =", epsilon)
            print("Intervall: [", a, ",", b, "]")
            print("Iterationen:", iterationen)
            print("Nullstelle:", nullstelle)
            print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))      # Berechnet die Abweichung von f(nullstelle) von 0, um zu überprüfen, wie gut die gefundene Nullstelle tatsächlich eine Nullstelle der Funktion ist

    except ValueError:
        print("Fehler: Bitte geben Sie gültige Zahlen ein.")

    except NameError:
        print("Fehler: Die Funktion enthält ungültige Variablen.")

    except SyntaxError:
        print("Fehler: Die Funktion ist syntaktisch falsch.")


if __name__ == "__main__":
    print("Automatische Tests für Aufgabe 5:")
    teste_wurzelfunktion(0.00001)                   # Führt automatische Tests für die Wurzelfunktion mit einer Genauigkeit von 0.00001 durch
    

    print("\nEigener Solver:")
    solver()