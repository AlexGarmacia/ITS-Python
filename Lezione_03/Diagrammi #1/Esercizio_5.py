# Legge il numero da input
while True:
    n = int(input("Inserisci un numero positivo: "))
    if n > 0:
        break
    print("Errore: Il numero deve essere positivo.")

is_prime  = True # Variabile per tracciare se il numero è primo

# Se il numero è minore di 2, non è primo
if n < 2:
    is_prime  = False
else:
    div = 2  # Inizializza il divisore

    while div < n:  # Controlla tutti i divisori da 2 a n-1
        if n % div == 0:
            is_prime = False  # Se trova un divisore, il numero non è primo
            break
        div += 1  # Incrementa il divisore

if is_prime:
    print("Il numero è primo")
else:
    print("Il numero non è primo")

import math
# Legge il numero da input
while True:
    n = int(input("Inserisci un numero positivo: "))
    if n > 0:
        break
    print("Errore: Il numero deve essere positivo.")

is_prime = True  # Variabile per tracciare se il numero è primo

# Se il numero è minore di 2, non è primo
if n < 2:
    is_prime = False
else:
    div = 2  # Inizializza il divisore
    limit = math.sqrt(n)  # Limite superiore della ricerca dei divisori (√n)

    while div <= limit:  # Controlla solo fino a √n
        if n % div == 0:
            is_prime = False  # Se trova un divisore, il numero non è primo
            break
        div += 1  # Incrementa il divisore

if is_prime:
    print("Il numero è primo")
else:
    print("Il numero non è primo")