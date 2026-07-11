# p33.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''If you are given three sticks, you may or may not be able to arrange them in
a triangle. For example, if one stick is 12 inches long and the other two are
one inch long, the short sticks will not meet in the middle.
Simple test for any three sticks:
"If any of the three sticks is greater than the sum of the other two, then you
cannot form a triangle. Otherwise, you can."
Write a function named isTriangle(a, b, c) that has three sides a, b, c as
parameters. The function returns True or False depending on whether a triangle
can be formed from the sides with the given lengths.

Function name:
def isTriangle(a, b, c):

Call it as:
print("Three sticks with length 3,4,5 can form a triangle:", isTriangle(3,4,5))
print("Three sticks with length 3,5,4 can form a triangle:", isTriangle(3,5,4))
print("Three sticks with length 4,3,5 can form a triangle:", isTriangle(4,3,5))
print("Three sticks with length 4,5,3 can form a triangle:", isTriangle(4,5,3))
print("Three sticks with length 5,4,3 can form a triangle:", isTriangle(5,4,3))
print("Three sticks with length 5,3,4 can form a triangle:", isTriangle(5,3,4))
print("Three sticks with length 20,3,4 can form a triangle:", isTriangle(20,3,4))
print("Three sticks with length 3,20,4 can form a triangle:", isTriangle(3,20,4))
print("Three sticks with length 3,4,20 can form a triangle:", isTriangle(3,4,20))'''


def isTriangle(a, b, c): # create an isTriangle function that takes inputs a,b,c (stick lengths)
    result = not (a > b+c or b > a+c or c > a+b) # check if any side is greater than the two others. since we want to output False when any of them are, take the inverse with 'not'. Assign the truth value to 'result'.
    return result # output 'result' value back

# check all conditions from assignment directions
print("Three sticks with length 3,4,5 can form a triangle:", isTriangle(3,4,5)) # should be True: 3,4,5 traiangle
print("Three sticks with length 3,5,4 can form a triangle:", isTriangle(3,5,4)) # should be True: 3,4,5 traiangle
print("Three sticks with length 4,3,5 can form a triangle:", isTriangle(4,3,5)) # should be True: 3,4,5 traiangle
print("Three sticks with length 4,5,3 can form a triangle:", isTriangle(4,5,3)) # should be True: 3,4,5 traiangle
print("Three sticks with length 5,4,3 can form a triangle:", isTriangle(5,4,3)) # should be True: 3,4,5 traiangle
print("Three sticks with length 5,3,4 can form a triangle:", isTriangle(5,3,4)) # should be True: 3,4,5 traiangle
print("Three sticks with length 20,3,4 can form a triangle:", isTriangle(20,3,4)) # should be False
print("Three sticks with length 3,20,4 can form a triangle:", isTriangle(3,20,4)) # should be False
print("Three sticks with length 3,4,20 can form a triangle:", isTriangle(3,4,20)) # should be False
        

'''

***PROGRAM OUTPUT***

Test Run 1 (six valid orderings of 3,4,5 -> True; three with a side of 20 -> False):
Three sticks with length 3,4,5 can form a triangle: True
Three sticks with length 3,5,4 can form a triangle: True
Three sticks with length 4,3,5 can form a triangle: True
Three sticks with length 4,5,3 can form a triangle: True
Three sticks with length 5,4,3 can form a triangle: True
Three sticks with length 5,3,4 can form a triangle: True
Three sticks with length 20,3,4 can form a triangle: False
Three sticks with length 3,20,4 can form a triangle: False
Three sticks with length 3,4,20 can form a triangle: False

'''
