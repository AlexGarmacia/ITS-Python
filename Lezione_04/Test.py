def alpha():
    print("Executing alpha")

def beta():
    alpha()
    print("Executing beta")

def gamma():
    print("Executing gamma")
    beta()

gamma()

'''
Output:

Executing gamma
Executing alpha
Executing beta

Ordine Esecuzione: gamma() -> beta() -> alpha()

Ordine Rimozione: alpha() -> beta() -> gamma()

Le callstack funzionao in modo: l'ultimo che è entrato sarà il primo 
ad essere eliminato. 

'''