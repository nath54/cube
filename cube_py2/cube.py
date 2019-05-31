#coding:utf-8
import Tkinter,threading,random,time,os,cube_levels
from cube_levels import *



normales=["green","blue","light blue","dark red","pink","yellow","#171515","#363434","brown","grey","light grey","purple","orange","dark green","#4b3e15"]
difficiles=["#202020","#ededed","#ef1313"]
dif=raw_input("quelle difficultee voulez vous pour les couleurs ?\n -(1)facile\n -(2)difficile\n : ")
if dif == "1": couleurs=normales
else: couleurs=difficiles

dif=raw_input("quelle difficultee voulez vous pour le chemin ?\n -(0)baby\n -(1)tres facile\n -(2)facile\n -(3)moyen\n -(4)difficile\n -(5)tres difficile\n -(6)hardcore\n : ")
if dif == "0": kak,kbk=10,60
elif dif == "1": kak,kbk=100,200
elif dif == "2": kak,kbk=400,700
elif dif == "3": kak,kbk=1000,1500
elif dif == "4": kak,kbk=2000,3000
elif dif == "5": kak,kbk=4000,5000
else: kak,kbk=5000,6000

lvl,aze,cas,pas,kjh,level_bon=create_level(kak,kbk)
pol=[]
lvb=[]

fenetre=Tkinter.Tk()
canvas=Tkinter.Canvas(fenetre,width=1000,height=700,bg="black")
canvas.pack()

levels_fait=0
vie=5
points=0
bg=0

def ecrire(texte,x,y,couleur,chcouleur):
    canvas_id=canvas.create_text(x,y,anchor="nw")
    canvas.itemconfig(canvas_id,text=texte,fill=couleur,activefill=chcouleur)
    canvas.insert(canvas_id,20,"")
    return canvas_id


color=random.choice(couleurs)

for x in range(0,len(lvl)):
    dd=lvl[x]
    pol.append(canvas.create_rectangle(dd[0],dd[1],dd[0]+20,dd[1]+20,fill=color,outline=color))

for x in range(0,len(level_bon)):
    dd=level_bon[x]
    lvb.append(canvas.create_rectangle(dd[0],dd[1],dd[0]+20,dd[1]+20,fill="#4e3506",outline="#4e3506"))

vv="vie ="+str(vie)
tv=ecrire(vv,900,50,"white","black")
pp="points ="+str(points)
pv=ecrire(pp,900,30,"white","black")
lv="lvl "+str(levels_fait)
pl=ecrire(lv,900,70,"white","black")

ax,ay=pas[0],pas[1]
ara=canvas.create_rectangle(ax,ay,ax+20,ay+20,fill="red",outline="red")
cx,cy,ctx,cty,cv=cas[0],cas[1],20,20,20
cc=canvas.create_rectangle(cx,cy,cx+ctx,cy+cty,fill="white",outline="white")

tt=time.time()

jj=1

def calcul_points(tp,kk,ng):
    za=20
    bt=0
    bk=0
    kg=0
    ttt=time.time()
    t=ttt-tp
    if tt < 30: bt += 10
    if tt < 20: bt += 10
    if tt < 10: bt += 10
    if kk > 500: bk += 10
    if kk > 900: bk += 10
    if kk > 1200: bk += 10
    if kg < 25 : kg -=10
    if kg < 12 : kg -= 10
    if kg < 6 : kg -= 10
    po=za+bt+bk-kg
    return po

def verif_bon():
    global level_bon,points,lvb
    for g in range(0,len(level_bon)):
        dd=level_bon[g]
        if cx == dd[0] and cy == dd[1]:
            print( "bonus")
            points+=10
            canvas.delete(lvb[g])

def clavier(event):
    global cx,cy,ctx,cty,cv,cc,ax,ay,ara,pnb,lvl,cas,pas,levels_fait,vie,points,kjh,bg,jj,level_bon,lvb,tv,vv,pv,ppcolor,pl,lv
    aa=event.keysym
    if aa == "Up" and jj:
        cy=cy-cv
        canvas.move(cc,0,-cv)
        bg+=1
    if aa == "Down" and jj:
        cy=cy+cv
        canvas.move(cc,0,cv)
        bg+=1
    if aa == "Left" and jj:
        cx=cx-cv
        canvas.move(cc,-cv,0)
        bg+=1
    if aa == "Right" and jj:
        cx=cx+cv
        canvas.move(cc,cv,0)
        bg+=1
    if aa == "q": exit()
#    print("cx = "+str(cx)+" , cy = "+str(cy))
    if cx == ax and cy == ay:
        jj=0
        print( "gagné")
        levels_fait+=1
        za=calcul_points(tt,kjh,bg)
        points+=za
        canvas.delete(cc)    
        canvas.delete(ara)
        for a in pol: canvas.delete(a)
        for b in lvb: canvas.delete(b)
        bg=0
        lvl,aze,cas,pas,kjh,level_bon=create_level(kak,kbk)
        color=random.choice(couleurs)
        for x in range(0,len(lvl)):
            dd=lvl[x]
            pol.append(canvas.create_rectangle(dd[0],dd[1],dd[0]+20,dd[1]+20,fill=color,outline=color))
        for  x in range(0,len(lvb)-1):
            del(lvb[x])
        lvb=[]
        for x in range(0,len(level_bon)):
            dd=level_bon[x]
            lvb.append( canvas.create_rectangle(dd[0],dd[1],dd[0]+20,dd[1]+20,fill="#4e3506",outline="#4e3506") )
        ax,ay=pas[0],pas[1]
        ara=canvas.create_rectangle(ax,ay,ax+20,ay+20,fill="red",outline="red")
        cx,cy=cas[0],cas[1]
        cc=canvas.create_rectangle(cx,cy,cx+ctx,cy+cty,fill="white",outline="white")
        time.sleep(1)
        jj=1
    canvas.delete(tv)
    canvas.delete(pv)
    canvas.delete(pl)
    vv="vie ="+str(vie)
    tv=ecrire(vv,900,50,"white","black")
    pp="points ="+str(points)
    pv=ecrire(pp,900,30,"white","black")
    lv="lvl "+str(levels_fait)
    pl=ecrire(lv,900,70,"white","black")
    for w in range(0,len(lvl)):
        dd=lvl[w]
        if cx == dd[0] and cy == dd[1] and bg != 0:
            jj=0
            print( "perdu")
            vie-=1
            points-=10
            time.sleep(0.4)
            canvas.delete(cc)
            cx,cy=cas[0],cas[1]
            cc=canvas.create_rectangle(cx,cy,cx+ctx,cy+cty,fill="white",outline="white")
            if vie == 0:
                trt=str(points)+"\n"+str(levels_fait)
                with open("cube.txt", "w") as fichier:
                    fichier.write(trt)
                print("PERDU, t'es nul, t'as fait que "+str(levels_fait)+" levels et t'as fait que "+str(points)+" points.")
                fenetre.destroy()
                os.system("python2 main.py")
            jj=1
    verif_bon()

canvas.bind_all("<Key>",clavier)
fenetre.mainloop()
