def mostrar_menu(menu_ingresado):
    """
    Esta es una función que al ser invocada muestra el menú de la pizzería

    """

    print("La Gran Pizza del Oeste")
    print("Menú")
    print("------------------------")

    for item in menu_ingresado: 
        print(item)
    print("-------------------------")

def tomar_pedido():

    """
    Esta función toma el pedido que llega por Whatsapp

    """

    seguir = 1

    pedido_ingresado = []

    while seguir != "x":
    
        variedad_ingresada = str(input("Por favor ingrese la variedad desdeada "))

        cantidad_ingresada = int(input("Por favor ingrese la cantidad de la variedad elegida "))

        pedido_ingresado.append((variedad_ingresada,cantidad_ingresada))

        seguir = input("Si desea continuar, presione 1, sino presione x para detener el ingreso del pedido ")

    return pedido_ingresado

def metrica_pizza(pedido_recibido):

    """
    Esta función analiza y devuelve cuál es la pizza menos pedida en el pedido

    """

    pizza_menos_solicitada = 100 #considero un número para poder inicializar

    for i in pedido_recibido:
        
        if i[1] < pizza_menos_solicitada: 

            pizza_menos_solicitada = i[1]
        
            pizza_menos_pedida = i[0] 
    
     
    return pizza_menos_pedida

def pedido_por_pantalla(mostrar_pedido):

    """
    Esta función muestra por pantalla el pedido tomado
    
    """
    
    print("Pedido")
    print("-------")
    for i in mostrar_pedido: 

        print(i[0], end="")
        print(": ", i[1])

def cocina(pedidoApreparar, numero_pedido):

    suma_pizzas = 0
    
    print("Pedido numero ", numero_pedido)

    for item in pedidoApreparar:
        
        print("Preparando", item[1] ," pizzas de ", item[0])

        suma_pizzas = suma_pizzas + item[1]

        #print(suma_pizzas) #solo para debuggear

    return suma_pizzas

def main():

    menu = ("Muzza a la Tupla", "Fugazza a la lista", "Palmitos a la Tupla", "Napo sin Tupla", "Vegetarian STR")

    mostrar_menu(menu)

    seguir = 1

    total = 0

    numero_pedido = 0 # al ingresar al sistema asumo que no hay ningún pedido

    while seguir != "x":

        pedidoAcocina = tomar_pedido() #entro a la función para tomar el pedido que luego entra como parámetro a la función cocina

        numero_pedido += 1 #informa a la cocina el número de pedido a preparar, ya que se preparan por orden de llegada

        subtotal = cocina(pedidoAcocina, numero_pedido) #paso los parámetros de la lista de pedidos tomados, y el número de pedido que es. También el retorno lo guardo en una variable subtotal

        print("subtotal", subtotal) #solo para debuggear

        total = total + subtotal

        seguir = input("Para ingresar otro pedido presione 1, o x para salir del sistema ") #consulta al usuario si va seguir ingresando pedido.Si dice que no, sale directamente del sistema, sería como el cierre del día


    print("El número total de pizzas preparadas es: ", total)

    menosPedida = metrica_pizza(pedidoAcocina)


    pedido_por_pantalla(pedidoAcocina)

    print(f"La pizza menos pedida es: {menosPedida}") #solo para debbugear
    

if __name__ == "__main__":
    main()

#me faltaría bajar a minúsculas el texto ingresado por el usuario, para evitar que se tome distinto por ejemplo: Fugazza y fugazza ya que impacta en la pizza menos pedida en esta instancia. 