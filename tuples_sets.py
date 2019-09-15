# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruits = ('Apples', 'Oranges', 'Grapes')


# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
# fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
# del fruits2

# Get length
print(len(fruits))


#Create a set
fruit_set = {'Apples', 'Orages', 'Mango'}

#Check if in set
print('Apples' in fruit_set)

#Add to set
fruit_set.add('Grape')

#Remove from set
fruit_set.remove('Grape')

#Clear set
fruit_set.clear() 

#del
del fruit_set


print(fruit_set)


