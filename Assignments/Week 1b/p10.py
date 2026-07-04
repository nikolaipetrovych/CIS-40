# p10.py
# Nikolai Petrovych
# 7/4/26
# Python 3.12.10
# Description: Program 10 - Letter Grades with Input Validation
'''Write a program which asks the user for a student's grade as a percent, and then returns their letter grade.
Validate the input to make sure that the number is between 0 - 100 . If for any other number, say "ERROR" and ask for another number)
A is 90% or above
B is between 80% and 90%
C is between 70% and 80%
D is between 60% and 70%
F is under 60%'''


# ask for percent grade
percentage = float(input("Please enter your grade as a percent (only the number): "))

# validate the input and determine grade
if percentage < 0 or percentage > 100:
    print('ERROR: Please enter a value between 0 and 100')
    quit()
elif percentage >= 90:
    grade = "A"
elif 80 <= percentage < 90:
    grade = "B"
elif 70 <= percentage < 80:
    grade = "C"
elif 60 <= percentage < 70:
    grade = "D"
elif percentage < 60:
    grade = "F"

# outpput letter grade
print(f'Your grade is \'{grade}\'')

'''

***PROGRAM OUTPUT***

Run 1 (A):
Please enter your grade as a percent (only the number): 100
Your grade is 'A'

Run 2 (B):
Please enter your grade as a percent (only the number): 89.9
Your grade is 'B'

Run 3 (C):
Please enter your grade as a percent (only the number): 70
Your grade is 'C'

Run 4 (D)
Please enter your grade as a percent (only the number): 65.00000000000001
Your grade is 'D'

Run 5 (F):
Please enter your grade as a percent (only the number): 0
Your grade is 'F'

Error test 1 (percentage > 100)
Please enter your grade as a percent (only the number): 102
ERROR: Please enter a value between 0 and 100

Error test 2 (percentage < 0)
Please enter your grade as a percent (only the number): -5.2
ERROR: Please enter a value between 0 and 100

Error test 3 (input is not a float):
Please enter your grade as a percent (only the number): hello
Traceback (most recent call last):
  File "[*file_path*]", line 16, in <module>
    percentage = float(input("Please enter your grade as a percent (only the number): "))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'hello'

'''