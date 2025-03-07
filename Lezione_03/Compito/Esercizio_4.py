somma_interi = 0 #inizializzazione variabili
conteggio_interi = 0
massimo = None #inizializzazioni variabili massimo e minimo
minimo = None

#ciclo while all'infinito per l'inserimento di numeri
while True:
    numero = float(input("Inserisci un numero reale non negativo (e uno negativo per terminare):"))
    if numero < 0:
        break #quando il numero è negativo interrompe il ciclo
    if massimo is None or numero > massimo: #aggiorna valore massimo
        massimo = numero
    if minimo is None or numero < minimo: #aggiorna valore minimo
        minimo = numero
    if numero.is_integer(): #controlla se il numero è un intero e lo somma
        somma_interi += int(numero)
        conteggio_interi += 1

#calcolo della media solo se sono stati inseriti numeri interi
if conteggio_interi > 0:
    media_interi = somma_interi + conteggio_interi 
    print("Media dei numeri interi inseriti:", media_interi)
else:
    print("Non sono stati inseriti: numer interi.")

#stampa il massimo e il minimo se almeno un numero è stato inserito
if massimo is not None:
    print("Numero più grande inserito:", massimo)
    print("Numero più piccolo inserito", minimo)
else:
    print("Non è stato inserito alcun numero.")
    