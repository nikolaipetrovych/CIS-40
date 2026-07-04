# p8.py
# Nikolai Petrovych
# 7/4/26
# Python 3.12.10
# Description: Multiplication Table
'''Write a program to print a multiplication table for float values  0.1, 0.2 and 0.3.'''

# set multiplication table values
n1 = 0.1
n2 = 0.2
n3 = 0.3

# output multiplication table
print(f'      {n1}    {n2}    {n3}')
print(f'{n1}   {n1*n1:.2f}   {n2*n1:.2f}   {n3*n1:.2f}')
print(f'{n2}   {n1*n2:.2f}   {n2*n2:.2f}   {n3*n2:.2f}')
print(f'{n3}   {n1*n3:.2f}   {n2*n3:.2f}   {n3*n3:.2f}')


'''

***PROGRAM OUTPUT***

      0.1    0.2    0.3
0.1   0.01   0.02   0.03
0.2   0.02   0.04   0.06
0.3   0.03   0.06   0.09

'''