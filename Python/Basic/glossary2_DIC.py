""" 
This is a Glossary 2 program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 05/2022 - 06/2022
"""

programming_words = {
    'key': 'keys are analogous to indexes of a list',
    'value': 'values is an inbuilt method in Python programming language that returns a view object',
    'get()': 'the get() method returns the value for the specified key if the key is in the dictionary',
    'dynamic structures': 'you can add new key-value pairs to a dictionary at any time',
    'dictionary': 'dictionary consists of a collection of key-value pairs',
    'argument': 'A value passed to a function (or method) when calling the function',
    'attribute': 'A value associated with an object which is referenced by name using dotted expressions',
    'class': 'A template for creating user-defined objects',
    'f-string': 'String literals prefixed with f or F are commonly called “f-strings” which is short for formatted string literals',
    'function': 'A series of statements which returns some value to a caller',
    }

for key, value in programming_words.items():
    print(f"\n{key.title()}: {value.title()}.\n")