# NO BORRAR - SE USA EN EL AV.-
def domicilios_de_entrega(lista_ventas):
	""" Se recibe un lista_ventas (ver ejemplo) y se genera un listado_entregas con domicilios únicos (ver ejemplo).
	(lista de tuplas) -> listado de str  
	Lista de ejemplo:
	[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
	Salida esperada:
	['Calle Las Flores 355', 'Mirasol 218', 'La Mancha 761']
	"""
	listado_entregas = []
	for item in lista_ventas:
			if item[3] not in listado_entregas:
				listado_entregas.append(item[3])
	return listado_entregas
  
def imprimir_lista(lista):
	for item in lista:
		print(item)
	return None
  
def main():
	ventas_del_mes = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
  
	entregas = domicilios_de_entrega(ventas_del_mes)
	print("Los domicilios de entrega de éste mes son:")
	imprimir_lista(entregas)
  
if __name__ == "__main__":
	main()