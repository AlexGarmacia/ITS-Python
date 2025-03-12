#Esercizio 3-8
luoghi:list=["Roma","Venezia","Milano","Firenze","Napoli"]
print("lista originale:")
print(luoghi)

print("\nlista in ordine alfabetico(senza modificare la lista)")
print(sorted(luoghi)) #stampa la lista in ordine alfabetico

print("\nlista originale dopo sorted():")
print(luoghi)

print("\nlista in ordine alfabetico inverso ")
print(sorted(luoghi, reverse=True)) #ordine alfabetico inverso

print("\nlista originale dopo sorted(reverse=True)")
print(luoghi)

luoghi.reverse() #per cambiare l'ordine della lista
print("\nlista dopo reverse():")
print(luoghi)

luoghi.reverse() #per riportarla al suo ordine originale
print("\nlista dopo il secondo reverse():")
print(luoghi)

luoghi.sort() #cambiare la lista in ordine alfabetico
print("\nlista dopo sort():")
print(luoghi)

luoghi.sort(reverse=True) #ordine alfabetico inverso
print("\nlista dopo sort(reverse=True):")
print(luoghi)