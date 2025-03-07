N = int(input("Inserisci il budget:"))
barrette_acquistate = N #numero iniziale di barrette acquistabili
buoni_sconto = N #numero di buoni sconto iniziali

#ciclo while sulle barrette da prendere prima di ottenere quella gratuita
while buoni_sconto >= 6:
    barrette_gratuite = buoni_sconto // 6
    barrette_acquistate += barrette_gratuite
    buoni_sconto = buoni_sconto % 6 + barrette_gratuite

print(f"Numero totale di barrette acquistabili: {barrette_acquistate}")
print(f"Buoni sconto: {buoni_sconto}")

