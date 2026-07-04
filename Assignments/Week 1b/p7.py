# p7.py
# Nikolai Petrovych
# 7/4/26
# Python 3.12.10
# Description: Circumference & Area of a Circle
'''Write a program to compute the circumference and area of a circle.
The user will input the radius of a circle.
Validate Input: Make sure that the radius is positive, or give an error message.
The program will show the circumference and area of a circle with that radius.
The answers should be rounded to the nearest tenth.'''


# ask for input (radius)
q = input("Would you like to enter radius or diameter (r/d)? ")
if q == 'r':
    rad = float(input('What is the radius (in inches) of the circle you want to draw?: '))
elif q == 'd':
    rad = float(input('What is the diameter (in inches) of the circle you want to draw?: ')) / 2
else:
    print('Input has to be either \'r\' or \'d\'')
    quit()

if rad <= 0: #check if radius is positive
    print('Radius/diameter value has to be greater than 0')
    quit()
else: # calculate area and circumference
    area = 3.1415*(rad**2)
    circumference = 2*3.1415*rad

# display results
print(f'A circle with radius {rad} inches has a circumference of {circumference:.1f} inches and an area of {area:.1f} sq. inches.')


'''

***PROGRAM OUTPUT***

Run 1 (radius):
Would you like to enter radius or diameter (r/d)? r
What is the radius (in inches) of the circle you want to draw?: 12.0
A circle with radius 12.0 inches has a circumference of 75.4 inches and an area of 452.4 sq. inches.

Run 1 (diameter):
Would you like to enter radius or diameter (r/d)? d
What is the diameter (in inches) of the circle you want to draw?: 24.001
A circle with radius 12.0005 inches has a circumference of 75.4 inches and an area of 452.4 sq. inches.

Error test 1 (rad <= 0):
Would you like to enter radius or diameter (r/d)? r
What is the radius (in inches) of the circle you want to draw?: -1.5
Radius/diameter value has to be greater than 0

Error test 2 (user input is not (r/d)):
Would you like to enter radius or diameter (r/d)? R
Input has to be either 'r' or 'd'

'''