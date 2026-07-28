# p25.py
# Nikolai Petrovych
# 7/10/26 - 7/17/26
# Python 3.12.10
# Description:
'''Write a program that asks the user to input a sentence.
The program will ask the user what two letters are to be counted.
You must use a "for" loop to go through the sentence & count how many times the
chosen letter appears in the sentence.
You are not allowed to use python built-in function "count()" or you'll get a Zero!
Output will show the sentence, the letter, and the number of times the letter
appears in the sentence.'''

sentence = input("Input a sentence: ")  # ask user for a sentence
sentencelow = sentence.lower()  # make a new variable to store the sentence in all lowercase (to standardize)
print("Which two letters would you like to count?")
letter1 = input("Enter 1st letter: ").lower()  # ask for letter #1 to search
letter2 = input("Enter 2nd letter: ").lower()  # ask for letter #2 to search

count1 = 0  # initial count 1
count2 = 0  # initial count 2
for i in sentencelow:  # go through every letter in the sentence
    if i == letter1:  # if letter matches letter #1, add to count 1
        count1 += 1
    if i == letter2:  # if letter matches letter #2, add to count 2
        count2 += 1

# display results of the program
print(f'The sentence was: "{sentence}"')  # use original sentence
print(f"The letter '{letter1}' appears {count1} time(s).")
print(f"The letter '{letter2}' appears {count2} time(s).")

'''

***PROGRAM OUTPUT***

Test Run 1:
Input a sentence: HELLO WORLD
Which two letters would you like to count?
Enter 1st letter: O
Enter 2nd letter: L
The sentence was: "HELLO WORLD"
The letter 'o' appears 2 time(s).
The letter 'l' appears 3 time(s).

Test Run 2:
Input a sentence: Mississippi River
Which two letters would you like to count?
Enter 1st letter: s
Enter 2nd letter: i
The sentence was: "Mississippi River"
The letter 's' appears 4 time(s).
The letter 'i' appears 5 time(s).

Error Test 1 (letter not found in sentence):
Input a sentence: Good morning
Which two letters would you like to count?
Enter 1st letter: z
Enter 2nd letter: q
The sentence was: "Good morning"
The letter 'z' appears 0 time(s).
The letter 'q' appears 0 time(s).

'''
