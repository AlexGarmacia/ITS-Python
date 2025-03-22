Cane:dict= {
    "nome":"Spike",
    "razza":"Pastore Tedesco",  
}
Gatto:dict= {
    "nome":"Fuffi",
    "razza":"Siberiano",  
}
Pappagallo:dict= {
    "nome":"Polly",
    "razza":"Ara",  
}

animali:list = [Cane, Gatto, Pappagallo]

for animale in animali:
    print(f"Nome: {animale['nome']}")
    print(f"Razza: {animale['razza']})")