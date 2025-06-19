'''
Esercizio 1.
 
- 8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.
    Si definiscano i metodi __init__, setter, getter, __str__, value.
    In particolare:
    - il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;
    - il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
    - i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati
     per default rispettivamente a 13 e 5. Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. 
     Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

    Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer().

'''

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, valore):
        if type(valore) == int:
            self.__numeratore = valore
        else:
            self.__numeratore = 13

    def set_denominatore(self, valore):
        if type(valore) == int and valore != 0:
            self.__denominatore = valore
        else:
            self.__denominatore = 5

    def get_numeratore(self):
        return self.__numeratore

    def get_denominatore(self):
        return self.__denominatore

    def value(self):
        return round(self.__numeratore / self.__denominatore, 3)

    def __str__(self):
        return f"{self.__numeratore} / {self.__denominatore}"


def mcd(x, y):
    while y != 0:
        x, y = y, x % y
    return abs(x) if x != 0 else 1


def semplifica(lista_frazioni):
    lista_semplici = []
    for f in lista_frazioni:
        n = f.get_numeratore()
        d = f.get_denominatore()
        divisore = mcd(n, d)
        nuova = Frazione(n // divisore, d // divisore)
        lista_semplici.append(nuova)
    return lista_semplici


def fractionCompare(originali, semplificate):
    for o, s in zip(originali, semplificate):
        print(f"Valore frazione originale: {o.value()} --- Valore frazione ridotta: {s.value()}")



l = [
    Frazione(1, 2),
    Frazione(2, 4),
    Frazione(3, 5),
    Frazione(6, 9),
    Frazione(4, 7),
    Frazione(24, 36),
    Frazione(12, 36),
    Frazione(40, 60),
    Frazione(5, 11),
    Frazione(10, 45),
    Frazione(42, 78),
    Frazione(9, 15)
]

l_s = semplifica(l)
fractionCompare(l, l_s)
