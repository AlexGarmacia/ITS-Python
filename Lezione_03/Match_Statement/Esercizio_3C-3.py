oggetti:list = [] #le parentesi vuote si usano per definire una lista vuota da riempire
for i in range(3): # Range= 0<=i<2  #chiediamo di inserire 3 oggetti
    oggetto:str = input("Inserisci il nome di un oggetto: ")
    oggetti.append(oggetto)
print(oggetti)

match oggetti:
    case ["penna","matita","quaderno"]:
        print(f"{oggetto} appartiene al materiale scolastico")
    case ["pane","latte","uova"]:
        print(f"{oggetto} fa parte dei prodotti alimentari")
    case ["sedia","tavolo","armadio"]:
        print(f"{oggetto} fa parte dei mobili")
    case ["telefono", "computer", "tablet"]:
        print(f"{oggetto} fa parte dei dispositivi elettronici")
    case _:
        print(f"{oggetto} appartiene a una categoria sconosciuta")
#Inserendo i nomi degli oggetti ci dirà a che categoria appartengono

