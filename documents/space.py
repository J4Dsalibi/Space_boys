import pygame  # necessaire pour charger les images et les sons


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = "O"
        self.position = 400
        self.image = pygame.image.load('vaisseau.png')
    def deplacer(self):
        if self.sens=='gauche':
            self.position-=0.5
        elif self.sens=='droite':
            self.position+=0.5
