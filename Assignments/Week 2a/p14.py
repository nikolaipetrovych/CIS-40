# p14.py
# Nikolai Petrovych
# 7/5/26 - 7/10/26
# Python 3.12.10
# Description: 
'''Write a program that asks the user for day and month of a birthday.
The program then tells the Zodiac signs that will be compatible with that birthday.

Constellation   English Name	    Dates	
-Aries		    The Ram			    Mar. 21-Apr. 19	
-Taurus		    The Bull		    Apr. 20-May  20	
-Gemini		    The Twins		    May  21-Jun. 21	
-Cancer		    The Crab		    Jun. 22-Jul. 22	
-Leo		    The Lion		    Jul. 23-Aug. 22	
-Virgo		    The Virgin		    Aug. 23-Sep. 22	
-Libra		    The Balance	        Sep. 23-Oct. 23	
-Scorpio	    The Scorpion	    Oct. 24-Nov. 21	
-Sagittarius    The Archer		    Nov. 22-Dec. 21	
-Capricorn	    The Goat		    Dec. 22-Jan. 19	
-Aquarius	    The Water Bearer    Jan. 20-Feb. 18	
-Pisces		    The Fishes	        Feb. 19-Mar. 20	'''


# ask for for month
print("Please enter the month and day you were born on.")
month = int(input('Enter the number corresponding to the month you were born in: '))

#check if month the entry is valid
if month < 1 or month > 12:
    print('***ERROR: Invalid month entry***')
    quit()

# ask for day
day = int(input('Enter the day: '))

#check if the day entry is valid
if (day < 1) or (day > 31):
    print('***ERROR: Invalid day entry***')
    quit()
elif (month == 4 or month == 6 or month == 9 or month == 11) and ((day < 1) or (day > 30)):
    print('***ERROR: Invalid day entry***')
    quit()
elif month == 2 and ((day < 1) or (day > 28)):
    print('***ERROR: Invalid day entry***')
    quit()


#check zodiac sign
# aries
if ( month == 3 and day >= 21 ) or ( month == 4 and day <= 19 ):
    print("Your Zodiac Sign is a Aries")

# taurus
if ( month == 4 and day >= 20 ) or ( month == 5 and day <= 20 ):
    print("Your Zodiac Sign is a Taurus")

# gemini
if ( month == 5 and day >= 21 ) or ( month == 6 and day <= 21 ):
    print("Your Zodiac Sign is a Gemini")

# cancer
if ( month == 6 and day >= 22 ) or ( month == 7 and day <= 22 ):
    print("Your Zodiac Sign is a Cancer")

# leo
if ( month == 7 and day >= 23 ) or ( month == 8 and day <= 22 ):
    print("Your Zodiac Sign is a Leo")

# virgo
if ( month == 8 and day >= 23 ) or ( month == 9 and day <= 22 ):
    print("Your Zodiac Sign is a Virgo")

# libra
if ( month == 9 and day >= 23 ) or ( month == 10 and day <= 23 ):
    print("Your Zodiac Sign is a Libra")

# scorpio
if ( month == 10 and day >= 23 ) or ( month == 11 and day <= 21 ):
    print("Your Zodiac Sign is a Scorpio")

# sagittarius
if ( month == 11 and day >= 22 ) or ( month == 12 and day <= 21 ):
    print("Your Zodiac Sign is a Sagittarius")

# capricorn
if ( month == 12 and day >= 22 ) or ( month == 1 and day <= 19 ):
    print("Your Zodiac Sign is a Capricorn")

# aquarius
if ( month == 1 and day >= 20 ) or ( month == 2 and day <= 18 ):
    print("Your Zodiac Sign is a Aquarius")

# pisces
if ( month == 2 and day >= 19 ) or ( month == 3 and day <= 20 ):
    print("Your Zodiac Sign is a Pisces")




'''

***PROGRAM OUTPUT***

Please enter the month and day you were born on.
Enter the number corresponding to the month you were born in: 8
Enter the day: 6
Your Zodiac Sign is a Leo

Please enter the month and day you were born on.
Enter the number corresponding to the month you were born in: 13
***ERROR: Invalid month entry***

Please enter the month and day you were born on.
Enter the number corresponding to the month you were born in: 0
***ERROR: Invalid month entry***

Please enter the month and day you were born on.
Enter the number corresponding to the month you were born in: 4
Enter the day: 31
***ERROR: Invalid day entry***

'''