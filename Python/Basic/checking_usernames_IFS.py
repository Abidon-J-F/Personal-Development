""" 
This is a Checking Usernames program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 04/2022 - 05/2022
"""

current_users = ['am45', 'po98', 'hj57', 'vb46', 'hf01']
current_users = [i.lower() for i in current_users]

new_users = ['AM45', 'among23', 'sus69', 'VB46', 'yolo077']
new_users = [i.lower() for i in new_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, {new_user} username is taken")
    else:
        print(f"{new_user} username is available")