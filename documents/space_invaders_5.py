import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((533,700))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('background2.png')
game_over_screen = pygame.Surface((800, 600))
game_over_background = pygame.image.load('game_over_background.png')  # Remplacez 'game_over_background.png' par votre propre image de fond
game_over = False
# creation du joueur
player = space.Joueur()
#Creation des coeurs

listePv = []
for indice in range(player.health):
    pv = space.Heart(player)
    listePv.append(pv)

# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            elif event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            elif event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"
        else:
            player.sens ='O'
    if player.health <= 0:
        game_over = True
        screen.blit(game_over_background, (0, 0))
    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            player.marquer()
            print(f"Score = {player.score} points")
            
        if ennemi.touchejoueur(player)==True:
            player.perte_de_pv(pv)
            print(f'Point de vie = {player.health}')
            if len(listePv)==0:
                listePv.pop(player.health)
            
    myfont = pygame.font.SysFont("Pixel.ttf", 30)
    score_display = myfont.render(f'Score = {player.score}', 1, (255,255,0))
    screen.blit(score_display, (25, 25))

    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.position,player.hauteur])# appel de la fonction qui dessine le vaisseau du joueur
    
    # Health
    z=0
    for health in listePv:
        screen.blit(health.image,[health.position, health.hauteur+z])
        z+=50
        
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    if game_over:
        screen.blit(game_over_background, (0, 0))
        myfont = pygame.font.SysFont("Pixel.ttf", 40)
        game_over_text = myfont.render("Game Over", 1, (255, 0, 0))
        score_text = myfont.render(f'Score: {player.score}', 1, (255, 255, 0))
        screen.blit(game_over_text, (200, 250))
        screen.blit(score_text, (200, 300))
        
    pygame.display.update() # pour ajouter tout changement à l'écran
