'''Scrivere un esercizio che somma i numeri da 1 a 10, da 20 a 37 
e da 35 a 49 utilizzando i cicli

Esempio: calcolare la somma dei numeri, da 1 a 10, da 20 a 37 e da 35 a 49.
Expected output:
la somma degli interi da 1 a 10 è 55
la somma degli interi da 20 a 37 è 513
la somma degli interi da 35 a 49 è 630 '''
#Si inizia inizializzando la variabile somma a 0 per ogni ciclo
somma = 0 #somma da 1 a 10
for n in range(1, 11):
    somma+= n
print(f"La somma da 1 a 10 è: {somma}")

somma = 0 #somma da 20 a 37
for n in range(20, 38): 
    somma += n
print(f"La somma da 20 a 37 è: {somma}")

somma = 0 #somma da 35 a 49
for n in range(35, 50): 
    somma += n
print(f"La somma da 35 a 49 è: {somma}")

#Rifacciamo l'esercizio utilizzando una funzione
def sum(a:int, b:int): 
	sum:int = 0
	for i in range(a, b+1):
		sum = sum + i
	return sum
print(f"la somma da 1 a 10 è {sum(1,10)}")
print(f"la somma da 20 a 37 è {sum(20,37)}")
print(f"la somma da 35 a 49 è  {sum(35,49)}")


''' Proviamo a definire una funzione chiamata subtract:
● Dovrebbe accettare 2 parametri.
● All'interno della funzione, dovrebbe sottrarre i due.
● Quindi, restituire il risultato.
Dopo averla definita, chiama la funzione con alcuni argomenti! '''

def sottrazione(a,b):  #definiamo la funzione, con i valori che prende in input
      risultato = a-b  #definiamo l'operazione che deve fare
      return risultato

#chiamiamo la funzione e assegnamo i valori
print(f"il risultato è: {sottrazione(10,5)}") 
print(f"il risultato è: {sottrazione(20,5)}")
print(f"Il risultato è: {sottrazione(100,50)}") 
