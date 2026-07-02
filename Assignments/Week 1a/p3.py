# p3.py
# Nikolai Petrovych
# 7/2/26
# Python 3.12.10
# Description: Program to take input in Python

name = input("Please enter your name: ") # this is a string
weightLbs = float(input("Please enter your weight in lbs: ")) # a float
age = int(input("Please enter your age (whole number): " )) # an integer
weightKg = weightLbs * 0.453592
title = "Human"

print("Hello", title, name, "your weight is")
print( weightLbs, "lbs")
print(f"which equals = {weightKg}", end=' ') # end=' ' prevents new line
print("kg")

'''

***PROGRAM OUTPUT***

Please enter your name: Nikolai
Please enter your weight in lbs: 165.5
Please enter your age (whole number): 20
Hello Human Nikolai your weight is
165.5 lbs
which equals = 75.069476 kg

'''