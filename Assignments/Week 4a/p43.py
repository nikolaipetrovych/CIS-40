# p43.py
# Nikolai Petrovych
# 7/11/26 - 7/24/26
# Python 3.12.10
# Description:
'''Write a function that sorts a list.
The function returns the sorted list in ASCENDING order if parameter 'reverse'
is False, and in DESCENDING order if parameter 'reverse' is True.

    def sort(alist, reverse):

Function Call:
alist = [5,1,4,3,2]
print( sort(alist, False) )   # [1, 2, 3, 4, 5]
print( sort(alist, True) )    # [5, 4, 3, 2, 1]

Hint: use Bubble Sort inside the function.
NOTE: You are not allowed to use any built-in python functions other than
print(), input(), len(), or range().'''


def sort(alist, reverse):
    sortedlist = alist
    for j in alist:
        for i in range(len(sortedlist)-1):
            if reverse == False:
                if sortedlist[i] > sortedlist[i+1]:
                    item = sortedlist[i]
                    sortedlist[i] = sortedlist[i+1]
                    sortedlist[i+1] = item
            else:
                if sortedlist[i] < sortedlist[i+1]:
                    item = sortedlist[i]
                    sortedlist[i] = sortedlist[i+1]
                    sortedlist[i+1] = item
    return sortedlist

alist = [5,1,4,3,2]
print(sort(alist, False)) #  [1, 2, 3, 4, 5]
print(sort(alist, True)) #  [5, 4, 3, 2, 1]


'''

***PROGRAM OUTPUT***

Test Run:
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]


'''
