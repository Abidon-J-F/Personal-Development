""" 
This is a Stages of Lifes program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 04/2022 - 05/2022
"""

age = 23

if age < 2:
    print("The person is a baby")
elif age == 2 or age < 4:
    print("The person is a toddler")
elif age == 4 or age < 13:
    print("The person is a kid")
elif age == 13 or age < 20:
    print("The person is a teenager")
elif age == 20 or age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")