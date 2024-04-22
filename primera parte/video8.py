
nombreCompleto = 'Lucas Quaroni'

# nombre = nombreCompleto[0:5]
# apellido = nombreCompleto[6:13]

nombre = nombreCompleto[:5]
apellido = nombreCompleto[6:]
#no hace falta poner inicio y fin, se puede obviar y agarra el inicio y el final

nombreInvertido = nombreCompleto[::-1]

print(nombre)
print(apellido)
print(nombreInvertido)

website1 = 'http://google.com'
website2 = 'http://wikipedia.com'

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
