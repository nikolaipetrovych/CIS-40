# p15.py
# Nikolai Petrovych
# 7/5/26
# Python 3.12.10
# Description: Program that asks the user to enter 4 numbers (positive or negative).
'''The program shows:
-the sum of all numbers (sumAll)
-the sum of positive numbers (sumPos),
-the sum of negative numbers (sumNeg)

The Algorithm for this problem:
-sumNeg is going to hold the total of all negative numbers, it starts at zero (0)
-sumPos is going to hold the total of all positive numbers, it starts at zero (0)
-if a number is negative you ADD it to sumNeg
-if a number is positive you ADD it to sumPos'''


# get inputs
num1 = float(input('num1: '))
num2 = float(input('num2: '))
num3 = float(input('num3: '))
num4 = float(input('num4: '))

# determine positive and negative numbers
if num1 >= 0:
    num1_pos = num1
    num1_neg = 0
elif num1 < 0:
    num1_pos = 0
    num1_neg = num1

if num2 >= 0:
    num2_pos = num2
    num2_neg = 0
elif num2 < 0:
    num2_pos = 0
    num2_neg = num2

if num3 >= 0:
    num3_pos = num3
    num3_neg = 0
elif num3 < 0:
    num3_pos = 0
    num3_neg = num3

if num4 >= 0:
    num4_pos = num4
    num4_neg = 0
elif num4 < 0:
    num4_pos = 0
    num4_neg = num4


# perform calculations
sumAll = num1 + num2 + num3 + num4
sumPos = num1_pos + num2_pos + num3_pos + num4_pos
sumNeg = num1_neg + num2_neg + num3_neg + num4_neg

# output
print(f'sumAll is {sumAll:.2f}')
print(f'sumPos is {sumPos:.2f}')
print(f'sumNeg is {sumNeg:.2f}')



'''

Test Run 1 (combo):


Test Run 2 (all numbers are positive):


Test Run 3 (all numbers are negative):


Error Test 1 (input is not an int):



'''