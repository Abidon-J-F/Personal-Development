""" 
This is a Rivers program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states of america',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river_keys in rivers.keys():
    print(river_keys.title())

for river_values in rivers.values():
    print(river_values.title())
