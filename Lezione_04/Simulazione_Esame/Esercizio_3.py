def list_statistics(numbers: list[int]) -> tuple[int, int, float]:
    massimo = max(numbers) #trova il valore massimo
    minimo = min(numbers) #trpva il valore minimo
    media = sum(numbers) / len(numbers) #calcola la media
    return massimo, minimo, media #restituisce una tupla contenente il massimo, minimo e media

print(list_statistics([1, 2, 3, 4, 5]))  # Output: (5, 1, 3.0)
