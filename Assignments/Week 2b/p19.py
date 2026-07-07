# p19.py
# Nikolai Petrovych
# 7/7/26
# Python 3.12.10
# Description: 
'''Write a program which asks the user for an integer  X.
The program then outputs the values from 1  to 1000 as X numbers per line,
where X is the value that the user entered.
You must use only 1 loop to display the numbers from 1 to 1000.
You may use a separate validation loop to make sure X is between 10 and 30.
Validate X to make sure that the numbers per line value is between (10 to 30).
Sample Run:
How many numbers per line would you like? 120
Numbers per line must be b/w 10-30: 12
Showing values 1 - 1000, as 12 numbers per line:'''

x = int(input('How many numbers per line would you like? (enter a whole number): '))
while  x < 10 or x > 30:
    print
    x = int(input('Numbers per line must be between 10-30, please enter a different number: '))

count = 1
for i in range (1, 1001):
    print(i, end = ' ')
    count += 1
    if count > x:
        print()
        count = 1


'''

***PROGRAM OUTPUT***

[------]

'''