# 100 days with Python 
# Auction game 
# DAY 9

import os
cls = lambda: os.system('cls')  # define of screan cleaning
cls()
from hangman_arch import logo_auction   # importing ascii art from other file
print(logo_auction)
print("Welcome to the simple auction program.")

auction_scores = {}
new_bider = "yes"

def counting(high_scores):      # define function that search for person who had the biggest bid in the auction
    first_amount = 0
    for key in auction_scores:
      amount = auction_scores[key] 
      if amount > first_amount:
        first_amount = amount
        winner = key   
    print(f"The winner is {winner} with the highest bid {first_amount}")

while new_bider == "yes":    # loop that add new bidders or gives the winner ..depend on the user answer
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    auction_scores[name] = bid
    new_bider = input("Are there any other bidders? Type 'yes' or 'no': ")
    cls()
if new_bider == "no":
    counting(auction_scores)



