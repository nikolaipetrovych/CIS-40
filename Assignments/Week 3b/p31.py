# p31.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write a function that has an integer N as a parameter and returns True if N
is even.
Be sure to TYPE the function name and the function calls (do not copy/paste).

Function name:
def isEven(n):

Call it as:
print( "3 is even: ", isEven(3) )
print( "4 is even: ", isEven(4) )
Hint: A number N is even if N % 2 == 0'''



def isEven(n): # define func isEven that takes input n
    result = (n % 2 == 0) # check if n is even and assign the boolean value to 'result'
    return result # return the boolean 'result' to user

print( "3 is even:", isEven(3)) # check if 3 is even, should be False
print( "4 is even:", isEven(4)) # check if 4 is even, should be True

'''

***PROGRAM OUTPUT***

Test Run:
3 is even: False
4 is even: True

'''
