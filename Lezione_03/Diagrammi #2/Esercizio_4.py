# Inizializzazione delle variabili
n_tutor:int = 10  # Numero iniziale di tutor disponibili
attesa:int = 0    # Numero iniziale di studenti in attesa

while True:
    # Lettura dell'ingresso dello studente
    studente:str = input("Inserisci il nome dello studente: ")

    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con successo.")
    else:
        attesa += 1
        print("Studente in attesa.")

    # Verifica della condizione di terminazione
    if n_tutor == 0 and attesa > 50:
        print("Numero massimo di studenti in attesa raggiunto. Terminazione del programma.")
        break