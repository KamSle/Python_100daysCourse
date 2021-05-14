# 100 days with Python 
# Guessing Game
# DAY 12

############### Our Guessing Game Rules #####################
# 1. You will try to guess number from 1 to 100
# 2. You can choose difficulty easy for 10 guesses(attempts) and hard for 5 guesses(attempts)
# 3. If all five or ten attempts run out without proper guess you lose

from random import randint

def guessing():
    user_guess = int(input("Make a guess: "))
    if user_guess < number:
        print("Too low!")
        return 0
    elif user_guess > number:
        print("Too high!")
        return 0
    else:
        print(f"You got it! You win! You guess the wright number {number}")       
        return 1 

def attempts(k):
    print(f"You have {k} attempts remaining to guess the number")
    for i in range(1,k+1):
        user_try = guessing()
        if user_try == 0:
            k -= 1 
            print(f"You have {k} attempts remaining to guess the number")
        else:
            print(f"You made it in {i} attempt")
            break
    if k == 0:
        print(f"You've run out of guesses, you lose!\nThe wright number is {number}")     

def game_level():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy': 
        attempts(10)                      
    elif level == 'hard':
        attempts(5)
    else:
        print("There is no such level!")

is_guessing = True
while is_guessing: 
    print("Welcome to my Guessing Game")
    print("I am thinking of a number between 1 and 100. Your task is to guess what namber I've choosen.")
    number = randint(1,100)    
    game_level()
    once_more = input("Would you like to play again? Type 'y' for yes or 'n' for no: ")
    if once_more == "n":
        is_guessing = False
        print("Thanks for game! Bye bye!")    

