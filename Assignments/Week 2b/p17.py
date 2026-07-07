# p17.py
# Nikolai Petrovych
# 7/7/26
# Python 3.12.10
# Description: 
'''Suppose that the tuition for a university is $10,000 this year and increases 5% every year.
Write a program that computes the tuition in ten years and displays a table of the years and tuition costs.
A loop must be used.'''


tuition = 10000 # initial tuition

for year in range (1,11):
    print(f'Year {year}:   ${tuition:.0f}')
    tuition *= 1.05


'''

***PROGRAM OUTPUT***

[------]

'''