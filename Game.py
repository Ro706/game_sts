# This is my first game coding !

import random

def gameWin(comp, you):
  if comp == you:
    return None 
  elif you == "stone":
    if comp == "paper":
      return False
    elif comp == "scissor":
      return True
      
  elif you == "paper":
    if comp == "stone":
      return True
    elif comp == "scissor":
      return False   
  
  elif you == "scissor":
    if comp == "paper":
      return True
    elif comp == "stone":
      return False
      
      
print("              it's your turn!⤵️")

you = (input("    enter: stone⛰️ , paper📃 or scissor✂️:\n👉 \t"))


print("\n            -:computer's turn:-    ")


comp = random.choice(("stone", "paper", "scissor"))
  
print(f"       computer has chosen 👉{comp}👈\n ")  
  
a = gameWin(comp, you)



if comp == you:
  print("\n             Game tied 🤐!")
elif a:
  print("\n      Superb, you won the Game ✌️! ")
else :
  print("\n      You lose, better luck next time 😥!")
