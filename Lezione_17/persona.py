class Persona:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name if type(first_name) == str else None
        self.__last_name = last_name if type(last_name) == str else None
        self.__age = 0 if self.__first_name and self.__last_name else None

    def set_name(self, first_name):
        if type(first_name) == str:
            self.__first_name = first_name
        else: 
            print("Il nome inserito non è una stringa")

    def setLastName(self, last_name):
        if type(last_name) == str:
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa")

    def setAge(self, age):
        if type(age) == int:
            self.__age = age
        else:
            print("L'età deve essere un numero intero")

    def getName(self):
        return self.__first_name
    
    def gestLastname(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age
    
    def greet(self):
        print(f"Ciao, sono {self.__first_name} {self.__last_name}, ho {self.__age} anni")

