#zona de import
from typing import Sequence
import pygame
from pygame import *
from enum import Enum,IntEnum
import random




#######################crear la interfaz grafica#######################
pygame.init()

VENTANA = pygame.display.set_mode([710,440])
tiempo = pygame.time.Clock()
ganar_WIDTH = 710
ganar_HEIGHT = 440
white = (255, 255, 255)
black = (0, 0, 0)
CARD_WIDTH = 100
CARD_HEIGHT = 150
ganar = pygame.display.set_mode((ganar_WIDTH, ganar_HEIGHT))
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

# Initialize Font and Score Texts
GUI_font = pygame.font.SysFont(None, 32)
ganar_font = pygame.font.SysFont(None, 42)
INST_font = pygame.font.SysFont(None, 16)
TITLE_font = pygame.font.SysFont(None, 24)

ganar_int = 0
ganar_str = ['', 'PLAYER ganarS', 'AI ganarS', 'PLAYER BUST — AI ganarS', 'PLAYER ganarS — AI BUST', 'TIED', 'NO ganarNERS']
ganar_x = [0, 100, 65, 180, 180, 40, 100]
ganar_y = [0, 30, 30, 30, 30, 30, 30]

# Display texts on screen / GUI
def draw_texts():
    # Display GUI texts
    ai_hand_text = GUI_font.render("AI HAND:",True,white)
    player_hand_text = GUI_font.render("PLAYER HAND:",True,white)
    hand_value_text = GUI_font.render('HAND VALUE: '+ str(obtener_valor_carta(player_hand)),True,white)
    ganarner_text = ganar_font.render(ganar_str[ganar_int],True,white)

    ganar.blit(ganarner_text, (ganar_WIDTH//2-ganar_x[ganar_int], ganar_HEIGHT//2-ganar_y[ganar_int]))
    ganar.blit(hand_value_text, (15,ganar_HEIGHT-CARD_HEIGHT-85))
    ganar.blit(ai_hand_text, (15,15))
    ganar.blit(player_hand_text, (15,ganar_HEIGHT-CARD_HEIGHT-60))


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
        ganar_int = 0
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


    VENTANA.blit(fondo,[0,0])
    boton_mano.dibujar()
    boton_x.dibujar()
    pygame.display.flip()
    tiempo.tick(60)

############delaer expand#######
full_deck = list(original_deck)

pygame.quit()