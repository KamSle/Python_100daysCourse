# 100 days with Python 
# Hangman game 
# DAY 7

import random
from hangman_arch import stages
from hangman_arch import logo
from hangman_arch import word_list

print(logo)  # logo importing from hangman_arch file
lives = 6 
chosen_word = random.choice(word_list)  # word is from the list of words we have in hangman_arch file

display = []                      # create here a list of number of signs '_' in choosen word but printing as a string
for letter in chosen_word:
  display += "_"
print("Let's play! Try to find the word.")  
print(f"{' '.join(display)}\n") 

end_of_the_game = False           # we have while loop here until end of the game change it's value to True(it happens only when lives = 0 or there is no _ in choosen word )
while not end_of_the_game:
  guess = input("Please, choose the letter or type 'quit' if you want to exit this game: ").lower()

  if guess == "quit":   # if user type quit the game is over
    break

  if guess in display:                  # if user type the letter that is already there we have the massage 
    print(f"This letter {guess} is already guessed.")

  for l in range(len(chosen_word)):           # all right guessed letters appears instead of '_' in the string
    if chosen_word[l] == guess:
      display[l] = guess 
      print(f"You guess right letter {guess}")
  print(f"{' '.join(display)}\n")

  if guess not in chosen_word:                 # when user type wrong letter looses one live and we have message and if there is no live left the game is over
    lives -= 1
    print(f"Wrong guess! Letter {guess} doesn't fit here!")
    if lives == 0:
      end_of_the_game = True
      print("You lose a life!")
      print(f"The word you didn't guess is {chosen_word}.")
  
  if not "_" in display:   # when there is no sign '_' left in the string the game ends with the user win 
    end_of_the_game = True
    print("You win!")
    
  print(stages[lives])  # here we get the picture of hangman live stage after every user guess
