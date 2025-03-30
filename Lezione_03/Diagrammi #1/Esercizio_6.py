# Richiede l'inserimento di un numero positivo
while True:
    n = int(input("Inserisci un numero positivo: "))
    if n > 0:
        break
    print("Errore: Il numero deve essere positivo.")

# Calcolo del fattoriale usando un ciclo for
fattoriale = 1
for i in range(1, n + 1):
    fattoriale *= i
# Stampa il risultato
print(f"Il fattoriale di {n} è: {fattoriale}")
