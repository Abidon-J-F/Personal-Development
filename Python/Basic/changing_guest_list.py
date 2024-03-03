""" 
This is an Changing Guest List program made in Python3.
Author: Abidon Jude Fernandes
Date: 02/2022 - 03/2022
"""

guests = ['jeff', 'bob', 'windy']
print(guests)


print(f"{guests[0].title()} cannot make it.")

del guests[0]
#print(guests)

guests.insert(0, 'adam')
#print(guests)

print(f"Welcome to our dinner {guests[0].title()}.")
print(f"Welcome to our dinner {guests[1].title()}.")
print(f"Welcome to our dinner {guests[2].title()}.")

#Length of the guest list
print(len(guests))
