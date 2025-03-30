# Lettura dei dati in input
r = float(input("Inserisci il reddito annuale: "))
m = float(input("Inserisci la media dei voti: "))

# Controllo delle condizioni per l'assegnazione della borsa di studio
if r < 20000 and m > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)")