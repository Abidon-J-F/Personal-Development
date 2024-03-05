""" 
This is a Cars program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a user."""
    car_info['manufacturer_name'] = manufacturer.title()
    car_info['model_name'] = model.title()
    return car_info

car = make_car('subaru', 'outback',
                color='blue',
                tow_package=True)

car2 = make_car('honda', 'city',
                color='maroon',
                tow_package=False)

print(car)
print(car2)