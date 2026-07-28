# Final.py
# Nikolai Petrovych
# 7/27/26 - 7/28/26
# Python 3.12.10
# Description:
'''Final Exam Program.
You may NOT use the built-in python functions: sum(), average(), sort(),
sorted(), median().
A) Use a loop to make 10 random numbers between 20 and 30, store them in a
   variable numList.
B) Sort the list using the bubble sort you learned in this class.
C) Show the sorted list and the unsorted list.
D) Find the sum, and average of the numbers in numList.
E) Find the median of the list.
F) Show how many numbers are evenly divisible by 2.
G) Copy/paste the Output of your program (A-F) as a multiline comment at the
   bottom of your program.'''

from random import randint

# PART A
numList = []
for i in range(10):
    num = randint(20, 30)
    numList.append(num)

# PART B
numListSorted = numList.copy()  # copy to keep the unsorted list for Part C
for j in range(len(numListSorted)):  # bubble sort
    for i in range(len(numListSorted) - 1):
        if numListSorted[i] > numListSorted[i+1]:
            # swap the two elements using temp
            temp = numListSorted[i]
            numListSorted[i] = numListSorted[i+1]
            numListSorted[i+1] = temp

# PART C
print(f"UNSORTED: numList = {numList}")
print(f"SORTED:   numList = {numListSorted}")

# PART D
total = 0
for x in numList:
    total += x
average = total / len(numList)
print(f"sum = {total}")
print(f"avg = {average:.3f}")

# PART E
# average of the 2 middle values, at indices 4 and 5
median = (numListSorted[4] + numListSorted[5]) / 2
print(f"median = {median:.1f}")

# PART F
numsDivisible = 0
for x in numList:
    if x % 2 == 0:
        numsDivisible += 1
print(f"{numsDivisible} numbers in the list are divisible by 2")

# PART G

'''

***PROGRAM OUTPUT***

Test Run 1:
UNSORTED: numList = [22, 28, 24, 25, 20, 24, 25, 29, 23, 23]
SORTED:   numList = [20, 22, 23, 23, 24, 24, 25, 25, 28, 29]
sum = 243
avg = 24.300
median = 24.0
5 numbers in the list are divisible by 2

Test Run 2:
UNSORTED: numList = [24, 30, 21, 21, 21, 28, 21, 21, 28, 21]
SORTED:   numList = [21, 21, 21, 21, 21, 21, 24, 28, 28, 30]
sum = 236
avg = 23.600
median = 21.0
4 numbers in the list are divisible by 2

Test Run 3:
UNSORTED: numList = [21, 30, 22, 23, 28, 25, 25, 26, 23, 22]
SORTED:   numList = [21, 22, 22, 23, 23, 25, 25, 26, 28, 30]
sum = 245
avg = 24.500
median = 24.0
5 numbers in the list are divisible by 2

'''
