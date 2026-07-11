# p30.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write a function which has two parameters, N and M.
The function returns True if N is evenly divisible by M, and False otherwise.
Be sure to TYPE the function name and the function calls (do not copy/paste).

Function name:
def isDivisible(n, j):

Call it as:
print( "4 is evenly divisible by 2: ", isDivisible(4,2) )
print( "5 is evenly divisible by 2: ", isDivisible(5,2) )
Hint: n is evenly divisible by j when n % j == 0'''


def isDivisible(n, m): # define func isDivisivle that takes inputs n and m
    value = (n % m == 0) # check if n is divisible by n and assign the truth value to 'value'
    return value # output 'value' to user

print( "4 is evenly divisible by 2:", isDivisible(4,2)) # check if 4 is divisible by 2, True
print( "5 is evenly divisible by 2:", isDivisible(5,2)) # check if 5 is divisible by 2, False


'''

***PROGRAM OUTPUT***

Test Run:
4 is evenly divisible by 2: True
5 is evenly divisible by 2: False


'''
