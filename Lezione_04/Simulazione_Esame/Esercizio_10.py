def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # Crea un nuovo dizionario unendo i due con dict1 come base
    merged_dict = dict1.copy()
    
    # Itera sulle chiavi e valori di dict2
    for key, value in dict2.items():
        # Se la chiave è già presente, somma i valori
        if key in merged_dict:
            merged_dict[key] += value
        else:
            # Altrimenti, aggiungi la nuova coppia chiave-valore
            merged_dict[key] = value
    
    return merged_dict

# Esempio di utilizzo
print(merge_dictionaries({'x': 5}, {'x': -5}))  # Output: {'x': 0}
