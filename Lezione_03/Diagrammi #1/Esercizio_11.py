# Inizializzazione del numero di posti liberi
liberi = 20
while True:
    # Lettura dell'opzione
    opzione = str(input("Scegli un'opzione (prenota/libera/visualizza/esci): ")).lower()

    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
                print("Posto prenotato con successo.")
            else:
                print("Non ci sono posti disponibili.")

        case "libera":
            if liberi < 20:
                liberi += 1
                print("Posto liberato con successo.")
            else:
                print("Tutti i posti sono già disponibili.")

        case "visualizza":
            print(f"Posti disponibili: {liberi}")
            print(f"Posti occupati: {20 - liberi}")

        case "esci":
            print("Uscita dal sistema.")
            break

        case _:
            print("Opzione non valida. Riprova.")