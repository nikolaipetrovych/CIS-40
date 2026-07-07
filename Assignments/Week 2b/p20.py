# p20.py
# Nikolai Petrovych
# 7/7/26
# Python 3.12.10
# Description: 
'''Write a program that reads in X whole numbers and outputs
(1) the sum of all positive numbers,
(2) the sum of all negative numbers, and
(3) the sum of all positive and negative numbers.
The user can enter the X numbers in any different order every time,
and can repeat the program if desired. '''


run = True
while run == True:
    sumAll = 0
    sumPos = 0
    sumNeg = 0
    x = int(input('How many numbers would you like to enter? '))
    for i in range(1, x+1):
        num = float(input(f'Please enter number {i}: '))
        sumAll += num
        if num < 0:
            sumNeg += num
        else:
            sumPos += num
    print(f'sumAll is {sumAll:.2f}, sumPos is {sumPos:.2f}, and sumNeg is {sumNeg:.2f}.')
    ask = input("The program will run again. Enter 'quit' to exit. Enter any key to run again: ").lower()
    if ask == 'quit':
        run = False
      

print('Thank you for using p20.py.')


'''

***PROGRAM OUTPUT***

[------]

'''