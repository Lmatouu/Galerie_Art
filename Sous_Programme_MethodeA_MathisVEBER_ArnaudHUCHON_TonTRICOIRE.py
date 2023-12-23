

"""
M�thode A
#---------------Partie cr�ation du polygone et le gardien par plusieurs droites suivant 360 degr�s-------------
#---(Clic gauche de la souris)
"""

import tkinter as tk
import math 

largeur=800 #Largeur de la fen�tre tkinter
hauteur=800 #Hauteur de la fen�tre tkinter
epaiseur=1 #taille des bordures du polygone
L=[] #cr�ation d'une liste avec tout les coordonn�es du polyn�me (event.x,event.y) 
Lsave=[]  #cr�ation d'une liste avec tout les coordonn�es des cot�s 
Lcote=[] #cr�ation d'une liste avec tout les coordonn�es des cot�s enregistr� dans un dossier texte


#---------------Partie cr�ation du p�lynome � la main droite pas droite-------------
#---(Clic gauche de la souris)

def creer_rect(event):
    """Gestion d'un clic : cr�er un rectangle r�duit au point du clic."""
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
    """Au relachement du bouton arr�ter de suivre les mouvements."""
    print("Le polygone est dessin�")
    
    xdepart,ydepart=L[0] #r�cup�ration du premier point 
    cnv.create_line(event.x, event.y, xdepart,ydepart,fill='black', width=3) #cr�ation de la derni�re ligne entre le point de d�part et le dernier point
    cnv.unbind('<Motion>')
    Lsave.append([event.x,event.y]) 
    cnv.delete('all')
    cnv.create_polygon(Lsave, fill='grey', width=epaiseur, outline='blue')
    del L[:]
   
#--Fonction Reset  ---------------------------------
def reset(event):
    
    cnv.unbind('<Motion>')
    cnv.delete('all') #Supprimer la f�netre et tout les �l�ments dans les liste
    del L[:]
    del Lsave[:]
    del listeevent[:]
    del Lcote[:]
    
    
    
listeevent=[]  
 
#---Fonction Gardian dessine rayon chanmp de vision suivit d'un carr�e noir marquant sa position-------------
#---(Clic droit de la souris)

def gardian(event): 
    """Gestion d'un clic dans le polygone: Cr�ation d'un champ de vision suivant 360 degr�s """
     #M�thode � l'aide des arcs param�triques cr�ation de 360 rayons autour du gardians avec m�thode overlapping pour stopper rayon
    x0, y0 = event.x, event.y # coordonn�es du point du clic
    coordonne=x0, y0
    listeevent.append(coordonne)
    
    cnv.itemconfigure('effaceligne', state="hidden") #Gestion de tag pour"faire disparaitre ancien rayon"
    cnv.itemconfigure('effacecarre', state="hidden") #Gestion de tag pour"cacher ancien carre"
    #cnv.create_rectangle(x0,y0,largeur,y0+1)
    
    carreselec=len(cnv.find_overlapping(x0-5,y0-5,x0+5,y0+5)) #mesure sur le nombre d'�l�ment sous le point 
    print(carreselec)
    if carreselec == 0 : #D�termination si point est � l'int�rieur du polygone ou � l'ext�rieur
        print('Placer un point � l int�rieur du polygone')
        cnv.itemconfigure('effacecarre', state="normal",fill='black')#Gestion de tag pour" faire faire raparaitre ancien rayon"
        cnv.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
        
        return
   
    
    
    C=[] #liste contenant tout les coordon�es des points de la bordure des rayons
    for k in range (360): # Pour faire un tour
        x=math.radians(k) #On convertie en radians pour l'utisation de cosinus et sinus   
        a=math.cos(x)
        b=math.sin(x)
        R=1
        collision=len(cnv.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b)) #mesure sur le nombre d'�l�ment sous le point 
        while collision==1: #On deplace le point suivant le rayon jusqu'a qu'il sorte du polyn�me 
            R+=1
            collision=len(cnv.find_overlapping(x0+R*a-1,y0+R*b-1,x0+R*a,y0+R*b))
        
        
        pointx=x0+(R-epaiseur)*a  #position du point suivant x - la taille de la bordure
        pointy=y0+(R-epaiseur)*b #position du point suivant y - la taille de la bordure
        coordonne=pointx,pointy
        C.append(coordonne) #on l'ajoute dans notre liste contenant tout les coordon�es des points de la bordure des rayons
        
    for k in range (360): #On dessine ici tout les rayons avec les positions enregistr�es dans la liste C
        pointx,pointy=C[k]
        cnv.create_line(x0, y0,pointx,pointy, fill='yellow',  width=1, tag='effaceligne' )#cr�ation d'un rayon avec deux coordonn�es
    cnv.itemconfigure('effaceligne', state="normal") #Gestion de tag pour" faire faire raparaitre ancien rayon"
    
    for k in range (len(listeevent)):#On dessine ici tout les carr�s de gardiant event m�moriser en premier plan
        x0,y0=listeevent[k]
        cnv.create_rectangle(x0-5, y0-5,x0+5,y0+5, fill='black', tag='effacecarre') #creation d"un carr� noir metant en lumi�re la position du clic soit du gardiant 


#----------Fonction Enregistrement d'un polygone enregistr�----------------------
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



#----------Fonction Dessiner d'un polygone enregistr�----------------------

def RecuperationPoint(fichier):
    file = open(f"{fichier}.txt", "r") 
    for ligne in file:
            Lcoordonne=ligne.split(' ')
            X=Lcoordonne[0]
            Y=Lcoordonne[1]
            cote=X,Y
            Lcote.append(cote)
            
    return Lcote



#----------Fonction Ouvrier Dossier Texte ou le polygone est enregistr�----------------------
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

#----------Cr�ation du polygone enregristr�-----------------
def Draw():
    
    fichier=e.get()
    
    Lcote=RecuperationPoint(fichier)#Recup�ration des coordonnees des cot�es dans le fichier enregistr�
    
    cnv.delete('all') #Supprime les �l�ments d�j� sur la fen�tre
    cnv.create_polygon(Lcote, fill='grey', width=epaiseur, outline='blue') #Cr�ation du polygone
    
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

