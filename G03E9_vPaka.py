#G03E9_Pakaversion
"""A) Solicitar al usuario que ingrese números enteros, los cuales se guardarán en una lista. 
Finalizar al ingresar el número 0, el cual no debe guardarse.
B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
C) Recorrer la lista para imprimir la sumatoria de todos los elementos. Realizar una función para 
sumar e imprimir desde el programa principal (función principal).
D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que 
sean menores que el número dado (realizarlo en una función). Imprimir esta nueva lista, 
iterando por ella."""

# punto A
def ingresar_numeros():
	""" pedir numeros enteros al user. Guardarlos en una lista"""
	lista_num = []
	num = int(input("Ingrese un número entero (0 para terminar): "))
	while num != 0:
		lista_num.append(num)		
		num = int(input("Ingrese un número entero (0 para terminar): "))
	return lista_num
  
# punto B
def eliminar_numero(lista_numeros):
	print("Vamos a eliminas un número de la lista")
	num = int(input("Ingrese un numero entero que ingresaste anteriormente: "))
	if num in lista_numeros:
		lista_numeros.remove(num)
	else:
		print(f"El numero {num} no está en esta lista de numeros")
	return lista_numeros
  
# punto C
def sumar_numeros(lista):
	suma = 0
	for numero in lista:
		suma = suma + numero
	return suma
  
# punto D
def generar_lista_menores(la_lista):
	lista_menores = []
	num_tope = int(input("Ingrese un número tope: "))
  
	for numero in la_lista:
		if numero < num_tope:
			lista_menores.append(numero)
	return lista_menores, num_tope
  
# punto D parte 2 imprimir lista
def imprimir_lista(lista_enteros):
	for item in lista_enteros:
		print(f"{item} ", end = "")  # recordar que el end = "" es para poder escribir en pantalla en la misma línea. 
	print()
	return None
  
def main():
	# parte A
	mi_listita_de_numeros = ingresar_numeros()
	#print(mi_listita_de_numeros)
	# parte B
	lista_modificada = eliminar_numero(mi_listita_de_numeros)
	print(lista_modificada)
	#print(sumar_numeros(lista_modificada)) # por si no quiero guardar la sumatoria
	# parte C
	suma = sumar_numeros(lista_modificada)
	print(f"La suma de los números que quedaron es: {suma}")
	# parte D
	# el enunciado pide usar la lista original. Para eso, tendríamos que realizar una copia de la misma antes de modificarla. Como no vimos cómo copiar una 'lista', vamos a omitirlo y usamos la lista_modificada
	mi_lista_menores, tope  = generar_lista_menores(lista_modificada)
	print(f"La lista de los numeros menores a {tope} es:")
	imprimir_lista(mi_lista_menores)
  
  	
if __name__ == '__main__':
	main()