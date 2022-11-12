"""Enunciado:cargar vector de 10 números, obtener promedio e informar cuáles son los que lo superan. 
Separando lo que es ingreso de datos, de proceso y recorrida del vector para mostrar resultados"""

import numpy as np

def cargar_array():
    pass
    mi_vector = np.array([])
    print (mi_vector)
    numero = input("Ingrese un numero (x para salir): ")
    while numero != 'x':
        mi_numero = float(numero)
        mi_vector = np.append(mi_vector, mi_numero)
        print(mi_vector)
        numero = input("Ingrese un numero (x para salir): ")
    return mi_vector


def procesar_mayores_promedio(array):
    pass
    for item in array:
        print(item)
    return None

# programa principal

mi_array = cargar_array()
print("Tamaño del Array es : ", mi_array.size)
procesar_mayores_promedio(mi_array)