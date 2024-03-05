""" 
This is a No Pastrami program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

sandwich_orders = ['chicken sandwich', 'veg sandwich', 'fish sandwich', 'cheese sandwich', 
                    'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []


print("Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich.title()}")
    finished_sandwiches.append(sandwich)

print("\nList of all the sandwichs that was made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())