#project2

print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent_tip = int(input("what percentage of tip would you like to add? 10, 12 or 15? "))
total_amount = total_bill + (percent_tip/100 * total_bill)
each_person_amount = round(total_amount/people,2)
print("Each person should pay: $",each_person_amount)

#in python if you write 123_456_789, _(underscores) are ignored and treated as a complete number

print(123_456_789) #o/p 123456789
print(1_2_3 + 4_5_6) # this is same as print(123+456) o/p will be 579

'''write a program that adds the digits in a 2 digit number
e.g if the input is 35, then the output should be 3+5 = 8
Example input = 39
Example output = 3+9 = 12
'''
two_digit = input("Enter a two digit number: ")
final_sum = int(two_digit[0]) + int(two_digit[1])
print(final_sum)

'''write a program to calculate the BMI'''
height =input("enter your height in m: ")
weight = input("enter your weight in m: ")
BMI = float(weight)/float(height)**2
print(BMI)

'''write a program using maths and f-strings that tell us hpw many days,weeks,months we have left
if we live until 90 years old.It will take our current age as input and output is message with our 
time left in the below format
you have x daysy,y weeks,and z months left. Here x,y and z are calculated values'''

age = input("what is your current age? ")
age_left = 90-int(age)
days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12
print(f"you have {days_left} days,{weeks_left} weeks,and {months_left} months left")
