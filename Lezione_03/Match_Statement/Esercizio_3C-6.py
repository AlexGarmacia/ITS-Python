mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]

habitats = {"terra", "aria", "acqua"}

# Inserimento dati
target_animal = input("Digita il nome di un animale: ").strip().lower()
target_habitat = input(f"Digita l'habitat in cui vive l'animale {target_animal}: ").strip().lower()

# Determinazione della categoria dell'animale
animal_type = "unknown"
if target_animal in mammiferi:
    animal_type = "Mammiferi"
elif target_animal in rettili:
    animal_type = "Rettili"
elif target_animal in uccelli:
    animal_type = "Uccelli"
elif target_animal in pesci:
    animal_type = "Pesci"

# Creazione del dizionario dell'animale
animal_data = {
    "nome": target_animal,
    "categoria": animal_type,
    "habitat": target_habitat
}

# Definizione compatibilità habitat
compatibility = {
    "Mammiferi": {"cane": {"terra"}, "gatto": {"terra"}, "cavallo": {"terra"}, "elefante": {"terra"}, "leone": {"terra"}, "balena": {"acqua"}, "delfino": {"acqua"}},
    "Rettili": {"serpente": {"terra"}, "lucertola": {"terra"}, "tartaruga": {"terra", "acqua"}, "coccodrillo": {"terra", "acqua"}},
    "Uccelli": {"aquila": {"aria", "terra"}, "pappagallo": {"aria", "terra"}, "gufo": {"aria", "terra"}, "falco": {"aria", "terra"}, "cigno": {"acqua", "terra"}, "anatra": {"acqua", "terra"}, "gallina": {"terra"}, "tacchino": {"terra"}},
    "Pesci": {"squalo": {"acqua"}, "trota": {"acqua"}, "salmone": {"acqua"}, "carpa": {"acqua"}}
}

# Output della classificazione
if animal_type == "unknown":
    print(f"Non so dire in quale categoria classificare l'animale {target_animal}!")
else:
    print(f"{target_animal.capitalize()} appartiene alla categoria dei {animal_type}!")

# Controllo habitat
if target_habitat not in habitats:
    print(f"Non sono in grado di fornire informazioni sull'habitat {target_habitat}.")
elif animal_type in compatibility and target_animal in compatibility[animal_type]:
    if target_habitat in compatibility[animal_type][target_animal]:
        print(f"L'animale {target_animal} è uno dei {animal_type.lower()} che può vivere in {target_habitat}!")
    else:
        print(f"Non ho mai visto l'animale {target_animal} vivere nell'habitat {target_habitat}.")
else:
    print("Non ho informazioni su questo animale.")
