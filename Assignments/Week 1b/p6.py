# p6.py
# Nikolai Petrovych
# 7/4/26
# Python 3.12.10
# Description: 
'''Write a program to compute a person's height.

INPUT: User will enter two whole numbers: feet and inches.
OUTPUT: Values input & total in inches.
INPUT VALIDATION: Make sure that feet and inches are positive values'''


# ask user to input feet and inches
print('Please only enter WHOLE numbers')
feet = int(input('Please enter the number of feet: '))
inches = int(input('Please enter the number of inches: '))

# check that feet and inches are positive

if feet < 0 or inches < 0:
    print('Please enter positive numbers for feet and inches')
    exit()
elif inches > 12:
    print('Inches values cannot exceed 12')
    exit()

# calculate total inches
total_inches = feet*12 + inches

# output total inches to user
print(f'{feet} feet and {inches} inch(es) is {total_inches} inches')


'''

***PROGRAM OUTPUT***

Run 1:
Please only enter WHOLE numbers
Please enter the number of feet: 4
Please enter the number of inches: 10
4 feet and 10 inch(es) is 58 inches

Error test 1 (inches > 12)
Please only enter WHOLE numbers
Please enter the number of feet: 4
Please enter the number of inches: 13
Inches values cannot exceed 12

Error test 2 (inches < 0)
Please only enter WHOLE numbers
Please enter the number of feet: 4
Please enter the number of inches: -1
Please enter positive numbers for feet and inches

Error test 3 (feet < 0)
Please only enter WHOLE numbers
Please enter the number of feet: -1
Please enter the number of inches: 10
Please enter positive numbers for feet and inches

'''