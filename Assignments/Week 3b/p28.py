# p28.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write a function which, given two integer parameters, returns their sum...
unless the two values are the same, then the function returns their doubled sum.
Be sure to type the function name and the function calls (do not copy/paste).

Function name:
def sum_double(a, b):

Call it as:
print( sum_double(1, 2) )  # shows 3   (values different -> sum)
print( sum_double(2, 2) )  # shows 8   (values same -> doubled sum)'''


def sum_double(a, b): # define function name and args
    sum = a+b # take a sum
    if a == b: # if a and b are same
        doublesum = 2*sum # double the sum
        return doublesum # output the doubled sum
    return sum # if a !=b don't double the sum

print("first sum:", sum_double(1, 2)) # double sum of 1 and 2 (will not be doubled, 1+2=3)
print("second sum:", sum_double(2, 2)) # double sum of 2 and 2 (will be doubled, 2*(2+2)=8)



'''

***PROGRAM OUTPUT***

Test Run:
first sum: 3
second sum:: 8


'''
