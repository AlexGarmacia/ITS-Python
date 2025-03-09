def calcola_fattoriale(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcola_fattoriale(n - 1)

numero = int(input("Inserisci un numero intero positivo: "))

if numero < 0:
    print("Per favore inserisci un numero positivo.")
else:
    risultato = calcola_fattoriale(numero)
    print(f"Il fattoriale di {numero} è {risultato}")  
