'''
Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

def filter_product_dict(dict_1:dict) -> dict:

    dict_4:dict = {}

    for key, value in dict_1.items():
        
        if value > 50:

            continue
        else:
            dict_4[key] = round(value + value * 0.10,2)

    return dict_4

dict_out: dict = filter_product_dict(dict_1=dict_5)
print(f"La soluzione dell'esercizio 3 è: {dict_out}")
