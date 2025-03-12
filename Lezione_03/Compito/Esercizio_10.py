numeri = []
numeri_pari = []
numeri_dispari = {}

# Inserimento numeri dall'utente
while True:
    num = int(input("Inserisci un numero (0 per terminare): "))
    if num == 0:
        break  # Termina l'inserimento se l'utente digita 0
    numeri.append(num)

    # Controlla se è pari o dispari
    if num % 2 == 0:
        numeri_pari.append(num)
    else:
        numeri_dispari[num] = numeri_dispari.get(num, 0) + 1  # Conta la frequenza dei dispari

# Calcolo della somma dei numeri pari
somma_pari = sum(numeri_pari)

# Calcolo della media dei numeri dispari
if numeri_dispari:
    media_dispari = sum(numeri_dispari.keys()) / len(numeri_dispari)
else:
    media_dispari = 0

# Trova il numero più frequente
if numeri:
    frequenze = {}
    for num in numeri:
        frequenze[num] = frequenze.get(num, 0) + 1

    max_frequenza = max(frequenze.values())
    numeri_piu_frequenti = [num for num, freq in frequenze.items() if freq == max_frequenza]
else:
    numeri_piu_frequenti = []

# Stampa i risultati
print(f"\nSomma dei numeri pari: {somma_pari}")
if numeri_dispari:
    print(f"Media dei numeri dispari: {round(media_dispari, 2)}")
else:
    print("Nessun numero dispari inserito.")

if numeri_piu_frequenti:
    print(f"Numero più frequente: {', '.join(map(str, numeri_piu_frequenti))} ({max_frequenza} volte)")
else:
    print("Nessun numero inserito.")
