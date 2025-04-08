# Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

def charDuplicator(s:str) -> str:
    if not s:
        return s
    else:
        