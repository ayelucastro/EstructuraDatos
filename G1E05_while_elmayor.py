# calcular el mayor de unan serie de 10

contador=1  #contador=contador+1
print("Ingrese 10 números para evaluar cual es el mayor.")
number = int(input('Ingrese número de cantidades vendidas: '))
el_mayor = number
while contador < 10:
    number = int(input('Ingrese número de cantidades vendidas: '))
    contador = contador + 1
    if number > el_mayor:
        el_mayor = number
print ('Mayor numero ingresado: ' , el_mayor)

 