
# __init__ is a code file asoociate with a module .. it is apackage .. but not recommeded .... 
from .calculator import Calc

def say_hello(name):
    print(f'hello {name}')
    
    
def factorial(n):
    return 1 if n <=1 else n * factorial(n-1)