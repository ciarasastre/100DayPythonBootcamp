'''
20/10/2022 Ciara Sastre 100 Days of Python
'''

fruits = ["Apple","Peach", "Pear"]

#Create variable fruit
for fruit in fruits:
  print(fruit)
  print(fruit + "Pie")
  
print(fruits)

#For loop with range Goes 1 to 10 skips(steps) by 3
for number in range(1, 11, 3):
  print(number)

total = 0
for numbers in range(1, 101):
  total += numbers
print(total)
####################################################

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Cant use len() or sum() for this challenge

#Need to find number of heights and divide that by total sum of height
numHeight = 0
sumHeight = 0

for height in student_heights:
    numHeight += 1 #Counter
    sumHeight = sumHeight + height

avgHeight = round(sumHeight/numHeight)

print(avgHeight)

# Getting len() and sum() easier
print(len(student_heights))
print(sum(student_heights))

easyAvgHeight = sum(student_heights)/len(student_heights)
print(round(easyAvgHeight))
print(max(student_heights)) # Gets higher number

#########################################################
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#You are not allowed to use the max or min functions.
highScore = 0

for score in student_scores:
    if score > highScore:
        highScore = score

print(f"The highest score in the class is: {highScore}")

##########################################################

#Write your code below this row 👇

'''
Write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
'''

total = 0

for numbers in range(2,101,2):
    total += numbers
print(total)

########################################################

#Write your code below this row 👇

#Print each number from 1 to 100
for num in range(1,101):
    # Check if it is divisable by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if it is divisable by 5
    elif num % 5 == 0:
        print("Buzz")
    # Check if it is divisable by 3
    elif num % 3 == 0:
        print("Fizz")
    #Other wise print number
    else:
        print(num)
###############################################

