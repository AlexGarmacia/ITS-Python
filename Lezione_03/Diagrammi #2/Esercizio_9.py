import sys

while True:
    n:int = int(input("Inserisci un numero intero positivo: "))

    if n > 0:
      break
    else:
      print("Errore: n deve essere positivo.")
      sys.exit()

# Inizializzazione delle variabili
cont:int = 0

# Ciclo per 10 iterazioni
for i in range(10):
    # Lettura del valore x
    x:int = int(input(f"Inserisci il valore {i + 1}: "))

    # Controllo se x è divisibile per n
    if x % n == 0:
        cont += 1

# Stampa del risultato
print(f"Il numero di valori multipli di {n} è: {cont}")