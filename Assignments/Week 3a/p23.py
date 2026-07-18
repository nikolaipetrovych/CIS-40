# p23.py
# Nikolai Petrovych
# 7/10/26 - 7/17/26
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

# get practice type and store it as choice + invalid input check
print("What kind of practice is wanted?")
choice = input("Choose addition (1), subtraction (2), or multiplication (3): ") # ask for input on type of practice
while True:
    if choice in ["1", "2", "3"]: # valid input, move on
        break
    else:
        choice = input("Only type 1, 2, or 3: ") # invalid input

# generate two random numbers
num1 = random.randint(0,9) 
num2 = random.randint(0,9)

# practice loop
while True:
    # calculate and get guesses
    if choice == "1":   # calculate addition result
        result = num1 + num2
        guess = input(f"Enter your guess: {num1} + {num2} = ") # ask for guess
    elif choice == "2": # calculate subtraction result
        result = num1 - num2
        guess = input(f"Enter your guess: {num1} - {num2} = ") # ask for guess
    else:               # calculate mult result
        result = num1 * num2
        guess = input(f"Enter your guess: {num1} * {num2} = ") # ask for guess

    # follow the menu choice
    # keep == "0" will skip this and repeat the loop
    keep = " "
    while keep not in ["0", "1", "2", "3"]:
        if int(guess) == result: # if guess matches the answer, say it is correct
            keep = input(f"That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? ")
        else: # if guess does not match the answer
            keep = input("Not correct. Would you like to guess again (0), get another problem (1), change mode (2), or quit (3)? ")

    if keep == "1": # new numbers, same mode
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

    elif keep == "2": # pick the mode again
        choice = input("Choose addition (1), subtraction (2), or multiplication (3): ")
        while choice not in ["1", "2", "3"]: # validate the new mode entry
            choice = input("Only type 1, 2, or 3: ")
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

    elif keep == "3": # quit
        break

'''

***PROGRAM OUTPUT***

Test Run 1 (addition):
What kind of practice is wanted?
Choose addition (1), subtraction (2), or multiplication (3): 1
Enter your guess: 2 + 9 = 5
Not correct. Would you like to guess again (0), get another problem (1), change mode (2), or quit (3)? 0
Enter your guess: 2 + 9 = 11
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 1
Enter your guess: 1 + 4 = 5
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 3

Test Run 2 (subtraction):
What kind of practice is wanted?
Choose addition (1), subtraction (2), or multiplication (3): 2
Enter your guess: 3 - 9 = -6
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 1
Enter your guess: 8 - 2 = 6
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 3

Test Run 3 (multiplication):
What kind of practice is wanted?
Choose addition (1), subtraction (2), or multiplication (3): 3
Enter your guess: 9 * 4 = 36
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 1
Enter your guess: 5 * 8 = 40
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 3

Error Test 1 (invalid operation choice):
What kind of practice is wanted?
Choose addition (1), subtraction (2), or multiplication (3): 5
Only type 1, 2, or 3: 1
Enter your guess: 0 + 1 = 1
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 3

Error Test 2 (non-integer answer):
What kind of practice is wanted?
Choose addition (1), subtraction (2), or multiplication (3): 1
Enter your guess: 6 + 8 = abc
Traceback (most recent call last):
  File "*file path*", line 50, in <module>
    if int(guess) == result: # if guess matches the answer, say it is correct
       ^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'abc'

Error Test 3 (invalid try-again choice):
What kind of practice is wanted?
Choose addition (1), subtraction (2), or multiplication (3): 1
Enter your guess: 0 + 1 = 1
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 9
That's correct! Would you like to get another problem (1), change mode (2), or quit (3)? 3

'''
