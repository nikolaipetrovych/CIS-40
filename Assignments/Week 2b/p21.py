# p21.py
# Nikolai Petrovych
# 7/7/26 - 7/10/26
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

print('============================================================')

if diff > 0:
    print(f'On the last day, you will make ${diff:.2f} more than if you had ${compare_to} right away.')

if diff < 0:
    print(f'On the last day, you will make ${-diff:.2f} less than if you had ${compare_to} right away.')

if diff == 0:
    print(f'On the last day, you will have the same amount with a penny as if you had ${compare_to} right away.')

'''

***PROGRAM OUTPUT***

On day 1, you will have $0.01
On day 2, you will have $0.02 from $0.01.
On day 3, you will have $0.04 from $0.01.
On day 4, you will have $0.08 from $0.01.
On day 5, you will have $0.16 from $0.01.
On day 6, you will have $0.32 from $0.01.
On day 7, you will have $0.64 from $0.01.
On day 8, you will have $1.28 from $0.01.
On day 9, you will have $2.56 from $0.01.
On day 10, you will have $5.12 from $0.01.
On day 11, you will have $10.24 from $0.01.
On day 12, you will have $20.48 from $0.01.
On day 13, you will have $40.96 from $0.01.
On day 14, you will have $81.92 from $0.01.
On day 15, you will have $163.84 from $0.01.
On day 16, you will have $327.68 from $0.01.
On day 17, you will have $655.36 from $0.01.
On day 18, you will have $1310.72 from $0.01.
On day 19, you will have $2621.44 from $0.01.
On day 20, you will have $5242.88 from $0.01.
On day 21, you will have $10485.76 from $0.01.
On day 22, you will have $20971.52 from $0.01.
On day 23, you will have $41943.04 from $0.01.
On day 24, you will have $83886.08 from $0.01.
On day 25, you will have $167772.16 from $0.01.
On day 26, you will have $335544.32 from $0.01.
On day 27, you will have $671088.64 from $0.01.
On day 28, you will have $1342177.28 from $0.01.
On day 29, you will have $2684354.56 from $0.01.
On day 30, you will have $5368709.12 from $0.01.
============================================================
On the last day, you will make $4368709.12 more than if you had $1000000 right away.

'''