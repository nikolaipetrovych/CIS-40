# p12.py
# Nikolai Petrovych
# 7/5/26 - 7/10/26
# Python 3.12.10
# Description: 
'''Write a program to determine if the user can vote.
The program will ask the user a series of questions - age, citizenship and registration.
The user will receive a message as to whether or not s/he may vote --
yes, no (with a reason - too young, not a citizen, hasn't registered to vote).'''


# ask all three questions

# get age
age = int(input('Please enter your age as a whole number: '))
if age < 0:
    print('Please only enter positive numbers for age.')
    quit()

# get citizenship
citizen = input('Are you a U.S. citizen (y/n)? ').lower()
if citizen != 'y' and citizen != 'n':
    print('Please only enter (y/n).')
    quit()

# get registration
reg = input('Are you currently registered to vote (y/n)? ').lower()
if reg != 'y' and reg != 'n':
    print('Please only enter (y/n).')
    quit()

# collect every reason the user can't vote
reasons = 0
if age < 18:
    print('- You must be over 18.')
    reasons += 1
if citizen != 'y':
    print('- You must be a citizen.')
    reasons += 1
if reg != 'y':
    print('- You must register to vote.')
    reasons += 1

# report the result
if reasons == 0:
    print('Congratulations! You are eligible to vote.')
else:
    print(f'Unfortunately, you are not able to vote. See the {reasons} reason(s) for that above.')



'''

***PROGRAM OUTPUT***

Test Run 1 (can vote):
Please enter your age as a whole number: 20
Are you a U.S. citizen (y/n)? y
Are you currently registered to vote (y/n)? y
Congratulations! You are eligible to vote.

Test Run 2 (too young):
Please enter your age as a whole number: 16
Are you a U.S. citizen (y/n)? y
Are you currently registered to vote (y/n)? y
- You must be over 18.
Unfortunately, you are not able to vote. See the 1 reasons for that above.

Test Run 3 (too young and not a citizen):
Please enter your age as a whole number: 16
Are you a U.S. citizen (y/n)? n
Are you currently registered to vote (y/n)? y
- You must be over 18.
- You must be a citizen.
Unfortunately, you are not able to vote. See the 2 reason(s) for that above.

Test Run 4 (too young, not a citizen, and not registered):
Please enter your age as a whole number: 16
Are you a U.S. citizen (y/n)? n
Are you currently registered to vote (y/n)? n
- You must be over 18.
- You must be a citizen.
- You must register to vote.
Unfortunately, you are not able to vote. See the 3 reason(s) for that above.

Error Test 1 (age is not an int):
Please enter your age as a whole number: 18.3
Traceback (most recent call last):
  File "*file path*", line 15, in <module>
    age = int(input('Please enter your age as a whole number: '))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '18.3'

Error Test 2 (age is neg):
Please enter your age as a whole number: -2
Please only enter positive numbers for age.

Error Test 3 (citizenship entry non y/n or Y/N):
Please enter your age as a whole number: 19
Are you a U.S. citizen (y/n)? u
Please only enter (y/n).

Error Test 4 (registration entry non y/n or Y/N):
Please enter your age as a whole number: 99
Are you a U.S. citizen (y/n)? y
Are you currently registered to vote (y/n)? 9
Please only enter (y/n).

'''