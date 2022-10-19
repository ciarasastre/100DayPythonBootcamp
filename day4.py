'''
19/10/2022 Ciara Sastre 100 days of programming
'''
import random
import my_module # importing a new py file

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

print(fruits[-5])

print(my_module.pi) # using Pi variable from other .py file

randomInt = random.randint(1, 10) # Start range from 1 to 10
print(randomInt)

#random() on its own will only go from 0.00 to 1.0000
randomFloat = random.random() * 6 # 0.0000 to 6.00000
print(randomFloat)
print(round(randomFloat, 2)) #Round to 2 decimal places

#The love score calculator from before can now be:
loveScore = random.randint(0,100)
print(f"Your love score is {loveScore}")

########### Heads or Tails #############
#Generate either a 0 or 1
headsOrTails = random.randint(0,1)

if headsOrTails == 0:
    print("Tails")
else:
    print("Heads")

#########################################

leinsterCounties = ["Dublin", "Wexford", "Wicklow", "Carlow", "Kildare", "Kilkenny", "Laois", "Longford", "Meath", "Offaly", "Westmeath"] ##11 -> max 10 entries including 0

print("I live in",leinsterCounties[0])
print(leinsterCounties[10])

print(leinsterCounties[-1]) # Going from the end of the list
print(leinsterCounties[-11]) # -11 being the start of the list

leinsterCounties[1] = "Wecksfurd" # Changing Data in a list

print(leinsterCounties)

leinsterCounties.append("Waterford") # Appending a string
leinsterCounties.extend(["Mayo", "Cork"]) # Adding a whole list

print(leinsterCounties)

################ Banker Roulette ##########################

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(names)
listLength = len(names)
#print(listLength)

ranNum = random.randint(0, listLength-1)

print(f"{names[ranNum]} is going to buy the meal today!")

#You can also use the choice function
personWhoWillPay = random.choice(names)
print(f"The choice function picked out {personWhoWillPay}")

##############################################################

'''
Nesting Lists
'''
fruits = ["Strawberrys","Nectarines", "Grapes"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

################################################################

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Take in input and translate to two individual ints
colInput = int(position[0])
rowInput = int(position[1])

#Change values to one lower than inputted
colInput -=1
rowInput -=1

#print(type(position))
map[rowInput][colInput] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
