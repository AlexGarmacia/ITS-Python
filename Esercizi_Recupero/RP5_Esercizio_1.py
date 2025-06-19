import random
# 1.A
def generaMAT(dim:int) -> list[list[int]]:
    matrice = []
    for i in range(dim):
        riga=[]
        for x in range(dim):
            n= random.randint(0,13)
            riga.append(n)
        matrice.append(riga)
    return matrice

#1.B
def printMAT(mat:int):
    for riga in mat:
        for i in riga:
            print(f"{i:5}")
        print()

#1.C
def calcolaCarico(mat:list[list[int]], r:int, c:int) ->int:
    somma_riga= sum(mat[r])
    somma_colonna=0
    for i in range(mat):
        somma_colonna += mat[i][c]
    return somma_riga - somma_colonna

#1.D
def caricoNullo(mat:list[list[int]]) -> list[tuple[int,int]]:
    dim = len(mat)
    posizioni = []
    for r in range(dim):
        for c in range(dim):
            if calcolaCarico(mat,r,c) == 0:
                posizioni.append(r,c)
        
    return posizioni

#1.E
def caricoMax(mat) -> tuple[int,int]:
    dim = len(mat)
    max_carico = None
    pos_max = (0,0)

    for r in range(dim):
        for c in range(dim):
            carico = calcolaCarico(mat,r,c)
            if(carico > max_carico):
                max_carico = carico
                pos_max = (r,c)
    
    print(max_carico)
    return pos_max

#1.F
def caricoMIN










    



