""" 
This is a Pizza Toppings program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

prompt = "\nEnter a pizza topping"
prompt += "\nEnter 'quit' to end the pizza topping program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"We'll add {message} topping to your pizza")