class Persona:
    #costruttore
    def __init__(self):
        self.name = "" #stringa vuota
        self.lastname = ""
        self.age = 0
    
    # funzione che mostri in output i dati relativi a una persona
    def displayData(self) -> None: #non mi ritorna niente in output
        print(f"Nome: {self.name}\n Cognome: {self.lastname} \n Età: {self.age}") 
    
    # funzione che ci consenta di impostare il valore di self.name
    def setName(self, name:str) -> None: #la funzione non ritorna niente perchè si limita a importare il valore di self.name
        self.name = name 
    
    # funzione che ci consenta di importare il valore di self.lastname
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname
    
    #funzione che ci consenta di impostare il valore di self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130: 
            self.age = 0
        else:
            self.age = age