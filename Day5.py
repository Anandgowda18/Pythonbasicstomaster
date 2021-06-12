'''Average Height
Instructions
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: 156, 178, 165, 171, 187

Example Output
171'''

student_heights = input("enter the list of student heights").split()
for i in range(0,len(student_heights)):
    student_heights[i] = int(student_heights[i])
average_height = round(sum(student_heights)/len(student_heights))
print(average_height)

#lets do without using sum and len functions

sum  = 0
count = 0
for j in student_heights:
    sum += j
    count+=1
avg_height = round(sum/count)
print(avg_height)

'''Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91'''

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max_value = 0
for i in student_scores:
    if i>max_value:
        max_value = i
print(max_value)

'''Adding Evens
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just 
print the final total and not every step of the calculation.'''

total = 0
for i in range(0,101,2):
    total+=i
print(total)

'''FizzBuzz
Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
  `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print'''

for i in range(1,101):
    if i%3==0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
symbol_select = random.sample(symbols,nr_symbols)
number_select = random.sample(numbers,nr_numbers)
nr_letters = nr_letters - nr_numbers - nr_symbols
letters_select = random.sample(letters,nr_letters)
password = symbol_select + number_select + letters_select
random.shuffle(password)
password_final = ''.join(password)
print(password_final)