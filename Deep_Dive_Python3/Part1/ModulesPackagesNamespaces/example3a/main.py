#main.py


import os.path 
import types
import sys

module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_name, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

 
# Read the source code from file 

with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()
    
    
# create a module object 
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path 


# set a refrence in sysmodule 
sys.modules[module_name] = mod 


# Compile the source code 
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# execute the compiled source code 
exec(code, mod.__dict__) 

# Done! 

mod.hello()