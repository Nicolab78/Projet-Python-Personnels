from tkinter import Tk, Canvas
import random

TAILLE = 300
JEU = [[0,0,0],[0,0,0],[0,0,0]]

def AfficheGrille(c="black"):
    canvas.create_line((100,0),(100,300),width=3,fill=c)
    canvas.create_line((200,0),(200,300),width=3,fill=c)
    canvas.create_line((0,100),(300,100),width=3,fill=c)
    canvas.create_line((0,200),(300,200),width=3,fill=c)

def AfficherPoints():
    for x in range(3):
        for y in range(3):
            xx = x * 100
            yy = y * 100
            A = (xx+20, yy+20)
            B = (xx+80, yy+80)
            C = (xx+20, yy+80)
            D = (xx+80, yy+20)
            if JEU[x][y] == 1:
                canvas.create_oval(A,B,fill="blue")
            if JEU[x][y] == 2:
                canvas.create_line(A,B,fill="red",width=10)
                canvas.create_line(C,D,fill="red",width=10)

def DetecteGagne():
    for j in [1,2]:
        for x in range(3):
            if JEU[x][0] == JEU[x][1] == JEU[x][2] == j : return j
        for y in range(3):
            if JEU[0][y] == JEU[1][y] == JEU[2][y] == j : return j
        if JEU[0][0] == JEU[1][1] == JEU[2][2] == j : return j
        if JEU[0][2] == JEU[1][1] == JEU[2][0] == j : return j
    return 0

def ChercherCaseVide():
    L = []
    for x in range(3):
        for y in range(3):
            if JEU[x][y] == 0:
                L.append((x,y))
    if len(L) == 0: return
    else:
        i = random.randint(0,len(L)-1)
        return L[i]

def PROG() :
    AfficheGrille()

def Affiche():
    canvas.delete("all")
    AfficheGrille()
    AfficherPoints()

def click(event):
    global JEU
    Affiche() 
    x = event.x // 100
    y = event.y // 100

    if DetecteGagne() != 0:
        JEU = [[0,0,0],[0,0,0],[0,0,0]]
        Affiche()
        return
    if JEU[x][y] != 0: return

    #Humain
    JEU[x][y] = 1
    AfficherPoints()
    if DetecteGagne() == 1:
        AfficheGrille("blue")
        return

    #Robot
    calcul = ChercherCaseVide()
    if calcul != False:
        x,y = calcul
        JEU[x][y] = 2
        AfficherPoints()
        if DetecteGagne() == 2:
            AfficheGrille("red")
            return


#Création de la fênetre de dessin
Mafenetre = Tk()
Mafenetre.geometry(str(TAILLE) +"x"+str(TAILLE))
canvas= Canvas(Mafenetre,width=TAILLE, height=TAILLE,borderwidth=0, highlightthickness=0,bg="lightgray")
canvas.pack()
Mafenetre.after(100,PROG)
Mafenetre.bind("<Button-1>", click)
Mafenetre.mainloop()