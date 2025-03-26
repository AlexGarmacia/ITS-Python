def remove_duplicates(lista) -> list:
    # definisci i parametri, cancella pass e scrivi il tuo codice
    risultati:list= [] # lista vuota per contenere l'output
    for elemento in lista:
        if elemento not in risultati:
            risultati.append(elemento)
    return risultati
        

  
    