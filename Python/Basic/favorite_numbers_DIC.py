""" 
This is a Favorite Numbers program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

person = {
    'david': [5, 9, 21],
    'james': [9],
    'mary': [21, 17, 90, 26],
    'jude': [65, 69],
    'luke': [31, 68, 34, 63, 55],
}

for name, numbers in person.items():
    print(f"\n{name.title()}'s favourite number/numbers is/are:")
    for number in numbers:
        print(f"\t{number}")