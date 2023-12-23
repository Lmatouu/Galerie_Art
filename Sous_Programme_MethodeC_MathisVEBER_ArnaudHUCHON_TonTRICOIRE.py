import tkinter as tk
from Barycentre import Barycentre
from math import atan, sqrt

largeur=600
hauteur = 600
Lsave = []
L=[]
epaiseur = 2
empGar=[]
barVal=[]
bar=[]
passage = 0

def Fenetre():

    global cnv,largeur,hauteur
    wnd = tk.Tk()
    wnd.title("Art_Gallery")
    cnv = tk.Canvas(wnd, width=largeur, height=hauteur, bg='white')
    cnv.pack()
    cnv.focus_set()      # quand on utilise le clavier cela aura lieu dans la fenetre cnv
    cnv.bind('<1>', creer_poly)
    cnv.bind('<a>', printBary)
    cnv.bind('<3>', gardian)
    wnd.mainloop()

def creer_poly(event):
    """Gestion d'un clic : créer un rectangle réduit au point du clic."""
    global x0, y0, id_rect
    x0, y0 = event.x, event.y
    Lsave.append([x0,y0])
    id_rect = cnv.create_line(x0, y0, x0, y0,fill='black', width=3)
    cnv.bind('<Motion>', redessiner_poly)
    cnv.bind('<t>', fixer_poly)

def redessiner_poly(event):
    """Gestion des mouvements de la souris : redessiner le rectangle."""
    cnv.coords(id_rect, x0, y0, event.x, event.y)
    coordonne=x0,y0
    L.append(coordonne)

def fixer_poly(event):
    """Au relachement du bouton arrêter de suivre les mouvements."""
    print("Le polynôme est déssiné")
    
    xdepart,ydepart=L[0] #récupération du premier point 
    cnv.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=1) #création de la dernière ligne entre le point de départ et le dernier point
    cnv.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnv.delete('all') #supprime tout les premiers traits 
    cnv.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]

def gardian(event):
    """Placement du gardien

    """
    global empGar
    empGar=[event.x,event.y]
    cnv.create_rectangle(empGar[0]-5, empGar[1]-5,empGar[0]+5,empGar[1]+5, fill='black')

def equation(B,D1,D2):     
    """Cherche si un point appartient a un segment

    Args:
        B (tupple): point que lon cherche a verifier
        D1 (tupple): premier point du segment
        D2 (tupple): deuxieme point du segment

    Returns:
        _type_: _description_
    """
    if D1[1] <= D2[1]:
        ymin = D1[1]
        ymax = D2[1]
    else:
        ymax = D1[1]
        ymin = D2[1]
    if D1[0] <= D2[0]:
        xmin = D1[0]
        xmax = D2[0]
    else:
        xmax = D1[0]
        xmin = D2[0]
    if B[1] <= ymax and B[1] >= ymin and B[0] <= xmax and B[0] >= xmin :
        if D2[0]-D1[0] != 0:
            a=abs(B[1]-(((D2[1]-D1[1])/(D2[0]-D1[0]))*B[0]+D1[1]-((D2[1]-D1[1])/(D2[0]-D1[0]))*D1[0]))
            if a<=1:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def equation2(B,D1,D2):     
    """Cherche si un point appartient a une droite

    Args:
        B (tupple): Point a tester
        D1 (tupple): Point de la droite
        D2 (tupple): Point de la droite

    Returns:
        Bool: _description_
    """
    if D2[0]-D1[0] != 0:
        a=abs(B[1]-(((D2[1]-D1[1])/(D2[0]-D1[0]))*B[0]+D1[1]-((D2[1]-D1[1])/(D2[0]-D1[0]))*D1[0]))
        if a<=1:
            return True
        else:
            return False
    else:
        return True

def module(P1,P2):
    """Calcule le module d'une droite

    Args:
        P1 (tupple): point 1
        P2 (tupple): point 2

    Returns:
        int: module
    """
    return sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)

def posDroite(G,A,B,C) :
    """Cherche si 2 droites sont du meme cote d'une droite

    Args:
        G (tupple): emplacement du gardien
        A (tupple): Angle du polygone
        B (tupple): angle precedent
        C (tupple): angle suivant

    Returns:
        bool: True meme cote et False cote different
    """
    if G[0]-A[0] != 0 :
        a = (((G[1]-A[1])/(G[0]-A[0]))*B[0]+A[1]-((G[1]-A[1])/(G[0]-A[0]))*A[0])
        b = (((G[1]-A[1])/(G[0]-A[0]))*C[0]+A[1]-((G[1]-A[1])/(G[0]-A[0]))*A[0])
        if a <= B[1] : 
            a = -1
        else :
            a = 1
        if b <= C[1] : 
            b = -1
        else :
            b = 1
        if a*b > 0 :
            return True
        else :
            return False
    else :
        if (A[1]-B[1])*(A[1]-C[1]) >= 0 :
            return True
        else :
            return False             

def lumiere(rayonL,n):
    """fonctionnement d'un rayon de lumiere qui passe par un angle

    Args:
        rayonL (list): coordonne de point qui sont aligné
        n (int): numeros de la répétition

    """
    global Lsave, barValTri2Sup
    #print(rayonL[n][1])
    if rayonL[n][1] not in Lsave :
        #print("aaaa")
        for i in range (n+1,len(rayonL)):         
            barValTri2Sup.append(rayonL[i][1])
    else :
        positionAngle = Lsave.index(rayonL[n][1])
        if positionAngle == 0 :
            if posDroite(empGar , Lsave[positionAngle], Lsave[2], Lsave[-2]) == True :
                n+=1
                return lumiere(rayonL,n)
        else :
            if posDroite(empGar , Lsave[positionAngle], Lsave[positionAngle+1], Lsave[positionAngle-1]) == True :
                n+=1
                return lumiere(rayonL,n)
        
        for i in range (n+1,len(rayonL)):         
            barValTri2Sup.append(rayonL[i][1])

def printBary(event):
    """Gere le tri de tout les barycentres pour ne garder que ceux qui nous interesse
    
    """
    global barVal, bar, barValTri2Sup, passage
    Lsave.append(Lsave[0])
    for j in range (len(Lsave)):
        for i in range (len(Lsave)-1):
            #print(empGar)            
            I= Barycentre(empGar,Lsave[j],Lsave[i],Lsave[i+1])
            pointBar=I.barycentre()

            #Sert a enlever les barycentre qui ne sont pas dans le bon quart du canvas

            #print(pointBar)
            #cnv.create_oval(int(pointBar[0])-4,int(pointBar[1])-4,int(pointBar[0])+4,int(pointBar[1])+4,fill="purple")
            if (empGar[0]-Lsave[j][0]>0 and empGar[1]-Lsave[j][1]>0):
                if (pointBar[0]<=empGar[0] and pointBar[1]<=empGar[1]):
                    #cnv.create_oval(int(pointBar[0])-4,int(pointBar[1])-4,int(pointBar[0])+4,int(pointBar[1])+4,fill="red")
                    barVal.append(pointBar)
            elif (empGar[0]-Lsave[j][0]<0 and empGar[1]-Lsave[j][1]<0):
                if (pointBar[0]>=empGar[0] and pointBar[1]>=empGar[1]):
                    #cnv.create_oval(int(pointBar[0])-4,int(pointBar[1])-4,int(pointBar[0])+4,int(pointBar[1])+4,fill="red")
                    barVal.append(pointBar)
            elif (empGar[0]-Lsave[j][0]<0 and empGar[1]-Lsave[j][1]>0):
                if (pointBar[0]>=empGar[0] and pointBar[1]<=empGar[1]):
                    #cnv.create_oval(int(pointBar[0])-4,int(pointBar[1])-4,int(pointBar[0])+4,int(pointBar[1])+4,fill="red")
                    barVal.append(pointBar)
            else:
                if (pointBar[0]<=empGar[0] and pointBar[1]>=empGar[1]):
                    #cnv.create_oval(int(pointBar[0])-4,int(pointBar[1])-4,int(pointBar[0])+4,int(pointBar[1])+4,fill="red")
                    barVal.append(pointBar)           

    barValTri1 = [] 
    [barValTri1.append(x) for x in barVal if x not in barValTri1] 

    barValTri2 = []
    barValTri2numerote = []

    #Retire tout les points qui ne sont pas sur un cote du polygone
    for y in range (len(Lsave)-1):
        for z in range (len(barValTri1)):
            if equation(barValTri1[z],Lsave[y],Lsave[y+1]) == True :
                barValTri2numerote.append([barValTri1[z][0],barValTri1[z][1],y])
                barValTri2.append([barValTri1[z][0],barValTri1[z][1]])
                #cnv.create_oval(int(barValTri2[-1][0])-4,int(barValTri2[-1][1])-4,int(barValTri2[-1][0])+4,int(barValTri2[-1][1])+4,fill="blue")

    barValTri2Uni = []
    [barValTri2Uni.append(x) for x in barValTri2 if x not in barValTri2Uni]

    pointSegment = []
    [pointSegment.append(x) for x in barValTri2 if x not in Lsave]
    
    aligne = []   # liste qui comprend les couples de ponts qui sont alignes

    #Parcour les cote du polygone et enregistre dans une liste les points qui sont alignes
    for xxx in pointSegment:
        combo=[xxx]
        for yyy in barValTri2Uni:
            if equation2(yyy,xxx,empGar) == True:
                if yyy not in combo:
                    combo.append(yyy)
                    #print("aaaaaaaaaaaaa")
                    if yyy in pointSegment:
                        pointSegment.remove(yyy)
        aligne.append(combo)
    #print (aligne)
    #print(aligne[0])      #point sur une meme droite
    #print(aligne[0][0])      #couple de coordonnees d'un point sur la droite
    #print(aligne[0][0][0])      #coordonnée

    #Cerche les points a retire car on ne les vois pas
    barValTri2Sup = []
    for droite in aligne:
        triModule=[]
        [triModule.append([module(point,empGar),point]) for point in droite]
        triModule.sort()
        lumiere(triModule,0)

    for pointSupp in barValTri2Sup :
        #cnv.create_oval(int(pointSupp[0])-4,int(pointSupp[1])-4,int(pointSupp[0])+4,int(pointSupp[1])+4,fill="black")
        if pointSupp in barValTri2Uni:
            barValTri2Uni.remove(pointSupp)

    """
    for point in barValTri2Uni : 
        cnv.create_oval(int(point[0])-4,int(point[1])-4,int(point[0])+4,int(point[1])+4,fill="green")
    """
    

    #print(barValTri2Uni)

    polygoneVue = []

    #Tri les points dans le bonne ordre pour tracer le polygon par la suite.
    for u in range (0,len(Lsave) - 1) :
        triPoint = []
        for point in barValTri2Uni :
            if equation(point,Lsave[u],Lsave[u+1]) == True :
                triPoint.append([module(Lsave[u],point),point])
        triPoint.sort()
        #print(triPoint)
        if triPoint != [] :
            if triPoint[0][1] not in polygoneVue :
                polygoneVue.append(triPoint[0][1])
            if triPoint[-1][1] not in polygoneVue :
                polygoneVue.append(triPoint[-1][1])
    #print(polygoneVue)

    cnv.create_polygon(polygoneVue,fill = "pink")
    """
    Affichenum = 0
    for point in polygoneVue : 
        Affichenum += 1
        cnv.create_oval(int(point[0])-4,int(point[1])-4,int(point[0])+4,int(point[1])+4,fill="pink")
        cnv.create_text(int(point[0])+10,int(point[1])+10,text = Affichenum)
    """
    cnv.create_rectangle(empGar[0]-5, empGar[1]-5,empGar[0]+5,empGar[1]+5, fill='black')
    


############Programme############
Fenetre()