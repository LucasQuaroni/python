import os

path = 'C:/Users/Lucas/Desktop/UAI/python/directorio/test.txt'

if os.path.exists(path):
    print('El directorio existe')
    if os.path.isfile(path):
        print('Y es un archivo')
    elif os.path.isdir(path):
        print('Y es un directorio')
else:
    print('El directorio no existe')
    
