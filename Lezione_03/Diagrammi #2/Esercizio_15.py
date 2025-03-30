import sys

while True:
  # Legge il numero intero n
  n:int = int(input("Inserisci un numero intero tra 1 e 100: "))

  # se n è compreso tra 1 e 100
  if n > 0 and n <= 100:
    somma:int = 0 # inizializza la somma
    for i in range(1,n+1):
      # Calcola la somma di tutti i valori pari tra 1 e n
      if i % 2 == 0:
        somma += i
    break
  # se n è 0 o negativo
  elif n == 0 or n < 0:
    print("errore")
    sys.exit() # interrompe l'esecuzione del programma
  # se n è maggiore di 100
  else:
    somma:int = 0 # inizializza la somma
    for i in range(1,n+1):
      # Calcola la somma di tutti i valori dispari tra 1 e n
      if i % 2 != 0:
        somma += i
    break

print("Somma: ", somma)