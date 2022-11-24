# module.py

print('----------------Runing {0} ------------------'.format(__name__))

def pprint_dict(header, d):
    print('\n\n ---------------------------------------')
    print('******   {0} .  *******'.format(header))
    for key, value in d.items():
        print(key,'  ', value)
    print('-------------------------------------\n\n')
    
    
pprint_dict('module.globlas', globals())


print('------------------------ End of {0} --------------------'.format(__name__))