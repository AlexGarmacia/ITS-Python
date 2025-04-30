# dal modulo esercizio12.py importare la classe MovieCatalog

from Esercirazione_Classi import MovieCatalog

# inizializzare un catalogo, ovvero un oggetto della classe MovieCatalog
catalog: MovieCatalog = MovieCatalog() 

#print(catalog)

catalog.add_movies("Steven Spielberg", ["Casper", "Il ritorno al fururo"])

catalog.add_movies("Steven Spielberg", ["ET"])

print(catalog)