# p23.py
# Nikolai Petrovych
# 7/10/26
# Python 3.12.10
# Description:
'''Write a program to let a child practice arithmetic skills.
The program should first ask for what kind of practice is wanted:
addition(1), subtraction(2), or multiplication(3)... (no division).
Then, the program will have a loop for each of the desired operations that lets the
user repeat the practice as many times as desired.
Two random numbers will be generated (0 - 9), and the child will have to add,
subtract or multiply them.
If the child answers correctly, congratulate them, and give them two different numbers.
If the child answers incorrectly, the problem should be repeated (same two numbers).
Note: You are not allowed to use the eval() or sum() functions!'''


import random

# get pracice type and store it as choice + invalid input check
print("What kind of practice is wanted?")
choice = input("Choose addition (1), subtraction (2), or multiplication (3): ")
while True:
    if choice in ["1", "2", "3"]:
        break
    else:
        choice = input("Only type 1, 2, or 3: ")


# practice loop

while True:
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    # calculate and get guesses
    if choice == "1":   # calculate addition result
        result = num1 + num2
        guess = input(f"Enter your guess: {num1} + {num2} = ")
    elif choice == "2": # caluclate subtraction result
        result = num1 - num2
        guess = input(f"Enter your guess: {num1} - {num2} = ")
    else:               # calculate mult result
        result = num1 * num2
        guess = input(f"Enter your guess: {num1} * {num2} = ")
    if int(guess) == result:
        print(f"That's correct!")
    else:
        input("Not correct. Would you like to guess again (1), get another problem (2), change mode (3), or quit (4)? ")
        
          

            


        '''

***PROGRAM OUTPUT***

Test Run 1 (addition):


Test Run 2 (subtraction):


Test Run 3 (multiplication):


Error Test 1 (invalid operation choice):


Error Test 2 (non-integer answer):


Error Test 3 (invalid try-again choice):


'''
