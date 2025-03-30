# Legge il numero intero n
n:int = int(input("Inserisci il numero di iterazioni (n deve essere intero positivo): "))
        
# Inizializzazione delle variabili
somma:int = 0
media:float = 0
somma_pari:int = 0
somma_dispari:int = 0
        
# Ciclo per leggere i numeri
for i in range(n):
  x:int = int(input("Inserisci un numero intero x: "))
    
  # Somma totale
  somma += x

  # Calcolo della media
  media = somma / (i + 1)

  # Controllo e assegnazione ai gruppi pari/dispari
  if x % 2 == 0 and x > media:
    somma_pari += x
  elif x < media or x % 2 != 0:
    somma_dispari += x

# Stampa delle somme
print(f"Somma pari: {somma_pari}")
print(f"Somma dispari: {somma_dispari}")

# Confronto tra le somme
if somma_pari > somma_dispari:
  print("Somma pari è maggiore")
elif somma_dispari > somma_pari:
  print("Somma dispari è maggiore")
else:
  print("Le somme sono uguali")