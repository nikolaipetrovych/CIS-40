# p26.py
# Nikolai Petrovych
# 7/10/26 - 7/17/26
# Python 3.12.10
# Description:
'''Write a program that generates a random list of numbers.
(start with an empty list and use append() )
The length of the list X can be a random number between 15 to 20.
Each of the random numbers on the list can be between 2 to 5.
Count how many times the number 3 appears.
You are not allowed to use python built-in function "count()" or you'll get a Zero!'''


import random

mylist = []  # create an empty list
x = random.randint(15, 20)  # generate x value between 15 and 20
for i in range(x):  # x times
    num = random.randint(2, 5)  # generate a number between 2 and 5
    mylist.append(num)  # add the number to list

print(f"List is {mylist}. Its length is {len(mylist)} since x was {x}.")  # display list

count = 0  # set initial count
for i in mylist:  # go through every number in the list
    if i == 3:  # if the number is 3, add 1 to count
        count += 1

print(f"Number 3 appears in the list {count} time(s).")  # display result

'''

***PROGRAM OUTPUT***

Test Run 1:
List is [5, 3, 5, 2, 4, 5, 3, 3, 3, 2, 2, 5, 4, 2, 5, 3, 4]. Its length is 17 since x was 17.
Number 3 appears in the list 5 time(s).

Test Run 2:
List is [2, 5, 3, 3, 2, 3, 5, 5, 2, 5, 2, 2, 2, 3, 4, 5]. Its length is 16 since x was 16.
Number 3 appears in the list 4 time(s).

Test Run 3:
List is [3, 2, 4, 5, 3, 3, 2, 2, 2, 2, 5, 3, 5, 3, 2, 3, 4]. Its length is 17 since x was 17.
Number 3 appears in the list 6 time(s).

'''
