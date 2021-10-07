#zona de import#########################################################################
from typing import Sequence
import pygame
from pygame import *
from enum import Enum,IntEnum
import random

from pygame import color




#######################crear la interfaz grafica#####################################
pygame.init()

VENTANA = pygame.display.set_mode([710,440])
tiempo = pygame.time.Clock()
pygame.display.set_caption("Mesa de Blackjack")

fondo = pygame.image.load("fondo.png").convert()

####################Boton###############################################################
imagen_mano = pygame.image.load("mano.png").convert_alpha()
imagen_x = pygame.image.load("pasar.png").convert_alpha()
imagen_reiniciar = pygame.image.load("reiniciar.png").convert_alpha()
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
boton_reiniciar = Boton(618,390,imagen_reiniciar)

#################clase carta###########################################################
class Carta():
    def __init__(self,suit,simbolo,valor,color):
        self.suit = suit
        self.simbolo = simbolo
        self.valor = valor
        self.color = color

#datos de las cartas
Valor_carta = [11,2,3,4,5,6,7,8,9,10,10,10]
Simbolo_carta = list(range(1,14))
Suit_carta = list(range(1,5))

#########################clase dealer####################################################
class Dealer():
    def dealer():
        deck = []
        for j in range(len(Valor_carta)):
            for k in Suit_carta:
                deck.append(Carta(Valor_carta[j],Simbolo_carta[j],k,color))
        return deck

original_deck = Dealer.dealer()
full_deck = list(original_deck)

########################Repartir cartas###################################################
#valores iniciales en las manos del jugador y del IA
player_hand = []
IA_hand = []
hidden_hand = []
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
    if obtener_valor_carta(IA_hand) < 18:
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
#########añadir texto###################################################################

Fuente = pygame.font.SysFont(None,30)
jugador_texto = Fuente.render("P:",0,(255,255,255))
IA_texto = Fuente.render("IA:",0,(255,255,255))
ganar = pygame.font.SysFont(None,42)
ganar_int = 0
ganar_str = ['','Jugador gana', 'IA gana', 'Jugador sobrepasa — IA gana', 'Jugador gana — IA sobrepasa', 'No ganadores']

def dibujar_carta():
    valor_mano = Fuente.render('P:'+ str(obtener_valor_carta(player_hand)),True,(255,255,255))
    VENTANA.blit(valor_mano,(200,344))
    #valor_IA = Fuente.render('IA:'+ str(obtener_valor_carta(IA_hand)),True,(255,255,255))
    #VENTANA.blit(valor_IA,(180,144))
    texto_ganador = ganar.render(ganar_str[ganar_int],True,(255,255,255))
    VENTANA.blit(texto_ganador,(710//2-ganar_x[ganar_int],440//2-ganar_y[ganar_int]))
    valor_PG = Fuente.render(str(Contador_Jugador),True,(255,255,255))
    VENTANA.blit(valor_PG,(100,190))
    valor_PP = Fuente.render(str(Contador_IA),True,(255,255,255))
    VENTANA.blit(valor_PP,(100,245))

ganar_x = [0, 100, 65, 180, 180, 40, 100]
ganar_y = [0, 30, 30, 30, 30, 30, 30]
###########el programa lee las teclas#################################################
keys = pygame.key.get_pressed()
# Boleans
main_loop = 0
run_game = True
reveal = False
session = True

Contador_IA = 0
Contador_Jugador = 0
#loop#########################################3########################################
run_game = True

while run_game:
#evento del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False #para cerrarlo solo es darle a la X

        #reiniciar juego
    if event.type == pygame.MOUSEBUTTONDOWN:
        if boton_reiniciar.rect.collidepoint(mouse_pos)and ganar_int != 0:    
            full_deck = list(original_deck)
            run_game = True
            main_loop = 0
            ganar_int = 0
            reveal = False
            session = True
            player_hand = []
            IA_hand = []
            hidden_hand = []
    
    #main loop
    if main_loop > 0:
        main_loop += 1
    if main_loop > 5:
        main_loop = 0

    mouse_pos = pygame.mouse.get_pos()


        #el jugador decide coger una carta
    if event.type == pygame.MOUSEBUTTONDOWN:
         if boton_mano.rect.collidepoint(mouse_pos) and main_loop == 0 and session:
            jugador_elije_carta()
            main_loop = 1

            IA_hit = IA_elije_carta()
            print("IA:", end='')
            print(obtener_valor_carta(IA_hand))

            #evaluar las posibilidade
            if obtener_valor_carta(IA_hand) > 21 and obtener_valor_carta(player_hand) > 21:
                session = False
                print("No ganadores")
                ganar_int = 5
                reveal = True
                #player gana y IA sobrepasa el numero 
            elif obtener_valor_carta(IA_hand) > 21:
                session = False
                print("AI sobrepaso, jugador gana")
                ganar_int = 4
                reveal = True
                Contador_Jugador += 1
                #IA gana y player sobrepasa el numero
            elif obtener_valor_carta(player_hand) > 21:   
                print('Jugador sobrepaso, IA gana')
                ganar_int = 3
                session = False
                reveal = True
                Contador_IA += 1
                #IA gana
            elif obtener_valor_carta(IA_hand) == 21 and obtener_valor_carta(player_hand) != 21:
                print('IA gana')
                ganar_int = 2
                session = False
                reveal = True
                Contador_IA += 1
            # PLAYER gana
            elif obtener_valor_carta(IA_hand) != 21 and obtener_valor_carta(player_hand) == 21:
                print('Jugador gana')
                ganar_int = 1
                session = False
                reveal = True
                Contador_Jugador += 1
    #el jugador decide pasar
    if event.type == pygame.MOUSEBUTTONDOWN:
        if boton_x.rect.collidepoint(mouse_pos) and main_loop == 0 and session:
            main_loop = 1

            AI_hit = IA_elije_carta()

            print("IA: ", end='')
            print(obtener_valor_carta(IA_hand))

            #evaluar las posibilidades
            if (AI_hit == False):
             if obtener_valor_carta(IA_hand) > obtener_valor_carta(player_hand):
                session = False
                print("AI gana")
                ganar_int = 2
                reveal = True
                Contador_IA += 1
            elif obtener_valor_carta(IA_hand) < obtener_valor_carta(player_hand):
                session = False
                print("Jugador gana")
                ganar_int = 1
                reveal = True
                Contador_Jugador += 1
        else:
            if obtener_valor_carta(IA_hand) > 21 and obtener_valor_carta(player_hand) > 21:
                session = False
                print("No hay ganadores")
                ganar_int = 5
                reveal = True
            elif obtener_valor_carta(IA_hand) > 21:
                session = False
                print("IA sobrepasa, jugador gana")
                ganar_int = 4
                reveal = True
                Contador_Jugador += 1
            elif obtener_valor_carta(IA_hand) == 21 and obtener_valor_carta(player_hand) != 21:
                # AI WINS
                print('IA GANA')
                ganar_int = 2
                session = False
                reveal = True
                Contador_IA += 1
            elif obtener_valor_carta(IA_hand) != 21 and obtener_valor_carta(player_hand) == 21:
                # PLAYER WINS
                print('Jugador gana')
                ganar_int = 1
                session = False
                reveal = True
                Contador_Jugador += 1


    VENTANA.blit(fondo,[0,0])
    boton_mano.dibujar()
    boton_x.dibujar()
    boton_reiniciar.dibujar()
    dibujar_carta()#carta jugador
    VENTANA.blit(IA_texto,(180,144))
    pygame.display.flip()
    tiempo.tick(60)

############delaer expand

pygame.quit()