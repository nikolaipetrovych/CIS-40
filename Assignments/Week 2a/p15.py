# p15.py
# Nikolai Petrovych
# 7/5/26 - 7/10/26
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

# calculate sumAll and set initial sumNeg and sumPos as 0
sumAll = num1 + num2 + num3 + num4
sumNeg = 0
sumPos = 0

# Check each number if pos or neg and add to apropriate sum
# num1
if num1 < 0:
    sumNeg += num1
else:
    sumPos += num1

# num2
if num2 < 0:
    sumNeg += num2
else:
    sumPos += num2

# num3
if num3 < 0:
    sumNeg += num3
else:
    sumPos += num3

# num4
if num4 < 0:
    sumNeg += num4
else:
    sumPos += num4

# output
print(f'sumAll is {sumAll}, sumPos is {sumPos}, and sumNeg is {sumNeg}.')


'''

***PROGRAM OUTPUT***

num1: -3.55
num2: 3
num3: -2.5
num4: 2.01
sumAll is -1.04, sumPos is 5.01, and sumNeg is -6.05.

'''