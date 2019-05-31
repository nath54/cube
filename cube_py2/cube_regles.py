#coding:utf-8
import Tkinter,os

fene=Tkinter.Tk()
canvas=Tkinter.Canvas(fene,width=1000,height=700,bg="dark blue")
canvas.pack()


def ecrire(texte,x,y,couleur):
    canvas_id=canvas.create_text(x,y,anchor="nw")
    canvas.itemconfig(canvas_id,text=texte,fill=couleur)
    canvas.insert(canvas_id,20,"")

canvas.create_rectangle(800,500,900,600,fill="red")
ecrire("quitter",850,550,"black")

ecrire("cube",480,50,"light blue")

texte="""
                REGLES DU JEU :

Vous etes un petit cube blanc, vous vous déplacez en utilisant les flèches du clavier. 
Votre but du jeu est d'ateindre le petit carré rouge tout en évitant les murs.
Vous n'avez que cinq vies, vous perdez une vie, des points et vous retournez au point de départ du level si vous touchez un mur. 
Vous pouvez obtenir plus de points en prenant les petits carré bruns.

Astuces :
  - Dès que vous touchez un mur ou que vous avez gagné un level, relachez le clavier pour éviter de perdre des vies bètement en réaparissant.
                
"""

ecrire(texte,50,80,"grey")

def clic(event):
    ax,ay=event.x,event.y
    if ax >= 800 and ax <= 900 and ay >= 500 and ay <= 600:
        fene.destroy()    

canvas.bind("<Button 1>",clic)
fene.mainloop()
