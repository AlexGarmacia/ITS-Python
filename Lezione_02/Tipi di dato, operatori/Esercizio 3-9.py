ospiti=["alex","maria","luca"]
for ospite in ospiti:
    print(f"ciao {ospite}, ti invito a cena")
print(f"purtroppo {ospiti[1]} non può venire a cena")
print("ho trovato un tavolo più grande")
ospiti.insert(2,"luca")
ospiti.insert(3,"giulia")
ospiti.insert(4,"marco")
print("Ecco i nuovi inviti per tutti:")
for ospite in ospiti:
    print(f"ciao {ospite}, ti invito a cena")

print("purtroppo, posso invitare solo 2 persone")
while len(ospiti) > 2:
    ospite_rimosso = ospiti.pop()
    print(f"mi dispiace {ospite_rimosso}, non posso invitarti")
    print("ecco i due ospiti che sono ancora invitati:")
    for ospite in ospiti:
        print("ciao {ospite}, ti invito ancora a cena")
    del ospiti[:]
    print(f"la lista degli ospiti è ora vuota:")
    print(ospiti)

ospiti=["Luca","Alex","Giulia","Maria","Marco"]
print(f"\nIl numero di persone invitate è: {len(ospiti)}")