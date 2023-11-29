# Instructions
# Given a “Matrix” string:

#    7ii
#    Tsx
#    h%?
#    i #
#    sM 
#    $a 
#    #t%
#    ^r!

#The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
#A grid means that you could potentially break it into rows and columns, like here:

#7	i	3
#T	s	i
#h	%	x
#i		#
#s	M	
#$	a	
##	t	%
#^	r	!

#Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
#To reproduce the grid, the matrix should be a 2D list, not a string
#To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.
#Using his technique, try to decode this matrix.
#Hints:
#Use
#● lists for storing data
#● Loops for going through the data
#● if/else statements to check the data
#● String for the output of the secret message

# matrix_string = """
#7ii
#Tsx
#h%?
#i #
#sM 
#$a 
##t%
#^r!
#"""

#rows = matrix_string.strip().split('\n')
#num_columns = max(len(row) for row in rows)
#matrix = [[' ' for _ in range(num_columns)] for _ in range(len(rows))]

#for i, row in enumerate(rows):
#    for j, char in enumerate(row):
#        matrix[i][j] = char

#decoded_message = ""
#for j in range(num_columns):
#    for i in range(len(rows)):
#        if matrix[i][j].isalpha():
#            decoded_message += matrix[i][j]
#        elif i > 0 and i < len(rows) - 1 and matrix[i][j] == ' ' and matrix[i-1][j].isalpha() and matrix[i+1][j].isalpha():
#            decoded_message += ' '

# print("Decrypted Message:")
# print(decoded_message)
