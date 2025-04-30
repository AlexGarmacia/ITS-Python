class Alieno:

    '''
    di un alieno di interessa sapere la galassia di provenienza
    self.galaxy: str
    '''

    #inizializzazione di un oggetto della classe Alieno
    def __init__(self,galaxy:str):

        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! la galassia di provenienza non può essere vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speack(self) -> None:
        print("fwmewfejknfwjnmkew")

    def __str__(self) -> str:
        return f"\ Alieno proveniente dalla galassia {self.getGalaxy()}"
    