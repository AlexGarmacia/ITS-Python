def countdown(n:int) -> None:
    if n >= 0:
        while n:
            print(n)
            n = n -1
    else:
        print("Il numero è negativo")

countdown(4)
countdown(-4)