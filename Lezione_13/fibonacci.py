def fibonacci(n:int) -> int: #restituisce un intero
    if n == 0:
        return 0 # se il valore è uguale a zero ritorno zero
    elif n == 1:
        return 1
    else:
        return int(fibonacci(n-1)) + (fibonacci(n-2))
    
print(fibonacci(6))
