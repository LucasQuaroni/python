# TP01 - Ejercicio Clubes:
#
# Luego de recabar datos de los socios en cada uno de los 17 clubes
# más importantes de la ciudad se quiere determinar, para cada una de ellos,
# entre los socios censados mayores de edad (tienen 18 años o más) quienes son
# más numerosos, los que son socios temporales (código 1) o los que son 
# socios permanentes (código 2).
# Para resolver esto se dispone, por cada socio de cada uno de los clubes,
# su código de asociado (1 para temporal, 2 para permanente) y edad. 
# Un código de asociado 0 (cero) indica que no hay más datos de ese club.
# Validar el código entre 0, 1 y 2; no permita otros valores.
# Validar la edad que no sea negativa y reconfirme (¿esta seguro?) 
# si es mayor a 100.
# 
# Utilzar funciones, listas.

NUM_CLUBES = 2
arrayClubes = []
contadorTemporales = [0] * NUM_CLUBES
contadorPermanentes = [0] * NUM_CLUBES

def ingresoDatos(lista):
    print("Ingreso de datos")
    for i in range(NUM_CLUBES):
        print("--------------------------------------------------------------------------------------")
        print("Club nro: ", i+1)
        lista.append([])
        for j in range(100):
            print("Socio nro: ", j+1)
            lista[i].append([])
            lista[i][j].append(int(input("Ingrese codigo de asociado: ")))
            if lista[i][j][0] == 0:
                break
            lista[i][j].append(int(input("Ingrese edad: ")))
            while lista[i][j][0] != 0:
                if lista[i][j][0] != 1 and lista[i][j][0] != 2:
                    print("Error en el codigo de asociado, reingrese")
                    lista[i][j][0] = int(input("Ingrese codigo de asociado: "))
                if lista[i][j][1] < 0:
                    print("Error en la edad, reingrese")
                    lista[i][j][1] = int(input("Ingrese edad: "))
                if lista[i][j][1] > 100:
                    print("Esta seguro que la edad es mayor a 100?")
                    respuesta = input("Ingrese si o no: ")
                    if respuesta == "si":
                        break
                    if respuesta == "no":
                        lista[i][j][1] = int(input("Ingrese edad: "))
                break
            if lista[i][j][0] == 0:
                break

def procesoDatos(lista):
    global contadorTemporales, contadorPermanentes
    print("Comienza el procesado de datos")
    for i in range(NUM_CLUBES):
        for j in range(100):
            if lista[i][j][0] == 0:
                break
            if lista[i][j][1] >= 18:
                if lista[i][j][0] == 1:
                    contadorTemporales[i] += 1
                if lista[i][j][0] == 2:
                    contadorPermanentes[i] += 1
        
def salidaDatos(temporales, permanentes):
    for i in range(NUM_CLUBES):
        print("--------------------------------------------------------------------------------------")
        print("Club nro: ", i+1)
        print("Cantidad de socios temporales mayores de edad: ", contadorTemporales[i])
        print("Cantidad de socios permanentes mayores de edad: ", contadorPermanentes[i])
        if contadorTemporales[i] > contadorPermanentes[i]:
            print("Los socios temporales son mas numerosos")
        elif contadorTemporales[i] < contadorPermanentes[i]:
            print("Los socios permanentes son mas numerosos")
        elif contadorTemporales[i] == contadorPermanentes[i]:
            print("La cantidad de socios temporales y permanentes es igual")

# llamadas a las funciones.
ingresoDatos(arrayClubes)
procesoDatos(arrayClubes)
salidaDatos(contadorTemporales, contadorPermanentes)
print("Fin programa")