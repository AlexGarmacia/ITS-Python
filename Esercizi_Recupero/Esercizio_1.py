'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.

tupla=(2,3,"ciao")
dizionario:dict={0:"v1"....}
'''

def convert_list_of_tuple_to_dict(list_1:list[tuple]) -> dict:

    dict_1:dict= {}

    for element in list_1: #stiamo prendendo le singole tuple

        key, value = element[0], element[1]

        if key in dict_1:

            dict_1[key] += value

        else:

            dict_1[key] = value

    return dict_1

lista_1: list[tuple] = [(0, "valore1"), (1,"valore2")]
dict_2:dict= convert_list_of_tuple_to_dict(list_1=lista_1)

print(dict_2)
 
