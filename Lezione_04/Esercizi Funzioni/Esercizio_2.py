def check_length(string):
    if len(string) > 10:
        print(f"La stringa '{string}' ha più di 10 caratteri")
    elif len(string) < 10:
        print(f"La stringa '{string}' ha meno di 10 caratteri")
    else:
        print(f"La stringa '{string}' ha esattamente 10 caratteri")

check_length("Ciao")
check_length("Ciao come va?")