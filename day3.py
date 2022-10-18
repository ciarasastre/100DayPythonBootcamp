'''
18/10/2022 Ciara Sastre
Day 3 in the 100 day Python Challenge
'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  
  if age < 12:
    bill = 5
    print(f"Child tickets are: €{bill}")
  elif age <= 18:
    bill = 7
    print(f"Youth tickets are: €{bill}")
  else:
    bill = 12
    print(f"Adult tickets are: €{bill}")
    
  wantsPhoto = input("Do you want a photo taken? Y or N.")
  if wantsPhoto == "Y":
    #Add 3 dollars to bill
    bill += 3
  
  print(f"Your final bill is €{bill}")
    
else:
  print("Sorry you have to grow taller before you can ride.")


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Get a number with or without remainder
answer = number % 2

# Check if the number is cleanly divisable by two (Even)
#(answer == 0):
if(answer == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")

'''
A shorter way to write this is
if number % 2 == 0:

No brackets needed & no extra variables created
'''
###################################################
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI Calculator
bmi = round(weight/(height**2))

#Get interpretation
if bmi < 18.5:
    result = "are underweight"
elif bmi < 25:
    result = "are a normal weight"
elif bmi < 30:
    result = "are slightly overweight"
elif bmi < 35:
    result = "are obese"
else:
    result = "are clinically obese"

print(f"Your BMI is {bmi}, you {result}.")

###################################################

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#True if evenly divisable by 4 - Pass round 1
if year % 4 == 0:
    #Pass round 1
    #True if not evenly divisable by 100 but evenly divisable by 400 - Pass round 2 
    if year % 100 == 0 and year % 400 == 0:
        #pass round 2
        print("Leap year.")
    #True is not divisable by 100 and not 400 Pass round 3
    elif year % 100 != 0 and year % 400 != 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


#####################################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
    bill += 15

    #Pepperoni for small is unique
    if add_pepperoni == "Y":
        bill += 2

if size == "M":
    bill += 20

if size == "L":
    bill += 25

if size == "M" or size == "L" and add_pepperoni == "Y":
    bill += 3

#Cheese is same for everyone
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is: ${bill}.")

#####################################################

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Reduce them to lower letters
lower_name1 = name1.lower()
lower_name2 = name2.lower()

#Check for number of times letters in TRUE occurs
name_T = lower_name1.count("t") + lower_name2.count("t")
name_R = lower_name1.count("r") + lower_name2.count("r")
name_U = lower_name1.count("u") + lower_name2.count("u")
name_E = lower_name1.count("e") + lower_name2.count("e")

#Check for number of times letters in LOVE occurs
name_L = lower_name1.count("l") + lower_name2.count("l")
name_O = lower_name1.count("o") + lower_name2.count("o")
name_V = lower_name1.count("v") + lower_name2.count("v")
name_E2 = lower_name1.count("e") + lower_name2.count("e")

nameTrue = name_T + name_R + name_U + name_E
nameLove = name_L + name_O + name_V + name_E2

trueLoveNum = str(nameTrue) + str(nameLove) # Concatonate them via string
trueLoveNum = int(trueLoveNum) #Turn back to int

#Now print out interpretations
# Score less than 10 or greater than 90
if trueLoveNum < 10 or trueLoveNum > 90:
    print(f"Your score is {trueLoveNum}, you go together like coke and mentos.")
# Score between 40 and 50
elif trueLoveNum <= 50 and trueLoveNum >= 40:
    print(f"Your score is {trueLoveNum}, you are alright together.")
# Other Score outside of these
else:
    print(f"Your score is {trueLoveNum}.")

############One of my favourites ######################