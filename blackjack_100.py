# 100 days with Python 
# Blackjack game
# Day 11
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from hangman_arch import logo_black
from random import randint

import os
cls = lambda: os.system('cls')  # define of screan cleaning

def blackjack_game():  #function for playing the game 
    
    print(logo_black)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_1 = cards[randint(0,12)]
    c_card_1 = cards[randint(0,12)]
    player_1 = [card_1,]
    computer = [c_card_1,]


    def add_u_card(next_card):   #function that adds a new card for user and counts the hand than checks if it exceeds the number of 21 and if there is an ase change it's value from 11 to 1  
        player_1.append(next_card)
        score_1 = sum(player_1)
        print(f"   Your cards are {player_1} and your curent score is {score_1}")
        print(f"   Computer first card is {computer}")
        if (card_1 == 11 or next_card == 11) and score_1 > 21:
            return score_1 - 10
        else:
            return score_1 

    def add_c_card(n_card):   #function that adds a new card for computer and counts its hand than checks if it exceeds the number of 21 and if there is an ase change it's value from 11 to 1 
        computer.append(n_card)    
        score_2 = sum(computer)
        if (c_card_1 == 11 or n_card == 11) and score_2 > 21:
            return score_2 - 10
        else:
            return score_2 
        
    user_game = True     
    while user_game:
        next_card = cards[randint(0,12)]
        score_u = add_u_card(next_card) 
        if score_u < 21:
            decision_2 = input("Do you want to get another card? Type 'y' for yes or 'n' for no: ")
            if decision_2 == "y":
                user_game = True
            else:
                user_game = False
        else:
            user_game = False 
            break
        
    comp_game = True    
    while comp_game:
        n_card = cards[randint(0,12)]
        score_c = add_c_card(n_card)
        if score_u >21:
            comp_game = False
        elif score_c < 17:
            comp_game = True
        else:
            comp_game = False
            break     
    print(f"   Your final cards are {player_1} and your final score is {score_u}")
    print(f"   Computer final cards are {computer} and his final score is {score_c}")
    if score_u > 21:
        print("Computer wins! You lost.") 
    elif score_u == score_c:
        print("It is a tie") 
    elif score_c < score_u <= 21:
        print("You win!")
    else: 
        print ("Computer wins! You lost.")     

decision = input("Do yo want to play Blackjack game? Type 'y' if you want to start or 'n' if not: ")
while decision == 'y':   # loop that starts blackjack function as long as user types 'n' means no as an answer to the question to continue the game
    cls()
    blackjack_game()
    decision = input("Do yo want to play Blackjack game? Type 'y' if you want to start or 'n' if not: ")
if decision == 'n':
    print("Bye Bye")
       