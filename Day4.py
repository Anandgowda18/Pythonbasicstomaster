'''Heads or Tails
Instructions
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails'''
import random
heads_tails = random.randint(0,1)
if heads_tails:
    print("Head")
else:
    print("Tails")

'''Instructions
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for
everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!'''

name_string = input("enter the names of people with comma separated")
name_list = name_string.split(',')
name_payee = random.randint(0,len(name_list)-1)
name = name_list[name_payee].lstrip()
print(f"{name} will pay the bill")

#using choice
name_string = input("enter the names of people with comma separated")
name_list = name_string.split(',')
name = random.choice(name_list).lstrip()
print(f"{name} will pay the bill")

'''Instructions
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list.
When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format t
In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the 
vertical column number and the second digit is the horizontal row number. e.g.:

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:
23
Example Output 1
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
'''

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1,row2,row3]
print(map)

x = int(input("two digit number"))
x1 = x%10
y1 = x//10

map[x1-1][y1-1] = 'x'
print(f"{row1}\n{row2}\n{row3}")

'''Day 4 project----Rock,paper,scissors'''

choice = int(input("what do you choose?Type 0 for Rock,1 for paper or 2 for scissors"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_choice = [rock,paper,scissors]
user_choice = list_choice[choice]
computer = random.randint(0,2)
computer_choice = list_choice[computer]
print(f"you chose {user_choice}")
print(f"computer chose:\n{computer_choice}")

if choice == computer:
    print("it's a draw")
elif choice == 0 and computer == 2:
    print("you win")
elif choice == 2 and computer == 1:
    print("you win")
elif choice == 1 and computer == 0:
    print("you win")
else:
    print("computer wins")