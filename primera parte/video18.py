utensillos = {'Tenedor', 'Cuchara', 'Cuchillo'}
platos = {'Plato1', 'Plato2', 'Plato3', 'Cuchara'}

for x in utensillos:
    print(x)

# los utensillos no tienen un orden especifico, por lo que cada vez que se ejecute el programa, el orden de los elementos puede cambiar

# esto es un conjunto, no una lista, por lo que no se puede acceder a los elementos por medio de un indice

utensillos.pop()
utensillos.clear()
utensillos.update(platos)

print(utensillos.difference(platos))
print(utensillos.intersection(platos))