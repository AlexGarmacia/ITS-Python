# Lettura del primo record (Nome, Vendite)
nome = str(input("Inserisci il nome del venditore: "))
vendite = float(input("Inserisci il numero di vendite: "))

# Inizializzazione dei valori massimo e minimo
max_nome = nome
max_vendite = vendite
min_nome = nome
min_vendite = vendite

# Ciclo per 19 iterazioni perché un record è già stato inserito
for cont in range(19):
    # Lettura dei nuovi valori
    new_nome = str(input("Inserisci il nome del venditore: "))
    new_vendite = float(input("Inserisci il numero di vendite: "))

    # Controllo del massimo
    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite

    # Controllo del minimo
    if new_vendite < min_vendite:
        min_nome = new_nome
        min_vendite = new_vendite

# Stampa dei risultati
print(f"Il venditore con più vendite è {max_nome} con {max_vendite} vendite.")
print(f"Il venditore con meno vendite è {min_nome} con {min_vendite} vendite.")