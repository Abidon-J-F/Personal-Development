""" 
This is an Motorcycles program made in Python3.
Author: Abidon Jude Fernandes
Date: 02/2022 - 03/2022
"""

##Modifying Elements in a List
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)


##Adding Elements to the List using the Append Function
#motorcycles.append('ducati')
#print(motorcycles)


#motorcycles = []

#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')

#print(motorcycles)


##Insert Elements into a List
#motorcycles = ['honda', 'yamaha', 'suzuki']

#motorcycles.insert(0, 'ducati')
#print(motorcycles)


##Delete List Statement
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#del motorcycles[1]
#print(motorcycles)


##Removing an Item Using the pop() Method

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)


##Removing suzuki to show you owned a previous motorcycles
#motorcycles = ['honda', 'yamaha', 'suzuki']

#last_owned = motorcycles.pop()
#print(f"The last motorcycle I owned was a {last_owned.title()}.")


##Popping Items from any Position in a List
#motorcycles = ['honda', 'yamaha', 'suzuki']

#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {first_owned.title()}.")


##Removing an Item by Value
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)

#motorcycles.remove('ducati')
#print(motorcycles)


##Removing an Item by Value and printing a reason for its removal
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)

#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print(f"\nA {too_expensive.title()} is too expensive for me.")

##Index Errors
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3])

##Use [-1] if you cannot figure out the last item number on the list
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[-1])

##Index Error 2
#motorcycles = []
#print(motorcycles[-1])

##Intentional Error
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3]) ##Wrong
#print(motorcycles[2]) ##Correct