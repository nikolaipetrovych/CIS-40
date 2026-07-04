# p9.py
# Nikolai Petrovych
# 7/4/26
# Python 3.12.10
# Description: Program 9 - User Height Message
'''Write a program to compute a person's height and print out a message.
The user will input their height in feet and inches.
The program will convert the feet and inches into total_inches, and then print a message.
If the total inches is greater than 72, the message should be something like, "You're tall."
If the total inches is between 5' and 6', a different message should appear, like "You are average"
If the total inches is less than 60, another message should appear, like "You are vertically challenged"'''

#from p6.py
print('Please only enter WHOLE numbers')
feet = int(input('Please enter the number of feet: '))
inches = int(input('Please enter the number of inches: '))

# check that feet and inches are positive

if feet < 0 or inches < 0:
    print('Please enter positive numbers for feet and inches')
    exit()
elif inches > 12:
    print('Inches values cannot exceed 12')
    exit()

# calculate total inches
total_inches = feet*12 + inches

# output total inches to user
print(f'{feet} feet and {inches} inch(es) is {total_inches} inches')

#end from p6.py / start new code

if total_inches > 72: # tall message
    print('Wow! You are tall :)')

elif 5*12 < total_inches < 6*12: # average message
    print('Your height is average')

elif total_inches < 60: # short message
    print('Your height is less than 5 feet :(')


'''

***PROGRAM OUTPUT***

Run 1 (tall):
Please only enter WHOLE numbers
Please enter the number of feet: 6
Please enter the number of inches: 5
6 feet and 5 inch(es) is 77 inches
Wow! You are tall :)

Run 2 (average):
Please only enter WHOLE numbers
Please enter the number of feet: 5 
Please enter the number of inches: 11
5 feet and 11 inch(es) is 71 inches
Your height is average

Run 3 (short):
Please only enter WHOLE numbers
Please enter the number of feet: 4 
Please enter the number of inches: 11
4 feet and 11 inch(es) is 59 inches
Your height is less than 5 feet :(

'''