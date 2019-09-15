# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Phil'
age = 33


#Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')


# String Formatting


#Arguments by Position
# print('My name is {name} and I am {age} years old'.format(name=name, age=age))

#F-strings(3.6+)
# print(f'Hello, my name is {name} and I am {age} years old')


# String Methods
s = 'hello world'

#Captitalize string

print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase()) 
print(lens(s)) #Get length
print(s.replace('world', 'everyone'))

#Count
sub= 'h'
print(s.count(sub)) #Count number of h's inside of string

print(s.startswith('hello')) #return a bool
print(s.endswith)('d'))

#Split into a list
print(s.split())

#Find a position
print(s.find('r')) # returns a position


#has space
print(s.isalpha())
print(s.isnumeric())