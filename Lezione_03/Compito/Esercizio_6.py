n1 = int(input("Inserisci il primo numero intero:"))
n2 = int(input("Inserisci il secondo numero intero:"))
prodotto = 1 #variabile prodotto inizializzata a 1

if n1 <= n2: #caso 1
    for i in range(n1,n2 + 1): #intera da n1 a n2 (inclusi)
        prodotto *= i
else: #caso 2
    for i in range (n2,n1 +1): #intera da n2 a n1 (inclusi)
        prodotto *= 1
print("il prodotto dei numero compreso tra", n1, "e", n2 "e", prodotto)
