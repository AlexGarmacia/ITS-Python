'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''

def product(lista_interi: list[Union[int, float ]],soglia:int = 50) -> int:

    for element in lista_interi:

        if type(element) != int:

            continue

        if element < soglia:

            prodotto_cumulato *= element

    return prodotto_cumulato

# 2 bis) Calcola il fattoriale di un numero n

def factorial(n:int) -> int:

    fattoriale: int = 1
    
    for i in range(n):
        fattoriale *= n - i

    return fattoriale

def factorial(n: int) -> int:

    if n == 1:
        return n

    return factorial(n-1) * n
