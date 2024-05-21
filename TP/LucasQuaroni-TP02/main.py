# Ejercicio 16 – Seguridad automóviles
# Para evaluar la seguridad de los automóviles, la empresa NCAP realiza pruebas que representan
# acciones reales que se dan en las rutas y que pueden significar daño, o incluso la muerte, tanto
# para los pasajeros como para los peatones. En estas pruebas, los fabricantes de automóviles
# tienen que demostrar que sus autos vienen equipados con los elementos tecnológicos y técnicos
# necesarios para evitar que se produzca un accidente o para mitigar sus efectos cuando sea
# irreversible. Algunas de las pruebas consisten en Impactos frontales, Laterales y Latigazos
# cervicales.

# Se realizan 5 pruebas de seguridad (numeradas del 1 al 5) sobre cada uno de los autos de un
# grupo, el resultado de cada prueba es un número real entre 0,0 y 1,0 inclusive, donde un 1,0
# indica que la prueba fue superada en un 100%.
# Se desea realizar un algoritmo que, recibiendo como datos, los resultados de cada una de las 5
# pruebas realizadas, informe por cada auto:
#  El promedio de las 5 pruebas.
#  La cantidad de pruebas con resultados inferiores a 0,5.
# Para todos los autos:
#  La cantidad de autos que obtienen en las 5 pruebas resultados superiores a 0,8.
#  El mejor promedio de las 5 pruebas.
# Se desconoce la cantidad de autos a evaluar, proponer un fin de datos adecuados.
# Utilizar POO, modulos y archivos.


# Definicion de la clase auto
class Auto:
    def __init__(self, resultados):
        self.resultados = resultados

    def promedio_pruebas(self):
        return sum(self.resultados) / len(self.resultados)

    def pruebas_inferiores_a(self, limite):
        return sum(1 for resultado in self.resultados if resultado < limite)


# Modulo de funciones auxiliares
def calcular_mejor_promedio(autos):
    return max(auto.promedio_pruebas() for auto in autos)

def contar_autos_pruebas_superiores(autos, limite):
    return sum(1 for auto in autos if all(resultado > limite for resultado in auto.resultados))

def leer_datos_archivo(nombre_archivo):
    autos = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            if line.strip():  # Ignorar líneas vacías
                resultados = list(map(float, line.strip().split()))
                auto = Auto(resultados)
                autos.append(auto)
    return autos


# Funcion principal
def main():
    nombre_archivo = 'resultados_pruebas.txt'
    autos = leer_datos_archivo(nombre_archivo)

    for i, auto in enumerate(autos, 1):
        promedio = auto.promedio_pruebas()
        inferiores_a_05 = auto.pruebas_inferiores_a(0.5)
        print(f"Auto {i}:")
        print(f"  Promedio de las 5 pruebas: {promedio:.2f}")
        print(f"  Cantidad de pruebas con resultados inferiores a 0.5: {inferiores_a_05}")
        print("---------------------------------------------------------------------------------------")

    autos_con_pruebas_superiores = contar_autos_pruebas_superiores(autos, 0.8)
    mejor_promedio = calcular_mejor_promedio(autos)

    print(f"\nCantidad de autos que obtienen en las 5 pruebas resultados superiores a 0.8: {autos_con_pruebas_superiores}")
    print(f"El mejor promedio de las 5 pruebas es: {mejor_promedio:.2f}")

if __name__ == "__main__":
    main()
    
    
# ACLARACIONES:
    # El archivo 'resultados_pruebas.txt' debe estar en la misma carpeta que el script 'main.py'
    # El archivo debe contener los resultados de las pruebas de cada auto, separados por espacios. No poseemos fin de datos. Tantas lineas se agreguen, se evaluaran.