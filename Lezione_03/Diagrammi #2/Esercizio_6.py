# Lettura del valore di x
x:float = float(input("Inserisci un valore positivo per x: "))

# Controllo se x è positivo
if x > 0:
    # Inizializzazione delle variabili
    somma:int = 0

    # Ciclo per 10 iterazioni
    for i in range(10):
        # Lettura del valore n
        n:int = int(input(f"Inserisci il valore {i + 1}: "))

        # Controllo della parità di x
        if x % 2 == 0:
            if n > x / 2:
                somma += n
        else:
            if n < x:
                somma += n

    # Stampa del risultato
    print(f"La somma calcolata è: {somma}")
else:
  print("Errore, x deve essere positivo.")
    