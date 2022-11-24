# main.py 

import module1
import sys 


print("========================================")

print("Running main.py -module name: {0}".format(__name__))



print(module1)

module1.pprint_dict('main.global', globals())

print(sys.path)

print(sys.modules['module1'])




print("========================================")


print("========================================")
print("========================================")
print("========================================")

del globals()['module1']

import module1
print(module1) # it is already cached .. so delete it 
