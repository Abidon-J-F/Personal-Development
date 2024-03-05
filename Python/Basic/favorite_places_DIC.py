""" 
This is a Favorite Places program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

favorite_places = {
    'jeff': ['gladstone park'],
    'bill': ['tower bridge', 'kew garden'],
    'jill': ['london eye', 'westminster abbey', 'chester zoo'], 
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favourite place/places is/are:")
    for place in places:
        print(f"\t{place.title()}")