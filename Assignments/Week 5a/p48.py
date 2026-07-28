# p48.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''Write a program which reads the data from the file sunspots.txt and computes
the average for each year, writing them one per line to a file averages.txt.

Submit both files: averages.txt and p48.py

HINT:
    # Open the File to Read
    myFile = open('sunspots.txt', 'r')
    # Read the data from file into a list
    listOfLines = myFile.read().splitlines()
    # Each list item is a new line from the file
    listItem = listOfLines[0].split() # split each line by spaces
    print(listItem) # ['1945','18.5','11.8',...,'28.4']
    # Convert each of the strings to float in order to do math with them!'''

sunspots = open("sunspots.txt", 'r')
averages = open("averages.txt", 'w')
sunspots_lines = sunspots.read().splitlines() #  make a list of lines

averages.write("Year   Avg\n")
for line in sunspots_lines:
    values = line.split() #  create a list of individual entries of a line
    year = int(values[0]) #  record first value in the line as a list
    total_sunspots = 0
    for i in range(1,len(values)): #  go over every value except first (year)
        total_sunspots += float(values[i])
    average = total_sunspots / (len(values) - 1)
    averages.write(f"{year}   ")
    averages.write(f"{average:.2f}\n")

sunspots.close()
averages.close()

'''

***PROGRAM OUTPUT***

Test Run:
*pasted from averages.txt*:
Year   Avg
1945   32.29
1946   99.88
1947   170.93
1948   166.61
1949   174.08
1950   103.70
1951   64.42
1952   30.53
1953   12.46
1954   3.36
1955   34.59
1956   125.92
1957   168.32
1958   172.12
1959   144.99
1960   102.11
1961   44.68
1962   29.81
1963   22.17
1964   7.44
1965   12.07
1966   38.66
1967   86.25
1968   97.49
1969   104.59
1970   107.38
1971   66.48
1972   67.33
1973   36.69
1974   32.34
1975   14.40
1976   11.58
1977   26.01
1978   86.90
1979   145.80
1980   149.07
1981   146.48
1982   115.14
1983   64.63
1984   43.60
1985   16.15
1986   11.08
1987   28.84
1988   100.67
1989   162.39
1990   144.89
1991   144.39
1992   93.72
1993   54.70
1994   30.98
1995   18.27
1996   8.40
1997   20.27
1998   61.58
1999   95.98
2000   123.33
2001   123.24
2002   109.47
2003   65.76
2004   43.32
2005   31.03
2006   15.33
2007   8.67
2008   2.42


'''
