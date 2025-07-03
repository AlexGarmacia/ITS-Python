from __future__ import annotations

from custom_types import *
from datetime import date
class Persona:
    _nome: str
    _cognome: str
    _cf: CodiceFiscale
    _nascita: date # <<immutable>>

    _is_uomo: bool # da fusione
    _is_donna: bool # da fusione
    _maternita: intGEZ | None # da fusione con donna
    _posizione_militare: PosizioneMilitare | None # da fusione con Uomo e aggregazione di

    def __init__(self, *nome:str, cognome:str, cf:CodiceFiscale, nascita: date,
                 maternita: IntGEZ|None = None,
                 posizione_militare: PosizioneMilitare | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self._nascita = nascita

        if maternita is not None:
            self.set_attributi_donna(maternita)
        if posizione_militare

    def set_nome