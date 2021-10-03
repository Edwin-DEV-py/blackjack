#zona de import
from typing import Sequence
import pygame
from pygame import *
from enum import Enum,IntEnum
import random

from pruebas import AI_hit



#######################crear la interfaz grafica#######################
pygame.init()

VENTANA = pygame.display.set_mode([710,440])
tiempo = pygame.time.Clock()
pygame.display.set_caption("Mesa de Blackjack")

fondo = pygame.image.load("fondo.png").convert()

####################Boton#######################
imagen_mano = pygame.image.load("mano.png").convert_alpha()
imagen_x = pygame.image.load("pasar.png").convert_alpha()
#class boton
class Boton():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def dibujar(self):
        VENTANA.blit(self.image,(self.rect.x, self.rect.y)) #dibujar el boton en la panytalla
#crear la instancia del boton
boton_mano = Boton(622,269, imagen_mano)
boton_x = Boton(622,337, imagen_x)
##click##################



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
#valores iniciales en las manos del jugador y del IA
player_hand = []
IA_hand = []
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

 #seleccion de carta al azar
def obtener_carta_random():
    global full_deck
    Random = random.randint(0,len(full_deck)-1)

    return full_deck.pop(Random)

#asiganar una carta en la mano del jugador
def jugador_elije_carta():
    player_hand.append(obtener_carta_random())

#asignar carta a la mano del IA
def IA_elije_carta():
    if obtener_valor_carta(IA_hand) < 17:
        IA_hand.append(obtener_carta_random())

        return True

    else:
        return False

#obtener el valor de las cartas del jugador / IA
def obtener_valor_carta(mano):
    if len(mano) == 0: #si la mano esta vacia obtener 8
        return 0
    else:
        Aces = []
        suma = 0

        for i in mano:
            if i.simbolo == 1:
                Aces.append(i)
            
            suma += i.valor
        
        if suma > 21 and (len(Aces) != 0): #cuando la suma es mas de 21 y hay un As
            suma -= 10
        return suma
##########delaer expand
original_deck = Dealer()

###########el programa lee las teclas#########
keys = pygame.key.get_pressed()

#loop#########################################3
run_game = True

while run_game:
#evento del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False #para cerrarlo solo es darle a la X
        #reiniciar juego
    if keys[pygame.K_ESCAPE]:
        full_deck = list(original_deck)
        run_game = True
        session = True
        main_loop = 0
        win_int = 0
        reveal = False
        session = True
        player_hand = []
        AI_hand = []
        hidden_hand = []
    mouse_pos = pygame.mouse.get_pos()


        #el jugador decide coger una carta
    if event.type == pygame.MOUSEBUTTONDOWN:
         if boton_mano.rect.collidepoint(mouse_pos) and main_loop == 0 and session:
            jugador_elije_carta()
            main_loop = 1

            AI_hit = IA_elije_carta()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if boton_x.rect.collidepoint(mouse_pos):
            run_game = False

    VENTANA.blit(imagen_mano,[500,200])
    VENTANA.blit(imagen_x,[622,280])
    VENTANA.blit(fondo,[0,0])
    boton_mano.dibujar()
    boton_x.dibujar()
    pygame.display.flip()
    tiempo.tick(60)

############delaer expand
full_deck = list(original_deck)

pygame.quit()