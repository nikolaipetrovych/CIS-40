# p39.py
# Nikolai Petrovych
# 7/11/26 - 7/24/26
# Python 3.12.10
# Description:
'''Write a program that asks the user to enter a sentence. Your program will:
1. Show how many words are in the sentence.
2. Show the last word of the sentence.
3. Ask the user to enter their own word, and count how many times that word
   appears in the sentence.
NOTE: you can't use the built-in python function count() to do this!

Sample Run:
Please enter a sentence: The fox and the dog
There are 5 words in the sentence you entered
The last word is 'dog'
Please enter a word to search: the
The word 'the' appears 2 times'''

sentence = input("Please enter a sentence: ")
splitsentence = sentence.lower()
splitsentence = splitsentence.split()

# count words
wordcount = 0
for word in splitsentence:
    wordcount += 1

print(f"There are {wordcount} words in the sentence you entered.")

# find last word
lastword = splitsentence[-1]
print(f"The last word in the sentence is '{lastword}'.")

# word search
while True:
    search = input("Please enter a word to search: ").lower()
    instancecount = 0
    for word in splitsentence:
        if word == search:
            instancecount += 1
    print(f"The word '{search}' appears {instancecount} time(s).")
    while True:
        keep = input("Would you like to search again (y/n)? ").lower()
        if keep != 'y' and keep != 'n':
            print("Invalid input. Enter y/n.")
        else:
            break
    if keep == 'n':
        break

'''

***PROGRAM OUTPUT***

Test Run 1 (search word appears multiple times):
Please enter a sentence: The fox and the dog
There are 5 words in the sentence you entered.
The last word in the sentence is 'dog'.
Please enter a word to search: the
The word 'the' appears 2 time(s).
Would you like to search again (y/n)? y
Please enter a word to search: Dog
The word 'dog' appears 1 time(s).
Would you like to search again (y/n)? n

Test Run 2 (search word does not appear):
Please enter a sentence: Plane and a guy
There are 4 words in the sentence you entered.
The last word in the sentence is 'guy'.
Please enter a word to search: Wow
The word 'wow' appears 0 time(s).
Would you like to search again (y/n)? n

'''
