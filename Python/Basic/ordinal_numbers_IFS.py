""" 
This is an Ordinal Numbers program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 04/2022 - 05/2022
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")