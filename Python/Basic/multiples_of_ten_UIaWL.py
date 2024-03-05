""" 
This is a Multiples of Ten program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

number = input("Enter a number, and I'll tell you if it's a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of ten")