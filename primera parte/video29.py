import random

x = random.randint(1, 6)
y = random.random()
mi_lista = ['Piedra', 'Papel', 'Tijera']

z = random.choice(mi_lista)
print(z)

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cartas)
print(cartas)