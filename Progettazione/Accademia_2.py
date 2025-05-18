class Progetto:
    def __init__(self, nome: str, acronimo: str, inizio: date, fine: date):
        self.nome = nome
        self.acronimo = acronimo
        self.inizio = inizio
        self.fine = fine

    def __eq__(self, other):
        return isinstance(other, Progetto) and self.acronimo == other.acronimo

    def __hash__(self):
        return hash(self.acronimo)

    def __repr__(self):
        return f"Progetto({self.acronimo})"
    

class WP:
    def __init__(self, nome: str, inizio: date, fine: date):
        self.nome = nome
        self.inizio = inizio
        self.fine = fine

    def __eq__(self, other): #si usa per definire 2 oggetti uguali
        return isinstance(other, WP) and self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)

    def __repr__(self):
        return f"WP({self.nome})"
    

class Docente:
    def __init__(self, nome: str, cognome: str, matricola: int):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def __eq__(self, other):
        return isinstance(other, Docente) and self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __repr__(self):
        return f"Docente({self.nome} {self.cognome})"
    

class PosizioneAccademica:
    def __init__(self, nome: str):
        self.nome = nome

    def __eq__(self, other):
        return isinstance(other, PosizioneAccademica) and self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)

    def __repr__(self):
        return f"Posizione({self.nome})"
    

class Impegno:
    def __init__(self, inizio: datetime, durata: int, descrizione: str, fine: Optional[datetime] = None):
        self.inizio = inizio
        self.durata = durata  # in unità coerente (es. minuti)
        self.descrizione = descrizione
        self.fine = fine

    def __eq__(self, other):
        return isinstance(other, Impegno) and self.inizio == other.inizio and self.descrizione == other.descrizione

    def __hash__(self):
        return hash((self.inizio, self.descrizione))

    def __repr__(self):
        return f"Impegno({self.descrizione})"
    

class TipologiaImpegno:
    def __init__(self, motivazione: str):
        self.motivazione = motivazione

    def __eq__(self, other):
        return isinstance(other, TipologiaImpegno) and self.motivazione == other.motivazione

    def __hash__(self):
        return hash(self.motivazione)

    def __repr__(self):
        return f"Tipologia({self.motivazione})"
    

class TipoTipologiaImpegno:
    def __init__(self, unita_temporale: str):
        if unita_temporale not in ['minuti', 'ore', 'giorni', 'settimane', 'mesi', 'anni']:
            raise ValueError("Unità temporale non valida.")
        self.unita_temporale = unita_temporale

    def __eq__(self, other):
        return isinstance(other, TipoTipologiaImpegno) and self.unita_temporale == other.unita_temporale

    def __hash__(self):
        return hash(self.unita_temporale)

    def __repr__(self):
        return f"Tipo({self.unita_temporale})"



