import math


def f(x: float, n: float, funktion: str) :
    """Berechnet den Funktionswert f(x) für eine gegebene Funktion."""
    return eval(funktion, {"x": x, "n": n, "math": math})   # Führt die Funktion aus und berechnet den Funktionswert für die gegebenen Werte von x und n


def regula_falsi(a: float,b: float,n: float,epsilon: float,funktion: str) :
    """Führt das Regula-falsi-Verfahren durch, um eine Nullstelle der Funktion f(x) = 0 zu finden"""
    fa = f(a, n, funktion)
    fb = f(b, n, funktion)

    if fa == 0:
        return a, 0

    if fb == 0:
        return b, 0

    if fa * fb > 0:
        print("Fehler: Kein gültiges Intervall gefunden.")
        return None

    iterationen = 0

    while True:
        fa = f(a, n, funktion)
        fb = f(b, n, funktion)

        c = b - fb * (b - a) / (fb - fa)
        fc = f(c, n, funktion)

        iterationen += 1

        if abs(fc) < epsilon:
            return c, iterationen

        if fa * fc < 0:
            b = c
        else:
            a = c


def teste_wurzelfunktion(epsilon: float) :
    """Testet das Regula-falsi-Verfahren an der Funktion f(x) = x^2 - n für verschiedene Werte von n"""

    funktion = "x**2 - n"                                   # Definiert die Funktion, die getestet werden soll, in diesem Fall die Wurzelfunktion, die die Nullstelle bei sqrt(n) hat
    testwerte = [25, 81, 144]

    for n in testwerte:
        a = 0
        b = n if n > 1 else 1

        ergebnis = regula_falsi(a, b, n, epsilon, funktion) # Führt das Regula-falsi-Verfahren für die Funktion f(x) = x^2 - n durch, um die Nullstelle zu finden

        if ergebnis is not None:                            # Wenn das Verfahren eine Nullstelle gefunden hat, werden die Ergebnisse mit der analytischen Lösung verglichen, um die Genauigkeit zu bewerten.
            nullstelle, iterationen = ergebnis
            analytische_loesung = math.sqrt(n)              # Berechnet die analytische Lösung, die Quadratwurzel von n, um die Genauigkeit der numerischen Lösung zu überprüfen
            abweichung = abs(nullstelle - analytische_loesung)  # Berechnet die Abweichung zwischen der numerischen Lösung und der analytischen Lösung 

            print("n =", n)
            print("Funktion:", funktion)
            print("Intervall: [", a, ",", b, "]")
            print("Epsilon =", epsilon)
            print("Iterationen:", iterationen)
            print("Numerische Lösung:", nullstelle)
            print("Analytische Lösung:", analytische_loesung)
            print("Abweichung:", abweichung)
            print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))  # Berechnet die Abweichung von f(nullstelle) von 0, um zu überprüfen, wie gut die gefundene Nullstelle tatsächlich eine Nullstelle der Funktion ist


def solver2() :
    """Fragt Benutzereingaben ab und startet Regula falsi."""

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

        ergebnis = regula_falsi(a, b, n, epsilon, funktion)         # Führt das Regula-falsi-Verfahren für die Funktion f(x) = x^2 - n durch, um die Nullstelle zu finden, die der Quadratwurzel von n entspricht. 

        if ergebnis is not None:                                    # Wenn das Verfahren eine Nullstelle gefunden hat, werden die Ergebnisse mit der analytischen Lösung verglichen, um die Genauigkeit zu bewerten.
            nullstelle, iterationen = ergebnis


            print("Funktion:", funktion)
            print("n =", n)
            print("Epsilon =", epsilon)
            print("Intervall: [", a, ",", b, "]")
            print("Iterationen:", iterationen)
            print("Nullstelle:", nullstelle)
            print("Abweichung f(x):", abs(f(nullstelle, n, funktion)))  # Berechnet die Abweichung von f(nullstelle) von 0, um zu überprüfen, wie gut die gefundene Nullstelle tatsächlich eine Nullstelle der Funktion ist. 

    except ValueError:
        print("Fehler: Bitte geben Sie gültige Zahlen ein.")

    except NameError:
        print("Fehler: Die Funktion enthält ungültige Variablen.")

    except SyntaxError:
        print("Fehler: Die Funktion ist syntaktisch falsch.")

    except ZeroDivisionError:
        print("Fehler: Division durch 0 im Regula-falsi-Verfahren.")


if __name__ == "__main__":
    print("Automatische Tests für Aufgabe 6:")
    teste_wurzelfunktion(0.00001)                         # Führt automatische Tests für die Wurzelfunktion mit einer Genauigkeit von 0.00001 durch

    print("\nEigener Regula-falsi-Solver:")
    solver2()