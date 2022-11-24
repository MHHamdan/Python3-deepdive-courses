# timingpy


print('Loading timeit timing ......')



"""
    Times how long a snippet of code takes to run over 
    multiple iteration 
    """
    
    
    
from time import perf_counter

from collections import namedtuple

import argparse


Timing = namedtuple('Timing', 'repeats elapsed average')

def timeit(code, repeats=10):
    #exec(code)
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start 
    average = elapsed / repeats 
    return Timing(repeats, elapsed, average)


if __name__ == '__main__': # To run thsi timing.py
    print('running this command line code .....')
    
    # get code, repeats from arguments 
    
    parser = argparse.ArgumentParser(description=__doc__) # disc 
    parser.add_argument('code',
                          type=str, help='The Python code snippet to time.') # positional arguments - named whatever it is going to comeback .. 
    parser.add_argument('-r', '--repeats',
                       type=int, default=10, help='Number of times to repat the test.') # key word argument .. 
    args = parser.parse_args() # get the arguments .. 
    print(args.code, args.repeats)
    
    
    print(f'timing: {args.code}....')
    print(timeit(code=str(args.code), repeats=args.repeats))