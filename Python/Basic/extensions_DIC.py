""" 
This is an Extensions program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

#Extensions
alien_1 = {
    'race': 'alien',   
    'color': 'green', 
    'points': 5, 
    'speed': 'slow', 
    }

alien_2 = {
    'race': 'predator',
    'color': 'yellow', 
    'points': 10, 
    'speed': 'medium',
    }

alien_3 = { 
    'race': 'necromorph',  
    'color': 'red', 
    'points': 15, 
    'speed': 'fast', 
    }

aliens = [alien_1, alien_2, alien_3]

for alien in aliens:
    race = alien['race']
    color = alien['color']
    points = alien['points']
    speed = alien['speed']

    print(f"Alien race: {race.title()}")
    print(f"\tColor: {color.title()}")
    print(f"\tPoints: {points}")
    print(f"\tSpeed: {speed.title()}\n")