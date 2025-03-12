# Chiede all'utente di inserire 5 numeri
numeri = []
for i in range(5):
    num = int(input(f"Inserisci un numero tra 1 e 30 ({i+1}/5): "))
    while num < 1 or num > 30:  # Controlla che il numero sia nel range corretto
        print("Numero non valido! Deve essere tra 1 e 30.")
        num = int(input(f"Inserisci un numero tra 1 e 30 ({i+1}/5): "))
    numeri.append(num)

# Stampa il grafico a barre
print("\nGrafico a barre:")
for num in numeri:
    print("*" * num)
