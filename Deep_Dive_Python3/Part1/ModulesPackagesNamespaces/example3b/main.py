# main.py

import sys 
import importer 



module1 = importer.import_('module1', 'module1_source.py', '.')

print("Sys says:", sys.modules.get('module1', 'Module1 not found' ))


import module2 

module2.hello()