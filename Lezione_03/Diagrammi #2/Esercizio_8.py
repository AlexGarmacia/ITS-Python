# Lettura dei valori di A e B
A:int = int(input("Inserisci il valore di A: "))
B:int = int(input("Inserisci il valore di B: "))

if A < B:
  if A > 0 and B > 0:
    # Inizializzazione della somma
    somma:int = 0

    # Calcolo della somma degli interi tra A e B
    for i in range(A, B + 1):
        somma += i

    # Stampa del risultato
    print(f"La somma degli interi tra {A} e {B} è: {somma}")
  else:
    print("Errore: A e B devono essere positivi.")
else:
  print("Errore: A deve essere minore di B.")