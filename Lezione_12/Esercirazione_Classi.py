class MovieCatalog:

    '''
    Attributi della classe MovieCatalog:
    self.catalog: dict [str, list[str]]
    '''

    # inizializzare un oggetto della classe MovieCatalog
    def __init__(self) -> None:
        self.catalog()

    # metodi getter

    # metodo che ritorna il valore dell'attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    
    # metodi setter

    # metodo che consente di inizializzare l'attributo self.catalog
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}

    # metodo per visualizzare i dettagli di un catalogo
    def __str__(self) -> str:
        
        string: str = " Cataglogo: "

        for key, values in self.catalog.items():
            temp_string: str = "\n" + str(key) + ": " + str(values)
            string = string + temp_string
        return string
    
    # metodi della classe MovieCatalog

    # metodo per aggiungere un film al catalogo
    def add_movies(self, director_name: str, movies: list[str]) -> None:
        # check se il registra non è valido
        if not director_name:
            print("il registra non è valido")
        # check se la lista di film non è valida
        elif not movies:
            print("La lista non puo essere vuota")
        # se i dati sono validi
        else:

            # se il registra è presente nel catalogo
            if director_name in self.catalog:

                # aggiungere la lista movies al catalogo
                # per ogni film nella lista movies
                for movie in movies:

                    # controllare che il film movies sia stato già aggiunto al catalogo

                    # dizionario[key] -> valore
                    # director_name è la chiave del dizionario che rappresenta il nome di un regista
                    # a questa chiave corrisponde una lista di film, ovvero i film prodotti dal regista in questione
                    # self.catalog[director_name] -> è il valore associato alla chiave director_name
                    # ovvero è la lista di tutti i film prodotti dal regista
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è già presente nel catalogo")

                    # se il film non è presente
                    else:

                        # aggiungere il film al catalogo
                        self.catalog[director_name].append(movie)

            # se il registra non è presente nel catalogo
            else:
                # creare un nuovo record
                self.catalog[director_name] = movies

