# p1.py
# Nikolai Petrovych
# 7/2/26 (edited on 7/28/26)
# Python 3.12.10
# Description: Program to show output in Python

print('hello world') # single quote
print("hello world") # double quote
print("he\nllo") # \n insert a new line (same as pressing Enter)

myName = "Nikolai" # declare/initialize string variable myName
weight = 165.5781 # declare/initialize float variable weight
age = 20 # declare/initialize int variable age
grades = [99, 96, 91.5]
nameZ = ["Nikolai", "Petrovych"]

print("Hello", myName)
print("Your weight is", weight, "and your age is ", age)
print("Your weight is %.2f and your age is %i" %(weight, age))
print("Lists: grades =", grades, "nameZ=", nameZ)
print("This is how you print", end=' ')
print("on the same line")

'''

***PROGRAM OUTPUT***

hello world
hello world
he
llo
Hello Nikolai
Your weight is 165.5781 and your age is  20
Your weight is 165.58 and your age is 20
Lists: grades = [99, 96, 91.5] nameZ= ['Nikolai', 'Petrovych']
This is how you print on the same line

'''
