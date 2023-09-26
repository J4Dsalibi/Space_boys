import pygame
import random
import math

class Joueur:

    def __init__(self):
        self.sens = "O"
        self.position = 350
        self.image = pygame.image.load('player.png')
        self.score = 0

    def deplacer(self):
        if self.sens == 'gauche' and self.position > 90:
            self.position -= 6
        elif self.sens == 'droite' and self.position < 520:
            self.position += 6
        elif self.sens == 'O':
            self.position

    def tirer(self):
        pass
    
    def marquer(self):
        self.score += 1

class Balle:

    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position
        self.hauteur = 492
        self.image = pygame.image.load('balle.png')
        self.etat = "attente"

    def bouger(self):
        if self.etat == "attente":
            self.depart = self.tireur.position + 33
            self.hauteur = 492
        elif self.etat == "tiree":
            self.hauteur -= 10

        if self.hauteur < 0:
            self.etat = "attente"
    def toucher(self,vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "attente"
            return True
        
class Ennemi() :
    NbEnnemis = 7

    def __init__(self):
        self.depart = random.randint(90,520)
        self.hauteur = 10
        self.type = random.randint(1,3)
        if  self.type == 1:
            self.image = pygame.image.load("camion.png")
            self.vitesse = 1
        elif self.type ==2:
            self.image = pygame.image.load("jaune.png")
            self.vitesse = 2
        elif self.type == 3:
            self.vitesse = 3
            self.image = pygame.image.load("rouge.png")

    def avancer(self):
        self.hauteur += self.vitesse
        
    def disparaitre(self):
        self.depart = random.randint(90,520)
        self.hauteur = 10
        self.type = random.randint(1,3)
        if  self.type == 1:
            self.image = pygame.image.load("camion.png")
            self.vitesse = 1
        elif self.type ==2:
            self.image = pygame.image.load("jaune.png")
            self.vitesse = 2
        elif self.type == 3:
            self.vitesse = 3
            self.image = pygame.image.load("rouge.png")
        
