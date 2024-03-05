""" 
This is a Sending Messages program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def show_messages(messages, show_send_messages):
    while messages:
        current_message = messages.pop()
        print(f"Short Message : {current_message}")
        show_send_messages.append(current_message)

def send_messages(show_send_messages):

    print("\nThe following messages have been printed:")
    for show_send_message in show_send_messages:
        print(show_send_message)


messages = ['i do not know', 'why are you running?!', 'among us!!!']
show_send_messages = []

show_messages(messages, show_send_messages)
send_messages(show_send_messages)