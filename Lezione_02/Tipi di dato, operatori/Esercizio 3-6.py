ospiti=["alex","maria","luca"]
print("ho trovato un tavolo più grande")
ospiti.insert(2,"luca")
ospiti.insert(3,"giulia")
ospiti.insert(4,"marco")
print("Ecco i nuovi inviti per tutti:")
for ospite in ospiti:
    print(f"ciao {ospite}, ti invito a cena")