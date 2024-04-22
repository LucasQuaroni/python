def saludo(nombre, apellido, lenguaje):
    print(f'Hola {nombre} {apellido}, bienvenido a {lenguaje}')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
lenguaje = input('Ingrese su lenguaje favorito: ')

saludo(lenguaje=lenguaje, nombre=nombre, apellido=apellido)