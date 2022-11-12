# pedir ingreso de números para sumar. Preguntar si desea seguir sumando (si/no).
# uso de centinela -> seguir
suma = 0
seguir = "si"
while seguir != "no":
	numero = int(input("Ingrese un numero entero: "))
#	suma = suma + numero
	suma += numero
	print("La suma es", suma)
	seguir = input("Desea seguir ingresando valores? (si/no)")