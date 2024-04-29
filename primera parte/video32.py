try:
    with open('primera parte\\test.txt') as file:
        print(file.read())
    print(file.closed)
except FileNotFoundError:
    print('File not found')