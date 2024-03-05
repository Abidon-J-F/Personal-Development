""" 
This is a Sandwiches program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def make_sandwiches(*items):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following item:")
    for item in items:
        print(f"- {item}")

#make_sandwiches('lettuce')
#make_sandwiches('lettuce', 'pepperoni', 'chicken strips')
#make_sandwiches('lettuce', 'cheese')
#Styling tick mark