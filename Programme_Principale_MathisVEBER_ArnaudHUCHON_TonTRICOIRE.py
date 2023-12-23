# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:51:29 2022

@author: mathi
"""
import tkinter as tk
from tkinter import *

from Barycentre import Barycentre
from math import atan, sqrt
import math 
import random
import time

#Pour garantir la fenetre menu la largeur doit être supérieur à 1100 et la hauteur supérieur à 500
largeur=1100 #Largeur de la fenêtre tkinter  
hauteur=700#Hauteur de la fenêtre tkinter
epaiseur=1 #taille des bordures du polygone
L=[] #création d'une liste avec tout les coordonnées du polygone (event.x,event.y) 
Lsave=[]  #création d'une liste avec tout les coordonnées des cotés 
Lcote=[] #création d'une liste avec tout les coordonnées des cotés enregistré dans un dossier texte
Lsavepolygon=[]
Lsaveor=[]
empGar=[]
barVal=[]
bar=[]
passage = 0



def menu():
    global wnd,wnda,cnv,cnva
    
    wnd =tk.Tk()
    wnd.title("Menu_Art_Gallery")
    
    fichier1='Ninterfacediagonale.png'
    fichier2='Nintefacecoté.png'
    fichier3='Ninterfacebarrycentre.png'
    fichier4='NVideo-Game-Controller-Icon-IDV-green.svg.png'

    
    cnv = tk.Canvas(wnd, width=largeur, height=hauteur, bg='white')
    
    photo1 = tk.PhotoImage(file=fichier1) 
    photo2 = tk.PhotoImage(file=fichier2) 
    photo3 = tk.PhotoImage(file=fichier3)
    photo4 = tk.PhotoImage(file=fichier4)
    
    
    btn=tk.Button(wnd,width=largeur//3,height=hauteur//2,image=photo1, bg='orange',command=methodea)
    btn.place(x=0,y=0)
    btn=tk.Button(wnd,width=largeur//3,height=hauteur//2,image=photo2,bg='orange',command=methodeb)
    btn.place(x=largeur//3,y=0)
    btn=tk.Button(wnd,width=largeur//3,height=hauteur//2,image=photo3,bg='orange',command=methodec)
    btn.place(x=0,y=hauteur//2)
    btn=tk.Button(wnd,width=largeur//3,height=hauteur//2,image=photo4,bg='orange',command=game)
    btn.place(x=largeur//3,y=hauteur//2)
    
    cnv.create_text(largeur*4//5,hauteur//2,text='                                 ART GALERIE\n \n \n CLASSE: P2C \n \n Mathis VEBER Tom TRICOIRE Arnaud HUCHON \n \n \n \n \n                                     NOTICE: \n \n \n Tracer polygone puis T  pour dessiner \n \n Clique droit pour afficher gardien \n \n RACOURCIE TOUCHE: \n \n R pour reset \n \n M pour sauvegarder \n \n L pour charger fichier \n \n B pour calculer aire avec la methode 1 \n \n N pour calculer aire avec la méthode 2 \n \n Touche mouvement jeu: ZQSD',anchor=tk.CENTER)
    cnv.pack()
    cnv.focus_set()
    wnd.mainloop()



#METHODE 1 alias a



#---------------Partie création du polygone et le gardien par plusieurs droites suivant 360 degrés-------------
#---(Clic gauche de la souris)

def methodea(): 
    global wnd,wnda,cnv,cnva
    
    wnd.destroy()
    wnda =tk.Tk()
    wnda.title("Methodea_Art_Gallery")
    cnva = tk.Canvas(wnda, width=largeur, height=hauteur, bg='white')
    btn=tk.Button(wnda,text="Sauvegarder",command=sauvegardePointbutton,bg='orange',activebackground='#345',activeforeground='white')
    btn.place(x=largeur-70,y=hauteur-50)
    btn=tk.Button(wnda,text="Charger",command=loadbuttona,bg='orange',activebackground='#345',activeforeground='white')
    btn.place(x=largeur-45,y=hauteur-25)
    btn=tk.Button(wnda,text="Menu",command=retourmenua,bg='orange', activebackground='#345',activeforeground='white')
    btn.place(x=largeur-35,y=hauteur-75)
    cnva.pack()
    cnva.focus_set()
    Titre = tk.Label(wnda,text="Dessiner polygone puis T pour dessiner")
    Titre2 = tk.Label(wnda,text="Clique droite gardien")
    Titre.pack()
    Titre2.pack()
    cnva.bind('<l>', loadraccourcia)
    cnva.bind('<1>', creer_polya)
    cnva.bind('<3>', gardiana)
    cnva.bind('<r>', reseta)
    cnva.bind('<m>', sauvegardePointraccourci)
    cnva.bind('<b>', airepoygonméthode1)
    cnva.bind('<n>', airepoygonméthode2)
    wnda.mainloop()
    
   
#fonction permettant la fermeture de la fenetre en cours et l'ouverture du menu 
def retourmenua():
    global wnd,wnda,cnv,cnva
    del L[:]
    del Lsave[:]
    del listeevent[:]
    del Lcote[:]
    wnda.destroy()
    menu()
    


#fonction permettant la création du polygone par l'utilsateur
    
def creer_polya(event):
    """Gestion d'un clic : créer une droite réduit au point du clic."""
    global x0, y0, id_rect,xdepart,ydepart
    x0, y0 = event.x, event.y
    Lsave.append([x0,y0])
    id_rect = cnva.create_line(x0, y0, x0, y0,fill='black', width=3)
    cnva.bind('<Motion>', redessiner_polya)
    """cnv.focus_set()"""
    cnva.bind('<t>', fixer_polya)

def redessiner_polya(event):
    """Gestion des mouvements de la souris : redessiner la droite"""
    cnva.coords(id_rect, x0, y0, event.x, event.y)
    coordonne=x0,y0
    L.append(coordonne)

#--Quand l'utilisateur a finit de tracer par points son polygone il appuie sur la touche 'T'-----------
def fixer_polya(event):
    """Au relachement du bouton arrêter de suivre les mouvements."""
    print("Le polygone est dessiné")
    
    xdepart,ydepart=L[0] #récupération du premier point 
    cnva.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=3) #création de la dernière ligne entre le point de départ et le dernier point
    cnva.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnva.delete('all')
    cnva.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]
   
#--Fonction Reset  ---------------------------------
def reseta(event):
    
    cnva.unbind('<Motion>')
    cnva.delete('all') #Supprimer la fênetre et tout les éléments dans les liste
    del L[:]
    del Lsave[:]
    del listeevent[:]
    del Lcote[:]
    
    
    
listeevent=[]  
 
#---Fonction Gardian dessine rayon chanmp de vision suivit d'un carrée noir marquant sa position-------------
#---(Clic droit de la souris)

def gardiana(event): 
    global cnva
    """Gestion d'un clic dans le polygone: Création d'un champ de vision suivant 360 degrés """
     #Méthode à l'aide des arcs paramètriques création de 360 rayons autour du gardians avec méthode overlapping pour stopper rayon
    x0, y0 = event.x, event.y # coordonnées du point du clic
    coordonne=x0, y0
    listeevent.append(coordonne)
    
    cnva.itemconfigure('effaceligne', state="hidden") #Gestion de tag pour"faire disparaitre ancien rayon"
    cnva.itemconfigure('effacecarre', state="hidden") #Gestion de tag pour"cacher ancien carre"
    #cnva.create_rectangle(x0,y0,largeur,y0+1)
    
    carreselec=len(cnva.find_overlapping(x0-5,y0-5,x0+5,y0+5)) #mesure sur le nombre d'élément sous le point 
    print(carreselec)
    if carreselec == 0 : #Détermination si point est à l'intérieur du polygone ou à l'extérieur 
        '''si la variable carreselec==0 il n'y a aucun d'élément à l'emplacement du clic donc le clic est à l'extérieur du polygone dessiné'''
        print('Placer un point à l intérieur du polygone')
        cnva.itemconfigure('effacecarre', state="normal",fill='black')#Gestion de tag pour" faire faire raparaitre ancien rayon"
        cnva.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
        
        return
   
    
    
    C=[] #liste contenant tout les coordonées des points de la bordure des rayons
    for k in range (360): # Pour faire un tour
        x=math.radians(k) #On convertie en radians pour l'utisation de cosinus et sinus   
        a=math.cos(x)
        b=math.sin(x)
        R=1
        collision=len(cnva.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b)) #mesure sur le nombre d'élément sous le point 
        while collision==1: #On deplace le point suivant le rayon jusqu'a qu'il sorte du polygone 
            R+=1
            collision=len(cnva.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b))
        
        
        pointx=x0+(R-epaiseur)*a  #position du point suivant x - la taille de la bordure
        pointy=y0+(R-epaiseur)*b #position du point suivant y - la taille de la bordure
        coordonne=pointx,pointy
        C.append(coordonne) #on l'ajoute dans notre liste contenant tout les coordonées des points de la bordure des rayons
        
    for k in range (360): #On dessine ici tout les rayons avec les positions enregistrées dans la liste C
        pointx,pointy=C[k]
        cnva.create_line(x0, y0,pointx,pointy, fill='yellow',  width=1, tag='effaceligne' )#création d'un rayon avec deux coordonnées
    cnva.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
    
    for k in range (len(listeevent)):#On dessine ici tout les carrés de gardiant event mémoriser en premier plan
        x0,y0=listeevent[k]
        cnva.create_rectangle(x0-5, y0-5,x0+5,y0+5, fill='black', tag='effacecarre') #creation d"un carré noir metant en lumière la position du clic soit du gardiant 
        


#----------Fonction Dessiner d'un polygone enregistré pour la methode 1----------------------

def RecuperationPoint(fichier):
    file = open(f"{fichier}.txt", "r") 
    for ligne in file:
            Lcoordonne=ligne.split(' ')
            X=int(Lcoordonne[0])
            Y=int(Lcoordonne[1])
            cote=X,Y
            Lcote.append(cote)
            
    return Lcote



#----------Fonction Ouvrier Dossier Texte ou le polygone est enregistré pour la méthode 1----------------------
#(Touche 'L') puis entrer nom dossier texte
def loadraccourcia(event):
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Ouvir Nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Drawa)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()
    
def loadbuttona():
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Ouvir Nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Drawa)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()

#----------Création du polygone enregristré-----------------
def Drawa():
    global Lsave
    del Lsave[:]
    fichier=e.get()
    
    Lsave=RecuperationPoint(fichier)#Recupération des coordonnees des cotées dans le fichier enregistré
    
    cnva.delete('all') #Supprime les éléments déjà sur la fenêtre
    cnva.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue') #Création du polygone
    fenetrePrincipale.destroy()



#METHODE 2 alias b



#---------------Partie création du pôlygone et du gardien suivant les points des cotés du polygone-------------
#---(Clic gauche de la souris)
C=[]

color=['blue','red', 'pink','green','yellow','purple']


def methodeb(): 
    global wnd,wndb,cnv,cnvb
    
    wnd.destroy()
    wndb =tk.Tk()
    wndb.title("Methodeb_Art_Gallery")
    cnvb = tk.Canvas(wndb, width=largeur, height=hauteur, bg='white')
    btn=tk.Button(wndb,text="Sauvegarder",command=sauvegardePointbutton,bg='orange',activebackground='#345',activeforeground='white')
    btn.place(x=largeur-70,y=hauteur-50)
    btn=tk.Button(wndb,text="Charger",command=loadbuttonb,bg='orange',activebackground='#345',activeforeground='white')
    btn.place(x=largeur-45,y=hauteur-25)
    btn=tk.Button(wndb,text="Menu",command=retourmenub,bg='orange', activebackground='#345',activeforeground='white')
    btn.place(x=largeur-35,y=hauteur-75)
    cnvb.pack()
    cnvb.focus_set()
    Titre = tk.Label(wndb,text="Dessiner polygone puis T pour dessiner")
    Titre2 = tk.Label(wndb,text="Clique droite gardien")
    Titre.pack()
    Titre2.pack()
    cnvb.bind('<l>', loadraccourcib)
    cnvb.bind('<1>', creer_polyb)
    cnvb.bind('<3>', gardianb)
    cnvb.bind('<r>', resetb)
    cnvb.bind('<m>', sauvegardePointraccourci)
    cnvb.bind('<b>', airepoygonméthode1)
    cnvb.bind('<n>', airepoygonméthode2)
    wndb.mainloop()
    
    
def retourmenub():
    global wnd,wndb,cnv,cnvb
    del L[:]
    del Lsave[:]
    del listeevent[:]
    del Lcote[:]
    wndb.destroy()
    menu()    
    
    
    
def creer_polyb(event):
    """Gestion d'un clic : créer une droite réduit au point du clic."""
    global x0, y0, id_rect,xdepart,ydepart
    x0, y0 = event.x, event.y
    Lsave.append([x0,y0])
    id_rect = cnvb.create_line(x0, y0, x0, y0,fill='black', width=3)
    cnvb.bind('<Motion>', redessiner_polyb)
    """cnvb.focus_set()"""
    cnvb.bind('<t>', fixer_polyb)

def redessiner_polyb(event):
    """Gestion des mouvements de la souris : redessiner la droite"""
    cnvb.coords(id_rect, x0, y0, event.x, event.y)
    coordonne=x0,y0
    L.append(coordonne)

#--Quand l'utilisateur a finit de tracer par points son polygone (Touche 'T')-----------
def fixer_polyb(event):
    """Au relachement du bouton arrêter de suivre les mouvements."""
    print("Le polygone est déssiné")
    
    xdepart,ydepart=L[0] #récupération du premier point 
    cnvb.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=3) #création de la dernière ligne entre le point de départ et le dernier point
    cnvb.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnvb.delete('all')
    cnvb.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]
   
#--Fonction Reset  ---------------------------------
def resetb(event):
    
    cnvb.unbind('<Motion>')
    cnvb.delete('all') #Supprimer la fênetre et tout les éléments dans les liste

    del L[:]
    del Lsave[:]
    del listeevent[:]
    del Lcote[:]
    
    

def gardianb(event):
    global cnvb
    C=[]
    P=[]
    del C[:]
    del P[:]
    P1=[]
    del P1[:]
    
    cnvb.delete('effaceligne') #Gestion de tag pour supprimer ancien rayon
    cnvb.delete('effacecarre') #Gestion de tag pour supprimer ancien carre
    x0, y0 = event.x, event.y
    print("Coordonne des cotées du polygones")
    print(Lsave)
    
    carreselec=len(cnvb.find_overlapping(x0-5,y0-5,x0+5,y0+5)) #mesure sur le nombre d'élément sous le point 
    print(carreselec)
    if carreselec == 0 : #Détermination si point est à l'intérieur du polygone ou à l'extérieur
        print('Placer un point à l intérieur du polygone')
        cnvb.itemconfigure('effacecarre', state="normal",fill='black')#Gestion de tag pour" faire faire raparaitre ancien rayon"
        cnvb.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
        
        return
    
    #on détermine si la droite partant du gardien et qui est orienté suivant un coté du polygone peut continuer suivant la même direction sans sortir du polygone 
    
    for k in range (len(Lsave)):
        pointx,pointy=Lsave[k]
        angle=math.atan2(-y0+pointy,-x0+pointx) # on mesure l'angle entre gardien et un coté
        a=math.cos(angle)
        b=math.sin(angle)
        R=1

        collision=len(cnvb.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b)) #on mesure le nombre d'éléments 
    
        while collision==1:
            R+=1
            collision=len(cnvb.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b)) 
            
        newpointx=int(x0+R*(a) - a*epaiseur)
        newpointy=int(y0+R*(b) - b*epaiseur)
        coordonne=newpointx,newpointy
        C.append(coordonne)
        
        if (distance(x0,y0,pointx,pointy)-distance(x0,y0,newpointx,newpointy))<-5:
            coordonnee=pointx,pointy
            C.append(coordonnee)
      
        
    C=remplace(Lsave,C) #si les nouveaux points sont confondues voire très proche d'un point de la liste des cotés du polygone on le supprime
    #print(' ')
    #print("Coordonnes de tous les points sans tri")
    #print(C)
        
    
    # Pour chaque cotés du polygone (deux points en paramètre à la suite) on détermine les points de la liste C sont compris sur l'équation puis on vérifie qu'ils sont compris entre ces deux valeurs 
    for i in range (-1,len(Lsave)-1):
        xa,ya=Lsave[i+1]
        x1,y1=Lsave[i]
        for j in range (len(C)):
            x,y=C[j]
            if equation(x,y,x1,y1,xa,ya)==True and verification(x,y,x1,y1,xa,ya)==True:
                P.append([x,y])
      
      # La suite P est donc les points compris sur une même droite du polygone
      # par la suite si la droite contient plus de deux termes on tri la liste
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
                    #print("1")
        #on détermine le premier terme de la suite P suivant l'ordre de la droite réprensenter par les deux coordonnes Lsave
                

        #on tri la liste maintenant l'ordre des points sur la même suivant les modules de ces points avec le premier points de la droite           
            while(stop==1):
             stop=0
             for m in range (len(P)-1):
                 point1x,point1y=P[m]
                 pointx,pointy=Lsave[i]
                 point2x,point2y=P[m+1]
                 if distance(pointx,pointy,point1x,point1y)>distance(pointx,pointy,point2x,point2y): #on compare deux modules de deux points à cotés ans la liste P
                     a=P[m]
                     P[m]=P[m+1]
                     P[m+1]=a
                     stop=1 #tant qu'il y a un changement on continue la boucle 
                     #print("trié croissant")
                     #print(P)
   
        [P1.append(x) for x in P if x not in P1]  #on ajoute la liste P à la liste globale P1 en supprimant les doublons 'un point peut intervenir dans deux droites du polygone'
        del P[:]
        
    #print("Ordre affiché Coordonne tout les points avec deuxieme tri sans doublons")
    #print(P1)  
    compteurbis=0
    for k in range(len(P1)): #on trace les droites et on numérote les nouveaux points triées mettant en lumière le champ de vision e l'utilisateur
        pointx,pointy=P1[k]
        compteurbis+=1
        couleur=random.choice(color)
        cnvb.create_line(x0, y0,pointx,pointy, fill=couleur,  width=2, tag='effaceligne' )#création d'un rayon avec deux coordonnées
        cnvb.create_text(pointx+10, pointy+10, text= f'n°{compteurbis}', tag='effaceligne')
        
    cnvb.create_polygon(P1,fill='blue',  width=1, tag='effaceligne' )#création d'un triangle avec deux coordonnées
    
    #print(' ')
    #print("Coordonne tout les points sans tri")
    #print(C)
    
    #creation d"un carré noir metant en lumière la position du clic soit du gardien
    cnvb.create_rectangle(x0-5, y0-5,x0+5,y0+5, fill='black', tag='effacecarre')



def distance(x1,y1,x2,y2): #Fonction qui permet le calcul  d'un module avec deux points en paramètre
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

  


 #Fonction qui permet de déterminer si un point (x,y) est compris sur la droite de points (x0,y0) et ((x1,y1))

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
        #print('supprimer')
        #print(x)
        #print(y)
        return False
    
    
def verification(x,y,x1,y1,xa,ya):# x1<x<xa et y1<x<ya on verifie si le point x,y compris entre les deux extrémites d'une droite 

    
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
    
    
# fonction qui permet d'enlever lees doublons d'une liste entre deux listes    
def remplace(ListeA,ListeB):
     for k in range(len(ListeB)):
         cordx,cordy=ListeB[k]
         for i in range((len(ListeA))):
             pointx,pointy=ListeA[i]
             if abs(cordx-pointx)<3 and abs(cordy-pointy)<3:
                 ListeB[k]=ListeA[i]
     return ListeB
 

#----------Fonction Ouvrier Dossier Texte ou le polygone est enregistré pour la méthode 2----------------------
#(Touche 'L') puis entrer nom dossier texte
def loadraccourcib(event):
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Ouvir Nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Drawb)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()
    
def loadbuttonb():
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Ouvir Nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Drawb)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()

#----------Création du polygone enregristré-----------------
def Drawb():
    global Lsave
    del Lsave[:]
    fichier=e.get()
    
    Lsave=RecuperationPoint(fichier)#Recupération des coordonnees des cotées dans le fichier enregistré
    
    cnvb.delete('all') #Supprime les éléments déjà sur la fenêtre
    cnvb.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue') #Création du polygone
    fenetrePrincipale.destroy()




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


def sauvegardePointraccourci(event):
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Sauvegarder nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Save)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()
    
def sauvegardePointbutton():
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Sauvegarder nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Save)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()



#-----------------------------------------------------------------------------------------------
"""Méthode de calcul de l'aire du polygone dessiné à l'aide des deux méthodes vue en partie théorique """   

#affichage l'aire du polygone sur la console du polygone dessiné 

#Méthode 1 par l'appuie de la touche B 
def airepoygonméthode1(event):
    global Lsave
    print(Lsave)
    duree=0
    somme=0
    second1 = time.time()
    for k in range(len(Lsave)):
        xi,yi=Lsave[k-1]
        yi=hauteur-yi
        xi1,yi1=Lsave[k]
        yi1=hauteur-yi1
        somme+=(xi+xi1)*(yi1-yi) 
    somme=abs((0.5)*somme)
    print('l aire du polygon est:')
    print(somme)
    second2 = time.time()
    duree=second2-second1
    print("Temps d'éxécution méthode 1:")
    print(duree)
    print(second1)
    print(second2)
    
         
#Méthode 2 par l'appuie de la touche N
def airepoygonméthode2(event):
    global Lsave
    print(Lsave)
    duree=0
    somme=0
    second1 = time.time()
    for k in range(len(Lsave)):
        xi,yi=Lsave[k-1]
        yi=hauteur-yi
        xi1,yi1=Lsave[k]
        yi1=hauteur-yi1
        somme+=(xi*yi1-xi1*yi)
    somme=abs((0.5)*somme)
    print('l aire du polygon est:')
    print(somme)
    second2 = time.time()
    duree=second2-second1
    print("Temps d'éxécution méthode 2:")
    print(duree)
    print(second1)
    print(second2)
    
#import time pour comparer le temps d'éxécution des deux méthodes
#on constate que les deux méthodes sont similaires 


#•-------------------------------------------------------------------------

#JEU alias game

#Fonction lancement du jeu l'ulisateur a le choix de 3 niveaux (boutons)     
  
def game():    
    global wndgame,cnvgame,wnd,cnv
    
    wnd.destroy()
    #creation de la fenètre
    wndgame = tk.Tk()
    wndgame.title("Choix du niveau")
    cnvgame = tk.Canvas(wndgame, width=largeur, height=hauteur, bg='white')
    
    #création des trois boutons représentant les trois niveaux (1,2,3) en colonne
    btn1=tk.Button(wndgame,text="Niveau 1", bg='orange',command=niveau1)
    btn2=tk.Button(wndgame,text="Niveau 2", bg='orange',command=niveau2)
    btn3=tk.Button(wndgame,text="Niveau 3", bg='orange',command=niveau3)
    btn4=tk.Button(wndgame,text="Menu", bg='orange',command=retourmenugame)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()

    
    Titre = tk.Label(wndgame,text="Choix du niveau")
    Titre.pack()
    
     
    cnvgame.pack()
    cnvgame.focus_set()
    wndgame.mainloop()
    
    
def retourmenugame():
    global wnd,wndgame,cnv,cnvgame
    
    del Lsavepolygon[:]
    del Lsaveor[:]
    del Ldecouvertor[:]
    
    wndgame.destroy()
    
    menu()
    

def gardiangame(x0,y0): 
    global Ldecouvertor
    """Gestion d'un clic dans le polygone: Création d'un champ de vision suivant 360 degrés """
     #Méthode à l'aide des arcs paramètriques création de 360 rayons autour du gardians avec méthode overlapping pour stopper rayon
    
    cnvgame.delete('effaceligne')#Gestion de tag pour"faire disparaitre ancien rayon"
    cnvgame.delete('effacecarre')#Gestion de tag pour"faire disparaitre ancien rayon"
    #cnv.create_rectangle(x0,y0,largeur,y0+1)
    cnvgame.delete('or2')#Gestion de tag pour"faire disparaitre lingot d'or"
    
    
    carreselec=len(cnvgame.find_overlapping(x0-5,y0-5,x0+5,y0+5)) #mesure sur le nombre d'élément sous le point 

    if carreselec == 0 : #Détermination si point est à l'intérieur du polygone ou à l'extérieur
        print('Placer un point à l intérieur du polygone')
        cnvgame.itemconfigure('effacecarre', state="normal",fill='black')#Gestion de tag pour" faire faire raparaitre ancien rayon"
        cnvgame.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
        cnvgame.itemconfigure('or2', state="normal")
        return
   
    
    
    C=[] #liste contenant tout les coordonées des points de la bordure des rayons
    for k in range (360): # Pour faire un tour
        x=math.radians(k) #On convertie en radians pour l'utisation de cosinus et sinus   
        a=math.cos(x)
        b=math.sin(x)
        R=1
        collision=len(cnvgame.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b)) #mesure sur le nombre d'élément sous le point 
        while collision==1 and R<50: #On deplace le point suivant le rayon jusqu'a qu'il sorte du polygone avec un rayon max de 50 
            R+=1
            collision=len(cnvgame.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b))
        
        
        pointx=x0+(R-epaiseur)*a  #position du point suivant x - la taille de la bordure
        pointy=y0+(R-epaiseur)*b #position du point suivant y - la taille de la bordure
        coordonne=pointx,pointy
        C.append(coordonne) #on l'ajoute dans notre liste contenant tout les coordonées des points de la bordure des rayons
        
    for k in range (360): #On dessine ici tout les rayons avec les positions enregistrées dans la liste C
        pointx,pointy=C[k]
        cnvgame.create_line(x0, y0,pointx,pointy, fill='yellow',  width=2, tag='effaceligne' )#création d'un rayon avec deux coordonnées
     
    photoperso='perso.png'
    photocarre = tk.PhotoImage(file=photoperso) 
    cnvgame.create_image(x0,y0, image=photocarre,tag='effacecarre')
    """"cnv.create_rectangle(x0-5, y0-5,x0+5,y0+5, fill='black', tag='effacecarre')""" #creation d"un carré noir metant en lumière la position du clic soit du gardiant 
    
    #Permet dessiner l'or au premier plan au dessus des rayons
    if (len(Ldecouvertor)!=0):
         photoor='Gold50.png'
         photo = tk.PhotoImage(file=photoor) 
         for k in range (len(Ldecouvertor)):
            x,y=Ldecouvertor[k]
            cnvgame.create_image(x,y, image=photo,tag='or2')
    wndgame.mainloop()



#Fonction qui permet permet de recupérer soit coordonné de polygon préenregitré ou emplacement lingot d'or caché
def RecuperationPoint(fichier):
    file = open(f"{fichier}.txt", "r") 
    Lcote=[]
    del Lcote[:]
    
    for ligne in file:
            Lcoordonne=ligne.split(' ')
            X=int(Lcoordonne[0])
            Y=int(Lcoordonne[1])
            cote=X,Y
            Lcote.append(cote)
            
    return Lcote


"""Gestion du premier clic gauche dans le polygone: Création d'un champ de vision de l'utilisateur suivant 360 degrés """


def premierpoint(event):
    global x0,y0
    x0, y0 = event.x, event.y # coordonnées du point du clic
    Verification() #Fonction qui calcul si un lingot d'or n'a pas été observé dans le champ de vision de l'utilisateur
    gardiangame(x0,y0) #fonction qui permet de tracer les rayons jaunes autours de l'utilsateurs
    

"""Gestion du mouvement haut de l'utilsateur dans le polygone: touche Z """

pas=20 #Pas de déplaecment de l'utilisateur 

def mouvementhaut(event):
     global x0,y0
     x0,y0=x0,y0-pas
     
     #Pour ne pas sortir du polygone
     #le voleur se déplace avec un pas de 20 soit suivant x ou y 
     #on calcule si son prochain emplacement est en de dehors du polygone
     #si oui le voleur reste sur place
     if (len(cnvgame.find_overlapping(x0,y0,x0+1,y0+1))==0):
         x0,y0=x0,y0+pas
     
     Verification()
     gardiangame(x0,y0)
     
"""Gestion du mouvement droit de l'utilsateur dans le polygone: touche D """
     
def mouvementdroit(event):
     global x0,y0
     x0,y0=x0+pas,y0
     
     #idem
     if (len(cnvgame.find_overlapping(x0,y0,x0+1,y0+1))==0):
         x0,y0=x0-pas,y0
     
     Verification()
     gardiangame(x0,y0)
     
"""Gestion du mouvement gauche de l'utilsateur dans le polygone: touche Q """
     
def mouvementgauche(event):
     global x0,y0
     x0,y0=x0-pas,y0
     
     #idem
     if (len(cnvgame.find_overlapping(x0,y0,x0+1,y0+1))==0):
         x0,y0=x0+pas,y0
     
     Verification()
     gardiangame(x0,y0)
     
"""Gestion du mouvement bas de l'utilsateur dans le polygone: touche S """
    
def mouvementbas(event):
     global x0,y0
     x0,y0=x0,y0+pas
     
     #idem
     if (len(cnvgame.find_overlapping(x0,y0,x0+1,y0+1))==0):
         x0,y0=x0,y0-pas
    
     Verification()   
     gardiangame(x0,y0)
     
     
     

#Fonction clic droit informative la position du clic(x,y) et le nombre d'élément sous le clic
    
def position(event):
    x0, y0 = event.x, event.y
    print(x0,y0)
    print(len(cnvgame.find_overlapping(x0-25,y0-25,x0+25,y0+25)))

         
        
         

    
#Fonction reset qui permet d'effacer les éléments (cnv dessin) dans la fenêtre utilisée
#Pour chaque changement de niveau
def reset():

    cnvgame.delete('all')
    del Lsavepolygon[:]
    del Lsaveor[:]
    del Ldecouvertor[:]
    

#Fonction du niveau 1

def niveau1():
     global Lsavepolygon,Lsaveor
     

     reset()
     
    #Chargement des cotés du polygone niveau1 dans un dossier texte
     fichierpolygon='map1' #nom du fichier où est stocké les coordonnes des côtés  du polygone
     Lsavepolygon=RecuperationPoint(fichierpolygon)#Récupération des coordonnées des cotées dans le fichier enregistré
    #Création du polygone
     cnvgame.create_polygon(Lsavepolygon,fill='grey',width=epaiseur, outline='blue')
     print(Lsavepolygon)
     
     
     """photoor='Gold50.png'"""
     fichieror='or1' #nom du fichier où est stocké les coordonnes des lingots d'or caché
     Lsaveor=RecuperationPoint(fichieror)#Récupération des coordonnées des cotées dans le fichier enregistré
     print(Lsaveor)
     """photo = tk.PhotoImage(file=photoor) """
     
     #Permets d'afficher tous les lingots d'or cachées
     """for k in range (len(Lsaveor)):
        xa,ya=Lsaveor[k]
        cnv.create_image(xa,ya, image=photo)
        cnv.create_rectangle(xa-5,ya-5,xa+5,ya+5,fill='blue',tag='or')
    
     #Fonctionnalité qui permet de cacher les éléments tag='or' ici les carrées bleu
     cnv.itemconfigure('or', state="hidden")"""
     
   
    #Gestion des boutons et touches     
     
     cnvgame.bind('<3>', premierpoint)
     cnvgame.bind('<1>', position)
     cnvgame.bind('<z>', mouvementhaut)
     cnvgame.bind('<s>', mouvementbas)
     cnvgame.bind('<d>', mouvementdroit)
     cnvgame.bind('<q>', mouvementgauche)
     
     wndgame.mainloop()
     
#Fonction du niveau 2
     
def niveau2():
    
     global Lsavepolygon,Lsaveor
     

     reset()
     
    #Chargement des cotés du polygone niveau1 dans un dossier texte
     fichierpolygon='map2' #nom du fichier où est stocké les coordonnes des côtés du polygone
     Lsavepolygon=RecuperationPoint(fichierpolygon)#Récupération des coordonnées des cotées dans le fichier enregistré
    #Création du polygone
     cnvgame.create_polygon(Lsavepolygon,fill='grey',width=epaiseur, outline='blue')
     print(Lsavepolygon)
     
     
     """photoor='Gold50.png'"""
     fichieror='or2' #nom du fichier où est stocké les coordonnes des lingots d'or caché
     Lsaveor=RecuperationPoint(fichieror)#Récupération des coordonnées des cotées dans le fichier enregistré
     print(Lsaveor)
     """photo = tk.PhotoImage(file=photoor) """
     
     #Permets d'afficher tous les lingots d'or cachées
     """for k in range (len(Lsaveor)):
        xa,ya=Lsaveor[k]
        cnv.create_image(xa,ya, image=photo)
        cnv.create_rectangle(xa-5,ya-5,xa+5,ya+5,fill='blue',tag='or')
    
     #Fonctionnalité qui permet de cacher les éléments tag='or' ici les carrées bleu
     cnv.itemconfigure('or', state="hidden")"""
     
   
    #Gestion des boutons et touches     
     
     cnvgame.bind('<3>', premierpoint)
     cnvgame.bind('<1>', position)
     cnvgame.bind('<z>', mouvementhaut)
     cnvgame.bind('<s>', mouvementbas)
     cnvgame.bind('<d>', mouvementdroit)
     cnvgame.bind('<q>', mouvementgauche)
     
     wndgame.mainloop()
    
#Fonction du niveau 3

def niveau3():
     global Lsavepolygon,Lsaveor
     

     reset()
     
    #Chargement des cotés du polygone niveau1 dans un dossier texte
     fichierpolygon='map3' #nom du fichier où est stocké les coordonnes des côtés  du polygone
     Lsavepolygon=RecuperationPoint(fichierpolygon)#Récupération des coordonnées des cotées dans le fichier enregistré
    #Création du polygone
     cnvgame.create_polygon(Lsavepolygon,fill='grey',width=epaiseur, outline='blue')
     print(Lsavepolygon)
     
     
     """photoor='Gold50.png'"""
     fichieror='or3' #nom du fichier où est stocké les coordonnes des lingots d'or caché
     Lsaveor=RecuperationPoint(fichieror)#Récupération des coordonnées des cotées dans le fichier enregistré
     print(Lsaveor)
     """photo = tk.PhotoImage(file=photoor) """
     
     #Permets d'afficher tous les lingots d'or cachées
     """for k in range (len(Lsaveor)):
        xa,ya=Lsaveor[k]
        cnv.create_image(xa,ya, image=photo)
        cnv.create_rectangle(xa-5,ya-5,xa+5,ya+5,fill='blue',tag='or')
    
     #Fonctionnalité qui permet de cacher les éléments tag='or' ici les carrées bleu
     cnv.itemconfigure('or', state="hidden")"""
     
   
    #Gestion des boutons et touches     
     
     cnvgame.bind('<3>', premierpoint)
     cnvgame.bind('<1>', position)
     cnvgame.bind('<z>', mouvementhaut)
     cnvgame.bind('<s>', mouvementbas)
     cnvgame.bind('<d>', mouvementdroit)
     cnvgame.bind('<q>', mouvementgauche)
     
     wndgame.mainloop()
     

    


        
Ldecouvertor=[] #Liste des coordonnes des lingots découvert par l'utilisateur


#Fonction qui permet de vérifier sur tous les emplacements de lingots d'or 
#si le champ de vision du voleur de là pas decouvert

def Verification():
    global Lsaveor, Ldecourvertor
       
#Pour tous les lingots d'or non trouvé on parcourt la liste et vérifie que le champ de vision de l'utilisateur ne survole pas un lingot d'or
    if len(Lsaveor)!=0: 
        for k in range (len(Lsaveor)):
            x,y=Lsaveor[k]
            if len(cnvgame.find_overlapping(x-5,y-5,x+5,y+5))>1: #on mesure le nombre d'élement à l'emplacement d'un lingot d'or
                """cnv.create_rectangle(x-10,y-10,x+10,y+10,fill='yellow')"""
                Ldecouvertor.append([x,y]) #on l'ajoute dans la liste lingot d'or découvvert pour l'affiché par la suite dans la fonction guardiant
                print(Ldecouvertor)
                del Lsaveor[k]  #on l'ajoute dans la liste lingot d'or non trouvé 
                break
                

    #Si tous les lingots d'or ont été trouvé le jeu est terminé la liste est nul
    if len(Lsaveor)==0:
        cnvgame.create_text(largeur//2,hauteur//2,text='Bien joué niveau completé 👍😊👌',font=("Arial", 40),fill='gold')
        




#---------------------------------------------------------------------------------------------------------

#METHODE 3 alias c 

#---------------Partie création du pôlygone et du gardien en utilisant utilisant les barrycentres-------------


def methodec():
    
    global wndc,cnvc,largeur,hauteur  
    
    wnd.destroy()
    wndc =tk.Tk()
    wndc.title("Methodec_Art_Gallery")
    cnvc = tk.Canvas(wndc, width=largeur, height=hauteur, bg='white')
    btn=tk.Button(wndc,text="Sauvegarder",command=sauvegardePointbutton,bg='orange',activebackground='#345',activeforeground='white')
    btn.place(x=largeur-70,y=hauteur-50)
    btn=tk.Button(wndc,text="Charger",command=loadbuttonc,bg='orange',activebackground='#345',activeforeground='white')
    btn.place(x=largeur-45,y=hauteur-25)
    btn=tk.Button(wndc,text="Menu",command=retourmenuc,bg='orange', activebackground='#345',activeforeground='white')
    btn.place(x=largeur-35,y=hauteur-75)
    cnvc.pack()
    cnvc.focus_set()
    Titre = tk.Label(wndc,text="Dessiner polygone puis T pour dessiner")
    Titre2 = tk.Label(wndc,text="Clique droite pour placer point puis touche A pour gardien ")
    Titre.pack()
    Titre2.pack()
    
    cnvc.pack()
    cnvc.focus_set()      # quand on utilise le clavier cela aura lieu dans la fenetre cnv
    cnvc.bind('<1>', creer_polyc)
    cnvc.bind('<a>', printBary)
    cnvc.bind('<3>', gardianc)
    cnvc.bind('<r>', resetc)
    cnvc.bind('<b>', airepoygonméthode1)
    cnvc.bind('<n>', airepoygonméthode2)
    
    wndc.mainloop()





""" Lsave = []
L=[]
epaiseur = 2
empGar=[]
barVal=[]
bar=[]"""


def retourmenuc():
    global wnd,wndc,cnv,cnvc
    
    del Lsave[:]    

    wndc.destroy()
    menu()
    
def creer_polyc(event):
    """Gestion d'un clic : créer une ligne réduit au point du clic."""
    global x0, y0, id_rect
    x0, y0 = event.x, event.y
    Lsave.append([x0,y0])
    id_rect = cnvc.create_line(x0, y0, x0, y0,fill='black', width=3)
    cnvc.bind('<Motion>', redessiner_polyc)
    cnvc.bind('<t>', fixer_polyc)

def redessiner_polyc(event):
    """Gestion des mouvements de la souris : redessiner la ligne."""
    cnvc.coords(id_rect, x0, y0, event.x, event.y)
    coordonne=x0,y0
    L.append(coordonne)

def fixer_polyc(event):
    """Au relachement du bouton arrêter de suivre les mouvements."""
    print("Le polygone est dessiné")
    
    xdepart,ydepart=L[0] #récupération du premier point 
    cnvc.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=1) #création de la dernière ligne entre le point de départ et le dernier point
    cnvc.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnvc.delete('all') #supprime tout les premiers traits 
    cnvc.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]

def gardianc(event):
    """Placement du gardien

    """
    global empGar
    empGar=[event.x,event.y]
    cnvc.create_rectangle(empGar[0]-5, empGar[1]-5,empGar[0]+5,empGar[1]+5, fill='black')

def equationc(B,D1,D2):     
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

def equation2(B,D1,D2):     #B coordonne du barycentre, D1 coordonne premier point de la droite; D2: coordonne deuxieme point de la droite
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

def posDroite(G,A,B,C) : # G gariden, A angle du polygone, B angle du polygone précedent, C angle du polygone suivant
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
            if equationc(barValTri1[z],Lsave[y],Lsave[y+1]) == True :
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
            if equationc(point,Lsave[u],Lsave[u+1]) == True :
                triPoint.append([module(Lsave[u],point),point])
        triPoint.sort()
        #print(triPoint)
        if triPoint != [] :
            if triPoint[0][1] not in polygoneVue :
                polygoneVue.append(triPoint[0][1])
            if triPoint[-1][1] not in polygoneVue :
                polygoneVue.append(triPoint[-1][1])
    #print(polygoneVue)

    cnvc.create_polygon(polygoneVue,fill = "pink")

    Affichenum = 0
    for point in polygoneVue : 
        Affichenum += 1
        cnvc.create_oval(int(point[0])-4,int(point[1])-4,int(point[0])+4,int(point[1])+4,fill="pink")
        cnvc.create_text(int(point[0])+10,int(point[1])+10,text = Affichenum)

    cnvc.create_rectangle(empGar[0]-5, empGar[1]-5,empGar[0]+5,empGar[1]+5, fill='black')
    

def resetc(event):

    cnvc.delete('all')
    del Lsave[:]
    del empGar[:]
    del barVal[:]
    del bar[:]


def loadbuttonc():
    global fenetrePrincipale, e
    fenetrePrincipale = tk.Tk()
    l = tk.Label(fenetrePrincipale, text = "Ouvir Nom du fichier:")
    e = tk.Entry(fenetrePrincipale)
    b = tk.Button(fenetrePrincipale ,text="Submit", command=Drawc)
    l.pack()
    e.pack()
    b.pack()
    fenetrePrincipale.mainloop()

def Drawc():
    global Lsave
    del Lsave[:]
    fichier=e.get()
    
    Lsave=RecuperationPoint(fichier)#Recupération des coordonnees des cotées dans le fichier enregistré
    
    cnvc.delete('all') #Supprime les éléments déjà sur la fenêtre
    cnvc.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue') #Création du polygone
    fenetrePrincipale.destroy()




menu()