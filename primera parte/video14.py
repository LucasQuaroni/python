nombre = ''

while True:
    nombre = str(input('Ingrese su nombre: '))
    if nombre != '':
        break

telefono = '123-456-7890'

for i in telefono:
    if i == '-':
        continue
    print(i, end='')
    
for i in range (1, 21):
    if i == 13:
        pass
    else:
        print(i)



