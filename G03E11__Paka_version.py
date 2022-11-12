# NO BORRAR
def mostrar_menu(lista_hamburquesas):
	print("Nuestro menu de Hamburguesas ;)")
	for item in lista_hamburquesas:
		print(f"La {item[0]} sale ${item[1]}")
	return None

def main():
	# Menu Hamburguesas
	# pasamos a una lista de listas, ya que ésto nos permitiría en un futuro cambiar el precio de las hamburguesa (por un tema inflacionario).
	menu = [["Hamburguesa Python", 230],["Hamburguesa Java", 320],["Hamburguesa Win", 330],["Hamburguesa Linux", 200]]
	mostrar_menu(menu)
	return None

# Programa Principal
if __name__ == "__main__":
	main()