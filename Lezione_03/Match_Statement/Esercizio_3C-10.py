giorno=int(input("Inserisci il giorno:"))
mese=int(input("Inserisci il mese:"))

data = (giorno, mese) #tupla per salvare le coordinate

match data:
    case (1,1):
        print("Oggi è capodanno")
    case (14,2):
        print("Oggi è San Valentino")
    case (2,6):
        print("Oggi è Festa della Repubblica")
    case (15,8):
        print("Oggi è Ferragosto")
    case (31,10):
        print("Oggi è Halloween")
    case (25,12):
        print("Oggi è Natale")
    case _:
        print(f"Nessuna festività per questa data")
    
    