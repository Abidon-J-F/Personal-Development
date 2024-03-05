""" 
This is an Even or Odd program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd")