# Dizionario per la prima persona
persona1 = {
    "nome": "Marco",
    "cognome": "Rossi",
    "età": 20,
    "città": "Roma"
}

# Dizionario per la seconda persona
persona2 = {
    "nome": "Giulia",
    "cognome": "Bianchi",
    "età": 25,
    "città": "Milano"
}

# Dizionario per la terza persona
persona3 = {
    "nome": "Luca",
    "cognome": "Verdi",
    "età": 30,
    "città": "Napoli"
}

persone = [persona1, persona2, persona3]

for persona in persone:
    print(f"Nome: {persona['nome']}")
    print(f"Cognome: {persona['cognome']}")
    print(f"Età: {persona['età']}")
    print(f"Città: {persona['città']}\n")
