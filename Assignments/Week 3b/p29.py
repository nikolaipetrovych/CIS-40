# p29.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''The absolute value of 1 is 1, and the absolute value of -1 is also 1.
Write a function that calculates and returns the absolute value of a number.
Do NOT just use the built-in python function abs()! You must write the
definition yourself!
Be sure to TYPE the function name and the function calls (do not copy/paste).

Function name:
def absolute(a):

Call it as:
print( 'The absolute value of -1 is', absolute(-1) )
print( 'The absolute value of 1 is', absolute(1) )'''


def absolute(a): # define func 'absolute' with an arg 'a'
    if a < 0: # if a is nonpositive
        abs_a = -a # invert the sign (take the absolute value)
        return abs_a # return the absolute value of the original negative value 'a'
    return a # if a was not nonpositive, return back a

print(f"The absolute value of -1 is {absolute(-1)}.") # take absolute value of -1, should be 1
print(f"The absolute value of 1 is {absolute(1)}.") # take absolute value of 1, should stay as 1


'''

***PROGRAM OUTPUT***

Test Run:
The absolute value of -1 is 1.
The absolute value of 1 is 1.

'''
