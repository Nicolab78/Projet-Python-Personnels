import tkinter
from PIL import Image, ImageTk
import random

fenetre = tkinter.Tk()
fenetre.geometry("400x400")
fenetre.title("Lancée de dé")

Blankline = tkinter.Label(fenetre, text="")
Blankline.pack()

HeadingLabel = tkinter.Label(fenetre, text="Lancé de dé",
   fg = "light green",
   bg = "dark green",
   font = "Helvetica 16 bold italic")
HeadingLabel.pack()

de = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
imagede = ImageTk.PhotoImage(Image.open(random.choice(de)))

ImageLabel = tkinter.Label(fenetre, image=imagede)
ImageLabel.image = imagede
ImageLabel.pack(expand=True)

def lancer_le_de():
    imagede = ImageTk.PhotoImage(Image.open(random.choice(de)))
    ImageLabel.configure(image=imagede)
    ImageLabel.image = imagede

button = tkinter.Button(fenetre, text="Lance de dé", fg="blue", command=lancer_le_de)
button.pack(expand=True)

fenetre.mainloop()
