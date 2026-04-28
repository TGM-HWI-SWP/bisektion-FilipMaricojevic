import matplotlib.pyplot as plt
import numpy as np


def f(x: float, n: float):
    """Berechnet f(x) = x² - n."""
    return x**2 - n


def plotter() :
    """Visualisiert die Bisektion mit matplotlib."""

    # Testwerte für Aufgabe 7
    n = 25
    epsilon = 0.0001
    a = 0
    b = 25

    if f(a, n) * f(b, n) > 0:
        print("Fehler: Kein gültiges Intervall.")
        return

    iterationen = []
    c_werte = []
    genauigkeiten = []

    x_werte = np.linspace(a, b, 400)
    y_werte = f(x_werte, n)

    iteration = 0

    while True:
        c = (a + b) / 2
        fc = f(c, n)
        iteration += 1

        iterationen.append(iteration)
        c_werte.append(c)
        genauigkeiten.append(abs(fc))

        # Diagramm aktualisieren
        plt.clf()

        # 1. Diagramm: Funktion und aktueller Näherungswert
        plt.subplot(3, 1, 1)
        plt.plot(x_werte, y_werte, label="f(x) = x² - n")
        plt.axhline(0, color="black", linewidth=1)
        plt.axvline(c, linestyle="--", label=f"c = {c:.5f}")
        plt.scatter(c, fc)
        plt.title("Bisektionsverfahren")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)

        # 2. Diagramm: Genauigkeit
        plt.subplot(3, 1, 2)
        plt.plot(iterationen, genauigkeiten, marker="o")
        plt.title("Aktuelle Genauigkeit je Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("|f(c)|")
        plt.grid(True)

        # 3. Diagramm: aktuelle Lösung c
        plt.subplot(3, 1, 3)
        plt.plot(iterationen, c_werte, marker="o")
        plt.title("Aktuelle Lösung je Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("c")
        plt.grid(True)

        plt.tight_layout()          # Optimiert die Anordnung der Diagramme, damit sie nicht überlappen und gut lesbar sind.
        plt.pause(0.7)              # Pausiert die Ausführung für 0.7 Sekunden, um die Diagramme anzuzeigen, bevor sie aktualisiert werden. Dies ermöglicht es dem Benutzer, die Entwicklung der Lösung und der Genauigkeit im Laufe der Iterationen zu verfolgen.

        if abs(fc) < epsilon:
            break

        if f(a, n) * fc < 0:
            b = c
        else:
            a = c

    print("Ergebnis der Bisektion")
    print("n =", n)
    print("Epsilon =", epsilon)
    print("Nullstelle:", c)
    print("Analytische Lösung:", np.sqrt(n))
    print("Iterationen:", iteration)
    print("Abweichung:", abs(c - np.sqrt(n)))

    plt.show()                  # Zeigt die finalen Diagramme an, nachdem die Bisektion abgeschlossen ist, damit der Benutzer die Ergebnisse und die Entwicklung der Lösung sehen kann.


if __name__ == "__main__":
    plotter()