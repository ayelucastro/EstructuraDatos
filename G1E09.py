#Ejercicio 9_5.5 Escriba un programa que utilice una instrucción while para sumar una secuencia de enteros. 
#Suponga que el primer entero leído especifica el número de valores que quedan por introducir. 
# Su programa debe leer sólo un valor por cada instrucción de entrada. 

def suma():
    suma = 0
    contador = 0    
    print('Vamos a realizar una suma.')
    num_cont = int(input("Ingrese la cantidad de números que va a sumar: "))
    while contador != num_cont:
        if contador <= num_cont:
            numero = int(input("Ingrese el número a sumar: "))
            suma = suma + numero
            contador += 1
    print("La suma total es:", suma)
    return None

#Programa Principal
suma()
