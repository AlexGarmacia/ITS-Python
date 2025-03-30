città = {
    "Roma": {
        "paese": "Italia",
        "popolazione": 2873000,
        "fatto": "Roma è conosciuta come la 'Città Eterna' per la sua lunga storia che risale a più di 2.500 anni.",
        "clima": "Mediterraneo",
        "moneta": "Euro"
    },
    "New York": {
        "paese": "Stati Uniti",
        "popolazione": 8419600,
        "fatto": "New York è famosa per la Statua della Libertà, simbolo di libertà e accoglienza.",
        "clima": "Continental",
        "moneta": "Dollaro USA"
    },
    "Tokyo": {
        "paese": "Giappone",
        "popolazione": 13929286,
        "fatto": "Tokyo è una delle città più popolose del mondo e un centro globale per tecnologia e cultura.",
        "clima": "Temperato",
        "moneta": "Yen"
    }
}

for città_nome, info in città.items():
    print(f"\n{'-'*40}")
    print(f"Informazioni su {città_nome}:")
    print(f"{'-'*40}")
    print(f"Città: {città_nome}")
    print(f"  Paese: {info['paese']}")
    print(f"  Popolazione: {info['popolazione']:,}")  
    print(f"  Clima: {info['clima']}")
    print(f"  Moneta: {info['moneta']}")
    print(f"  Fatto interessante: {info['fatto']}")
    print(f"{'-'*40}")
