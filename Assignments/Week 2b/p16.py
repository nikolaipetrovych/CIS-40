# p16.py
# Nikolai Petrovych
# 7/7/26
# Python 3.12.10
# Description: 
'''Program which uses a while loop to display a conversion table,
with kilograms on the left and pounds on the right.
Pounds are rounded to 1 decimal digit.
1 kg = 2.2 lb
Include every other (odd) values of kilograms, from 1 to 199.'''


print('Kilograms:   Pounds:')

kg = 1

while kg < 200:
    lb = kg*2.2
    print(f'{kg}            {lb:.2f}')
    kg += 2


'''

***PROGRAM OUTPUT***

[------]

'''