# p41.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write a function which outputs as many crosses as the parameter 'numCrosses'
indicates.

    def stars(numCrosses):

For example, when numCrosses equals 5, the function displays:
+
+ +
+ + +
+ + + +
+ + + + +

You are NOT allowed to use string concatenation or multiplication. The use of a
list and appending to a list is NOT permitted. You must solve the problem using
2 loops (one 'for' loop nested inside the other).

Hint: outer loop = each row; print one '+' with end=' ' (no newline yet), then
an inner loop prints the extra '+' for that row on the same line, then print()
an empty line to move to the next row.'''


def stars(numCrosses):
    for row in (range(1, numCrosses + 1)):
        for column in range(row):
            print("+", end = ' ')
        print()


stars(5)

'''

***PROGRAM OUTPUT***

Test Run 1 (stars(5)):
+ 
+ + 
+ + + 
+ + + + 
+ + + + + 

'''
