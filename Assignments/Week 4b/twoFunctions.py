# twoFunctions.py
# Nikolai Petrovych
# 7/26/26 - 7/27/26
# Python 3.12.10
# Description: Two Functions
'''Write the following two function definitions, and call each function appropriately in order to test and show how each function works.
Write and test both functions in the same twoFunctions.py file.
For full credit please submit your working program test runs, as usual. You are not allowed to use built-in functions to sort or find median.
Function 1:
Write a function named "speed" which has 2 PARAMETERS: distance, time.
The functions computes and PRINTS the speed = distance/ time . The value is shown rounded to 2 values to the right of the decimal point.
Sample Call:
speed(730,12)
Sample Test Run:
60.83
Function 2:
Write a function named "middle" which has 3 PARAMETERS: num1, num2, num3.
The function RETURNS the middle/median value of the 3 arguments. Assume 3 different values as parameters.
You are not permitted to use built-in python functions sort(), sorted(), median()
Note: Median is not the same as Average! Show the value that the function returns after it was called.
Sample Calls:
print( middle(1,2,5) )
print( middle(2,1,5) )
print( middle(1,5,2) )'''


def speed(dist, time):
    speed_result = dist / time  # calculate
    print(f"{speed_result:.2f}")  # output


def middle(num1, num2, num3):
    if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):  # num1 is median
        median_result = num1
    elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):  # num2 is median
        median_result = num2
    elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):  # num3 is median
        median_result = num3
    else:
        print("Values have to be distinct")
        return

    return median_result


speed(730, 12)

print(middle(1, 2, 5))
print(middle(2, 1, 5))
print(middle(1, 5, 2))

'''

***PROGRAM OUTPUT***

Test Run:
60.83
2
2
2

'''
