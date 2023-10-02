import pygame
import random
import math

class Joueur:

    def __init__(self):
        self.sens = "O"
        self.position = 350
        self.image = pygame.image.load('player.png')
        self.score = 0
        self.health=3
        self.hauteur=500

    def deplacer(self):
        if self.sens == 'gauche' and self.position > 55:
            self.position -= 6
        elif self.sens == 'droite' and self.position < 415:
            self.position += 6
        #elif self.sens == 'O':
            #self.position

    def tirer(self):
        pass
    
    def marquer(self):
        self.score += 1
    
    def perte_de_pv(self,heart):
        self.health-=1
        heart.pv_perdu()
        return True

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

    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40) and self.etat=='tiree':
            self.etat = "attente"
            vaisseau.respawn()  # Réinitialisez la position de l'ennemi ici
            return True

class Ennemi:
    NbEnnemis = 6

    def __init__(self):
        self.respawn()
        self.type = random.randint(1, 3)
        if self.type == 1:
            self.image = pygame.image.load("camion.png")
            self.vitesse = 1
        elif self.type == 2:
            self.image = pygame.image.load("jaune.png")
            self.vitesse = 2
        elif self.type == 3:
            self.vitesse = 3
            self.image = pygame.image.load("rouge.png")


    def avancer(self):
        self.hauteur += self.vitesse

        if self.hauteur > 700:
            self.respawn()

    def respawn(self):
        self.type = random.randint(1, 3)
        if self.type == 1:
            self.image = pygame.image.load("camion.png")
            self.vitesse = 1
        elif self.type == 2:
            self.image = pygame.image.load("jaune.png")
            self.vitesse = 2
        elif self.type == 3:
            self.vitesse = 3
            self.image = pygame.image.load("rouge.png")
        self.depart = random.randint(50, 415)
        self.hauteur = 10
        
    def touchejoueur(self,joueur):
        if (math.fabs(self.hauteur - joueur.hauteur) < 40) and (math.fabs(self.depart - joueur.position) < 40):
            self.respawn()
            return True

class Heart():
    def __init__(self,joueur):
        self.image = pygame.image.load("heart3.png")
        self.joueur = joueur
        self.position = 450
        self.hauteur = 20
        
    def pv_perdu(self):
        self.position+=100
