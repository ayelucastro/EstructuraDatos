#def cocina():

def mostrar_menu(menu, titulo):
# punto a
    print(titulo,"\n")
    for item in menu:
        print(item)

def tomar_pedido():
# punto b
    pedido = []
    pizza = input("ingrese tipo de pizza: ")
    while pizza != "x":
        cantidad = int(input("cuantas querés? "))
        mi_tupla = (pizza, cantidad)
        pedido.append(mi_tupla)
        pizza = input("ingrese tipo de pizza: ")
    return pedido

def analisis_pedido(pedido, menos_pedida):
    """ Se analiza la lista de pizzas "pedido" y se guarda el nombre de la pizza que menos cantidad se pidió en la lista
    menos_pedida. lista de tuplas [('Vegetarian STR', 4), ]
    (lista de tuplas(string, int))-> lista de str"""
# punto c
    la_menos_pedida = ""
    cantidad =  1000 # considero que es el máximo de pizzas que me pueden pedir.
    for item in pedido:
        if item[1] != 0:  #si es cero, no hay pedido de pizza de ese tipo
            if item[1] < cantidad:
                la_menos_pedida = item[0]
                cantidad = item[1]
    menos_pedida.append(la_menos_pedida)
    return menos_pedida

def imprimir_pedido(el_pedido):
# punto d
    print("\nEl pedido registrado es:\n")
    for item in el_pedido:
        print(f"De la pizza {item[0]}, pidieron {item[1]}")
    return None

def main():
# Estructuras de datos utilizadas
    MENU_PIZZA = ("Muzza a la Tupla", "Fugazza a la Lista", "Palmitos a la Tupla", "Napo sin Tupla", "Vegetarian STR")
    pizza_menos_pedida = []


# punto a
    mostrar_menu(MENU_PIZZA, "Menu de la La Gran Pizza del Oeste")

# punto b
    tomar_pedidos = input("¿Desea ingresar pedidos? (Si -> enter / x para salir)")
  
    while tomar_pedidos.lower() != "x":
        el_pedido = tomar_pedido()

#punto c
        pizzas_menos_pedida = analisis_pedido(el_pedido, pizza_menos_pedida)
        # print(pizzas_menos_pedida)  # para debuguear
#punto d
        imprimir_pedido(el_pedido)


        tomar_pedidos = input("¿Desea ingresar pedidos? (Si -> enter / x para salir)")
     

    #mostramos la lista de las pizzas menos pedidas !!
    mostrar_menu(pizza_menos_pedida, "Estas son las pizzas que menos quieren")

    return None


if __name__ == "__main__":
    main()

