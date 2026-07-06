# p12.py
# Nikolai Petrovych
# 7/5/26
# Python 3.12.10
# Description: 
'''Write a program to determine if the user can vote.
The program will ask the user a series of questions - age, citizenship and registration.
The user will receive a message as to whether or not s/he may vote --
yes, no (with a reason - too young, not a citizen, hasn't registered to vote).'''


# ask for inputs and check eligibility

# check age
age = int(input('Please enter your age as a whole number: '))

if age >= 18:
    pass
elif age < 0:
    print('Please only enter positive numbers for age')
    quit()
elif age < 18:
    print('Unfortanately, you are too young to vote.')
    quit()

# check citizenship
citizen = input('Are you a U.S. citizen (y/n)? ').lower()

if citizen == 'y':
    pass
elif citizen == 'n':
    print('Unfortanately, you need to be a U.S. citizen to vote.')
    quit()
else:
    print('Please only enter (y/n).')
    quit()

# check registration
reg = input('Are you currently registered to vote (y/n)? ').lower()

if reg == 'y':
    pass
elif reg == 'n':
    print('Unfortanately, you need to registered to vote.')
    quit()
else:
    print('Please only enter (y/n).')
    quit()

print('Congratulations! You are eligible to vote.')


'''

***PROGRAM OUTPUT***

Test run 1 (eligible):
Please enter your age as a whole number: 18
Are you a U.S. citizen (y/n)? Y
Are you currently registered to vote (y/n)? y
Congratulations! You are eligible to vote.

Test Run 2 (too young):
Please enter your age as a whole number: 16
Unfortanately, you are too young to vote.

Test Run 3 (not a citizen):
Please enter your age as a whole number: 45
Are you a U.S. citizen (y/n)? N
Unfortanately, you need to be a U.S. citizen to vote.

Test Run 4 (not registered):
Please enter your age as a whole number: 60
Are you a U.S. citizen (y/n)? y
Are you currently registered to vote (y/n)? N
Unfortanately, you need to registered to vote.

Error Test 1 (age is not an int):
Please enter your age as a whole number: 18.3
Traceback (most recent call last):
  File "*file path*", line 15, in <module>
    age = int(input('Please enter your age as a whole number: '))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '18.3'

Error Test 2 (age is neg):
Please enter your age as a whole number: -2
Please only enter positive numbers for age

Error Test 3 (citizenship entry non y/n or Y/N):
Please enter your age as a whole number: 19
Are you a U.S. citizen (y/n)? U
Please only enter (y/n).

Error Test 4 (registration entry non y/n or Y/N):
Please enter your age as a whole number: 99
Are you a U.S. citizen (y/n)? y
Are you currently registered to vote (y/n)? 9
Please only enter (y/n).

'''