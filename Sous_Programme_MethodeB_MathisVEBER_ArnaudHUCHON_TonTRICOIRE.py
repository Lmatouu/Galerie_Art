# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:35:54 2022

@author: mathi
"""



import tkinter as tk
import math 
import random

largeur=800
hauteur=800
epaiseur=1
L=[] #création d'une liste avec tout les coordonnées du polynôme (event.x,event.y) 
Lsave=[]
supprime=[]
C=[]

color=['blue','red', 'pink','green','yellow','purple']

def creer_rect(event):
    """Gestion d'un clic : créer un rectangle réduit au point du clic."""
    global x0, y0, id_rect,xdepart,ydepart
    x0, y0 = event.x, event.y
    Lsave.append([x0,y0])
    id_rect = cnv.create_line(x0, y0, x0, y0,fill='black', width=3)
    cnv.bind('<Motion>', redessiner_rect)
    """cnv.focus_set()"""
    cnv.bind('<t>', fixer_rect)

def redessiner_rect(event):
    """Gestion des mouvements de la souris : redessiner le rectangle."""
    cnv.coords(id_rect, x0, y0, event.x, event.y)
    coordonne=x0,y0
    L.append(coordonne)

def fixer_rect(event):
    """Au relachement du bouton arrêter de suivre les mouvements."""
    print("Le polynôme est déssiné")
    
    xdepart,ydepart=L[0] #récupération du premier point 
    cnv.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=1) #création de la dernière ligne entre le point de départ et le dernier point
    cnv.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnv.delete('all') #supprime tout les premiers traits 
    cnv.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]
    
def reset(event):
    
    cnv.unbind('<Motion>')
    cnv.delete('all') #Supprime tout les éléments de la fenêtre
    del L[:] #Supprime les listes
    del Lsave[:]
   
    
    
def distance(x1,y1,x2,y2): #Fonction qui permet le calcul  d'un modul avec deux points en paramètre
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist




    
def equation(x,y,x0,y0,x1,y1):
    if (x1-x0)==0:
        if y1-y0>0:
            if y>y0 and y<y1:
                return True 
            else:
                return False
        else:
            if y>y1 and y<y0:
                return True 
            else:
                return False
        
        
    if (abs(y-(((y1-y0)/(x1-x0))*x+y0-((y1-y0)/(x1-x0))*x0))<=20):
      
        return True
    else:
        print('supprimer')
        print(x)
        print(y)
        return False
    
    
    
    
    
def enlever_doublons(liste):
    liste_finale = []
    for coord in liste:
        if coord not in liste_finale:
            liste_finale.append(coord)
    return liste_finale    
    
    
    
def remplace(ListeA,ListeB):
     for k in range(len(ListeB)):
         cordx,cordy=ListeB[k]
         for i in range((len(ListeA))):
             pointx,pointy=ListeA[i]
             if abs(cordx-pointx)<3 and abs(cordy-pointy)<3:
                 ListeB[k]=ListeA[i]
     return ListeB
 


def verification(x,y,x1,y1,xa,ya):# x1<x<xa et y1<x<ya point compris entre les deux cote d'une droite 

    
    if (x1>xa):
        xmax=x1
        xmin=xa
        
    else:
        xmax=xa
        xmin=x1
    
    if (y1>ya):
        ymax=y1
        ymin=ya
    else:
        ymax=ya
        ymin=y1
    
    if (xmin-x<=1 and x-xmax<=1 and ymin-y<=1 and y-ymax<=1):
        return True
    else:
        return False

def gardian(event):
    C=[]
    P=[]
    del C[:]
    del P[:]
    P1=[]
    del P1[:]
    
    cnv.itemconfigure('effaceligne', state="hidden") #Gestion de tag pour"faire disparaitre ancien rayon"
    x0, y0 = event.x, event.y
    print("Coordonne tout les cotées")
    print(Lsave)
    for k in range (len(Lsave)):
        pointx,pointy=Lsave[k]
        angle=math.atan2(-y0+pointy,-x0+pointx)
        a=math.cos(angle)
        b=math.sin(angle)
        R=1
        collision=len(cnv.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b))
        
        while collision==1:
            R+=1
            collision=len(cnv.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b))
            
        newpointx=int(x0+R*(a) - a*epaiseur)
        newpointy=int(y0+R*(b) - b*epaiseur)
        coordonne=newpointx,newpointy
        C.append(coordonne)
        
        if (distance(x0,y0,pointx,pointy)-distance(x0,y0,newpointx,newpointy))<-5:
            coordonnee=pointx,pointy
            C.append(coordonnee)
            
    C=remplace(Lsave,C)
    print(' ')
    print("Coordonne tout les points sans tri")
    print(C)
    
    for k in range(len(C)):
        pointx,pointy=C[k]
        cnv.create_line(x0, y0,pointx,pointy, fill='red',  width=1, tag='effaceligne' )#création d'un rayon avec deux coordonnées

        
    for i in range (-1,len(Lsave)-1):
        xa,ya=Lsave[i+1]
        x1,y1=Lsave[i]
        for j in range (len(C)):
            x,y=C[j]
            if equation(x,y,x1,y1,xa,ya)==True and verification(x,y,x1,y1,xa,ya)==True:
                P.append([x,y])
      

             
        stop=1
        if (len(P)>1):
            time=1
            for j in range (len(P)):
                Px,Py=P[j]
                Lsavex,Lsavey=Lsave[i]
                if Px==Lsavex and Py==Lsavey and time==1:
                    valeurx,valeury=P[0]
                    P[0]=[Lsavex,Lsavey]
                    P[j]=[valeurx,valeury]
                    time=0
                    print("1")
                    
                

                    
            while(stop==1):
             stop=0
             for m in range (len(P)-1):
                 point1x,point1y=P[m]
                 pointx,pointy=Lsave[i]
                 point2x,point2y=P[m+1]
                 if distance(pointx,pointy,point1x,point1y)>distance(pointx,pointy,point2x,point2y):
                     a=P[m]
                     P[m]=P[m+1]
                     P[m+1]=a
                     stop=1
                     print("trié croissant")
                     print(P)
       
        [P1.append(x) for x in P if x not in P1] 
        del P[:]
        
    print("Ordre affiché Coordonne tout les points avec deuxieme tri sans doublons")
    print(P1)  
    compteurbis=0
    for k in range(len(P1)):
        pointx,pointy=P1[k]
        compteurbis+=1
        couleur=random.choice(color)
        cnv.create_line(x0, y0,pointx,pointy, fill=couleur,  width=2, tag='effaceligne' )#création d'un rayon avec deux coordonnées
        cnv.create_text(pointx+10, pointy+10, text= f'n°{compteurbis}', tag='effaceligne')
        
    #cnv.create_polygon(P1,fill='blue',  width=1, tag='effaceligne' )#création d'un triangle avec deux coordonnées
    
    print(' ')
    print("Coordonne tout les points sans tri")
    print(C)

    

#----------Fonction Enregistrement d'un polygone enregistré----------------------
#(Touche 'S') puis entrer nom dossier texte

def Save():
    global Lsave
    print(Lsave)
    fichier = e.get()
    file = open(f"{fichier}.txt", "w") 
    for i in Lsave:
        print(f"{i[0]} {i[1]}")
        file.write(f"{i[0]} {i[1]} \n") 
    file.close()
    fenetrePrincipale.destroy()

def sauvegardePoint(event):
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Sauvegarder nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Save)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()



#----------Fonction Dessiner d'un polygone enregistré----------------------

def RecuperationPoint(fichier):
    global Lcote
    Lcote=[]
    file = open(f"{fichier}.txt", "r") 
    for ligne in file:
            Lcoordonne=ligne.split(' ')
            X=int(Lcoordonne[0])
            Y=int(Lcoordonne[1])
            cote=X,Y
            Lcote.append(cote)
            
    return Lcote



#----------Fonction Ouvrier Dossier Texte ou le polygone est enregistré----------------------
#(Touche 'L') puis entrer nom dossier texte

def load(event):
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Ouvir Nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Draw)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()

#----------Création du polygone enregristré-----------------
def Draw():
    global Lsave
    Lcote=[]
    Lsave=[]
    fichier=e.get()
    del Lcote[:]
    Lcote=RecuperationPoint(fichier)#Recupération des coordonnees des cotées dans le fichier enregistré
    
    cnv.delete('all') #Supprime les éléments déjà sur la fenêtre
    cnv.create_polygon(Lcote, fill='grey', width=epaiseur, outline='blue') #Création du polygone
    Lsave[:]=Lcote
    
    fenetrePrincipale.destroy()
    



wnd = tk.Tk()
wnd.title("Art_Gallery_MethodeB")
cnv = tk.Canvas(wnd, width=largeur, height=hauteur, bg='white')
cnv.pack()
cnv.focus_set()
cnv.bind('<1>', creer_rect)
cnv.bind('<l>', load)
cnv.bind('<3>', gardian)
cnv.bind('<r>', reset)
cnv.bind('<s>', sauvegardePoint)

wnd.mainloop()
