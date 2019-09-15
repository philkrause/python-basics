# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create a dictionary

person = {
    'first_name': 'Phil',
    'last_name': 'Doe',
    'age': 33
}

# print(person, type(person))

#Use contructor
# person2 = dict(first_Name='Sara', last_name='Williams')


#Get Value
# print(person['first_name'])
# print(person.get('last_name'))


#Add key value
person['phone'] = '555-555-5555'
# print(person)

#Get dict keys
# print(person.keys())

#Get dict items
# print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

#Remove and item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Get length
# print(len(person2))

# print(person)


#List of dictionaries
people = [
    {'name': 'John', 'age': 25},
    {'name': 'Phil', 'age': 21}
]

print(people[1]['name'])