# 100 days with Python 
# rock paper scissors game 
# DAY 4

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint

player1 = int(input("Choose 0 for rock 1 for paper or 2 for scissors: "))
image = [rock, paper, scissors]

if player1 >= 3 or player1 < 0:
  print("Wrong choice You loose!") 
else:
  print(image[player1])      

player2 = randint(0,2)
print(f"Computer choice: {player2}")
print(image[player2]) 


if player1 == player2:
  print("It's a tie") 
elif (player1 == 2 and player2 == 1) or (player1 == 1 and player2 == 0) or (player1 == 0 and player2 == 2):
  print("Player1 wins!")
else:
  print("Player2 wins!")  

 ## Day 5 ex 1
 ### the len and sum using for loop in lists

 # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total = 0
i = 0
for person in student_heights:
  total += person
  i+=1
total_high = total
times = i
print(round(total/i)) 

## Day 5 exe 2
####the maximum value in the list with for loop
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
score = 0
for number in student_heights:
  if number > score:
    score = number
print(f"the max is {score}")   

## Day 5 project Password Generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for i in range(nr_letters):
  password += (random.choice(letters))
for i in range(nr_symbols):
  password += (random.choice(symbols))
for i in range(nr_numbers):
  password += (random.choice(numbers))
l_l = list(password)
random.shuffle(l_l)
print(''.join(l_l))