import os
import shutil

path = 'primera parte\\test2.txt'

try:
    os.remove(path)
    # shutil.rmtree(path)
    print('El archivo se ha eliminado correctamente.')
except FileNotFoundError:
    print('El archivo no existe.')
except PermissionError:
    print('No tienes permisos para eliminar el archivo.')
except OSError:
    print('Error al intentar eliminar el archivo.')
