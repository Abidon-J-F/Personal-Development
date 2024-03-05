""" 
This is a Three Exits program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

prompt = "\nEnter a pizza topping"
prompt += "\nEnter 'quit' to end the pizza topping program. "
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"We'll add {message} topping to your pizza")