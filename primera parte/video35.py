import os

origen = 'primera parte\\test.txt'
destino = 'primera parte\\test2.txt'

try:
    if os.path.exists(destino):
        print('El archivo de destino ya existe.')
    else:
        os.replace(origen, destino)
        print('El archivo se ha movido correctamente.')
except FileNotFoundError:
    print('El archivo de origen no existe.')