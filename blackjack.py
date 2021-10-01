#zona de import
import pygame
from pygame import *



#crear la interfaz grafica
pygame.init()

VENTANA = pygame.display.set_mode([710,440])
tiempo = pygame.time.Clock()
pygame.display.set_caption("Mesa de Blackjack")

fondo = pygame.image.load("fondo.png").convert()

run_game = True

while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False #para cerrarlo solo es darle a la X
    
    VENTANA.blit(fondo,[0,0])

    pygame.display.flip()
    tiempo.tick(60)

pygame.quit()