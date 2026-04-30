import math

def f(x: float, n: float, funktion: str) -> float:
    """Berechnet den Funktionswert f(x)."""
    return eval(funktion, {"x": x, "n": n, "math": math})   # Wertet die eingegebene Funktion aus


def regula_falsi(a: float, b: float, n: float, epsilon: float, funktion: str) -> tuple[float, int] | None:
    """Berechnet eine Nullstelle mit dem Regula-falsi-Verfahren."""

    fa = f(a, n, funktion)          # Funktionswert an der linken Grenze
    fb = f(b, n, funktion)          # Funktionswert an der rechten Grenze

    if fa == 0:                     # a ist bereits eine Nullstelle
        return a, 0

    if fb == 0:                     # b ist bereits eine Nullstelle
        return b, 0

    if fa * fb > 0:                 # Kein Vorzeichenwechsel im Intervall
        print("Fehler: Kein gültiges Intervall.")
        return None

    iterationen = 0                 # Zählt die Iterationen

    while True:
        fa = f(a, n, funktion)      # Aktueller Funktionswert bei a
        fb = f(b, n, funktion)      # Aktueller Funktionswert bei b

        c = b - fb * (b - a) / (fb - fa)    # Regula-falsi-Formel
        fc = f(c, n, funktion)              # Funktionswert am neuen Punkt
        iterationen += 1                    # Iterationszähler erhöhen

        if abs(fc) < epsilon:       # Genauigkeit erreicht
            return c, iterationen

        if fa * fc < 0:             # Nullstelle liegt zwischen a und c
            b = c
        else:
            a = c                   # Nullstelle liegt zwischen c und b


def ausgabe(funktion: str, n: float, a: float, b: float, epsilon: float, nullstelle: float, iterationen: int) -> None:
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

    funktion = "x**2 - n"           # Wurzelfunktion als Nullstellenproblem

    for n in [25, 81, 144]:
        a = 0                       # Linke Intervallgrenze
        b = n if n > 1 else 1       # Rechte Intervallgrenze
        ergebnis = regula_falsi(a, b, n, epsilon, funktion)

        if ergebnis is not None:
            nullstelle, iterationen = ergebnis
            analytisch = math.sqrt(n)   # Exakte Wurzel zum Vergleich

            ausgabe(funktion, n, a, b, epsilon, nullstelle, iterationen)
            print("Analytische Lösung:", analytisch)
            print("Abweichung zur Wurzel:", abs(nullstelle - analytisch))


def solver2() -> None:
    """Fragt Benutzereingaben ab und startet Regula falsi."""

    while True:                                             # Wiederholt die Eingabe bei Fehlern
        try:
            print("Beispiel: x**2 - n")
            funktion = input("Funktion f(x): ")             # Funktion als Text eingeben
            n = float(input("Wert für n: "))                # Wert für n einlesen
            epsilon = float(input("Genauigkeit epsilon: ")) # Genauigkeit einlesen

            if epsilon <= 0:                                # Prüft, ob epsilon positiv ist
                print("Fehler: epsilon muss positiv sein.")
                continue                                    # Startet die Eingabe neu

            a = float(input("Linker Intervallwert a: "))    # Linke Intervallgrenze
            b = float(input("Rechter Intervallwert b: "))   # Rechte Intervallgrenze

            ergebnis = regula_falsi(a, b, n, epsilon, funktion) # Startet Regula falsi

            if ergebnis is not None:                        # Prüft, ob eine Nullstelle gefunden wurde
                nullstelle, iterationen = ergebnis          # Speichert Ergebniswerte
                ausgabe(funktion, n, a, b, epsilon, nullstelle, iterationen)

            break                                           # Beendet die Schleife nach gültigem Durchlauf

        except ValueError:
            print("Fehler: Bitte gültige Zahlen eingeben.") # Fehler bei falscher Zahleneingabe
        except NameError:
            print("Fehler: Ungültige Variable in der Funktion.") # Fehler bei falscher Variable
        except SyntaxError:
            print("Fehler: Die Funktion ist syntaktisch falsch.") # Fehler bei falscher Funktionsschreibweise
        except ZeroDivisionError:
            print("Fehler: Division durch 0 im Regula-falsi-Verfahren.") # Fehler bei Division durch 0

if __name__ == "__main__":
    print("Automatische Tests für Aufgabe 6:")
    teste_wurzelfunktion(0.00001)   # Testet n = 25, 81 und 144

    print("\nEigener Regula-falsi-Solver:")
    solver2()