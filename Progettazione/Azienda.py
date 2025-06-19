from datetime import date
from custom_types import *
class Impiegato:
    _nome: str #noto alla nascita
    _cognome: str #noto alla nascita
    _nascita: date #immutabile, noto alla nascita
    _stipendio: Importo #noto alla nascita

    def nome(self) -> str:
        return self._nome
    


    class Dipartimento:
        _nome: str #noto alla nascita
        _telefono: Telefono #noto alla nascita

        def nome(self) -> str:
            return self._nome
        def set_nome(self, nome:str) ->None:
            self._nome = nome

        def set_telefono(self, telefono: Telefono) -> None: 
            self._telefono