""" 
This is an Alien No Points program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

#alien_0 = {'color': 'green', 'speed': 'slow'}

#print(alien_0['points'])

###
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)