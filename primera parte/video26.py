def suma (*cosas):
    suma = 0
    cosas = list(cosas)
    cosas[0] = 0
    for cosa in cosas:
        suma += cosa
    return suma

print(suma(1,2,3,4,5,6,7,8,9,10)) # 55