def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0  # Se la lista è vuota, restituisce 0 
    else:
        return sum(numbers) / len(numbers)  # Media = somma dei numeri / numero degli elementi
