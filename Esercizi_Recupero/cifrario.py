from string import ascii_lowercase

def cifrario(s: str, k:int) -> str:

    l: str = ""

    for carattere in s:

        index: int = ascii_lowercase.index(carattere)

        index = (index + k) % len(ascii_lowercase)

        l += ascii_lowercase[index]

    elif carattere in ascii_uppercase:
    
        index:int = ascii_uppercase.index(carattere)
    
        index = (index + k) %len(ascii_uppercase)
    
        l += ascii_uppercase[index]

    
    else:
        l+= carattere

    return l