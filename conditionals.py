# If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 5


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values


# if x > y:
#     print(f'{x} is greater than {y}')


#If else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')


#elif

# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{y} is equal to {x}')
# else:
#     print(f'{y} is greater than {x}')


#Nested if
# if x > 5:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')



# Logical operators (and, or, not) - Used to combine conditional statements
#AND
# if x > 5 and x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')

# #OR
# # if x > 5 or x <= 10:
# #         print(f'{x} is greater than 2 and less than or equal to 10')

# #NOT
# if not(x == y):
#     print(f'{x} is not equal to y')
 


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#Contains in List(Array)
# if x in numbers:
#     print(x in numbers)

#If doesn't contain
# if x not in numbers:
#     print(x not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# #is
# if x is y:
#     print(x is y)

if x is not y:
    print(x is not y)