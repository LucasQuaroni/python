temperatura = int(input('Ingrese la temperatura: '))

if (temperatura >= 0 and temperatura <= 30):
    print('La temperatura de hoy esta bien.')
elif (temperatura < 0 or temperatura > 30):
    print('La temperatura de hoy esta mal, es o muy alta o muy baja.')