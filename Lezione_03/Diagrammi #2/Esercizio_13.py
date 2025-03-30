while True:
  # Chiede all'utente di inserire un intero positivo x
  x:int = int(input("Inserisci il valore di x: "))
  
  if x > 0:
    break
  else:
    print("x deve essere intero e positivo.")
  

while True:
  # Chiede all'utente di inserire un intero positivo y
  y:int = int(input("Inserisci il valore di y: "))
  
  if y > 0:
    break
  else:
    print("y deve essere intero e positivo.")

while True:
  # Chiede all'utente di inserire un intero positivo z
  z:int = int(input("Inserisci il valore di z: "))
  
  if z > 0:
    break
  else:
    print("z deve essere intero e positivo.")

# Verifica delle condizioni finali
if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
  print("Regole rispettate")
else:
  print("Regole non rispettate")