punteggio:int = 0 # Inizializza il punteggio a 0

while punteggio < 100:
  while True:
    # Chiede all'utente di inserire un valore intero compreso tra 1 e 6
    d1:int = int(input("Inserisci il valore per il primo dado (da 1 a 6): "))

    if 1 <= d1 <= 6:
      break

  while True:
    # Chiede all'utente di inserire un valore intero compreso tra 1 e 6
    d2:int = int(input("Inserisci il valore per il secondo dado (da 1 a 6): "))

    if 1 <= d2 <= 6:
      break

  # Somma i valori inseriti
  somma:int = d1 + d2

  # Verifica delle condizioni di punteggio
  if d1 % 2 == 0 and d2 % 2 == 0 and somma == 8:
    punteggio = 100
  elif d1 == 6 or d2 == 6 or somma == 7:
    punteggio += 10
  else:
    punteggio = 0
    print("Sconfitta")
    break

  if punteggio >= 100:
    print("Vittoria")
    break
  
while True:
    while True:
      # Chiede all'utente di inserire un valore intero compreso tra 1 e 6
      d1:int = int(input("Inserisci il valore per il primo dado (da 1 a 6): "))

      if 1 <= d1 <= 6:
        break

    while True:
      # Chiede all'utente di inserire un valore intero compreso tra 1 e 6
      d2:int = int(input("Inserisci il valore per il secondo dado (da 1 a 6): "))

      if 1 <= d2 <= 6:
        break
    
    # Somma i valori inseriti
    somma:int = d1 + d2

    # Verifica delle condizioni di punteggio
    if d1 % 2 == 0 and d2 % 2 == 0 and somma == 8:
      punteggio = 100
    elif d1 == 6 or d2 == 6 or somma == 7:
      punteggio += 10
    else:
      punteggio = 0

    if punteggio >= 100 or punteggio == 0:
      if punteggio >= 100:
        print("Vittoria")
        break
      else:
        print("Sconfitta")
        break