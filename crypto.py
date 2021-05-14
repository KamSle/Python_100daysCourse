# 100 days with Python 
# Crypto game 
# DAY 8

# #Import and print the logo from hangman_arch.py when the program starts.
# from hangman_arch import logo_caesar
# print(logo_caesar)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
# answer = "yes"
# while answer == "yes":
#   direction = input("Choose direction: Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   if direction in ("encode","decode"):
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     if shift >= 27:
#       shift = shift%26
#     def codeme(first, second, third):
#       new_text=""
#       alphabet.extend(alphabet)
#       for char in first:
#         if char in alphabet: 
#           place = alphabet.index(char)
#           if third == "decode":
#             new_place = place - second
#           else:
#             new_place = place + second  
#           new_letter = alphabet[new_place]
#           new_text += new_letter
#         else:
#           new_text += char  
#       print(f"The {third} text is: {new_text}")  
#     codeme(first=text,second=shift,third=direction)
#   else:
#       print("Wrong direction!")
#   answer = input("Do you want to restart the program? Type 'yes' if you want to go again. Otherwise type 'no'.: ").lower()
#   if answer not in ("yes","no"):
#     print("Wrong choice. You quit the game!")
#     break
#   if answer == "no":
#     print("This was fun. Thanks!")
#     break



#other better look of the crypto game
from hangman_arch import logo_caesar
print(logo_caesar)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Choose direction: Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def codeme(first, second, third):
  new_text=""
  alphabet.extend(alphabet)
  for char in first:
    if char in alphabet: 
      place = alphabet.index(char)
      if third == "decode":
        new_place = place - second
      else:
        new_place = place + second  
      new_letter = alphabet[new_place]
      new_text += new_letter
    else:
      new_text += char  
  print(f"The anwser for the {third} text {first} will be: {new_text}")  
  
answer = "yes"
while answer == "yes": 
  if direction in ("encode","decode"):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= 27:
      shift = shift%26 
    codeme(first=text,second=shift,third=direction)
  answer = input("Do you want to restart the program? Type 'yes' if you want to go again. Otherwise type 'no'.: ").lower()
  if answer not in ("yes","no"):
    print("Wrong choice. You quit the game!")
    break
  if answer == "no":
    print("This was fun. Thanks!")
    break