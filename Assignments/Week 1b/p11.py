# p11.py
# Nikolai Petrovych
# 7/4/26
# Python 3.12.10
# Description: Program 11 - Rock, Paper, Scissors
'''Write a program to simulate rock-paper-scissors game.
Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.
The program then shows the winner on the basis of:
-Paper covers Rock
-Rock breack Scissors
-Scissors cut Paper
-Tie'''


import random #random number generation module

# get p1 and p2 input
mode = input('Would you like P2 to generate randomly? (y/n): ') # ask if P2 should be randomly generated or chose manually
if mode == 'y':
    p1 = input('P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: ') #ask for p1 input
    p2 = random.randint(1,3) #generate a random p2 choice between 1 and 3
elif mode == 'n':
    p1 = input('P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: ') #ask for p1 input
    p2 = input('P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: ') #ask for p2 input
else:
    print('Only enter (y/n).')
    quit()

# convert R/P/S into 1/2/3 and check if all inputs are valid

#check P1
if p1 == 'R' or p1 == '1':
    p1 = 1
elif p1 == 'P' or p1 == '2':
    p1 = 2
elif p1 == 'S' or p1 == '3':
    p1 = 3
else:
    print('Please only enter (1/2/3 or R/P/S)')
    quit()


#check P2
if mode =='n': #only check when P2 is entered manually (as a string)
    if p2 == 'R' or p2 == '1':
        p2 = 1
    elif p2 == 'P' or p2 == '2':
        p2 = 2
    elif p2 == 'S' or p2 == '3':
        p2 = 3
    else:
        print('Please only enter (1/2/3 or R/P/S)')
        quit()

#set 1/2/3 as rock/paper/scissors variables
rock = 1
paper = 2
scissors = 3

# show choices
print(f'P1 choice is {p1}')
print(f'P2 choice is {p2}')

# check win conditions for P1
if p1 == rock and p2 == scissors:
    print("P1 wins, rock breaks scissors")
elif p1 == paper and p2 == rock:
    print("P1 wins, paper covers rock")
elif p1 == scissors and p2 == paper:
    print ("P1 wins, scissors cut paper")

# check win conditions for P2
if p2 == rock and p1 == scissors:
    print("P2 wins, rock breaks scissors")
elif p2 == paper and p1 == rock:
    print("P2 wins, paper covers rock")
elif p2 == scissors and p1 == paper:
    print ("P2 wins, scissors cut paper")

#check tie conditions
if p1 == p2:
    print('It\'s a tie!')


'''

***PROGRAM OUTPUT***

Run 1 (P1 wins, rock beats scissors, 1-3):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 1
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: S
P1 choice is 1
P2 choice is 3
P1 wins, rock breaks scissors

Run 2 (P1 wins, scissors cut paper, 3-2):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 3
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 2
P1 choice is 3
P2 choice is 2
P1 wins, scissors cut paper

Run 3 (P1 wins, paper covers rock, 2-1)
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: P
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 1
P1 choice is 2
P2 choice is 1
P1 wins, paper covers rock

Run 4 (P2 wins, rock beats scissors, 3-1):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: S
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: R
P1 choice is 3
P2 choice is 1
P2 wins, rock breaks scissors

Run 5 (P2 wins, scissors cut paper, 2-3):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 2
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 3
P1 choice is 2
P2 choice is 3
P2 wins, scissors cut paper

Run 6 (P2 wins, paper covers rock, 1-2):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 1
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 2
P1 choice is 1
P2 choice is 2
P2 wins, paper covers rock

Run 7 (TIE):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: S
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: S
P1 choice is 3
P2 choice is 3
It's a tie!

Run 8 (P2 is randomly generated):
Would you like P2 to generate randomly? (y/n): y
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: S
P1 choice is 3
P2 choice is 1
P2 wins, rock breaks scissors

Error test 1 (invalid entry for random P2 prompt):
Would you like P2 to generate randomly? (y/n): Y
Only enter (y/n).

Error test 2 (invalid entry for P1 - choice is not 1/2/3 or R/P/S):
Would you like P2 to generate randomly? (y/n): y
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 6
Please only enter (1/2/3 or R/P/S)

Error test 3 (invalid entry for P2 - choice is not 1/2/3 or R/P/S):
Would you like P2 to generate randomly? (y/n): n
P1: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: 3
P2: Please enter 1 or R for rock, 2 or P for paper, 3 or S for scissors: T
Please only enter (1/2/3 or R/P/S)

'''