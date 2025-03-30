print("Inserire se è uscito testa o croce")

testa = 0
croce = 0

testa = 0
croce = 0

for i in range(8):
    while True:  # Ripete finché l'utente non inserisce un valore corretto
        risultato = input(f"Lancio {i+1} (inserisci 't' per testa o 'c' per croce): ").strip().lower()
        match risultato:
            case "t":
                testa += 1
                break  # Esce dal while e passa al lancio successivo
            case "c":
                croce += 1
                break
            case _:
                print("Errore! Devi inserire solo 't' o 'c'. Riprova.")

# Calcolo percentuali
percent_testa = (testa / 8) * 100
percent_croce = (croce / 8) * 100

# Output finale
print(f"\nTotale 'testa': {testa}")
print(f"Percentuale 'testa': {percent_testa:.2f}%")
print(f"Totale 'croce': {croce}")
print(f"Percentuale 'croce': {percent_croce:.2f}%")



