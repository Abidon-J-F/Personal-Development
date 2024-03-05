""" 
This is a Favorite Languages program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")

###
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}.")

###
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#for name in favorite_languages.keys():
##for name in favorite_languages.keys(): <- same as the above ^
#    print(name.title())

###
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print(f"Hi {name.title()}.")

#    if name in friends:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language}!")

###
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")

###
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for taking the poll.")

###
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#print(f"The following languages have been mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

###

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#}

#print(f"The following languages have been mentioned:")
#for language in set(favorite_languages.values()):
#    print(language.title())

###
#languages = {'python', 'ruby', 'python', 'c'}
#print(languages)

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")