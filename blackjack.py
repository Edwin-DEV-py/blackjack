#zona de import
import pygame



#crear la interfaz grafica
pygame.init()

VENTA_ANCHO = 600
VENTANA_LARGO = 600
VENTANA = pygame.display.set_mode((VENTA_ANCHO,VENTANA_LARGO))
pygame.display.set_caption("Mesa de Blackjack")

run_game = True

while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False #para cerrarlo solo es darle a la X

pygame.quit()