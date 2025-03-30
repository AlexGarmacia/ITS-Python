# Lettura del numero intero positivo
n:int = int(input("Inserisci un numero intero positivo: "))

# Controllo se n è un intero positivo
if n > 0:
    # Inizializzazione della somma
    somma:int = 0

    # Calcolo della somma dei quadrati con un ciclo for
    for i in range(1, n + 1):
        somma += i * i

    # Stampa del risultato
    print(f"La somma dei quadrati fino a {n} è: {somma}")
else:
    print("Errore, n deve essere intero e positivo.")