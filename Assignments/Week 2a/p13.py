# p13.py
# Nikolai Petrovych
# 7/5/26
# Python 3.12.10
# Description: 
'''Write a program to convert any given number of total cents (under 100)
into the correct number of: quarters, dimes, nickels, pennies.'''

# ask for total cents
total = int(input('Enter the total amount of cents (whole number): '))
running_total = total

# check if total is <100
if total >= 100:
    print('Total amount of cents needs to be under 100.')
    total = int(input('Reenter the total amount of cents (whole number): '))
    if total >= 100:
        print('Total amount of cents needs to be under 100. Restart the program.')
    quit()

# calculate quarters
quarters = int(running_total/25)
running_total -= quarters*25 # update total count

# calculate dimes
dimes = int(running_total/10)
running_total -= dimes*10 # update total count

# calculate nickels
nickels = int(running_total/5)
running_total -= nickels*5 # update total count

# calculate pennies
pennies = running_total
running_total -= pennies
# display result
print(f'Change is {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.')

# # check result (uncomment)
# print(running_total)

# total_check = 25*quarters + 10*dimes + 5*nickels + pennies
# print(total_check)

'''

***PROGRAM OUTPUT***

Test Run 1 (under 100):
Enter the total amount of cents (whole number): 75
Change is 3 quarters, 0 dimes, 0 nickels, and 0 pennies.

Test Run 2 (over 100, reenter under 100):
Enter the total amount of cents (whole number): 104
Total amount of cents needs to be under 100.
Reenter the total amount of cents (whole number): 99
Change is 4 quarters, 0 dimes, 0 nickels, and 4 pennies.

Error Test 1 (input is not an int):
Enter the total amount of cents (whole number): abc
Traceback (most recent call last):
  File "file path", line 10, in <module>
    total = int(input('Enter the total amount of cents (whole number): '))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'abc'

Error Test 2 (amount is over 100 twice):
Enter the total amount of cents (whole number): 105
Total amount of cents needs to be under 100.
Reenter the total amount of cents (whole number): 800
Total amount of cents needs to be under 100. Restart the program.

'''