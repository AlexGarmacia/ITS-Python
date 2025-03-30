# Inizializzazione delle variabili
cont:int = 0
somma:int = 0

while True:
    # Lettura della scelta dell'utente
    scelta:str = input("Vuoi inserire un voto? (si/no): ").lower()

    match scelta:
        case "si":
            # Lettura del voto
            voto:float = float(input("Inserisci il voto: "))

            if voto > 0:
                cont += 1
                somma += voto
            else:
                print("Errore: il voto deve essere positivo.")

        case "no":
            # Calcolo della media solo se sono stati inseriti voti
            if cont > 0:
                media:float = somma / cont
                print(f"La media dei voti è: {media:.2f}")
            else:
                print("Nessun voto inserito, impossibile calcolare la media.")
            break

        case _:
            print("Opzione non valida. Rispondi con 'si' o 'no'.")