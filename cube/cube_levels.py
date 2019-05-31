import random

def create_level(a,b):
    kjh=random.randint(a,b)
    fx=[]
    fy=[]
    for x in range(3,49):
        fx.append(x*20)
    for x in range(3,34):
        fy.append(x*20)
    xx,yy=random.choice(fx),random.choice(fy)
    aze=[]
    level_bon=[]
    for w in range(kjh):
        dd=random.choice(["haut","bas","gauche","droite"])
        if dd == "haut":
            yy += 20
            if yy >= 680:
                yy = 660
#                w-=1
        elif dd == "bas":
            yy -= 20
            if yy <= 20:
                yy = 40
#                w-=1
        if dd == "droite":
            xx += 20
            if xx >= 980:
                xx = 960
#                w-=1
        if dd == "gauche":
            xx -= 20
            if xx <= 20:
                xx = 40
#                w-=1
        aze.append([xx,yy])
    lvl=[[0,0]]
    xxx,yyy=0,0
    qsd=1
    while qsd:
        if xxx == 980 and yyy == 680: break
        h=0
        if xxx != 980:
            xxx += 20
        elif xxx == 980:
            xxx = 0
            yyy += 20
        for s in range(0,len(aze)):
            j=aze[s]
            if xxx == j[0] and yyy == j[1]:
                h=1
                break
        if h == 0:
            lvl.append([xxx,yyy])
    for f in range(3):
        t=random.randint(2,len(aze)-5)
        level_bon.append([aze[t][0],aze[t][1]])
    ccs=[aze[0][0],aze[0][1]]
    pas=[aze[len(aze)-1][0],aze[len(aze)-1][1]]
    return lvl,aze,ccs,pas,kjh,level_bon

