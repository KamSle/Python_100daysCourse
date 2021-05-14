# 100 days with Python 
# HigherLower Game
# DAY 14

from hangman_arch import logo_hl
from hangman_arch import data_hl
from hangman_arch import vs
from random import choice

import os
cls = lambda: os.system('cls')  # define of screan cleaning
        
def person_detail(person):
    name = person['name']
    description = person['description']
    country = person['country']
    return f"{name}, a {description}, from {country}"
    
def chcek_followers():
    a_count = a_person['follower_count']
    b_count = b_person['follower_count']
    answer = ""
    if a_count > b_count:
        answer = "A"
        print(f"a = {a_count}")
    else: 
        answer = "B"
        print(f"b = {b_count}")
    return answer

print ("Welcom to my version of HigherLower game!\nYour task is to guess who is the one with higher or lower number of instagram followers")
print(logo_hl)
i = 0
game_on = True
a_person = choice(data_hl)
b_person = choice(data_hl)
while game_on:
    if a_person == b_person:
        b_person = choice(data_hl)
        
    print(f"Compare A: {person_detail(a_person)}") 
    print(vs)
    print(f"Against B: {person_detail(b_person)}") 

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()   

    result = chcek_followers()
    print(result)
    if user_choice == result:
        a_person = b_person
        i +=1
        cls()
        print(logo_hl)
        print(f"     Good choice. Your score is {i}")
        game_on = True
    else:
        cls()
        print(logo_hl)
        print(f"     Sorry that's wrong. Final score {i}") 
        game_on = False
        if input("Do you want to paly again? Type 'y' for yes or 'n' for no: ").lower() == "y":
            i = 0
            a_person = choice(data_hl)
            b_person = choice(data_hl)
            cls()
            print ("Welcom to my version of HigherLower game!\nYour task is to guess who is the one with higher or lower number of instagram followers")
            print(logo_hl)
            game_on = True
        else: 
            print("Bye Bye") 
            game_on = False
               
