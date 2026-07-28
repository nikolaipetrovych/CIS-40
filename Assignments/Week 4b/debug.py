# debug.py
# Nikolai Petrovych
# 7/26/26 - 7/27/26
# Python 3.12.10
# Description:
''' Debug the program below so that it works as shown in the test run.
num = input ("Please enter a number: ")
def  isEven( ): # should have a parameter
  if  num%2 = 0
     retrn True:
  else (num%2 != 0):
     return False

def  main(): # needs to be called first
   print ("The number %i is even: %s" , (num; iseven(num))
main

Test Run:
Enter a number: 5
The number 5 is even: False'''


def isEven(value):
    return (value % 2) == 0  # check if even


def main():
    num = int(input("Enter a number: "))  # get number
    print(f"The number {num} is even: {isEven(num)}")  # output


main()

'''

***PROGRAM OUTPUT***

Test Run 1 (odd):
Enter a number: 5
The number 5 is even: False

Test Run 2 (even):
Enter a number: 6
The number 6 is even: True

'''
