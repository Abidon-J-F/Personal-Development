""" 
This is an My & Your Pizzas program made in Python3.
Author: Abidon Jude Fernandes
Date: 03/2022 - 04/2022
"""

my_pizzas = ['cheese pizza', 'ham & cheese pizza', 'pepperoni pizza']

friend_pizzas = ['cheese pizza', 'ham & cheese pizza', 'pepperoni pizza']

my_pizzas.append('chicken feast pizza')
friend_pizzas.append('pineapple & salmon pizza')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza2 in friend_pizzas:
    print(pizza2.title())
