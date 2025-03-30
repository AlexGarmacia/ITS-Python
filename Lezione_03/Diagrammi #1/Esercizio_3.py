sum_value = 0
cont = 0

while True: # Ciclo per 5 iterazioni
    n = float(input("Inserisci un numero: "))  # Legge il numero
    if n > 0:  # Se il numero è positivo, lo aggiunge alla somma
        sum_value += n
    cont += 1  # Incrementa il contatore
    if cont == 5:
        break

print("La somma dei numeri positivi è:", sum_value)