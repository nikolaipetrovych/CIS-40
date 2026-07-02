# p5.py
# Nikolai Petrovych
# 7/2/26
# Python 3.12.10
# Description: Program that computes the sum and product of two numbers entered by the user.
'''
Algorithm:
Ask the user to enter two numbers.
store those two numbers in 2 variables, num1, num2.
make two new variables sum = num1 + num2, and product = num1*num2
Then, output the sum and product of to the user.
'''

# ask for user input on two numbers
print('PLEASE ENTER WHOLE NUMBERS')
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

# calculate the sum and product of num1 & num2
sum = num1 + num2
product = num1 * num2

#output results
print(f'The result of {num1}+{num2} is {sum}')
print(f'The result of {num1}*{num2} is {product}')

'''

***PROGRAM OUTPUT***

PLEASE ENTER WHOLE NUMBERS
Enter 1st number: 5
Enter 2nd number: 10
The result of 5+10 is 15
The result of 5*10 is 50

'''