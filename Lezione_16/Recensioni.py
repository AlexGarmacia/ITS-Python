class Media:

    _title: str
    _reviws: list[int]

    def __init__(self, title:str, reviews: list[int]) -> None:

        self.setTitle()

    def set_title(self, title:str):

        self._title = title

    def get_title(self) -> str:

        return self._title
    
    def aggiungiValutazione(self, voto:str) -> None:

        if 1 <= voto <= 5:

            self._reviews.append(voto)
        else:
            raise ValueError("Il voto deve essere compreso tra 1 e 5")
    
    def getMedia(self):

        if not self._reviews:

            raise RuntimeError("Questo file non ha reviews, non si può calcolare la media")
        
        else:
            somma: int = 0

            for v in self._reviews:+
                somma += v

            media








