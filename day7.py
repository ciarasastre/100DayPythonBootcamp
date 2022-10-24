#Step1
from replit import clear
import random
from hangman_art import logo, stages
from hangman_words import word_list


display = []
guessList = []
game = 0
correct = 0
lives = 5

chosen_word = random.choice(word_list)
#print(f"Chosen word is {chosen_word}") Testing purposes

wordLength = len(chosen_word)

#for spaces in chosen_word:
#  display.append("_")
#print(display)

for spaces in range(wordLength):
  display += "_"

print(logo)
while game == 0:

  guess = input("Can you guess a letter?")
  clear()
  
  if guess in display:
    print("You have already guessed this try again")
  
  # Show all guesses
  guessList += guess
  #print(f"{' '.join(guessList)}")
  print(f"Your guess are {' '.join(guessList)}")
  #guessList += guess
    
  for position in range(wordLength): # Go from 0 to N
    letters = chosen_word[position] # Pick the strings exact position
    if letters == guess:
      display[position] = guess
      correct += 1
  
  if guess not in chosen_word:
    print("Incorrect you lose a life")
    lives -= 1
    print(f"You have {lives} lives left")
  
  if lives == 0:
    print("YOU LOSE!")
    print(f"The correct word was: {chosen_word}")
    game = 1
  
  if correct == wordLength:
    print("YOU WIN!")
    game = 1

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Print out lives
  print(stages[lives])
  
  '''
  First attempt
  i = 0
    for letters in chosen_word:
    index = letters.find(guess)
    print(index)
    
    if index == 0:
      display[i] = guess
      correct += 1

    if correct == len(chosen_word):
      print(len(chosen_word))
      print(correct)
      print("You got the correct word!")
      game = 1

    i+= 1
  
  print(display)

'''