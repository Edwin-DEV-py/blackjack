# Program by Myron Ho
# ME 4990
# Final Project
# Black Jack

# Card Image Source: http://acbl.mybigcommerce.com/52-playing-cards/

import pygame
from enum import Enum, IntEnum
import random



## CUSTOM FUNCTIONS

# Create Card Object
class Card():
    def __init__(self,V,N,S,P):
        self.value = V      # Card Value
        self.name = N       # Card Name
        self.suit = S       # Card Suit
        self.image = P      # Card Picture





# Display texts on screen / GUI
def draw_texts():
    # Display GUI texts
    ai_hand_text = GUI_font.render("AI HAND:",True,white)
    player_hand_text = GUI_font.render("PLAYER HAND:",True,white)
    hand_value_text = GUI_font.render('HAND VALUE: '+ str(get_card_value(player_hand)),True,white)
    winner_text = WIN_font.render(win_str[win_int],True,white)

    win.blit(winner_text, (WIN_WIDTH//2-win_x[win_int], WIN_HEIGHT//2-win_y[win_int]))
    win.blit(hand_value_text, (15,WIN_HEIGHT-CARD_HEIGHT-85))
    win.blit(ai_hand_text, (15,15))
    win.blit(player_hand_text, (15,WIN_HEIGHT-CARD_HEIGHT-60))





# Initialize Font and Score Texts
GUI_font = pygame.font.SysFont(None, 32)
WIN_font = pygame.font.SysFont(None, 42)
INST_font = pygame.font.SysFont(None, 16)
TITLE_font = pygame.font.SysFont(None, 24)

win_int = 0
win_str = ['', 'PLAYER WINS', 'AI WINS', 'PLAYER BUST — AI WINS', 'PLAYER WINS — AI BUST', 'TIED', 'NO WINNERS']
win_x = [0, 100, 65, 180, 180, 40, 100]
win_y = [0, 30, 30, 30, 30, 30, 30]


# Initialize booleans for GUI mantainence
main_loop = 0
run_game = True
reveal = False
session = True
spectate = False



# Main Game Loop
while run_game:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # GUI window will remain open until [X] button is clicked or GUI is closed.
            run_game = False

    # Create background
    win.fill(black)
    draw_texts()

    # Used to prevent button spam
    if main_loop > 0:
        main_loop += 1
    if main_loop > 5:
        main_loop = 0


    # Obtain all keys pressed
    keys = pygame.key.get_pressed()

    # Restart Game
    if keys[pygame.K_ESCAPE]:
        # Reinitialize everything
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

    # Player hit / obtain another card
    if keys[pygame.K_SPACE] and main_loop == 0 and session:
        player_draw_cards()
        main_loop = 1
        
        AI_hit = AI_draw_card()

        print("AI: ", end='')
        print(get_card_value(AI_hand))

        # Test all possible outcomes
        if get_card_value(AI_hand) > 21 and get_card_value(player_hand) > 21:
            session = False
            print("NO WINNERS")
            win_int = 6
            reveal = True
        elif get_card_value(AI_hand) > 21:
            session = False
            print("AI BUST, PLAYER WINS")
            win_int = 4
            reveal = True
        elif get_card_value(player_hand) > 21:
            # PLAYER BUST
            # AI WINS     
            print('PLAYER BUST, AI WINS')
            win_int = 3
            session = False
            reveal = True
        elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) == 21:
            # TIED
            print('TIED')
            win_int = 5
            session = False
            reveal = True
        elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) != 21:
            # AI WINS
            print('AI WINS')
            win_int = 2
            session = False
            reveal = True
        elif get_card_value(AI_hand) != 21 and get_card_value(player_hand) == 21:
            # PLAYER WINS
            print('PLAYER WINS')
            win_int = 1
            session = False
            reveal = True
    
    # Player passes
    if (keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]) and main_loop == 0 and session:
        main_loop = 1

        AI_hit = AI_draw_card()

        print("AI: ", end='')
        print(get_card_value(AI_hand))

        # Test all possible outcomes
        if (AI_hit == False):
            if get_card_value(AI_hand) > get_card_value(player_hand):
                session = False
                print("AI WINS")
                win_int = 2
                reveal = True
            elif get_card_value(AI_hand) < get_card_value(player_hand):
                session = False
                print("PLAYER WINS")
                win_int = 1
                reveal = True
            else:
                session = False
                print("TIED")
                win_int = 5
                reveal = True
        else:
            if get_card_value(AI_hand) > 21 and get_card_value(player_hand) > 21:
                session = False
                print("NO WINNERS")
                win_int = 6
                reveal = True
            elif get_card_value(AI_hand) > 21:
                session = False
                print("AI BUST, PLAYER WINS")
                win_int = 4
                reveal = True
            elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) == 21:
                # TIED
                print('TIED')
                win_int = 5
                session = False
                reveal = True
            elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) != 21:
                # AI WINS
                print('AI WINS')
                win_int = 2
                session = False
                reveal = True
            elif get_card_value(AI_hand) != 21 and get_card_value(player_hand) == 21:
                # PLAYER WINS
                print('PLAYER WINS')
                win_int = 1
                session = False
                reveal = True


pygame.quit()