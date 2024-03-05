""" 
This is a Pets program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

dogs = {   
    'breed': 'german shepherd', 
    'owner': 'jeff', 
    }

cats = {
    'breed': 'maine coon', 
    'owner': 'jenna', 
    }

hamsters = {   
    'breed': 'campbell\'s dwarf hamster', 
    'owner': 'kyle', 
    }

pets = [dogs, cats, hamsters]

for pet in pets:
    pet_breed = f"{pet['breed']}"
    owner = pet['owner']

    print(f"\tPet breed: {pet_breed.title()}")
    print(f"\tOwner: {owner.title()}\n")
