# p18.py
# Nikolai Petrovych
# 7/7/26
# Python 3.12.10
# Description: 
'''Write a program that displays the characters in the ASCII character table from ! to ~.
Display ten characters per line.
The characters are separated by exactly one space.'''

count = 1
for ascii in range (33, 127):
    print(chr(ascii), end = ' ')
    count += 1
    if count > 10: 
        print()
        count = 1 


'''

***PROGRAM OUTPUT***

[------]

'''