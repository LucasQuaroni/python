fila = int(input('Cuantas filas? '))
columna = int(input('Cuantas columnas? '))
simbolo = input('Ingrese un simbolo: ')


for i in range (fila):
    for j in range (columna):
        print(simbolo, end='')
    print()