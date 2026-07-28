# p51.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''1) Create a Date class.
   1a) The class should have 3 properties (instance variables):
       - month
       - day
       - year
   1b) The class should have 2 actions (functions / methods):
       - setDate()  - allows the user to enter a date in 12/31/02 format
       - showDate() - displays the date
2) Create an instance of the Date class.
3) Test the object's setDate() and showDate() methods.
4) Submit your program code, including the test run at the bottom of your code.'''


class Date:
    def __init__(self, month, day, year):  # constructor
        self.month = month
        self.day = day
        self.year = year

    def setDate(self):
        date = input("Enter new date in MM/DD/YY format: ")
        mdy = date.split("/")  # split entry into 3 individual values: MM, DD, YY
        self.month = mdy[0]
        self.day = mdy[1]
        self.year = mdy[2]

    def showDate(self):
        print(f"Date is {self.month}/{self.day}/{self.year}")


# create instance of Date and call methods
date1 = Date("01", "01", "01")
date1.showDate()
date1.setDate()
date1.showDate()

'''

***PROGRAM OUTPUT***

Test Run:
Date is 01/01/01
Enter new date in MM/DD/YY format: 12/31/20
Date is 12/31/20

'''
