# Legge il valore della soglia
soglia = float(input("Inserisci il valore della soglia: "))

# Iterazione per 7 volte
for cont in range(7):
    # Legge il numero
    n = float(input("Inserisci un numero: "))
    # Se il numero è maggiore della soglia, lo stampa
    if n > soglia:
        print(f"Numero maggiore della soglia: {n}")