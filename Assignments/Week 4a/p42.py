# p42.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write the below 5 functions according to the following requirements:
1. sum(list_parameter)     : returns the sum of the numbers inside a list
2. average(list_parameter) : returns the average of the numbers inside a list
3. min(list_parameter)     : returns the smallest of all numbers inside a list
4. max(list_parameter)     : returns the largest of all numbers inside a list
5. main()                  : calls all the other functions above

You must write these yourself (do not use built-in sum/min/max, etc.).
Remember to call main() at the bottom so the other functions run.'''


def sum(list_parameter):
    sum = 0
    for num in list_parameter:
        sum += num
    return sum
    
def average(list_parameter):
    sum = 0
    for num in list_parameter:
        sum += num
    average = sum / len(list_parameter)
    return average
    
def min(list_parameter):
    min = list_parameter[0]
    for num in list_parameter:
        if num < min:
            min = num
    return min
    
def max(list_parameter):
    max = list_parameter[0]
    for num in list_parameter:
        if num < max:
            max = num
    return max
    
def main():
    mylist = [1,2,3,4,5,6,7,8,9,10]
    print(f"{sum(mylist)}, {average(mylist)}, {min(mylist)}, {max(mylist)}")

main()
    


'''

***PROGRAM OUTPUT***

Test Run 1 (main() prints sum, average, min, max of a list):


'''
