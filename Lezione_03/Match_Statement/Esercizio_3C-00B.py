#Esercizio 3C-00B
nome=input("inserire il nome:")
genere=input("inserire il genere, m per maschio, f per femmina:")

match genere:
    case "m":
        print(f"Nome: {nome}")
        print("genere: Maschio")
    case "f":
        print(f"Nome: {nome}")
        print("genere: Femmina")
    case _:
        print(f"mi dispiace {nome}, non è possibile procedere")     