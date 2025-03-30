a = float(input("Inserisci il valore di a: "))
b = float(input("Inserisci il valore di b: "))

if a > b:
    c = (a**2 - b**2) ** (1/2)
    print("Il valore di c è:", c)
else:
    print("Errore")