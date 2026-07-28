# p47.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''Write a program which:
1. Writes a random number (50 to 55) of numbers (0 to 100) in a file
2. Opens the file and reads the numbers from it into a list
3. Sorts the list and Shows it.
4. Calculates the median.

Note: You may NOT use the Python built in functions: sort(), sorted(), sum(),
median().'''

from random import randint


def customsort(alist):  # from p43.py, bubblesort
    sortedlist = alist
    for j in alist:
        for i in range(len(sortedlist) - 1):
            if sortedlist[i] > sortedlist[i + 1]:
                item = sortedlist[i]
                sortedlist[i] = sortedlist[i + 1]
                sortedlist[i + 1] = item
    return sortedlist


def custommedian(alist):
    if len(alist) % 2 != 0:  # when odd
        medianindex = int(len(alist) / 2)  # int() rounds down giving middle index
        median = alist[medianindex]
    else:  # when even
        medianindex1 = int(len(alist) / 2)  # get right value index
        medianindex2 = int(len(alist) / 2 - 1)  # get left value index
        median = (alist[medianindex1] + alist[medianindex2]) / 2
    return median


# generate file
numofentries = randint(50, 55)
file = open("numbers.txt", 'w')
for i in range(numofentries):
    number = randint(0, 100)
    file.write(f"{number} ")
file.close()

# turn file into list of ints
file = open("numbers.txt", 'r')
numlist = []
for x in file.read().split():
    numlist.append(int(x))
numlistsorted = customsort(numlist)
file.close()

# display results
print(f"The sorted list is {numlistsorted}")
print(f"The median of all values is {(custommedian(numlistsorted)):.1f}")

'''

***PROGRAM OUTPUT***

Test Run 1:
The sorted list is [2, 10, 11, 12, 13, 13, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 26, 27, 29, 30, 31, 33, 34, 36, 39, 42, 47, 48, 49, 51, 52, 53, 56, 56, 58, 59, 65, 65, 66, 67, 71, 78, 81, 82, 85, 85, 85, 87, 91, 94, 96, 98, 99]
The median of all values is 47.0

Test Run 2:
The sorted list is [5, 6, 7, 7, 8, 9, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 21, 28, 32, 34, 35, 36, 37, 38, 41, 44, 45, 46, 47, 50, 50, 52, 55, 55, 57, 57, 58, 59, 60, 61, 61, 62, 66, 66, 70, 78, 82, 86, 87, 88, 91, 92, 96, 99]
The median of all values is 45.0

Test Run 3:
The sorted list is [5, 7, 10, 10, 10, 12, 12, 14, 19, 19, 21, 21, 21, 22, 24, 24, 29, 29, 31, 33, 35, 36, 37, 38, 41, 44, 44, 46, 46, 47, 50, 50, 51, 54, 55, 59, 61, 62, 65, 66, 74, 77, 77, 78, 79, 82, 85, 88, 88, 98]
The median of all values is 42.5

'''
