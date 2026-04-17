def f(x, n):
    return x**2 - n

def bisektion(a, b, n, epsilon):
    if f(a, n) * f(b, n) > 0:
        print("Fehler: Kein gültiges Intervall gefunden.")
        return None
    i = 0
    while True:
        c = (a + b) / 2
        i+=1

        if abs(f(c, n)) < epsilon:
            return c, i
        
        if f(a, n) * f(c, n) < 0:
            b = c
        else:
            a = c

def solver():
    try:
        n = float(input("Geben Sie die Zahl n ein, deren Quadratwurzel Sie berechnen möchten: "))
        epsilon = float(input("Geben Sie die gewünschte Genauigkeit (epsilon) ein: "))
        
        if n < 0:
            print("Fehler: n muss eine nicht-negative Zahl sein.")
            return
        if epsilon <= 0:
            print("Fehler: epsilon muss eine positive Zahl sein.")
            return
        a=0
        b = n if n > 1 else 1
        ergebnis = bisektion(a, b, n, epsilon)
        if ergebnis is not None:
            nullstelle, iterationen = ergebnis
            print("n = ", n)
            print("Epsilon = ", epsilon)
            print("Iterationen:", iterationen)
            print("nullstelle:", nullstelle)
            print("interval: [", a, ",", b, "]")
            
    except ValueError:
        print("Fehler: Bitte geben Sie gültige Zahlen ein.")

if __name__ == "__main__":
    
    solver()