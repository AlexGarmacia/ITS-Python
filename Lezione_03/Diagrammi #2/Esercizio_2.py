# Lettura del numero di veicoli in entrambe le direzioni
nord_sud:int = int(input("Inserisci il numero di veicoli nella direzione Nord-Sud: "))
est_ovest:int = int(input("Inserisci il numero di veicoli nella direzione Est-Ovest: "))
# Soglia definita
soglia:int = 70

# Calcolo del tempo di segnalazione in base alle condizioni
if nord_sud > soglia and est_ovest > soglia:
    time_ns:int = 50
    time_eo:int = 50
elif nord_sud > soglia:
    time_ns:int = 60
    time_eo:int = 40
elif est_ovest > soglia:
    time_ns:int = 40
    time_eo:int = 60
else:
    time_ns:int = (nord_sud / (nord_sud + est_ovest)) * 100
    time_eo:int = (est_ovest / (nord_sud + est_ovest)) * 100

# Stampa dei risultati
print(f"Il tempo assegnato alla direzione Nord-Sud è: {time_ns:.2f} secondi")
print(f"Il tempo assegnato alla direzione Est-Ovest è: {time_eo:.2f} secondi")