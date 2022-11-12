def imprimerectangulo(n):
	imprimelineaborde(n)
	for i in range(1,n-1):
		imprimelineaintermedia(n)
	imprimelineaborde(n)

def imprimelineaborde(n):
	for i in range(1,n):
		print("*", end="")
	print("*")

def imprimelineaintermedia(n):
	print("*", end="")
	for i in range(1,n-1):
		print(" ", end="")
	print("*")


# Escriba un programa que pida al usuario que introduzca el tamaño del lado de un cuadrado y que muestre un cuadrado hueco 
# de ese tamaño, compuesto de asteriscos y espacios en blanco. Su programa debe funcionar con cuadrados que tengan lados 
# de todas las longitudes entre 1 y 20. Por ejemplo, si su programa lee un tamaño de 5, debe imprimir: 
# *****
# *   *
# *   *
# *   *
# *****
tamanio = int(input("Ingrese el tamaño del rectángulo a imprimir: "))
imprimerectangulo(tamanio)
