def compoundinterest(m:int, t:int) -> float:
    if t <= 0:
        return 0
    elif t == 1:
        return m * 1.005
    else: 
        return m * 1.005 + compoundinterest(m, t-1)
    
print(compoundinterest(12,5))