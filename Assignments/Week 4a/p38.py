# p38.py
# Nikolai Petrovych
# 7/11/26
# Python 3.12.10
# Description:
'''Write a program that asks the user to enter a sentence.
The program then finds the longest word in the sentence and shows it.
NOTE: The use of python functions max() and sorted() is NOT permitted!'''


sentence = input("Please enter a sentence: ")
splitsentence = sentence.split()


lettercount_max = 0
for word in splitsentence:
    lettercount = 0
    for letter in word:
        lettercount += 1
    if lettercount > lettercount_max:
        lettercount_max = lettercount
        longestword = word
        
print(f"The longest word in '{sentence}' is *{longestword}*, and has *{lettercount_max}* letters.")

'''

***PROGRAM OUTPUT***

Test Run 1 (clear single longest word):
Please enter a sentence: thisisareallylongword and this is much shorter
The longest word in 'thisisareallylongword and this is much shorter' is *thisisareallylongword*, and has *21* letters.

Test Run 2 (different sentence):
Please enter a sentence: Does this program work?
The longest word in 'Does this program work?' is *program*, and has *7* letters.

'''
