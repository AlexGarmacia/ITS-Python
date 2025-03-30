# Legge il numero intero n
n:int = int(input("Inserisci un numero intero positivo: "))

if n > 0:
  # Controllo se n è pari o dispari
  if n % 2 == 0:
    cont:int = 4
    result:int = 0
    # Somma i numeri da 1 a n che sono divisibili per 4
    while cont <= n:
      result = result + cont
      cont = cont + 4
  else:
    cont:int = 1
    result:int = 1
    # Moltiplica i numeri dispari da 1 a n
    while cont <= n:
      result = result * cont
      cont = cont + 2

  # Stampa del risultato
  print("Risultato:", result)
else: # Se n è ngativo, mostra messaggio di errore
  print("Errore")