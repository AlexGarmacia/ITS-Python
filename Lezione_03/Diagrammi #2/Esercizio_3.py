# Lettura del nome del corso
nome_corso:str = input("Inserisci il nome del corso: ")
# Inizializzazione del numero massimo di posti disponibili
max_posti:int = 100

while True:
    # Lettura dell'opzione
    opzione:str = input("Scegli un'opzione (iscrivi/annulla/visualizza/elimina/esci): ").lower()

    match opzione:
        case "iscrivi":
            if max_posti > 0:
                max_posti -= 1
                print(f"Iscrizione effettuata con successo al corso {nome_corso}.")
            else:
                print("Non ci sono posti disponibili.")

        case "annulla":
            if max_posti < 100:
                max_posti += 1
                print(f"Annullamento effettuato con successo per il corso {nome_corso}.")
            else:
                print("Tutti i posti sono già disponibili.")

        case "visualizza":
            print(f"Posti disponibili per {nome_corso}: {max_posti}")
            print(f"Posti occupati: {100 - max_posti}")

        case "elimina":
            print(f"Il corso {nome_corso} è stato eliminato.")
            # Reimposta il numero di posti e chiede un nuovo corso
            max_posti = 100
            nome_corso = input("Inserisci il nuovo nome del corso: ")
            print(f"Nuovo corso creato: {nome_corso}")

        case "esci":
            print("Uscita dal sistema.")
            break

        case _:
            print("Opzione non valida. Riprova.")