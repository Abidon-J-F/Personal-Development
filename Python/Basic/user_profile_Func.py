""" 
This is an User Profile program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

#def build_profile(first, last, **user_info):
#    """Build a dictionary containing everything we know about a user."""
#    user_info['first_name'] = first
#    user_info['last_name'] = last
#    return user_info

#user_profile = build_profile('albert', 'einstein', 
#                                location='princeton',
#                                field='physics')

#print(user_profile)

###User Profile Test:
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('abidon', 'fernandes',
                                university='greenwich',
                                location='london',
                                field='computer science')

print(user_profile)