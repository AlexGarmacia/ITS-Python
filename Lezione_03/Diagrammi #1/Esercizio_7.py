# Inizializzazione delle variabili
pari = 0
dispari = 0

# Ciclo per 10 iterazioni
for cont in range(10):
    n = int(input("Inserisci un numero: "))  # Legge un numero
    if n % 2 == 0:  # Controlla se è pari
        pari += 1
    else:  # Se non è pari, è dispari
        dispari += 1

# Stampa i risultati
print(f"Numeri pari inseriti: {pari}")
print(f"Numeri dispari inseriti: {dispari}")