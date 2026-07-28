# p56.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''1) Type and run the following program (the Caesar Cipher):
2) You are given the encrypted sentence: CLGUBA VF TERNG
Using a Shift of 13, what is the original (decyphered) message?'''

# loop to show the 'original alphabet'
alphabet = ''
for i in range(65,91):
    alphabet += chr(i)

print(f"Alphabet is {alphabet}")

shift = 3
#  show the shift 'key'
print(f"The shift is {shift} letters")

#  loop to show shifted alphabet
encrypted = ""
for i in range(65,91):
    if i + shift < 91:
        encrypted += chr(i + shift)
    if i + shift >= 91:
        encrypted += chr(65 + (i + shift - 91))

#  show encrypted alphabet
print(f"Encrypted alphabet: {encrypted}")

encrypt = {}
decypher = {}
encrypt[" "] = " "
decypher[" "] = " "

for i in range (len(alphabet)):
    encrypt[alphabet[i]] = encrypted[i]
    decypher[encrypted[i]] = alphabet[i]

original_message = "HELLO WORLD"
encrypted_message = ""
for i in range(len(original_message)):
    if original_message[i] == " ":
        encrypted_message += " "
    else:
        encrypted_message += encrypt[original_message[i]]

print(f"Original sentence is {original_message}")
print(f"Encrypted sentence is {encrypted_message}")
print("... Decyphered: ", end = "")
for i in range(len(encrypted_message)):
    print(decypher[encrypted_message[i]], end = "")

#  PART 2
print()
print()
print("===== PART 2 =====")

# generate actual alphabet
alphabet = ''
for i in range(65,91):
    alphabet += chr(i)
print(f"Alphabet is {alphabet}")

#  set shift
shift = 13
print(f"The shift is {shift} letters")

# apply shift to find encrypted alphabet
encrypted = ""
for i in range(65,91):
    if i - shift >= 65:
        encrypted += chr(i - shift)
    else:
        encrypted += chr(i - shift + 26)

print(f"Encrypted alphabet: {encrypted}")

#  create an empty dict and map space character to itself
decypher = {}
decypher[" "] = " "

# map decyphered letters alphabet
for i in range (len(alphabet)):
    decypher[encrypted[i]] = alphabet[i]

original_message = ""
encrypted_message = "CLGUBA VF TERNG"
for i in range(len(encrypted_message)):
        original_message += decypher[encrypted_message[i]]

print(f"Encrypted sentence is {encrypted_message}")
print(f"... Decyphered: {original_message}")

'''

***PROGRAM OUTPUT***

Test Run:
Alphabet is ABCDEFGHIJKLMNOPQRSTUVWXYZ
The shift is 3 letters
Encrypted alphabet: DEFGHIJKLMNOPQRSTUVWXYZABC
Original sentence is HELLO WORLD
Encrypted sentence is KHOOR ZRUOG
... Decyphered: HELLO WORLD

===== PART 2 =====
Alphabet is ABCDEFGHIJKLMNOPQRSTUVWXYZ
The shift is 13 letters
Encrypted alphabet: NOPQRSTUVWXYZABCDEFGHIJKLM
Encrypted sentence is CLGUBA VF TERNG
... Decyphered: PYTHON IS GREAT

'''
