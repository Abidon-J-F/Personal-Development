""" 
This is a Cities program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

cities ={
    'austin':{
        'country': 'usa',
        'population': '950,807',
        'fact': 'austin is home to the last remaining moonlight towers',
    },

    'london':{
        'country': 'uk',
        'population': '8.982 million',
        'fact': 'london is the smallest city in england',
    },

    'paris':{
        'country': 'france',
        'population': '2.161 million',
        'fact': 'you can visit an old guillotine spot',
    }
}

for city, city_info in cities.items():
    print(f"\nCity name: {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")