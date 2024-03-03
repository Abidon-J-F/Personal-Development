"""
This is a Tip Calculator program made in Python2.
Author: Abidon Jude Fernandes
Date: 02/02/2024
"""

meal = 44.50
tax = 0.0675
tip = 0.15

wallet = 75

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
