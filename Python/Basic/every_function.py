""" 
This is an Every Function program made in Python3.
Author: Abidon Jude Fernandes
Date: 02/2022 - 03/2022
"""

######################

countries = ['us', 'uk', 'canada', 'france', 'italy']
print(countries)

print(countries[0])

print(countries[0].title())

print(countries[0])
print(countries[1])

print(countries[-1])

message = f"My favourite country is the {countries[0].title()}."
print(message)

#################
countries = ['us', 'uk', 'canada', 'france', 'italy']
print(countries)

countries[3] = 'germany'
print(countries)

countries.append('france')
print(countries)

countries = []
countries.append('us')
countries.append('uk')
countries.append('canada')
countries.append('france')
countries.append('italy')

print(countries)

countries = ['us', 'uk', 'canada', 'france', 'italy']
countries.insert(0, 'portugal')
print(countries)

del countries[0]
print(countries)

countries = ['us', 'uk', 'canada', 'france', 'italy']
popped_countries = countries.pop()
print(countries)
print(popped_countries)

print(f"I admire the {popped_countries.title()}.")

popped_countries1 = countries.pop(0)
print(f"I admire the {popped_countries1.title()}.")

countries = ['us', 'uk', 'canada', 'france', 'italy']
countries.remove('italy')

too_expensive = 'canada'
countries.remove(too_expensive)
print(countries)
print(f"\nA {too_expensive.title()} is too expensive for me.")


#######################
countries = ['us', 'uk', 'canada', 'france', 'italy']
countries.sort()
print(countries)

countries = ['us', 'uk', 'canada', 'france', 'italy']
countries.sort(reverse=True)
print(countries)

countries = ['us', 'uk', 'canada', 'france', 'italy']

print("Here is the original list:")
print(countries)

print("\nHere is the original list:")
print(sorted(countries))

print("\nHere is the original list:")
print(countries)

countries = ['us', 'uk', 'canada', 'france', 'italy']
print(countries)

countries.reverse()
print(countries)

countries = ['us', 'uk', 'canada', 'france', 'italy']
print(len(countries))