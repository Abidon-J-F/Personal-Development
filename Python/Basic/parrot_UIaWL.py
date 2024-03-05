""" 
This is a Parrot program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 06/2022 - 07/2022
"""

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

###
#prompt = "\nTell me something, and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit':
#        print(message)

####
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)