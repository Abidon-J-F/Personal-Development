""" 
This is an Foods program made in Python3.
Author: Abidon Jude Fernandes
Date: 03/2022 - 04/2022
"""

#my_foods = ['pizza', 'falafel', 'carrot cake']
#friend_foods = my_foods[:]

#print("My favorite foods are:")
#print(my_foods)

#print("\nMy friend's favourite foods are:")
#print(friend_foods)

###

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#This doesn't work:
#friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)