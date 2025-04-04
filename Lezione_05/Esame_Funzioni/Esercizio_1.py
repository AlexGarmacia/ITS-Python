def prime_factors(n: int) -> list[int]:
    fattori_primi = []
    divisore = 2
    
    while divisore * divisore <= n: # Continua a dividere n finché divisore <= n
        while n % divisore == 0:
            fattori_primi.append(divisore)
            n //= divisore  # Dividi n per il divisore
        divisore += 1
    
    # Se alla fine n è maggiore di 1, n è un fattore primo
    if n > 1:
        fattori_primi.append(n)
    
    return fattori_primi

print(prime_factors(56))
print(prime_factors(97))
print(prime_factors(100))
print(prime_factors(1))
print(prime_factors(0))
print(prime_factors(-5))

