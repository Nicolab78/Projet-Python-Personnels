import random

def genere3chiffres(dec):
    a =random.randint(0,9)
    b =random.randint(0,9)
    c =random.randint(0,9)
    while b == a:
        b = random.randint(0,9)
    while c == b or c == a:
        c = random.randint(0,9)
    return [a+dec,b+dec,c+dec]

def genere3x9nombres():
    nombregrille = []
    for i in range(9):
        nombregrille.append(genere3chiffres(i*10))
    return nombregrille
def affichergrille(grille, nombregrille):
    for ligne in range(3):
        for col in range(9):
            if grille[ligne][col] == '0': 
                print(" ##", end="")
            else:  
                v = nombregrille[col][ligne]
                print(f"{v:3}", end="")
        print()

def Combiner9cases():
    ListeCombinaison = []
    H = ["000","001","010","011","100","101","110","111"]
    for a in H:
        for b in H:
            for c in H:
                ListeCombinaison.append(a+b+c)
    return ListeCombinaison
    
def Compterligne(L):
    s = 0
    for i in range(9):
        if L[i] == "1":
            s+=1
    return s

def VerificationLC( L1, L2, L3):
    for i in range(9):
        V = L1[i] + L2[i] + L3[i]
        if V == "000" or V == "111":
            return False
    return True

def Filtreligne(ListeCombinaison):
    LigneValide = []
    for combinaison in ListeCombinaison:
        if "111" not in combinaison and "000" not in combinaison:
            if Compterligne(combinaison) == 5:
                LigneValide.append(combinaison)
    return LigneValide

def MasqueGrille(LigneValide):
    nb = len(LigneValide)
    L1 = LigneValide[random.randint(0 , nb - 1)]
    L2 = LigneValide[random.randint(0 , nb - 1)]
    L3 = LigneValide[random.randint(0 , nb - 1)]

    while VerificationLC(L1,L2,L3):
        L1 = LigneValide[random.randint(0 , nb - 1)]
        L2 = LigneValide[random.randint(0 , nb - 1)]
        L3 = LigneValide[random.randint(0 , nb - 1)]
    
    return [L1,L2,L3]


L = Combiner9cases()
LigneValide = Filtreligne(L)
SOL = MasqueGrille(LigneValide)
nombregrille = genere3x9nombres()
affichergrille(SOL, nombregrille)


