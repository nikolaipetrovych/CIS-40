# shapes.py
# Nikolai Petrovych
# 7/26/26 - 7/27/26
# Python 3.12.10
# Description:
'''A quadrilateral is a shape with 4 sides and 4 angles.
Write a program that lets the user enter 4 sides and 4 angles into LISTS.
The program checks if the type of quadrilateral is either: 
- Rhombus
- Square
- Rectangle
1)  Input, Validation, Repetition (30 pts) :
 a) The user enters 4 sides into a LIST of type float. (5pts)
 b) The user enters 4 angles into a LIST of type float. (5pts)
 c) The program validates that all 8 numbers are positive. (10pts)
 e) The program can repeat if user choses to. (10pts)
2)  Use the LISTS to identify the Type of Quadrilateral (30 pts) :
 a) Rhombus (all 3 must be true) (10 pts): 
  1. All four sides have the same length. 
  2. Angle 1 equals Angle 3 
  3. Angle 2 equals Angle 4 
 b) Square (both must be true) (10 pts):
  1. All four sides have the same length.
  2. All angles are equal to each other
 c) Rectangle (all 3 must be true) (10 pts):
  1. Side 1 equals Side 3
  2. Side 2 equals Side 4
  3. All angles are equal to each other'''


def allequal(list):
    x0 = list[0]
    for x in list: #  checks if every entry is equal to the first
        if not x == x0:
            return False
    return True

def rhombus(s, a): #  2a
    if allequal(s) and a[0] == a[2] and a[1] == a[3]:
        return True
    return False


def square(s, a): #  2b
    if allequal(s) and allequal(a):
        return True
    return False


def rect(s, a): #  2c
    if allequal(a) and s[0] == s[2] and s[1] == s[3]:
        return True
    return False


def checkall(s, a): #  call functions and output
    print()
    print("=======================")
    print(f"Shape is a rhombus: {rhombus(s, a)}")
    print(f"Shape is a square: {square(s, a)}")
    print(f"Shape is a rectangle: {rect(s, a)}")



while True: #  main loop/1d
    print("=== Please enter Sides ===") #  1a
    sides = []
    for i in range(4):
        while True:
            side = float(input(f"Enter side {i+1}: "))
            if side > 0: #  1c.1
                break
            else:
                print("Side values must be positive. Please reenter.")
        sides.append(side)

    print()
    print("=== Please enter Angles ===") #  1b
    angles = []
    for i in range(4):
        while True:
            angle = float(input(f"Enter angle {i+1}: "))
            if angle > 0: #  1c.2
                break
            else:
                print("Angle values must be positive. Please reenter.")
        angles.append(angle)

    checkall(sides, angles)
    
    while True:  
        repeat = input("Would you like to repeat? (1-Yes, 2-No): ") #  1d
        if repeat == "1" or repeat == "2":
            break
        else:
            print("Enter only 1 or 2.")
    
    if repeat == "2":
        break


'''

***PROGRAM OUTPUT***

Test Run 1 (matching the sample run: square, rhombus, rectangle):
=== Please enter Sides ===
Enter side 1: -1
Side values must be positive. Please reenter.
Enter side 1: 1
Enter side 2: 1
Enter side 3: -1
Side values must be positive. Please reenter.
Enter side 3: 1
Enter side 4: 1

=== Please enter Angles ===
Enter angle 1: -1
Angle values must be positive. Please reenter.
Enter angle 1: 90
Enter angle 2: 90
Enter angle 3: -1
Angle values must be positive. Please reenter.
Enter angle 3: 90
Enter angle 4: 90

=======================
Shape is a rhombus: True
Shape is a square: True
Shape is a rectangle: True
Would you like to repeat? (1-Yes, 2-No): 1
=== Please enter Sides ===
Enter side 1: 1
Enter side 2: 1
Enter side 3: 1
Enter side 4: 1

=== Please enter Angles ===
Enter angle 1: 120
Enter angle 2: 60
Enter angle 3: 120
Enter angle 4: 60

=======================
Shape is a rhombus: True
Shape is a square: False
Shape is a rectangle: False
Would you like to repeat? (1-Yes, 2-No): 1
=== Please enter Sides ===
Enter side 1: 10
Enter side 2: 20
Enter side 3: 10
Enter side 4: 20

=== Please enter Angles ===
Enter angle 1: 90
Enter angle 2: 90
Enter angle 3: 90
Enter angle 4: 90

=======================
Shape is a rhombus: False
Shape is a square: False
Shape is a rectangle: True
Would you like to repeat? (1-Yes, 2-No): 2


Test Run 2 (additional side/angle validation, zero entry, decimal values, shape is none of the three, invalid repeat choices):
=== Please enter Sides ===
Enter side 1: 0
Side values must be positive. Please reenter.
Enter side 1: 2.5
Enter side 2: -3
Side values must be positive. Please reenter.
Enter side 2: 0
Side values must be positive. Please reenter.
Enter side 2: 4.5
Enter side 3: 2.5
Enter side 4: -0.5
Side values must be positive. Please reenter.
Enter side 4: 4.5

=== Please enter Angles ===
Enter angle 1: 100
Enter angle 2: 0
Angle values must be positive. Please reenter.
Enter angle 2: 80
Enter angle 3: 100
Enter angle 4: -80
Angle values must be positive. Please reenter.
Enter angle 4: 80

=======================
Shape is a rhombus: False
Shape is a square: False
Shape is a rectangle: False
Would you like to repeat? (1-Yes, 2-No): y
Enter only 1 or 2.
Would you like to repeat? (1-Yes, 2-No): 0
Enter only 1 or 2.
Would you like to repeat? (1-Yes, 2-No): 1
=== Please enter Sides ===
Enter side 1: 3.5
Enter side 2: 3.5
Enter side 3: 3.5
Enter side 4: 3.5

=== Please enter Angles ===
Enter angle 1: 110.5
Enter angle 2: 69.5
Enter angle 3: 110.5
Enter angle 4: 69.5

=======================
Shape is a rhombus: True
Shape is a square: False
Shape is a rectangle: False
Would you like to repeat? (1-Yes, 2-No): 1
=== Please enter Sides ===
Enter side 1: 6
Enter side 2: 4
Enter side 3: 6
Enter side 4: 4

=== Please enter Angles ===
Enter angle 1: 90
Enter angle 2: 90
Enter angle 3: 90
Enter angle 4: 89

=======================
Shape is a rhombus: False
Shape is a square: False
Shape is a rectangle: False
Would you like to repeat? (1-Yes, 2-No): 3
Enter only 1 or 2.
Would you like to repeat? (1-Yes, 2-No): 2

'''
