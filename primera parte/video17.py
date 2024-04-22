estudiantes = ('Alexa', 22, 'M')

print(estudiantes.count(22))
print(estudiantes.index('M'))

# Las tuplas no pueden ser modificadas

for x in estudiantes:
    print(x)

if 'Alex' in estudiantes:
    print('Alex está en la tupla')
else:
    print('Alex no está en la tupla')