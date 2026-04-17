def f(x: float, n: float) -> float:
    """Diese Funktion berechnet f(x) = x^2 - n, um die Nullstelle zu finden, die der Quadratwurzel von n entspricht."""
    return x**2 - n

def bisektion(a: float, b: float, n: float, epsilon: float):
    """Diese Funktion implementiert das Bisektionsverfahren, um die Nullstelle von f(x) = x^2 - n zu finden."""
    if f(a, n) * f(b, n) > 0:                           # Überprüfen, ob die Funktion an den Endpunkten des Intervalls unterschiedliche Vorzeichen hat
        print("Fehler: Kein gültiges Intervall gefunden.")  
        return None
    i = 0
    while True:
        c = (a + b) / 2                         # Berechnung des Mittelpunkts des Intervalls    
        i+=1                                    # Erhöhung der Iterationszähler

        if abs(f(c, n)) < epsilon:              # Überprüfen, ob die Funktion am Mittelpunkt nahe genug an Null ist
            return c, i                         # Rückgabe der Nullstelle und der Anzahl der Iterationen
        
        if f(a, n) * f(c, n) < 0:               # Überprüfen, ob die Nullstelle im linken oder rechten Teilintervall liegt
            b = c
        else:
            a = c

def solver():                               
    """Diese Funktion fordert den Benutzer auf, die Zahl n und die gewünschte Genauigkeit epsilon einzugeben, 
       und ruft dann die bisektion-Funktion auf, um die Quadratwurzel von n zu berechnen."""
    try:
        n = float(input("Geben Sie die Zahl n ein, deren Quadratwurzel Sie berechnen möchten: "))   # Eingabe der Zahl n, deren Quadratwurzel berechnet werden soll
        epsilon = float(input("Geben Sie die gewünschte Genauigkeit (epsilon) ein: "))              # Eingabe der gewünschten Genauigkeit epsilon, die bestimmt, wie nahe die Nullstelle an Null sein muss, um als Lösung akzeptiert zu werden
        
        if n < 0:
            print("Fehler: n muss eine nicht-negative Zahl sein.")                                  # Überprüfen, ob n negativ ist, da die Quadratwurzel von negativen Zahlen nicht definiert ist
            return
        if epsilon <= 0:                                                                            # Überprüfen, ob epsilon eine positive Zahl ist, da die Genauigkeit positiv sein muss
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return
        a=0
        b = n if n > 1 else 1                                                                       # Festlegen des Intervalls [a, b], wobei a = 0 und b entweder n oder 1 ist, je nachdem, ob n größer als 1 ist oder nicht    
        ergebnis = bisektion(a, b, n, epsilon)                                                      # Aufrufen der bisektion-Funktion, um die Nullstelle zu berechnen   
        if ergebnis is not None:                                                                    # Überprüfen, ob die bisektion-Funktion eine gültige Nullstelle zurückgegeben hat
            nullstelle, iterationen = ergebnis                                                      # Extrahieren der Nullstelle und der Anzahl der Iterationen aus dem Ergebnis        
            print("n = ", n)
            print("Epsilon = ", epsilon)
            print("Iterationen:", iterationen)
            print("nullstelle:", nullstelle)
            print("interval: [", a, ",", b, "]")
            print("abweichung:", abs(nullstelle**2 - n))

    except ValueError:
        print("Fehler: Bitte geben Sie gültige Zahlen ein.")

if __name__ == "__main__":
    
    solver()