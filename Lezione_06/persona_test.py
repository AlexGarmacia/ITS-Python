# dal file persona.py importa la classe Persona
from persona import Persona 

# creare un oggetto di tipo persona
ag:Persona = Persona("Alex", "Garmacia", 20)

print(ag)
print(ag.name, ag.lastname, ag.age)

# dal file persona2.py importa la classe Persona
from persona2 import Persona

ag:Persona = Persona() #oggetto vuoto

# voglio richiamare la funzione displayData della classe persona per stampare in output le informazioni relativa alla persona ag
ag.displayData()

# impostare il nome della persona ag
ag.setName("Alex")
print("---------")
ag.displayData()

# impostare il cognome della persona ag
ag.setLastname("Garmacia")

# impostare l'età della persona ag
ag.setAge(20) #si mette l'età in negativo

print("-----------")
ag.displayData()

