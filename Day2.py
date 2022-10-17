'''
17/10/2022 Ciara Sastre
Day 2 of the 100 Days of Programming Bootcamp
'''

print("Hello" [4]) # Subscripting
print(123_456_789) # Ignores underscores 123,456,789

num_char = len(input("What is your name?"))
print(type(num_char)) # type Int

new_num_char = str(num_char) # change to string
print("Your name has",new_num_char,"letters") # Now you can display


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#My Variables
num1 = 0
num2 = 0
numResult = 0

#Assign numbers and change to int
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

#Add together and print result
numResult = num1 + num2
print(numResult)

####################################### Done

'''
Operators:
3+5
7-4
3*2    #3 multiplied by 2
6/3    #6 divided by 3 gives float
2**2   #Two to the power of two

Order of Operations:
PEMDAS Left to Right
()
**
*
/
+
-
print(3 * 3 + 3 / 3 - 3) = 7.0
print(3 * (3 + 3) / 3 - 3) = 3.0
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#My Variables 
myResult = 0

#Convert to floats
height = float(height)
weight = float(weight)

#print(type(height))
#print(type(weight))

myResult = (weight/(height*height))

print(int(myResult))

############################################ Done

print(round(2.6666666, 2))
print(4/2) # Will be a float

score = 0
height = 1.8
isWinning = True

#f-String - An easier way to turn all variables to string
print(f"Your Score is {score}, your height is {height}, you are winning is {isWinning}")


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#My Variables
age = int(age) # Change value
years = 90

#Do years as is easiest
#yearsLeft = years - age
#print(f"You have {yearsLeft} years left to live.")

#Do Months
ageInMonths = age * 12
yearsInMonths = years * 12
monthsLeft = yearsInMonths - ageInMonths

#print(monthsLeft)

#Do Weeks
ageInWeeks = age * 52
yearsInWeeks = years * 52
weeksLeft = yearsInWeeks - ageInWeeks

#print(weeksLeft)

#Do Days
ageInDays = age * 365
yearsInDays = years * 365
daysLeft = yearsInDays - ageInDays

#print(daysLeft)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")

'''
A better way to write this is as years/days/weeks remaining

yearsRemaining = 90 - age
days_Remaining = yearsRemainging * 365
weeks_Remaining = yearsRemainging * 52
months_Remaining = yearsRemainging * 12

'''

######################################## Done
#If the bill was €150.00, split up between 5 people with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.60
#Round the result to two decimal places

print("Welcome to the tip calculator")

#One Way 
print("What was the total bill? €")
totalBill = input()
totalBill = float(totalBill)

#Another Way which is shorter
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))

numPeople = float(input("How many people to split the bill?"))

#Get percentageTip
percentageTip = (tip/100) # 0.12
totalTip = totalBill * percentageTip #18.0
resultPay = totalBill + totalTip # 168

#Split result pay by amount of people
individualPay = resultPay / numPeople

#Round Result pay
individualPay = round(individualPay, 2)
print("Each person should pay: €" + str(individualPay))