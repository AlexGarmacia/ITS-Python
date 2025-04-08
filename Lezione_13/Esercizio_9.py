# Scrivi una funzione che elimi tutte le vocali da una stringa

def vowelRemover(s:str) -> str:
    if not s:
        return s
    if s[0].lower() in ["a", "e", "i", "o", "u"]:
        return "" + vowelRemover(s[1:])
    else:
        return s[0] + vowelRemover(s[1:])

print(f"\"\" -> {vowelRemover("")}")
print(f"\"ciao\" -> {vowelRemover('ciao')}")