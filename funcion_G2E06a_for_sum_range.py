#**Ejercicio 6: Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número 
#hasta el segundo inclusive. 
#Nota: el usuario siempre ingresa el segundo número mayor que el primero. No hay que validar de que realmente sea así.
#Salida:
#SUMA ENTRE VALORES
#Escriba un número entero positivo: 30
#Escriba un número entero mayor que 30: 32
#La suma desde 30 hasta 32 es 93
total = 0
men = int(input('Escriba un número entero positivo:  '))
may = int(input('Escriba un número entero mayor que ' + str(men)+': '))
for i in range(men, may+1):
    total = total + i    #total+=numero
print('La suma desde ',men, 'hasta ', may, ' es ' , total)