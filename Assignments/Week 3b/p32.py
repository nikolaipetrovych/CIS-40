# p32.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write a function multAdd(a, b, c) that returns a*b + c.
Write a main() function which calls the multAdd(a, b, c) function.
Pass the three arguments (such as 1, 2, 3) from the call in main().

Function name:
def multAdd(a, b, c):

Example of calling one function from another:
def main():
    print( multAdd(1,2,3) )
main()'''


def multAdd(a, b, c): # func multAdd takes three arguments: a,b,c
    result = a*b + c # calculate a*b+c and store in 'result'
    return result # return 'result' to user

def main(): # define the main function that takes 0 arguments
    result = multAdd(1, 2, 3) # the main function will pass 1,2,3 as arguments to multAdd function
    print(f"The result of 1*2+3 is {result}.") # the function main will output the result of multAdd back as a string.

main() # call func main(). it will pass a=1, b=2, c=3 into multAdd and print out the result as a string.




'''

***PROGRAM OUTPUT***

Test Run 1 (main() -> multAdd(1,2,3) -> 5):
The result of 1*2+3 is 5.

'''
