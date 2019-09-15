# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# CORE moduules
from datetime import date
from time import time

# today = datetime.date.today()

today = date.today()
timestamp = time()

print(timestamp)


#pip module
from camelcase import CamelCase

##Captilizes first letter of every string
# c = CamelCase()
# print(c.hump('hello there world'))



#import custom module
from validator import validate_email

email = 'test@test.com'

if validate_email(email):
    print(f'{email} is valid')
else:
    print(f'{email} is not valid')