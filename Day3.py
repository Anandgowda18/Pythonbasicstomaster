'''write a program to check if a given number is odd or even'''
number = int(input("enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

'''write a roller coaster problem where if the height of a person is greater than 120cm than the person can rode roller
coaster else the person cant. also if a person can ride the if the age of the person is greater than 18 the price is $12
else the price should be $7'''

print("welcome to roller coaster")
height = int(input("what is you height? "))
if height >=120:
    print("you can ride roller coaster")
    age = int(input("what is your age? "))
    if age>=18:
        print("$12")
    else:
        print("$7")
else:
    print("you can't ride the roller coaster")

'''enhancement for the previous program where there will be different age group
if the age group is less than 12  then price is $5, if the age group is 12 to 18 price $7 else the age is greater than 18 than
the price should be $12'''
height = int(input("what is you height? "))
if height >=120:
    print("you can ride roller coaster")
    age = int(input("what is your age? "))
    if age>=18:
        print("$12")
    elif age<=12:
        print("$5")
    else:
        print("$7")
else:
    print("you can't ride the roller coaster")

'''BMI 2.0 write a program that interprets the Body Mass Index(BMI) based on users weight and height
it should tell them the interpretation of their BMI based BMI value
1.under 18.5 they are underweight
2.between 18.5 and 25 they are normal
3.over 25 and but below 30 they are overweight
4.over 30 but below 35 they are obese
5.over 35 they are clinically obese'''

weight = float(input("enter your weight in kgs"))
height = float(input("enter you height in m"))
BMI = weight/(height**2)
if BMI<=18.5:
    print("underweight")
elif BMI>18.5 or BMI<=25:
    print("Normal")
elif BMI>25 or BMI<=30:
    print("over weight")
elif BMI>30 or BMI<=35:
    print("over weight")
else:
    print("clinically obese")

'''to find the leap year, logic if a number is divisible by 4 than its a leap year except 
if a year is evenly divisible by 100 unless the year is divisible by 400
e.g 2000/4 =500(leap)
2000/100 = 20(not Leap)
2000/400 = 5(leap)
2000 is a leap year'''

year = int(input("enter the year you need to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap")
        else:
            print("not leap")
    else:
        print("leap")
else:
    print("not leap")

'''roller coaster problem to enhance the photos taken for $3'''

print("welcome to roller coaster problem")
height = int(input("enter your height in cm"))
bill = 0
if height>=120:
    print("you can ride the roller coaster")
    age = int(input("enter you age"))
    if age < 12:
        print("the roller coaster ride would cost $5")
        bill = 5
    elif age<=18:
        print("the roller coaster ride would cost $7")
        bill = 7
    else:
        print("the roller coaster ride would cost $12")
        bill = 12
    photo = input("do you want a photo, this would cost you $3? y for yes and n for no")
    if photo == 'y':
        bill = bill+3
    print(f"the total bill for the roller coaster ride is ${bill}")
else:
    print("you have to become taller to ride the roller coaster")

'''Pizza delivery
Based on user's order, work out their final bill
small pizza:$15
medium pizza:$20
Large Pizza:$25

pepperoni for small pizza : +$2
pepperoni for medium or large pizza : +$1

example input
size = L
add_pepperoni = y
extra_cheese = n

example output
your final bill is : $28'''

print("welcome to python pizza deliveries!!")
size = input("what size pizza do you want? s,m or l")
add_pepperoni = input("do you want pepperoni? y or n")
extra_cheese = input("do you want extra cheese? y or n")
bill = 0
if size == 's':
    bill = 15
elif size == 'm':
    bill = 20
else:
    bill = 25
if add_pepperoni == 'y':
    if size == 's':
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == 'y':
    bill = bill +1

print(f"your total bill is ${bill}")

'''Love calculator
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53
Print: Your score is 53.'''

print("Welcome to the Love calculator")
name1 = input("enter your name")
name2 = input("enter their name")
name1 = name1.lower()
name2 = name2.lower()
count_T = name1.count('t') + name2.count('t')
count_R = name1.count('r') + name2.count('r')
count_U = name1.count('u') + name2.count('u')
count_E = name1.count('e') + name2.count('e')
count_L = name1.count('l') + name2.count('l')
count_O = name1.count('0') + name2.count('o')
count_V = name1.count('v') + name2.count('v')

true = count_T+count_R+count_U+count_E
love = count_L+count_O+count_V+count_E

true_love = str(true)+str(love)
true_love = int(true_love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif true_love >= 40 or true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("left or right?")
if left_right == 'left':
    swim_wait = input("swim or wait")
    if swim_wait == 'wait':
        door = input("Which door? Red,Blue or Yellow")
        if door == 'yellow':
            print("you win")
        else:
            print("you lose")
    else:
        print("you lose")
else:
    print("you lose")
