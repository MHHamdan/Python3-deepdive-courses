# main.py 
# best approach 
import common.helpers as helpers
import common.helpers 

import common.validators2 as validators
import common 
#import common.models as models

import common.models.posts 
import common.models.users#.user  

# from common.models import * # not recommed way for import 



mohammed = common.models#.users#.user 

#mhamdanPost = common.models.Post()
#mhamdanPost =  Post() # * impor t


validators.boolean.is_boolean('True')
print('**'*88)
validators.json.is_json('{}')




# import common.validators.boolean
# import common.validators.date
# import common.validators.json
# import common.validators.numeric

# #better appraoch
# from common.validators.numeric import is_integer, is_numeric


# #best appraoch 
# import common.validators as validators 



# is_numeric(2)

# validators.numeric.is_numeric()

from common.validators2 import *

validators.is_boolean('true')
validators.is_json('{}')

validators.json.is_json('{}')
validators.date.is_date('2022-01-01')

#validators.numeric.is_integer('d')

print('\n\n ****** self **********')
for k in dict(globals()).keys(): # k is a symbol in namespace ... iterable globals dic make a copy
    print(k)
    
print('\n\n ********* common **********')
for k in common.__dict__.keys():
    print(k)
    
    
print('\n\n ********* validators **********')
for k in validators.__dict__.keys():
    print(k)
    
    
    
print('\n\n ********* numeric **********')
for k in validators.numeric.__dict__.keys():
    print(k)
    
print('\n\n ********* boolean **********')
for k in validators.boolean.__dict__.keys():
    print(k)
    
    
print('\n\n ********* models **********')
for k in common.models.__dict__.keys():
    print(k)
    
print('\n\n ********* posts (packages) **********')
for k in common.models.posts.__dict__.keys():
    print(k)
 
    
print('\n\n ********* users (packages) **********')
for k in common.models.users.__dict__.keys():
    print(k)
 
 
print('\n\n ********* name space models  **********')
for k in common.models.__dict__.keys():
    print(k)
 
 
 
 

calc = common.helpers.Calc() 

cl = common.helpers.say_hello('Python... ')

print(helpers.say_hello('Python'))
print(helpers.factorial(8))




import asyncio

import email