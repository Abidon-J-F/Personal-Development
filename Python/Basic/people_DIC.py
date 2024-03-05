""" 
This is a People program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

abidon = {   
    'first_name': 'abidon', 
    'last_name': 'fernandes', 
    'age': '23', 
    'city': 'austin',
    }

ashley = {
    'first_name': 'ashley', 
    'last_name': 'mbaso', 
    'age': '22', 
    'city': 'london',
    }

david = {   
    'first_name': 'david', 
    'last_name': 'westfield', 
    'age': '21', 
    'city': 'paris',
    }

people = [abidon, ashley, david]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age.title()}")
    print(f"\tCity: {city.title()}\n")