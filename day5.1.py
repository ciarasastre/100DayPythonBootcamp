'''
20/10/2022 Ciara Sastre Python 100 Day challenge
Password Generator Project
'''
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easyPassword = ""

for char in range(0, nr_letters):
  easyPassword += random.choice(letters) # this is random from list
  #easyPassword += letters[char] This is sequential (abcd)
  #print(letters[char])

for sym in range(0, nr_symbols):
  easyPassword += random.choice(symbols)

for num in range(0, nr_numbers):
  easyPassword += random.choice(numbers)

print(easyPassword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Take easyPassword in and convert to list
list = list(easyPassword)

random.shuffle(list) # Shuffle the list
result = ''.join(list) # Re-join as string

print(result)

'''
A For loop way of re-joining list to string

hardPassword - ""

for char in list:
  hardPassword += char
'''
