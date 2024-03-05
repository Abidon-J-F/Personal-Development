""" 
This is a T-Shirt program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def make_shirt(size, message_on_tshirt):
    """Display information about a pet."""
    print(f"\nI am size {size}.")
    print(f"The text on my T-shirt is {message_on_tshirt}, and I am a size {size}.")

#Postional argument
make_shirt('medium', 'Among Us')

##Keyword argument
make_shirt(message_on_tshirt= 'Among Us', size= 'medium')
