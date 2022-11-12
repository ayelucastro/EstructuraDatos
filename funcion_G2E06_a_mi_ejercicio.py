#Ejercicio 6b: Una vez que funciona su programa, repiénselo y utilice funciones para modularizar el programa. 
# primera: Deberá tener una función que reciba los dos números, calcule la sumatoria pedida y la devuelva. 
# segunda: Luego utilice otra función para exhibir en pantalla y retorne None al programa principal.

#SUMA ENTRE VALORES
def primera():
    """ recibe dos números enteros, calcula la sumatoria pedida de todos los enteros desde el primer número 
    hasta el segundo inclusive. Se esperan 2 valores (int)"""
    total=0
    men=int(input('Escriba un número entero positivo:  '))
    may=int(input('Escriba un número entero mayor que ' + str(men)+': '))
    for i in range(men, may+1):
        total = total + i    #total+=numero 
    return total

#PROGRAMA PRINT SCREEN
def segunda(total):
    """Esta función es para exhibir en pantalla y retorne None al programa principal.""" 
    print('El total de la suma es: ' , str (total) )
    return 'none'

#PROGRAMA PRINCIPAL
print("Vamos a calcular la suma de todos los enteros desde el primer número hasta el segundo inclusive.")
total=primera()
segunda(total)