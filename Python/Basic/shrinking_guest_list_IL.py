""" 
This is a Shrinking Guest List program. Python3 creation.
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

print(f"{guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()}, {guests[5].title()}. Only two people can make it to the dinner party")

gone1 = guests.pop(0)
gone2 = guests.pop(0)
gone3 = guests.pop(0)
gone4 = guests.pop(2)

#print(guests)

print(f"Sorry I cannot invite you {gone1.title()}.")
print(f"Sorry I cannot invite you {gone2.title()}.")
print(f"Sorry I cannot invite you {gone3.title()}.")
print(f"Sorry I cannot invite you {gone4.title()}.")


print(f"Welcome to our dinner {guests[0].title()}.")
print(f"Welcome to our dinner {guests[1].title()}.")

del guests[0]
del guests[0]

print(guests)

#Length of the guest list
print(len(guests))