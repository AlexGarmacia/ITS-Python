def check_parentheses(expression: str) -> bool:
    # cancella pass e scrivi il tuo codice
    contatore = 0
    for carattere in expression:
        if carattere == "(":
            contatore += 1
        elif carattere == ")":
            contatore -= 1
        if contatore < 0:
            return False
    return contatore == 0

print(check_parentheses("()()"))