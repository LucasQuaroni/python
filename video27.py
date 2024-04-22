def hola(**kwargs):
    print('Hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'] + ', tienes ' + str(kwargs['edad']) + ' años')

hola(nombre='Lucas', apellido='Quaroni', edad=25)

