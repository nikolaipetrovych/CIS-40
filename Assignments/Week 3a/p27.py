# p27.py
# Nikolai Petrovych
# 7/10/26
# Python 3.12.10
# Description:
'''Write a program that generates a random list of letters.
# start with an empty_list = [ ]  and use empty_list.append(Letter) to add letters.
The length of the list of letters changes every time you run the program.
There can be a random number of X letters on the list, where X is a random number
between 50 to 75.
Each of the letters on the list is a random letter between A to F (uppercase).
Use a loop to generate the list and then show the generated list of letters to the user.
Count and then show to the user how many times the letter B appears.
In order to receive credit, you may not use python built-in function "count()" !
Hint: ascii A = 65 ... F = 70; use chr(randint(65,70)) to make a random letter.'''


import random

empty_list = [] # create empty list
x = random.randint(50,75) # generate a random value x for list length

for i in range(x): # create list
    letter = chr(random.randint(65,70)) # generate random letter from A to F
    empty_list.append(letter) # add the random letter to list

print(f"The list is {empty_list} and has a length of {len(empty_list)}.") # display list and its length to the user

count = 0 # set initial count
for i in range(len(empty_list)): # go through the whole list one by one
    if empty_list[i] == "B": # if 'B' is found
        count += 1 # add 1 to count

print(f"The letter 'B' appears in the list {count} time(s).") # display final count of 'B' to user
      
'''

***PROGRAM OUTPUT***

Test Run 1:
The list is ['F', 'B', 'A', 'E', 'B', 'A', 'C', 'F', 'E', 'D', 'F', 'A', 'B', 'D', 'E', 'B', 'E', 'C', 'D', 'E', 'B', 'B', 'D', 'D', 'B', 'E', 'F', 'D', 'D', 'F', 'E', 'A', 'F', 'A', 'F', 'C', 'A', 'D', 'D', 'A', 'A', 'D', 'A', 'C', 'B', 'D', 'D', 'F', 'E', 'C', 'F', 'B', 'E', 'C', 'B', 'F', 'E', 'C', 'F', 'C', 'F', 'F', 'E', 'D', 'E', 'B', 'D', 'B', 'E', 'E', 'B'] and has a length of 71.
The letter 'B' appears in the list 13 time(s).

Test Run 2:
The list is ['F', 'D', 'C', 'C', 'D', 'C', 'D', 'F', 'B', 'B', 'E', 'F', 'B', 'C', 'E', 'E', 'F', 'A', 'D', 'E', 'A', 'B', 'D', 'D', 'F', 'D', 'D', 'F', 'A', 'E', 'D', 'D', 'C', 'A', 'B', 'D', 'B', 'F', 'E', 'C', 'B', 'C', 'D', 'B', 'A', 'F', 'C', 'F', 'B', 'B', 'A', 'D', 'A', 'B', 'D', 'A', 'C', 'D', 'E', 'E', 'A', 'C', 'F', 'F', 'E', 'A', 'B', 'E', 'D'] and has a length of 69.
The letter 'B' appears in the list 12 time(s).

Test Run 3:
The list is ['D', 'D', 'B', 'C', 'D', 'D', 'E', 'A', 'B', 'B', 'C', 'D', 'C', 'C', 'D', 'F', 'E', 'F', 'E', 'A', 'E', 'E', 'C', 'D', 'A', 'D', 'A', 'E', 'E', 'F', 'B', 'D', 'B', 'E', 'B', 'B', 'B', 'C', 'B', 'C', 'E', 'D', 'F', 'E', 'C', 'E', 'A', 'B', 'C', 'A', 'C', 'F', 'C', 'E', 'A', 'E', 'A', 'C', 'D', 'E', 'A', 'F', 'C'] and has a length of 63.
The letter 'B' appears in the list 10 time(s).


'''
