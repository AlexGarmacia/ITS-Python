soglia = int(input("Inserisci il valore della soglia: ")) 

numeri_maggiori = []

for _ in range(7):
    numero = int(input("Inserisci un numero: "))
    
    if numero > soglia:
        numeri_maggiori.append(numero)

if numeri_maggiori:
    print("I numeri maggiori della soglia sono:", numeri_maggiori)
else:
    print("Nessun numero è maggiore della soglia.")
