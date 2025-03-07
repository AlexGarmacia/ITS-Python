while True:
    parole:str=input("Inserisci una parola:") #chiede l'input
    
    if parole == "fine": #quando viene digitato"fine" va avanti
        break 
if parole [0] == parole[-1]: #il carattere
    print(f"La parola {parole} ha il primo e ultimo carattere uguali")
else:
    print(f"la parole {parole} non ha il primo e ultimo carattere uguali")
