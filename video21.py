def saludo(nombre, apellido, edad):
    print('Hola ' + nombre + ' ' + apellido + ', tienes ' + str(edad) + ' años')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))

saludo(nombre, apellido, edad)