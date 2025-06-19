def leggi_intero_positivo(prompt):
    while True:
        valore = input(prompt)
        if valore.isdigit():
            numero = int(valore)
            return numero
        else:
            print("Devi inserire un numero intero positivo!")

x = leggi_intero_positivo("Inserisci il numero x (intero positivo): ")

sequenza = []
while True:
    num = leggi_intero_positivo("Inserisci un numero della sequenza (0 per terminare): ")
    if num == 0:
        break
    sequenza.append(num)

print("\nSequenza inserita:", sequenza)

occorrenze = sequenza.count(x)
if occorrenze > 0:
    posizione = sequenza.index(x)
    print(f"Il numero {x} compare {occorrenze} volta{'e' if occorrenze > 1 else ''} nella sequenza")
    print(f"Il numero {x} compare per la prima volta in posizione {posizione} nella sequenza")
else:
    print(f"Il numero {x} non compare nella sequenza")

somma_diversi = sum(num for num in sequenza if num != x)
print(f"La somma dei valori della sequenza diversi da {x} è {somma_diversi}")
