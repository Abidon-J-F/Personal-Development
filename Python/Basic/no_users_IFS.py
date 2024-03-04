""" 
This is a No Users program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 04/2022 - 05/2022
"""

usernames = ['admin', 'jeff19', 'bob78', 'emily60', 'alice003']

#chosen_username = ['admin']
#chosen_username = ['jeff19']
#chosen_username = ['bob78']
#chosen_username = ['emily60']
#chosen_username = ['alice003']
chosen_username = []

for username in chosen_username:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    elif username in usernames:
        print(f"Hello {username}, thank you for logging in again")
if not usernames:
    print("We need to find some users!")