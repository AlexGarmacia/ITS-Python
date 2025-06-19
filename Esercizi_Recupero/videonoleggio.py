class Movie:
    '''
    Classe Movie rappresenta i film da noleggiare
    '''

    def __init__(self, movie_id: str, title: str, director: str):

        self.movie_id: str = movie_id
        self.title: str = title
        self.director: str = director
        self.is_rented: bool = False

    def rent(self) -> None:

        if self.is_rented:
            
            print("Il film è gia stato affittato!")

        else:

            self.is_rented = True

    def return_movie(self) -> None:

        if not self.is_rented:

            print("Il film non è stato noleggiato da questo cliente!")

        else:
            
            self.is_rented = False
        
class Customer:

    def __init__(self,customed_id: str, name: str):

        self.customed_id: str = customed_id
        self.name: str = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:

        if movie.is_rented:

            print("Il film è gia stato affittato!")

        else:

            movie.rent()
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie) -> None:

        if movie not in self.rented_movies:

            print("L'utente non ha affittato il film!")
        else:

            movie.return_movie()
            self.rented_movies.remove(movie)

class VideoRentalStore:

    def __init__(self, customers: dict[str, Customer] = {}, movies: dict[str,Movie] = {}):
    
        self.customers: dict[str, Customer] = customers if customers is not None else {}
        self.movies: dict[str, Movie] = movies if movies is not None else {}
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:

        if movie_id in self.movies:

            print("Il film è gia presente nel catalogo!")

        else:
            movie: Movie = Movie (movie_id, title, director)
            self.movies[movie_id] = movie

    def register_customer(self, customer_id: str, name: str) -> None:

        if customer_id in self.customers:

            print("Il cliente è gia registrato!")
        else:

            customer: Customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
    
    def rent_movie(self, customer_id: str, movie_id: str) -> None:

        if customer_id not in self.customers or movie_id not in self.movies:

            print("Il cliente o film non presenti nel sistema!")
        
        else:

            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)

    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id not in self.customers:

            print("il cliente non è nel sistema!")

            return [] 
        else:
            return self.customers[customer_id].rented_movies
        
        
        