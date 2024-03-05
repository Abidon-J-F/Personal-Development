""" 
This is a Cities program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def describe_city(name, country='u.s'):
    """Display information about a city and its country."""
    print(f"{name.title()} is in {country.title()}.")

##Default country value
describe_city(name='texas')

##Default country value 2
describe_city(name='new york')

##random shirt size and message
describe_city(name='paris', country='france')
