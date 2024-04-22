try:
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    division = numerador / denominador
except ZeroDivisionError as e:
    print(e)
    print("No se puede dividir por cero!")
except ValueError as e:
    print(e)
    print("Debes introducir un numero!")
except Exception as e:
    print(e)
    print("Algo salio mal!")
else:
    print("La division es: ", division)
finally:
    print("Operacion finalizada!")