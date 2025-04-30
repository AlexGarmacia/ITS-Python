from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape("Rettangolo")

    def draw(self) -> None:

        print(f"\n{self.getShape()}\n")