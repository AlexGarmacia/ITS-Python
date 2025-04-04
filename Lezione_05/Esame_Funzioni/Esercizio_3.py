def even_odd_pattern(numbers: list[int]) -> list[int]:
    """
    Funzione che restituisce una lista contenente i numeri in ordine alternato
    tra pari e dispari, mantenendo l'ordine originale.
    
    :param numbers: Lista di numeri interi
    :return: Lista con i numeri in ordine alternato tra pari e dispari
    """
    # controllo dei numeri pari
    numeri_pari = [num for num in numbers if num % 2 == 0]
    
    # controllo dei numeri dispari
    numeri_dispari = [num for num in numbers if num % 2 != 0]
    
    # Lista per l'output finale, prima i pari poi i dispari
    output = []
    
    # Aggiungi alternatamente i numeri pari e dispari
    for i in range(max(len(numeri_pari), len(numeri_dispari))):
        if i < len(numeri_pari):
            output.append(numeri_pari[i])
        if i < len(numeri_dispari):
            output.append(numeri_dispari[i])
    
    return output

# Esempio di utilizzo
print(even_odd_pattern([1, 2, 3, 4, 5, 6]))  # Output: [2, 1, 4, 3, 6, 5]
print(even_odd_pattern([2, 4, 6, 8, 10]))   # Output: [2, 4, 6, 8, 10]
