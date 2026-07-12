# p40.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Ask the user to enter X numbers into a list. Calculate and show the sum,
average, min, and max of those numbers.
NOTE: You are not allowed to use any pre-existing python functions such as
sample(), sum(), min(), max(), average(), sort(), sorted()!!! ...unless you
write them yourself.

Hints:
- Ask how many numbers, then loop that many times appending each input to a list.
- Smallest: set smallest = list[0], loop the rest; if any value < smallest,
  smallest = that value. (Largest is the mirror image.)
- Sum: total = 0, loop adding each element. Average = total / len(list).

Sample Run:
How many numbers would you like to enter? 11
Enter number  1: 26
...
List:  [ 26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34 ]
Sum = 377
Average = 377 / 11 = 34.3
Smallest = 20
Largest = 49'''


x = int(input("How many numbers would you like to enter? "))

xlist = []
xsum = 0
for num in range(x):
    entry = float(input(f"Enter number {num + 1}: "))
    xlist.append(entry)
    xsum += entry

xavg = xsum/x
xmin = xlist[0]
xmax = xlist[0]
for num in xlist:
    if num < xmin:
        xmin = num
    elif num > xmax:
        xmax = num
        
# print(x, xlist, xsum, xavg, xmin, xmax)

print(f"List: {xlist}")
print(f"Sum = {xsum}")
print(f"Average = {xsum} / {x} = {xavg}")
print(f"Smallest = {xmin}")
print(f"Largest = {xmax}")

    
'''

***PROGRAM OUTPUT***

Test Run 1 (several numbers, mixed values):


Test Run 2 (different count / values):


'''
