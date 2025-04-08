# Scrivere una funzione ricorsiva che conti il numero di vocali in una stringa

def vowelsCounter(s:str) -> int:
    if not s: # se la stringa è vuota
        return 0
    if s[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1 + vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])
    
print(vowelsCounter("ciao"))