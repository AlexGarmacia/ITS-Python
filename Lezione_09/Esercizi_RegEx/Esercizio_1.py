'''1. Riconoscere numeri

Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

    Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
    Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).
'''

import re

#Esercizio 1
list_num:str="837 98734"
n_int_pos:list[int] = re.findall(r"\d+", list_num)
print(n_int_pos)

#Esercizio 2
list_num:str="-837 98734"
