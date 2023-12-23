

"""
Game:La ruée vers l'or

Le but du jeu est de trouver tous les lingots d'or le plus vite possible selon tous les niveaux
"""

import tkinter as tk
import math 
largeur=1100 #Largeur de la fenêtre tkinter
hauteur=700 #Hauteur de la fenêtre tkinter
epaiseur=1 #taille des bordures du polygone
L=[] #création d'une liste avec tout les coordonnées du polynôme (event.x,event.y) 
Lsave=[]  #création d'une liste avec tout les coordonnées des cotés 
Lcote=[] #création d'une liste avec tout les coordonnées des cotés enregistré dans un dossier texte
Lsavepolygon=[]
Lsaveor=[]





    
listeevent=[]  
 
#---Fonction Gardian dessine rayon chanmp de vision suivit d'un avatar marquant sa position-------------
#---(Clic droit de la souris pour positioner le premier point)

    
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
        while collision==1 and R<50: #On deplace le point suivant le rayon jusqu'a qu'il sorte du polynôme 
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
     
     #Pour ne pas sorit du polygone
     #le voleur se déplace avec un pas de 20 soit suivant x ou y 
     #on calcule si son prochain emplacement est en de dehors du polygone
     #si oui le voleur reste sur place
     if (len(cnvgame.find_overlapping(x0-1,y0-1,x0+1,y0+1))==0):
         x0,y0=x0,y0+20
     
     Verification()
     gardiangame(x0,y0)
     
"""Gestion du mouvement droit de l'utilsateur dans le polygone: touche D """
     
def mouvementdroit(event):
     global x0,y0
     x0,y0=x0+pas,y0
     
     #idem
     if (len(cnvgame.find_overlapping(x0-1,y0-1,x0+1,y0+1))==0):
         x0,y0=x0-pas,y0
     
     Verification()
     gardiangame(x0,y0)
     
"""Gestion du mouvement gauche de l'utilsateur dans le polygone: touche Q """
     
def mouvementgauche(event):
     global x0,y0
     x0,y0=x0-pas,y0
     
     #idem
     if (len(cnvgame.find_overlapping(x0-1,y0-1,x0+1,y0+1))==0):
         x0,y0=x0+pas,y0
     
     Verification()
     gardiangame(x0,y0)
     
"""Gestion du mouvement bas de l'utilsateur dans le polygone: touche S """
    
def mouvementbas(event):
     global x0,y0
     x0,y0=x0,y0+pas
     
     #idem
     if (len(cnvgame.find_overlapping(x0-1,y0-1,x0+1,y0+1))==0):
         x0,y0=x0,y0-20
    
     Verification()   
     gardiangame(x0,y0)
     
     
     

#Fonction clic droit informative la position du clic(x,y) et le nombre d'élément sous le clic
    
def position(event):
    x0, y0 = event.x, event.y
    print(x0,y0)
    print(len(cnvgame.find_overlapping(x0-25,y0-25,x0+25,y0+25)))

         
        
         
#Fonction lancement du jeu l'ulisateur a le choix de 3 niveaux (boutons)     
  
def game():    
    global wndgame,cnvgame
    #creation de la fenètre
    wndgame = tk.Tk()
    wndgame.title("Choix du niveau")
    cnvgame = tk.Canvas(wndgame, width=largeur, height=hauteur, bg='white')
    
    #création des trois boutons représentant les trois niveaux (1,2,3) en colonne
    btn1=tk.Button(wndgame,text="Niveau 1", bg='orange',command=niveau1)
    btn2=tk.Button(wndgame,text="Niveau 2", bg='orange',command=niveau2)
    btn3=tk.Button(wndgame,text="Niveau 3", bg='orange',command=niveau3)
    """btn4=tk.Button(wnd,text="Menu", bg='orange',command=retourmenu)"""
    btn1.pack()
    btn2.pack()
    btn3.pack()
    """btn4.pack()"""

    
    Titre = tk.Label(wndgame,text="Choix du niveau")
    Titre.pack()
    
     
    cnvgame.pack()
    cnvgame.focus_set()
    wndgame.mainloop()
    
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
        
game()

