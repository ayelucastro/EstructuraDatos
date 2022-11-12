#ayelenlunacastro@gmail.com
#Ejercicio 6b: Una vez que funciona su programa, repiénselo y utilice funciones para modularizar el programa. 
# primera: Deberá tener una función que reciba los dos números, calcule la sumatoria pedida y la devuelva. 
# segunda: Luego utilice otra función para exhibir en pantalla y retorne None al programa principal.
totalg=0
print("Vamos a calcular la suma de todos los enteros desde el primer número hasta el segundo inclusive."  )
menorg=int(input('Escriba un número entero positivo:  '))
mayorg=int(input('Escriba un número entero mayor que ' + str(menorg)+': '))
for i in range(menorg, mayorg+1):
    totalg = totalg + i    #totalg+=numero 

#SUMA ENTRE VALORES
def primera():
    """recibe dos números enteros, calcula la sumatoria pedida de todos los enteros desde el primer número 
    hasta el segundo inclusive. Se esperan 2 valores (int)"""
    return totalg

#PROGRAMA PRINT SCREEN
def segunda():
    """Esta función es para exhibir en pantalla y retorne None al programa principal.""" 
    print('El total de la suma es: ' , totalg,)
    return 'none'

#PROGRAMA PRINCIPAL
primera()
segunda()