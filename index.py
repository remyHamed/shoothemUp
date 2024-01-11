import pygame
import sys

pygame.init()


largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Shoot Them Up')
fond = pygame.image.load('./assset/background/background.png')
fond = pygame.transform.scale(fond, (largeur, hauteur))

y_fond = 0
vitesse_defilement = 1

joueur_image = pygame.image.load('./assset\player\ship.png')
newWidht = 50  
newHight = 50 

joueur_image = pygame.transform.scale(joueur_image, (newWidht, newHight))
joueur_pos = [largeur // 2, hauteur // 2] 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y_fond += vitesse_defilement
    if y_fond >= hauteur:
        y_fond = 0

  
    fenetre.blit(fond, (0, y_fond))
    fenetre.blit(fond, (0, y_fond - hauteur))
    
    fenetre.blit(joueur_image, joueur_pos)

    pygame.display.update()


pygame.quit()
sys.exit()
