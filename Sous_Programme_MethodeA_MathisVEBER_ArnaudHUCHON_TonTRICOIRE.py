

"""
Méthode A
#---------------Partie création du polygone et le gardien par plusieurs droites suivant 360 degrés-------------
#---(Clic gauche de la souris)
"""

import tkinter as tk
import math 

largeur=800 #Largeur de la fenêtre tkinter
hauteur=800 #Hauteur de la fenêtre tkinter
epaiseur=1 #taille des bordures du polygone
L=[] #création d'une liste avec tout les coordonnées du polynôme (event.x,event.y) 
Lsave=[]  #création d'une liste avec tout les coordonnées des cotés 
Lcote=[] #création d'une liste avec tout les coordonnées des cotés enregistré dans un dossier texte


#---------------Partie création du pôlynome à la main droite pas droite-------------
#---(Clic gauche de la souris)

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

#--Quand l'utilisateur a finit de tracer par points son polygone (Touche 'T')-----------
def fixer_rect(event):
    """Au relachement du bouton arrêter de suivre les mouvements."""
    print("Le polygone est dessiné")
    
    xdepart,ydepart=L[0] #récupération du premier point 
    cnv.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=3) #création de la dernière ligne entre le point de départ et le dernier point
    cnv.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnv.delete('all')
    cnv.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]
   
#--Fonction Reset  ---------------------------------
def reset(event):
    
    cnv.unbind('<Motion>')
    cnv.delete('all') #Supprimer la fênetre et tout les éléments dans les liste
    del L[:]
    del Lsave[:]
    del listeevent[:]
    del Lcote[:]
    
    
    
listeevent=[]  
 
#---Fonction Gardian dessine rayon chanmp de vision suivit d'un carrée noir marquant sa position-------------
#---(Clic droit de la souris)

def gardian(event): 
    """Gestion d'un clic dans le polygone: Création d'un champ de vision suivant 360 degrés """
     #Méthode à l'aide des arcs paramètriques création de 360 rayons autour du gardians avec méthode overlapping pour stopper rayon
    x0, y0 = event.x, event.y # coordonnées du point du clic
    coordonne=x0, y0
    listeevent.append(coordonne)
    
    cnv.itemconfigure('effaceligne', state="hidden") #Gestion de tag pour"faire disparaitre ancien rayon"
    cnv.itemconfigure('effacecarre', state="hidden") #Gestion de tag pour"cacher ancien carre"
    #cnv.create_rectangle(x0,y0,largeur,y0+1)
    
    carreselec=len(cnv.find_overlapping(x0-5,y0-5,x0+5,y0+5)) #mesure sur le nombre d'élément sous le point 
    print(carreselec)
    if carreselec == 0 : #Détermination si point est à l'intérieur du polygone ou à l'extérieur
        print('Placer un point à l intérieur du polygone')
        cnv.itemconfigure('effacecarre', state="normal",fill='black')#Gestion de tag pour" faire faire raparaitre ancien rayon"
        cnv.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
        
        return
   
    
    
    C=[] #liste contenant tout les coordonées des points de la bordure des rayons
    for k in range (360): # Pour faire un tour
        x=math.radians(k) #On convertie en radians pour l'utisation de cosinus et sinus   
        a=math.cos(x)
        b=math.sin(x)
        R=1
        collision=len(cnv.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b)) #mesure sur le nombre d'élément sous le point 
        while collision==1: #On deplace le point suivant le rayon jusqu'a qu'il sorte du polynôme 
            R+=1
            collision=len(cnv.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b))
        
        
        pointx=x0+(R-epaiseur)*a  #position du point suivant x - la taille de la bordure
        pointy=y0+(R-epaiseur)*b #position du point suivant y - la taille de la bordure
        coordonne=pointx,pointy
        C.append(coordonne) #on l'ajoute dans notre liste contenant tout les coordonées des points de la bordure des rayons
        
    for k in range (360): #On dessine ici tout les rayons avec les positions enregistrées dans la liste C
        pointx,pointy=C[k]
        cnv.create_line(x0, y0,pointx,pointy, fill='yellow',  width=1, tag='effaceligne' )#création d'un rayon avec deux coordonnées
    cnv.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
    
    for k in range (len(listeevent)):#On dessine ici tout les carrés de gardiant event mémoriser en premier plan
        x0,y0=listeevent[k]
        cnv.create_rectangle(x0-5, y0-5,x0+5,y0+5, fill='black', tag='effacecarre') #creation d"un carré noir metant en lumière la position du clic soit du gardiant 


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
    file = open(f"{fichier}.txt", "r") 
    for ligne in file:
            Lcoordonne=ligne.split(' ')
            X=Lcoordonne[0]
            Y=Lcoordonne[1]
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
    
    fichier=e.get()
    
    Lcote=RecuperationPoint(fichier)#Recupération des coordonnees des cotées dans le fichier enregistré
    
    cnv.delete('all') #Supprime les éléments déjà sur la fenêtre
    cnv.create_polygon(Lcote, fill='grey', width=epaiseur, outline='blue') #Création du polygone
    
    del Lcote[:]
    fenetrePrincipale.destroy()




    
wnd = tk.Tk()
wnd.title("Art_Gallery_MethodeA")
cnv = tk.Canvas(wnd, width=largeur, height=hauteur, bg='white')
cnv.pack()
cnv.focus_set()
Titre = tk.Label(wnd,text="Dessiner polygon puis T  pour dessiner")
Titre2 = tk.Label(wnd,text="Clique droite gardian")
Titre.pack()
Titre2.pack()
cnv.bind('<l>', load)
cnv.bind('<1>', creer_rect)
cnv.bind('<3>', gardian)
cnv.bind('<r>', reset)
cnv.bind('<s>', sauvegardePoint)

wnd.mainloop()

