from persona import Persona
class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name,last_name)
        self.__specialization = specialization if type(specialization) == str else None
        self.__parcel = parcel if type (parcel) == float else None

    def setSpecialization(self, specialization):
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa")

    def setParcel(self, parcel):
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float")

    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.getAge() >30:
            print(f"Il dottore {self.getName()} {self.getLastname()} è valido")
        else:
            print(f"Il dottore {self.getName()} {self.getLastname()} non è valido")

    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.__specialization}") 

        
            
        