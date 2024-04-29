import random

def ppt():
    lista = ['piedra', 'papel', 'tijeras']
    eleccion = input('Piedra, papel o tijeras?')
    eleccion = eleccion.lower()
    if eleccion in lista:
        computadora = random.choice(lista)
        print('La computadora eligió:', computadora)
        if eleccion == computadora:
            print('Empate!')
        elif eleccion == 'piedra' and computadora == 'tijeras':
            print('Ganaste!')
        elif eleccion == 'papel' and computadora == 'piedra':
            print('Ganaste!')
        elif eleccion == 'tijeras' and computadora == 'papel':
            print('Ganaste!')
        else:
            print('Perdiste!')
    else:
        print('Opción inválida. Inténtalo de nuevo.')
        ppt()
    
ppt()
