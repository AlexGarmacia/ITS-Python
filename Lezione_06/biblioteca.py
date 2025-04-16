class Libro:
    def __init__(self):
        self.titolo:str = ""
        self.autore:str = ""
        self.genere:list[str] = ""


    def set_autore(self, nome_autore:str):
        self.autore = nome_autore

    def set_titolo(self,titolo_libro:str):
        self.titolo = titolo_libro

    def set_genere(self, lista_genere:list[str]):
        self.genere = lista_genere


    def get_autore(self) ->str:
        return self.autore
    
    def get_titolo(self) -> list:
        return self.titolo

    def get_genere(self) -> list[str]:
        return self.genere
    
class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []

    def set_libro(self, libro:Libro):   
        self.libri.append(libro)

    def get_libri_titolo(self) -> str:
        for item in self.libri:
            print(item.get_titolo())

collezione:Biblioteca = Biblioteca()



piccolo_principe:Libro = Libro() #libro 1
piccolo_principe.set_titolo("Piccolo Principe")
piccolo_principe.set_autore("AutorePiccoloPrincipe")
piccolo_principe.set_genere(["Narrativa"])  

fm:Libro = Libro() #libro 2
fm.set_titolo("Le avventure di Federico March")
fm.set_autore("Federico March")
fm.set_genere(["comico", "dramma"])

# Inserimento libro 1 e libro 2 nella biblioteca
collezione.set_libro(piccolo_principe)
collezione.set_libro(fm)
print("Libri aggiunti alla collezione")
print("------------------")
collezione.get_libri_titolo()

test:Libro = Libro() #libro 3
test.set_titolo("Harry Potter")
test.set_autore("J.K. Rowling")
test.set_genere(["Fantasy"])

collezione.set_libro(test)
print("Libri aggiunti alla collezione")
print("------------------") 
collezione.get_libri_titolo()
 
