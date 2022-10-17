'''
17/10/2022 - Ciara Sastre
This is my code for Day 1 of the 100 Days of Python Challenge
'''

#My Variables
myName = ""
nameLength = 0
num1 = 0
num2 = 0
numTemp = 0

print("Welcome to programming python day 1!")
print("What is your name?")
myName = input()

#Say hello back
print("Hello",myName,"it is nice to meet you!")
#Say how many letters are in their name
print("You have",len(myName), "letters in your name.")

#Now enter in two numbers and flip their positions
print("Can you give me a number?")
num1 = input()
print("Can you give me another number?")
num2 = input()

print("Before:")
print(num1)
print(num2)

numTemp = num1
num1 = num2
num2 = numTemp

print("After:")
print(num1)
print(num2)