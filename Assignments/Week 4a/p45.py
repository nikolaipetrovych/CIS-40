# p45.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''EXTRA CREDIT.
Write a program that calculates and shows all prime numbers between 3 and 100.
A prime number can only be evenly (remainder 0) divided by itself and 1.'''


primes = []
for i in range(3,101):
    for k in range(2,i):
        if i % k == 0:
            isprime = False
            break
        else:
            isprime = True
    if isprime:
        primes.append(i)

print(primes)
print(f"There are {len(primes)} prime numbers between 3 and 100")


'''

***PROGRAM OUTPUT***

Test Run 1 (all primes from 3 to 100):
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
There are 24 prime numbers between 3 and 100

'''
