""" 
This is a Messages program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def show_messages(messages):
    """Print a simple short text message to each user in the list."""
    for message in messages:
        msg = f"Message: {message.title()}!"
        print(msg)

short_text_messages = ['i do not know', 'why are you running?!', 'among us!!!']
show_messages(short_text_messages)