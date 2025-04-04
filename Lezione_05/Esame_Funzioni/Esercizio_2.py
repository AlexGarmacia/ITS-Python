def find_disappeared_numbers(nums: list[int]) -> list[int]:
    # elimina il pass e inserisci il codice
    n = len(nums) #lunghezza definita da n
    n_lista= set(nums)
    n_completi= range(1, n+1)
    n_mancanti= [x for x in n_completi if x not in n_lista]
    
    return n_mancanti

# Esempio di utilizzo
print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
print(find_disappeared_numbers([1,984]))