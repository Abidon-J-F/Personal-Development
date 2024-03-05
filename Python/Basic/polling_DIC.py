""" 
This is a Polling program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jeff': 'c++',
}



for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
if 'donald' not in favorite_languages.keys():
    print("\nDonald, please take our poll.")
if 'kyle' not in favorite_languages.keys():
    print("Kyle, please take our poll.")
if 'mary' not in favorite_languages.keys():
    print("Mary, please take our poll.")


### Other option
#not_taken = {
#    'mary': 'c',
#    'kyle': 'java',
#    'donald': 'javascript',
#}

#for name in sorted(not_taken.keys()):
#        print(f"{name.title()}, please take our poll.")