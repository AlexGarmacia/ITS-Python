#inizializzazione delle liste a e b
n = int (input("inserisci la lunghezza delle liste:"))
a = []
b = []
for i in range(n):
    a.append(int(input(f"Inserisci l'elemento {i+1} della lista a:")))
    b.append(int(input(f"Inserisci l'elemento {i+1} della lista b:")))
#calcolo della somma incrociata e memorizzazione nella lista c
c = []
for i in range(n):
    somma_incrociata = a[i] + b[n - 1 - i] #calcola la somma incrociata
    c.append(somma_incrociata) #aggiunge la somma alla lista c

#visualizzazione delle liste
print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)
