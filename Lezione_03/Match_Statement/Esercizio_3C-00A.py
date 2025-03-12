#Esercizio 3C-00A
numero_neonati = int(input("Inserire il numero di neonati:"))
match numero_neonati:
    case 1:
        print("Congrazioni")
    case 2:
        print("Wow! Gemelli")
    case 3:
        print("Wow! Tre!")
    case 4: 
        print("Mamma mia quattro! Wow")
    case 5:
        print("Incredibile! Cinque!")
    case _:
        print(f"Non ci credo! {numero_neonati} bambini")
