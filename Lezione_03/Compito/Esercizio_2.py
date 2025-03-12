stringa_inserita:str=input("Inserisci una frase:")
numero_spazi=0

for carattere in stringa_inserita:
    if carattere == " ":
        numero_spazi += 1
        
print("il numero di spazi è:" ,numero_spazi)
