import matplotlib.pyplot as plt
import numpy as np


def f(x: float, n: float) -> float:
    """Berechnet f(x) = x² - n."""
    return x**2 - n


def plotter() -> None:
    """Visualisiert Bisektion und Regula falsi."""

    n = 25                  # Zahl, aus der die Wurzel berechnet wird
    epsilon = 0.0001        # Genauigkeit, bei der abgebrochen wird

    # Startintervall für Bisektion
    a_bis = 0
    b_bis = 25

    # Startintervall für Regula falsi
    a_reg = 0
    b_reg = 25

    # Prüft, ob im Intervall eine Nullstelle liegen kann
    if f(a_bis, n) * f(b_bis, n) > 0:
        print("Fehler: Kein gültiges Intervall.")
        return

    # Listen für die Werte der Animation
    iterationen = []
    c_bis_werte = []
    c_reg_werte = []
    genauigkeit_bis = []
    genauigkeit_reg = []

    # Werte für den Funktionsgraphen
    x_werte = np.linspace(0, 25, 400)
    y_werte = f(x_werte, n)

    iteration = 0

    while True:
        iteration += 1

        # Bisektion: Mittelpunkt des Intervalls berechnen
        c_bis = (a_bis + b_bis) / 2
        fc_bis = f(c_bis, n)

        # Regula falsi: neue Grenze mit Sekantenformel berechnen
        fa_reg = f(a_reg, n)
        fb_reg = f(b_reg, n)
        c_reg = b_reg - fb_reg * (b_reg - a_reg) / (fb_reg - fa_reg)
        fc_reg = f(c_reg, n)

        # Aktuelle Werte speichern
        iterationen.append(iteration)
        c_bis_werte.append(c_bis)
        c_reg_werte.append(c_reg)
        genauigkeit_bis.append(abs(fc_bis))
        genauigkeit_reg.append(abs(fc_reg))

        # Alte Zeichnung löschen, damit die Animation neu gezeichnet wird
        plt.clf()

        # Erstes Diagramm: Funktion und aktuelle Näherungen
        plt.subplot(3, 1, 1)
        plt.plot(x_werte, y_werte, label="f(x) = x² - n")
        plt.axhline(0, color="black", linewidth=1)
        plt.scatter(c_bis, fc_bis, label="Bisektion")
        plt.scatter(c_reg, fc_reg, label="Regula falsi")
        plt.title("Nullstellenfindung")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)

        # Zweites Diagramm: Genauigkeit der beiden Verfahren
        plt.subplot(3, 1, 2)
        plt.plot(iterationen, genauigkeit_bis, marker="o", label="Bisektion")
        plt.plot(iterationen, genauigkeit_reg, marker="x", label="Regula falsi")
        plt.title("Genauigkeit je Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("|f(c)|")
        plt.legend()
        plt.grid(True)

        # Drittes Diagramm: Annäherung an die Lösung
        plt.subplot(3, 1, 3)
        plt.plot(iterationen, c_bis_werte, marker="o", label="Bisektion")
        plt.plot(iterationen, c_reg_werte, marker="x", label="Regula falsi")
        plt.title("Lösung je Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("c")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()      # Diagramme ordentlich anordnen
        plt.pause(0.7)          # Kurze Pause für die Animation

        # Intervall der Bisektion aktualisieren
        if f(a_bis, n) * fc_bis < 0:
            b_bis = c_bis
        else:
            a_bis = c_bis

        # Intervall von Regula falsi aktualisieren
        if f(a_reg, n) * fc_reg < 0:
            b_reg = c_reg
        else:
            a_reg = c_reg

        # Abbruch, wenn beide Verfahren genau genug sind
        if abs(fc_bis) < epsilon and abs(fc_reg) < epsilon:
            break

    print("--------------------------------")
    print("n =", n)
    print("Epsilon =", epsilon)
    print("Analytische Lösung:", np.sqrt(n))
    print("Bisektion:", c_bis)
    print("Regula falsi:", c_reg)
    print("Iterationen:", iteration)

    plt.show()


if __name__ == "__main__":
    plotter()