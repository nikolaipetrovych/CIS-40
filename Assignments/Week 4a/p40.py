# p40.py
# Nikolai Petrovych
# 7/11/26 - 7/24/26
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
    entry = int(input(f"Enter number {num + 1}: "))
    xlist.append(entry)
    xsum += entry

xavg = xsum / x
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
print(f"Average = {xsum} / {x} = {xavg:.1f}")
print(f"Smallest = {xmin}")
print(f"Largest = {xmax}")


'''

***PROGRAM OUTPUT***

Test Run 1 (several numbers, mixed values):
How many numbers would you like to enter? 11
Enter number 1: 26
Enter number 2: 23
Enter number 3: 48
Enter number 4: 32
Enter number 5: 44
Enter number 6: 21
Enter number 7: 32
Enter number 8: 20
Enter number 9: 49
Enter number 10: 48
Enter number 11: 34
List: [26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34]
Sum = 377
Average = 377 / 11 = 34.3
Smallest = 20
Largest = 49

Test Run 2 (different count / values):
How many numbers would you like to enter? 5
Enter number 1: 7
Enter number 2: 3
Enter number 3: 15
Enter number 4: 9
Enter number 5: 1
List: [7, 3, 15, 9, 1]
Sum = 35
Average = 35 / 5 = 7.0
Smallest = 1
Largest = 15

'''
