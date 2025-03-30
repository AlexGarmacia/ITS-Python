# Chiede all'utente di inserire un numero intero n
n:int = int(input("Inserisci il numero di iterazioni: "))

for i in range(n):
  # Chiede all'utente di inserire due numeri x e y
  x:float = float(input("Inserisci il valore di x: "))
  y:float = float(input("Inserisci il valore di y: "))

  # Verifica le condizioni sui valori di x e y
  if x > 0 and y > 0:
    result:float = x * y
  elif x < 0 and y < 0:
    print("errore")
    continue
  else:
    result:float = x - y

  # Stampa il risultato
  print("Risultato:", result)
