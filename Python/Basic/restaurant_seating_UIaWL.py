""" 
This is a Restaurant Seating program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

seating = input("How many people are in their dinner group?: ")
seating =int(seating)

if seating > 8:
    print("\nThey'll have to wait for a table.")
else:
    print("\nTheir table is ready.")