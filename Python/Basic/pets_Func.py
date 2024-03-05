""" 
This is a Pets program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')

####
#Wrong order. Order matters
#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet('harry', 'hamster')

#####
#def describe_pet(animal_type, pet_name):
#    """Display information about a pet."""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(animal_type= 'hamster', pet_name='harry')

####
#Equivalent answers
#describe_pet(animal_type= 'hamster', pet_name='harry')
#describe_pet(pet_name='harry', animal_type= 'hamster')

##
#def describe_pet(pet_name, animal_type= 'dog'):
#    """Display information about a pet."""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(pet_name='willie')

## Other animal beside dog
#describe_pet(pet_name='harry', animal_type= 'hamster')

## Equivalent function calls
#def describe_pet(pet_name, animal_type='dog'):
    
    # A dog named Willie.
#    describe_pet('willie')
#    describe_pet(pet_name='willie')

 # A hamster named Harry.
#    describe_pet('harry', 'hamster')
#    describe_pet(pet_name='harry', animal_type='hamster')
#    describe_pet(animal_type='hamster', pet_name='harry')

##Error with no arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()

#Styling tick mark