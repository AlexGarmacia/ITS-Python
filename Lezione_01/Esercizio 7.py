#Inizializzazione contatori pari e dispari
pari = 0
dispari = 0

for _ in range(10): #ciclo for che chiede di inserire 10 numeri
    numero = int(input("Inserisci un numero: "))
    
    # Verifico se il numero è pari o dispari
    if numero % 2 == 0:
        pari += 1
    else:
        dispari += 1

# Stampo il risultato
print("Numeri pari:", pari)
print("Numeri dispari:", dispari)
