#zona de import
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
##########################crear los botones###########################



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
##Buscar las cartas dentro del array
def buscar_carta(valor,suit):
    if suit == 'pica':
        T = 1
    elif suit == 'trebol':
        T = 2
    elif suit == 'diamante':
        T = 3
    elif suit == 'corazon':
        T = 4
    else:
        print("error")
    
    return (valor-1)*4 + (T-1)