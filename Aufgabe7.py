import matplotlib.pyplot as plt
import numpy as np


def f(x: float, n: float) -> float:
    """Berechnet f(x) = x² - n."""
    return x**2 - n


def plotter() -> None:
    """Visualisiert die Bisektion mit matplotlib."""

    n = 25                       # Testwert für die Wurzel
    epsilon = 0.0001             # Gewünschte Genauigkeit
    a = 0                        # Linke Intervallgrenze
    b = 25                       # Rechte Intervallgrenze

    if f(a, n) * f(b, n) > 0:    # Prüft, ob das Intervall gültig ist
        print("Fehler: Kein gültiges Intervall.")
        return

    iterationen = []             # Speichert die Iterationsnummern
    c_werte = []                 # Speichert die Näherungswerte
    genauigkeiten = []           # Speichert |f(c)|

    x_werte = np.linspace(a, b, 400)    # x-Werte für den Funktionsgraphen
    y_werte = f(x_werte, n)             # y-Werte für den Funktionsgraphen

    iteration = 0

    while True:
        c = (a + b) / 2                 # Mittelpunkt berechnen
        fc = f(c, n)                    # Funktionswert bei c
        iteration += 1                  # Iteration erhöhen

        iterationen.append(iteration)
        c_werte.append(c)
        genauigkeiten.append(abs(fc))

        plt.clf()                       # Vorheriges Diagramm löschen

        plt.subplot(3, 1, 1)
        plt.plot(x_werte, y_werte, label="f(x) = x² - n")
        plt.axhline(0, color="black", linewidth=1)       # x-Achse
        plt.axvline(c, linestyle="--", label=f"c = {c:.5f}")
        plt.scatter(c, fc)
        plt.title("Bisektionsverfahren")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)

        plt.subplot(3, 1, 2)
        plt.plot(iterationen, genauigkeiten, marker="o")
        plt.title("Aktuelle Genauigkeit je Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("|f(c)|")
        plt.grid(True)

        plt.subplot(3, 1, 3)
        plt.plot(iterationen, c_werte, marker="o")
        plt.title("Aktuelle Lösung je Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("c")
        plt.grid(True)

        plt.tight_layout()              # Ordnet die Diagramme sauber an
        plt.pause(0.7)                  # Kurze Pause für die Animation

        if abs(fc) < epsilon:           # Genauigkeit erreicht
            break

        if f(a, n) * fc < 0:            # Nullstelle liegt links
            b = c
        else:
            a = c                       # Nullstelle liegt rechts

    print("--------------------------------")
    print("Ergebnis der Bisektion")
    print("n =", n)
    print("Epsilon =", epsilon)
    print("Nullstelle:", c)
    print("Analytische Lösung:", np.sqrt(n))
    print("Iterationen:", iteration)
    print("Abweichung:", abs(c - np.sqrt(n)))

    plt.show()                          # Zeigt das fertige Diagramm


if __name__ == "__main__":
    plotter()