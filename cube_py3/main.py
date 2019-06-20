#coding:utf-8
import tkinter,os

fen=tkinter.Tk()
canvas=tkinter.Canvas(fen,width=1000,height=700,bg="dark blue")
canvas.pack()


def ecrire(texte,x,y,couleur,chcouleur):
    canvas_id=canvas.create_text(x,y,anchor="nw")
    canvas.itemconfig(canvas_id,text=texte,fill=couleur,activefill=chcouleur)
    canvas.insert(canvas_id,20,"")
    return canvas_id

cb=ecrire("cube",300,40,"white","light blue")
    
with open("cube.txt", "r") as fichier:
                    score_points=fichier.readline()
                    score_levels=fichier.readline()

with open("rc.txt", "r") as fichier:
                    record_score_points=fichier.readline()
                    record_score_levels=fichier.readline()

if float(score_points) > float(record_score_points):
    record_score_points=score_points
if float(score_levels) > float(record_score_levels):
    record_score_levels=score_levels

trt=record_score_points+record_score_levels

with open("rc.txt", "w") as fichier:
                    fichier.write(trt)

scp="vous avez faits "+score_points+" points"
scl="vous avez faits "+score_levels+" levels"

sp=ecrire(scp,710,90,"light blue","orange")
sl=ecrire(scl,710,130,"light blue","orange")

rscp="votre record de points est de "+record_score_points+" points"
rscl="votre record de levels est de "+record_score_levels+" levels"

rsp=ecrire(rscp,410,90,"light blue","orange")
rsl=ecrire(rscl,410,130,"light blue","orange")


b1=canvas.create_rectangle(300,200,700,400,fill="dark orange")
b2=canvas.create_rectangle(800,500,900,600,fill="red")
b3=canvas.create_rectangle(100,100,150,150,fill="dark red")
b4=canvas.create_rectangle(100,500,200,600,fill="dark green")

tre=ecrire("jouer",500,300,"black","red")
xre=ecrire("quitter",850,550,"black","orange")
rre=ecrire("règles",150,550,"black","white")

def clic(event):
    ax,ay=event.x,event.y
    if ax >= 300 and ax <= 700 and ay >= 200 and ay <= 400:
        print( "jouer !!!" )
        fen.destroy()
        os.system("python cube.py")
    if ax >= 800 and ax <= 900 and ay >= 500 and ay <= 600:
        exit()
    if ax >= 100 and ax <= 200 and ay >= 500 and ay<= 600:
        os.system("python cube_regles.py")
    if ax >= 100 and ax <= 150 and ay >= 100 and ay <= 150:
        cgc=[tre,xre,sp,sl,rsp,rsl,cb,b1,b2,b3,b4,rre]
        for a in cgc:
            canvas.delete(a)
        

canvas.bind("<Button 1>",clic)
fen.mainloop()
