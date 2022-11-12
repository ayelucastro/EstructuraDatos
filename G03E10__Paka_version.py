# NO BORRAR
"""Ejercicio 10
Realizar con tuplas. Menú de Hamburguesas.
Piense los nombres de 4 hamburguesas para un menú de un nuevo local (no te olvides de los vegetarianes ni
veganes). Guárdalos en una tupla de tu programa. Utiliza un loop for para recorrer la tupla e imprimir en
pantalla el menú del local. 
"""
def mostrar_menu(lista_hamburquesas):
	print("Nuestro menu de Hamburguesas ;)")
	for item in lista_hamburquesas:
  		print (item)
	return None
  
def main():
	# Menu Hamburguesas
	# Los nombres de las hamburguesas no cumplen con la consigna :P
	HAMBURGUESAS = ("Hamburguesa Python", "Hamburguesa Java", "Hamburguesa Win", "Hamburguesa Linux")
	# nombres de HAMBURGUESAS definida como una tupla
	mostrar_menu(HAMBURGUESAS)
	return None
  
# Programa Principal
if __name__ == "__main__":
	main()