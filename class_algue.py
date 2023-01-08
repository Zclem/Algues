"""
Created on Thu Dec 22 10:52:18 2022

@author: Team algues
"""
import random as rd
import numpy as np
import settings as config

# === Population d'algues === #
        
class Population:
    """
    Représente une population d'algues. Chaque algue est représenté par son indice i, et 
    les informations de chaque algue sont stocké dans des tableaux numpy. Ainsi, une algue
    est définie par sa position x, y, son age (temps entre les reproductions), sa taille 
    (stade de reproduction), son statut (aggloméré ou non.). Ainsi, la population est définie 
    aussi par son effectif (nombre_algues). 
    AVIS?
    """
    def __init__(self, nombre_algues, Box):
        # Nombre d'algues de la population
        self.nombre_algues = nombre_algues
        # Coordonnées de chaque algue
        self.x = np.array([])
        self.y = np.array([])
        # Age de chaque algue
        self.age = np.array([])
        # Stade de croissance / Taille
        self.taille = np.array([])
        # Etat: True si aggregee, False si non aggrégée
        self.aggregat = np.array([])
        
        # Generation de chaque algue, en vérifiant qu'aucune ne soit à la même coordonnée
        for i in range(nombre_algues):
            x1 = rd.randint(0, Box.x_max)
            y1 = rd.randint(0, Box.y_max)
            # Verification de la présence des coordonnées dans la liste, si oui on les modifie
            not_in_list = False
            while not_in_list == False:
                not_in_list = True
                for j in range(i):
                    if x1 == self.x[j] and y1 == self.y[j]:
                        x1 = rd.randint(0, Box.x_max)
                        y1 = rd.randint(0, Box.y_max)
                        not_in_list = False
                        j = i
            # Ajout de l'algue dans la population
            self.x = np.append(self.x, x1)
            self.y = np.append(self.y, y1)
            self.age = np.append(self.age, 0)
            self.taille = np.append(self.taille, 0)
            self.aggregat = np.append(self.aggregat, False)
            
    def afficher_coord_algues(self):
        """
        Affiche les coordonnées de chaque algue dans la console. 
        """
        print("x ; y \n")
        for i in range (self.nombre_algues):
            print("{} ; {}\n".format(self.x[i], self.y[i]))
            
    
    def supprimer_algue(self, tab):
        """
        Supprime de la population l'ensemble des élements dont l'indice est dans le tableau. 
        tab est soit un tableau d'entier soit un entier (quand on veut supprimer une cellule)
        
        Paramètres
        ------
        tab: tableau d'entiers, ou nombre entier positif
            Indices à supprimer. Doivent être plus petit que le nombre d'algues.
        """
        self.x = np.delete(self.x, tab, 0)
        self.y = np.delete(self.y, tab, 0)
        self.age = np.delete(self.age, tab, 0)
        self.aggregat = np.delete(self.aggregat, tab, 0)
        self.taille = np.delete(self.taille, tab, 0)
        self.nombre_algues = np.size(self.x)
    

        
        
# === Zone de simulation des algues === #

class Box:
    """
    Représente la zone de simulation où se déplaceront et évolueront les algues. 
    Est défini par un couple x_max et y_max entiers, qui représentent les limites de
    l'affichage et donc de la simulation.
    
    Parametres
    ------
    x_max: float
        coordonée x maximale de la zone de simulation
    y_max: float
        coordonée y maximale de la zone de simulation
        
    """
    
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
    
    def modifier(self, x, y):
        """
        Modifie le couple x_max y_max de la Box par un nouveau couple x,y. 
        
        Paramètres        
        ------
        x: entier strictement positif
            nouvelle coordonnée x_max
        y: entier strictement positif
            nouvelle coordonnée y_max
        """
        self.x_max = x
        self.y_max = y
    
    def afficher_dimensions(self):
        """
        Affiche les dimensions de la zone de simulation. 
        """
        print("Dimensions: {} x {}".format(self.x_max, self.y_max))
 

    