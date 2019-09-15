# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create a list

numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Use a constructor
# numbers2 = list((1,2,3,4,5))

print(fruits[1])

print(len(fruits))

#Append to list
fruits.append('Mangos')


#Remove from list
fruits.remove('Grapes')

#Insert into position
fruits.insert(2, 'Strawberries')

#Remove with pop
fruits.pop(2)

fruits.reverse()

fruits.sort() #alphabetical sort

fruits.reverse()

#change value
fruits[0] = 'Blueberries    '

print(fruits)