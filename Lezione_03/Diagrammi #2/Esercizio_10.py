# Chiede all'utente di inserire la propria età e la converte in un numero intero
eta:int = int(input("Inserisci la tua età: "))

# Controlla se l'età rientra nel range consentito (18-65 anni inclusi)
if 18 <= eta <= 65:
    print("Puoi partecipare all'attività")
else:
    # Se l'età è inferiore a 18, stampa un messaggio di errore specifico
    if eta < 18:
        print("Non puoi partecipare all'attività perché non hai raggiunto l'età minima richiesta")
    # Se l'età è superiore a 65, stampa un altro messaggio di errore
    else:
        print("Non puoi partecipare all'attività perché hai superato l'età massima consentita")