'''
19/10/2022 Ciara Sastre 100 Days python challenge
Rock, Paper, Sissors Game.
'''
import random

print("What do you choose?")
print("Type 0 for Rock") # Beats Sissors/2
print("Type 1 for Paper") # Beats Rock/0
print("Type 2 for Sissors") # Beats Paper/1

userPicks = int(input())
compPicks = random.randint(0,2)
names = ["Rock", "Paper", "Sissors"]

print(f"You picked {names[userPicks]} and the Computer picked {names[compPicks]}")

#If i am 0 or 1 i will lose +1 above me except when i am 2
if userPicks == 0 or userPicks == 1:
  if compPicks == userPicks + 1:
    print("You Lose...")
  elif userPicks == compPicks:
    print("You Draw.")
  else:
    print("You Win!")

#Now if i am 2 "sissors"
if userPicks == 2:
  if userPicks == 2 and compPicks == 1:
    print("You Win!")
  elif userPicks == compPicks:
    print("You Draw.")
  else:
    print("You Lose...")
  
  '''
The above shows reduced code from what i had before which was:
(Some code may be missing due to copy and paste but it is rough work)

#if userPicks == compPicks:
  #print("You Draw.")
  
if userPicks == 0:
  #Show rock
  print(f"You picked Rock{userPicks}")
  
  if compPicks == 1:
    #Show Paper
    print(f"The computer picked Paper{compPicks}")
    print("You Lose...")
    
  elif compPicks == 2:
    #Show Sissors
    print(f"The computer picked Sissors{compPicks}") 
    print("You Win!")
  
elif userPicks == 1:
  #Show Paper
  print(f"You picked Paper{userPicks}")
    
  if compPicks == 0:
    #Show rock
    print(f"The computer picked Rock{compPicks}")
    print("You Win!")
    
  elif compPicks == 2:
    #Show Sissors
    print(f"The computer picked Sissors{compPicks}") 
    print("You Lose...")

elif userPicks == 2:
  #Show Sissors
  print(f"You picked Sissors{userPicks}")
    
  if compPicks == 0:
    #Show rock
    print(f"The computer picked Rock{compPicks}")
    print("You Lose...")
    
  elif compPicks == 1:
    #Show Paper
    print(f"The computer picked Paper{compPicks}")
    print("You Win!")
else:
  print("Input not found")
'''
