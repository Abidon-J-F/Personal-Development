""" 
This is a City Names program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def city_country(city, country):
    """Return a full name, neatly formatted."""
    city_and_country = f"{city}, {country}"
    return city_and_country.title()
       
city_names = city_country('santiago', 'chile')
print(city_names)

city_names = city_country('paris', 'france')
print(city_names)

city_names = city_country('berlin', 'germany')
print(city_names)