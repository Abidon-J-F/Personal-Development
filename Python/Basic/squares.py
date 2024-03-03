""" 
This is an Squares program made in Python3.
Author: Abidon Jude Fernandes
Date: 03/2022 - 04/2022
"""

#squares = []
#for value in range(1, 11):
#        square = value ** 2
#        squares.append(square)
#print(squares)


##Temporary variable
#squares = []
#for value in range(1, 11):
#        squares.append(value**2)

#print(squares)


##List Comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)