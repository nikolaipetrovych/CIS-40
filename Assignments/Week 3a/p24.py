# p24.py
# Nikolai Petrovych
# 7/10/26
# Python 3.12.10
# Description:
'''Write a program that generates X random integers Num.
Num is a random number between 20 to 50.
X is a random number between 10 to 15.
Calculate and show the Smallest, Largest, Sum, and Average of those numbers.
You are not allowed to use Python functions sample(), min(), max(), average(),
sort(), sorted()!!'''


import random

x = random.randint(10,15)
lower = 20
upper = 50
list1 = []
smallest = upper
largest = lower
sumall = 0
for i in range(x):
    num = random.randint(lower,upper)
    list1.append(num)
    if list1[i] > largest:
        largest = list1[i]
    if list1[i] < smallest:
        smallest = list1[i]
    sumall += num
        
average = sumall / x
print(f"List is {list1}. The length of the list is {len(list1)}.")
print(f"Smallest is {smallest}, Largest is {largest}, Sum is {sumall}, Average is {average:.4f}")


'''

***PROGRAM OUTPUT***

Test Run 1:
List is [27, 27, 40, 35, 45, 47, 36, 37, 47, 22, 21, 46, 26, 33, 21]. The length of the list is 15.
Smallest is 21, Largest is 47, Sum is 510, Average is 34.0000

Test Run 2:
List is [33, 45, 50, 45, 35, 32, 28, 32, 21, 50, 36]. The length of the list is 11.
Smallest is 21, Largest is 50, Sum is 407, Average is 37.0000

Test Run 3:
List is [20, 38, 30, 21, 23, 20, 41, 45, 45, 42, 49]. The length of the list is 11.
Smallest is 20, Largest is 49, Sum is 374, Average is 34.0000

'''
