""" 
This is a Movie Tickets program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

age = input("How old are you? ")
age = int(age)

while True:
    
    if age < 3:
        print("\nThe ticket is free!")
        break
    if age >= 3 <= 12:
        print("\nThe ticket is $10.")
        break
    if age > 12:
        print("\nThe ticket is $15.")
        break
    else:
        print("\nError")
        break