# p21.py
# Nikolai Petrovych
# 7/7/26
# Python 3.12.10
# Description: 
'''Which of the below gives you more money?
1) A penny which doubles it's value every day over 30 days, or
2) A million dollars
Write a program which calculates exactly how much more (or less) you can make with the penny on day 30.
A loop must be used.'''


days = 30
starting_amt = 0.01
print(f'On day 1, you will have ${starting_amt}')
running_amt = starting_amt
compare_to = 1000000

for day in range(1, days):
    running_amt *= 2 
    print(f'On day {day + 1}, you will have ${running_amt:.2f} from ${starting_amt}.')

diff = running_amt - compare_to

print('')

if diff > 0:
    print(f'On the last day, you will make ${diff:.2f} more than if you had ${compare_to} right away.')

if diff < 0:
    print(f'On the last day, you will make ${-diff:.2f} less than if you had ${compare_to} right away.')

if diff == 0:
    print(f'On the last day, you will have the same amount with a penny as if you had ${compare_to} right away.')

'''

***PROGRAM OUTPUT***

[------]

'''