# 100 days with Python 
# Calculator
# DAY 10

import os
cls = lambda: os.system('cls')  # define of screan cleaning
cls()

from hangman_arch import logo_calculator   # importing ascii art from other file

def calculations(a,b):
        if operator == "+":
            return a+b
        elif operator == "-":
            return a-b
        elif operator == "*":
            return a*b
        else:
            return a/b
        
decision = "n"
while decision == "n":
    cls()
    print(logo_calculator)
    print("Welcome to the simple calculator program.")

    zero_number = float(input("Enter the first number: "))
    decision = "y"
    result = zero_number
    while  decision == "y":
        first_number = result 
        operator = input("+\n-\n*\n/\nPick an operation symbol: ")
        if operator not in ("+","-","*","/"):
            print("Upss.. you type a strange operator ..it can't be calculated")
            break
        next_number = float(input("What is the next number?: "))
        result = calculations(first_number,next_number)  
        print(f"{first_number} {operator} {next_number} = {result}")   
        decision = input(f"Type 'y' to continue this calculating operation with {result} number or type 'n' to exit: ").lower()   

if decision not in ("y","n"):
  print("Wrong choice!")                  