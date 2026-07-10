# p22.py
# Nikolai Petrovych
# 7/10/26
# Python 3.12.10
# Description:
'''Write a Dice Game program that generates two random dice values between 1 and 6
for you, and 2 for the computer.
You get to roll as many times as you like (if you don't like your 2 dice), while the
computer only rolls once, after you have decided that you like your two dice.
Determine who wins, you or the computer.
Test your program for: 1) You win  2) You lose  3) Tie'''


import random

# generate user dice values
userdice1 = random.randint(1,6)
userdice2 = random.randint(1,6)

# display user dice values and ask if user wants to reroll
while True:
    keepgoing = input(f'You rolled {userdice1} and {userdice2}. Would you like to roll again? (y/n): ').lower()
    if keepgoing == 'n':
        break
    elif keepgoing == 'y':
        userdice1 = random.randint(1,6)
        userdice2 = random.randint(1,6)
    else:
        print('Answer has to be in format (y/n).')

# generate computer dice values
computerdice1 = random.randint(1,6)
computerdice2 = random.randint(1,6)

# display computer values
print(f'Computer rolled {computerdice1} and {computerdice2}.')

#compute and compare scores
usersum = userdice1 + userdice2
computersum = computerdice1 + computerdice2
if usersum > computersum:
    print(f'{usersum} is higher than {computersum}. You won!')
elif usersum < computersum:
    print(f'{usersum} is lower than {computersum}. You lost.')
else:
    print(f"You both scored {usersum}. It's a tie!")


'''

***PROGRAM OUTPUT***

Test Run 1 (you win):
You rolled 6 and 2. Would you like to roll again? (y/n): n
Computer rolled 3 and 2.
8 is higher than 5. You won!

Test Run 2 (you lose):
You rolled 3 and 2. Would you like to roll again? (y/n): n
Computer rolled 5 and 4.
5 is lower than 9. You lost.

Test Run 3 (tie):
You rolled 5 and 4. Would you like to roll again? (y/n): n
Computer rolled 3 and 6.
You both scored 9. It's a tie!

Error Test 1 (keepgoing entry non y/n):
You rolled 1 and 2. Would you like to roll again? (y/n): x
Answer has to be in format (y/n).
You rolled 1 and 2. Would you like to roll again? (y/n): n
Computer rolled 1 and 4.
3 is lower than 5. You lost.

'''
