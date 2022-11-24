# importer.py

#main.py


import os.path 
import types
import sys


print("Runing importer.py")

def import_(module_name, module_file, module_path):
    
    if module_name in sys.modules:
        return sys.modules[module_name]
    

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
    
    return sys.modules[module_name]

# Done! 

