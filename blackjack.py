#zona de import
from _typeshed import Self
import pygame
from pygame import *
from enum import Enum,IntEnum
import random



#######################crear la interfaz grafica#######################
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

####################Boton#######################

# codigo para implementar boton de inicio 
# self.play_boton = boton(self, "Play")

# codigo para poner la pantalla de jugar en el caso que no se encuentre en partida
# if not self.juego_activado:
#     self.play_boton.dibujaboton()

# codigo para evento en el que al precionar play lo envia al juego
# elif event.type == pygame.MOUSEBUTTONDOWN:
#     mousepos = pygame.mouse.get_pos()
#     self.checaboton(mousepos)

class Botton:
    def __init__(self, a_game, texto):
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.color = (255,0,0)
        self.textcolor = (255, 255, 255)

        self.font = pygame.font.sysfont(None, 48)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prepara_texto(texto)

#boton inicio
    def prepara_texto(self, texto):
        self.texto_image = self.font.render(texto, True, self.textcolor, self.color)
        self.texto_image_rect = self.texto_image.get_rect()
        self.texto_image_rect.center = self.rect.center

    def dibujaboton(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.texto_image, self.texto_image_rect)
    
#boton de reiniciar cuando el juego no se este ejecutando

    def checaboton(self, mousepos):
        self.botonp = self.play_boton.rect.colllidepoint(mousepos)
        if self.botonp and not self.run_game:
            self.estadistica.reinicia()
            self.run_game = True


#################clase carta#######################
class Carta():
    def __init__(self,suit,simbolo,valor,color):
        self.value = suit
        self.value = simbolo
        self.value = valor
        self.value = color

#datos de las cartas
Valor_carta = [11,2,3,4,5,6,7,8,9,10,10,10]
Simbolo_carta = list(range(1,14))
Suit_carta = list(range(1,5))

#########################clase dealer#####################

class Dealer():
    def dealer():
        deck = []
        for j in range(len(Valor_carta)):
            for k in Suit_carta:
                deck.append(Carta(Valor_carta[j],Simbolo_carta[j],k))

        return deck

#########################Clase player#########################



########################Repartir cartas######################
