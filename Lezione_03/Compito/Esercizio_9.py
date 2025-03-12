pi_greco = 0
segno = 1  # Alterna tra +1 e -1
denominatore = 1
termini = 0

# Soglie di precisione richieste
soglie = [3.14, 3.141, 3.1415, 3.14159]
risultati = {}

# Ciclo finché non troviamo tutti i valori richiesti
for soglia in soglie:
    while round(pi_greco, len(str(soglia)) - 2) != soglia:  
        pi_greco += segno * (4 / denominatore)
        segno *= -1  # Cambia segno
        denominatore += 2
        termini += 1
    risultati[soglia] = termini  # Salva il numero di termini trovati

# Stampa i risultati
for soglia, num_termini in risultati.items():
    print(f"Per ottenere π ≈ {soglia} servono {num_termini} termini.")
