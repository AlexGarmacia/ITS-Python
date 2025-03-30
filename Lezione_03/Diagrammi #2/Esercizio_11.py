# Chiede all'utente di inserire un numero intero
n:int = int(input("Inserisci un numero: "))

# Controlla se il numero è pari e maggiore di 10
if n % 2 == 0 and n > 10:
  print("Numero valido")
else:
  print("Numero non valido")