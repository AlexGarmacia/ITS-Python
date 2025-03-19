def build_profile(marca: str, modello: str, **kwargs):
    car = {
        "marca": marca,
        "modello": modello
    }
    for chiave, valore in kwargs.items():
        car[chiave] = valore
    return car

car = build_profile("Ford", "Fiesta", color="White")
print(car)
