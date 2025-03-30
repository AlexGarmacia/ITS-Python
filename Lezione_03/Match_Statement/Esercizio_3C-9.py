coordinate_x = int(input("Inserisci la coordinata x:"))
coordinate_y = int(input("Inserisci la coordinata y:"))

punto = (coordinate_x, coordinate_y) #tupla per salvare le coordinate

match punto:
    case (0,0):
        print("Il punto si trova nell'origine")
    case (x,0):
        print(f"Il punto si trova sull'asse X")
    case (0,y):
        print(f"Il punto si trova sull'asse Y")
    case (x, y) if x > 0 and y > 0:
        print(f"Il punto ({x},{y}) si trova nel primo quadrante.")
    case (x, y) if x < 0 and y > 0:
        print(f"Il punto ({x},{y}) si trova nel secondo quadrante.")
    case (x, y) if x < 0 and y < 0:
        print(f"Il punto ({x},{y}) si trova nel terzo quadrante.")
    case (x, y) if x > 0 and y < 0:
        print(f"Il punto ({x},{y}) si trova nel quarto quadrante.")


