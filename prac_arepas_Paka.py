# AREPAS - Posible resolución del ejercicio

def mostrar_menu(menu, nombre_local):
# punto a
    print(f"Menu de '{nombre_local}'\n")
    for arepa in menu:
        print(arepa)
    return None

def tomar_pedido():
    """ Se realiza la toma de un pedido. Se genera una lista de tuplas con el
        tipo de arepa y la cantidad pedida. None -> lista de tuplas (string, int)
    """
# punto b
    pedido = []
    arepa = input("ingrese tipo de arepa (x para terminar): ")
    while arepa.lower() != "x":
        cantidad = int(input("cuantas querés? "))
        mi_tupla = (arepa, cantidad)  # acá genero la tupla que me piden
        pedido.append(mi_tupla)
        # tambien se puede poner directmente ->
        # pedido.append((arepa, cantidad))
        arepa = input("ingrese tipo de arepa (x para terminar): ")
    return pedido

def mostrar_pedido(pedido):
    total_arepas = 0
    print("Pedido:")
    for item in pedido:
        print(f"{item[0]} {item[1]} unidades")
        total_arepas += item[1]
    print(f"Total de Arepas pedidas {total_arepas} unidades")
    return None

def main():
# Estructuras de datos utilizadas
    MENU_AREPAS = ("Reina", "Pelua", "Pabellon", "Domino", "Vegetarian")
  
# punto a
    mostrar_menu(MENU_AREPAS, "SUPER AREPAS")
# fin punto a

# punto b
    el_pedido = tomar_pedido()
    # print(el_pedido) # para probar el punto b

# punto c
    mostrar_pedido(el_pedido)


if __name__ == "__main__":
  main()
