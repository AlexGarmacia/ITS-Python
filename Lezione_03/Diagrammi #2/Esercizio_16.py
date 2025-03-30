# Inizializzazione dei contatori
dispari:int = 0
pari:int = 0
negativi:int = 0
positivi:int = 0

# Ciclo per leggere 10 numeri
for i in range(10):
    while True:
      # Chiede all'utente di inserire un numero intero
      n:int = int(input("Inserisci un numero intero: "))

      if n != 0:
        break

    # Se n è maggiore di 0    
    if n > 0:
      # Incrementa il contatore dei numeri positivi 
      positivi += 1
      # Se n è pari e maggiore di 20, incrementa il contatore dei numeri pari
      if n % 2 == 0 and n > 20:
        pari += 1
    else:
      # Altrimenti, incremente il contatore dei numeri negativi
      negativi += 1
      # Se n è dispari e minore di -10, incrementa il contatore dei numeri dispari
      if n % 2 != 0 or n < -10:
        dispari += 1

# Stampa i risultati
print("Positivi:", positivi)
print("Negativi:", negativi)
print("Pari:", pari)
print("Dispari:", dispari)