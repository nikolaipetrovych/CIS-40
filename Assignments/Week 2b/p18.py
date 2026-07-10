# p18.py
# Nikolai Petrovych
# 7/7/26 - 7/10/26
# Python 3.12.10
# Description: 
'''Write a program that displays the characters in the ASCII character table from ! to ~.
Display ten characters per line.
The characters are separated by exactly one space.'''

count = 1
for ascii in range (33, 127):
    print(chr(ascii), end = ' ')
    count += 1
    if count > 10: 
        print()
        count = 1 


'''

***PROGRAM OUTPUT***

! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 

'''