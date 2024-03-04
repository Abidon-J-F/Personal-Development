""" 
This is a More Guests program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 02/2022 - 03/2022
"""

guests = ['jeff', 'bob', 'windy']
print(guests)


print(f"{guests[0].title()} cannot make it.")

del guests[0]

guests.insert(0, 'adam')


print(f"Welcome to our dinner {guests[0].title()}.")
print(f"Welcome to our dinner {guests[1].title()}.")
print(f"Welcome to our dinner {guests[2].title()}.")

print(f"{guests[0].title()}, {guests[1].title()}, {guests[2].title()} I have found a huge dinning table for us to eat")

guests.insert(0, 'mary')
guests.insert(2, 'ryan')
guests.append('jesus')

print(guests)

print(f"Welcome to our dinner {guests[0].title()}.")
print(f"Welcome to our dinner {guests[1].title()}.")
print(f"Welcome to our dinner {guests[2].title()}.")
print(f"Welcome to our dinner {guests[3].title()}.")
print(f"Welcome to our dinner {guests[4].title()}.")
print(f"Welcome to our dinner {guests[5].title()}.")

#Length of the guest list
print(len(guests))