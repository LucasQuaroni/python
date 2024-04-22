nombre = 'Lucas Quaroni'

if nombre[0].islower():
    print('El nombre no empieza con Mayuscula')
else:
    print('El nombre empieza con Mayuscula')


primer_nombre = nombre[:5].upper()
print(primer_nombre)

apellido = nombre[6:].lower()
print(apellido)

ultimo_caracter = nombre[-1]
print(ultimo_caracter)