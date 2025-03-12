stringa_inserita:str=input("iserire una stringa:") #chiede di inserire una stringa
stringa_invertita= "" #inizializzazione stringa vuota per contenere quella invertia

for carattere in range(len(stringa_inserita) -1, -1, -1): #ciclo for che legge la stringa
    stringa_invertita += stringa_inserita[carattere] #riscrive la stringa invertita
print(f"{stringa_invertita}")