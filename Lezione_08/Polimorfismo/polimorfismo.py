from persona import Persona
from alieno import Alieno

# creare un oggetto p della classe Persona
p: Persona = Persona("Federico", "March", 29)

# visualizzare le informazioni relative all'oggetto p
print(p)

#creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")

#visualizzare le informazioni relative all'oggetto et
print(et)

# l'oggetto p invoca il metodo speak() della classe Persona
p.speak()

# l'oggetto et invoca il metodo speak() della classe Alieno
et.speak()

