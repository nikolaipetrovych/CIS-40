# p44.py
# Nikolai Petrovych
# 7/11/26 - 7/24/26
# Python 3.12.10
# Description:
'''EXTRA CREDIT.
You have 1000 lockers and 1000 students. All lockers are initially locked.
- 1st student opens all lockers.
- 2nd student closes every other locker.
- 3rd student toggles (opens if closed, closes if open) every 3rd locker.
- 4th student toggles every 4th locker.
- ... 1000th student toggles every 1000th locker.
Write a program to determine which exact locker numbers are open, and the total
number that are open.
NOTE: You are not allowed to use Python function count()!!'''

lockers = []
for i in range(1000):
    lockers.append(True)

for student in range(2, 1001):
    for i in range(student - 1, 1000, student):
        if lockers[i]:
            lockers[i] = False
        else:
            lockers[i] = True

openlockers = []
for i in range(1000):
    if lockers[i]:
        openlockers.append(i + 1)
print(openlockers)  # locker numbers that are open

# count
totalopen = 0
for i in lockers:
    if i:
        totalopen += 1
print(f"{totalopen} total lockers are open.")

'''

***PROGRAM OUTPUT***

Test Run 1 (open locker numbers are the perfect squares 1..961, total open = 31):
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]
31 total lockers are open.


'''
