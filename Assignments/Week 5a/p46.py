# p46.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''Write a Python program to do the following:
1. Let the user enter a file name (such as "myMovies.txt").
2. Let the user enter the titles of 4 of their favorite movies using a loop.
3. Write using a loop the 4 movie titles to a file, one per line, and closes
   the file.
4. Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them
   in a list, and then shows the list.
5. Write the titles in reverse order into a file "reverseOrder.txt"
Sample Run:
Please enter a file name: myMovies.txt
Please enter a movie title #1: movie1
Please enter a movie title #2: movie2
Please enter a movie title #3: movie3
Please enter a movie title #4: movie4
... Writing the 4 movie titles to file 'myMovies.txt'
... Reading the 4 movie titles from file into a list: [movie1, movie2, movie3, movie4]
... Writing the 4 movie titles in revers to 'reverseOrder.txt'
Content of myMovies.txt:
movie1
movie2
movie3
movie4
Content of reverseOrder.txt:
movie4
movie3
movie2
movie1'''

#  get name of file
filenameuser = input("Please enter a file name: ")
filename = filenameuser + ".txt"

#  get movie names and append them into a list
movies = []
for i in range(4):
    movies.append(input(f"Please enter a movie title #{i + 1}: "))

#  write movies to new file
print(f"... Writing the 4 movie titles to file '{filename}'")
file = open(filename, 'w')
for x in movies:  # ruff:ignore[for-loop-writes]
    file.write(f"{x}\n")
file.close()

#  read movies from file back into list
print("... Reading the 4 movie titles from file into a list")
file = open(filename, 'r')
movielistnew = file.read().splitlines()
file.close()

#  create a reverse file and write movies in reverse order
print("... Writing the 4 movie titles in reverse to 'reverseOrder.txt'")
reversefile = open("reverseOrder.txt", 'w')
for i in range(len(movielistnew) - 1, -1, -1):
    reversefile.write(f"{movielistnew[i]}\n")
reversefile.close()
print(f"List created: {movielistnew}")

#  display content
file = open(filename, 'r')
reversefile = open("reverseOrder.txt", 'r')
print(f"Content of {filename}:")
print(file.read())
print("Content of reverseOrder.txt:")
print(reversefile.read())
file.close()
reversefile.close()

'''

***PROGRAM OUTPUT***

Test Run:
Please enter a file name: myMovies
Please enter a movie title #1: movie1
Please enter a movie title #2: movie2
Please enter a movie title #3: movie3
Please enter a movie title #4: movie4
... Writing the 4 movie titles to file 'myMovies.txt'
... Reading the 4 movie titles from file into a list
... Writing the 4 movie titles in reverse to 'reverseOrder.txt'
List created: ['movie1', 'movie2', 'movie3', 'movie4']
Content of myMovies.txt:
movie1
movie2
movie3
movie4

Content of reverseOrder.txt:
movie4
movie3
movie2
movie1


'''
