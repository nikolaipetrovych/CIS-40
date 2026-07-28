# p57.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''In a weighted alphabet, every symbol is assigned a positive real number
called a weight. A string formed from a weighted alphabet is called a weighted
string, and its weight equals the sum of the weights of its symbols. The
standard weight of each member of the 20-symbol amino acid alphabet is the
monoisotopic mass of the corresponding amino acid.
1) The mass of each possible amino acid is given in the file aa.txt.
   - Put the contents of aa.txt into a dictionary: dictionary['Letter'] = value
2) Ask the user to enter an amino acid string consisting of ONLY the letters
   shown in aa.txt.
   - if the user enters an incorrect letter, the program asks for another
     string. (The invalid letters are B, J, O, U, X, Z.)
3) Calculate the total weight of the amino acid string:
   a) use the characters of the string as keys for the dictionary from (1)
   b) sum the weights for all letters and show the total weight
Sample Input:  SKADYEK
Sample Output: 821.392'''

#  create a dictionary from file / 1)
file = open("aa.txt", 'r')
file_values = file.read().split()
dict = {}
for i in range(0,len(file_values),2): #  iterate over every letter (2 steps apart)
    dict[file_values[i]] = float(file_values[i+1]) #  assign a corresponding value to each letter
file.close()

#  input prompt and validation / 2)
while True:
    letters = input("Enter letters (no special symbols): ").upper()
    isvalid = True
    for x in letters:
        found = False
        for i in range(0, len(file_values), 2): # iterate over valid letters
            if x == file_values[i]: # check if a letter matches one in the dict
                found = True
                break
        if not found: #  invalid input
            isvalid = False
            break
    if isvalid:
        break
    print("Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)")

# calculate total weight and output result / 3)
total_weight = 0
for x in letters:
    total_weight += dict[x]

print(f"Total weight: {total_weight:.3f}")

'''

***PROGRAM OUTPUT***

Test Run (matching the sample run):
Enter letters (no special symbols): abc
Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)
Enter letters (no special symbols): ajc
Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)
Enter letters (no special symbols): aoc
Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)
Enter letters (no special symbols): auc
Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)
Enter letters (no special symbols): axc
Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)
Enter letters (no special symbols): azc
Not a valid letter. Please reenter. (Invalid letters are B, J, O, U, X, Z.)
Enter letters (no special symbols): skadyek
Total weight: 821.392

'''
