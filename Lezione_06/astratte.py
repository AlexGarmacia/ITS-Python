from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def __init__(self,nome: str, cognome: str, cf: str):
        self.set_nome(nome)
        self._cognome = cognome

        def set_nome(nome:str):
            self._nome = nome 

if __name__ == '__main__':
    p = Person('Giovanni', 'Rossi', 'efklwekwefk')
    print(p.get_nome())
    
