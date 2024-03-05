""" 
This is a Large Shirts program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def make_shirt(size='large', message_on_tshirt='I love Python'):
    """Display information about a pet."""
    print(f"\nI am size {size}.")
    print(f"The text on my T-shirt is {message_on_tshirt}, and I am a size {size}.")

##Default 
make_shirt()

##meduim with default message
make_shirt(size= 'medium')

##random shirt size and message
make_shirt(size= 'small', message_on_tshirt= 'No Way')