""" 
This is a More Conditional Tests program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 04/2022 - 05/2022
"""

meat = 'pork'

print("\nIs meat == 'pork'? I predict True.")
print(meat == 'pork')

print("\nIs chicken == 'chicken'? I predict False.")
print(meat == 'chicken')

##
meat = 'Pork'

print("\nIs meat non-capital == 'pork'? I predict True.")
print(meat.lower() == 'pork')

print("\nIs meat non-capital == 'pork'? I predict False.")
print(meat.upper() == 'pork')

##
age = 23

print("\nIs age == '23'? I predict True.")
print(age == 23)

print("\nIs age == '23'? I predict False.")
print(age == 18)

##
year = 2018

print("\nIs the year == '2018'? I predict True.")
print(year == 2018)

print("\nIs the year == '2021'? I predict False.")
print(year == 2021)

print("\nIs the year > '2021'? I predict False.")
print(year > 2021)

print("\nIs the year < '2021'? I predict True.")
print(year < 2021)

print("\nIs the year >= '2021'? I predict False.")
print(year >= 2021)

print("\nIs the year <= '2021'? I predict True.")
print(year <= 2021)


##
age_0 = 22
age_1 = 18

print("\nIs the year >= 'age_0' and 'age_1'? I predict False.")
print(age_0 >= 21 and age_1 >= 21)

print("\nIs the year >= 'age_0' or 'age_1'? I predict True.")
print(age_0 >= 21 or age_1 >= 21)

##
requested_subjects = ['science', 'english', 'mathematics']

print("\nIs science in requested subject? I predict True.")
print('science' in requested_subjects)

print("\nIs mayonnaise in requested subject? I predict False.")
print('mayonnaise' in requested_subjects)


print("\nIs scince not in requested subject? I predict False.")
print('science' not in requested_subjects)

print("\nIs mayonnaise not in requested subject? I predict True.")
print('mayonnaise' not in requested_subjects)