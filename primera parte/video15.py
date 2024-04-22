comida = ['Pizza', 'Hamburguesa', 'Tacos', 'Hotdog', 'Pozole']

comida.append('Tamales')
comida.remove('Pizza')
comida.pop()
comida.insert(1, 'Sushi')
comida.sort()
comida.clear()

# Las listas pueden tener diferentes tipos de datos

for x in comida:
    print(x)