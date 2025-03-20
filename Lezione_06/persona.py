class Persona: #definizione di classe sempre con lettera maiuscola
    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona)
    Le informazioni saranno:
    - nome
    - cognome
    - età

    come li rappresento in python?
    self.name:str (attributi di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)
    '''

    # costruttore
    def __init__(self,name:str, lastname:str, age:int): #attraverso questo metodo inizializziamo la variabile Persona
        self.name = name #l'attributo name della classe persona lo inizializzo con un valore generico name
        self.lastname = name 
        self.age = age