# Lettura del numero massimo di posti disponibili
max_posti:int = int(input("Inserisci il numero massimo di posti disponibili: "))
# Inizializzazione dei posti liberi
liberi:int = max_posti

while True:
    # Lettura dell'opzione
    opzione:str = input("Scegli un'opzione (ingresso/uscita/stato/esci): ").strip().lower()

    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
                print("Ingresso effettuato con successo.")
            else:
                print("Non ci sono posti disponibili.")

        case "uscita":
            if liberi < max_posti:
                liberi += 1
                print("Uscita registrata con successo.")
            else:
                print("Tutti i posti sono già disponibili.")

        case "stato":
            print(f"Posti disponibili: {liberi}")
            print(f"Posti occupati: {max_posti - liberi}")

        case "esci":
            print("Uscita dal sistema.")
            break

        case _:
            print("Opzione non valida. Riprova.")