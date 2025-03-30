frase=str(input("Inserisci una frase: "))

match frase:
    case _ if frase.endswith("?") and len(frase) % 2 == 0:
        print("Si")
    case _ if frase.endswith("?") and len(frase) % 2 == 1:
        print("No")
    case _ if frase.endswith("!"):
        print("Wow!")
    case _:
        print(f'Tu dici "{frase}"')
