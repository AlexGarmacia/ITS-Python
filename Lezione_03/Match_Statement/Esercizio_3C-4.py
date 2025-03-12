mammiferi:list=["cane","gatto","cavallo","elefante","leone"]
rettili:list=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli:list=["aquila","pappagallo","gufo","falco"]
pesci:list=["squalo","trota","salmone","carpa"]

animale = input("Inserisci il nome di un animale: ")

match animale:
    case animale if animale in mammiferi:
        print(f"L'animale {animale} è un mammifero")
    case animale if animale in rettili:
        print(f"L'animale {animale} è un rettile")
    case animale if animale in uccelli:
        print(f"L'animale {animale} è un uccello")
    case animale if animale in pesci:
        print(f"L'animale {animale} è un pesce")
    
    case _: 
        print(f"Non sono in grado di classificare {animale}")

#L'esercizio chiede di inserire un animale e ti dice a che categoria appartiene