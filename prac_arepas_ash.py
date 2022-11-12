# IFTS21 – Practica primer parcial de Estructura de Datos - Fecha: 16/10/2022
# Nombres y Apellidos: Ayelen Luna Castro
# Nombre del tema: Arepas
 
#A
def show_menu(lista_arepas):
    """se imprime el menu de arepas"""
    print("Menu de 'Super Arepas'")
    for item in lista_arepas:
        print(item)   #will print 'text' in my list.
    return None   #or None?  

#B
def pedidos():
    """ Se toma un pedido. Se genera una lista de tuplas con cada pedido. Cada tupla tendra: tipo de arepa
    y su cantidad. Tuplas (string, int)"""
    pedido = []
    pedido_arepa = input('Por favor ingrese el tipo de arepa que quiere. Cuando haya terminado ingrese la letra x: ')
    while pedido_arepa.lower() != 'x':
        cantidad = int(input('Cuantas quiere? '))
        tupla_pedido = (pedido_arepa, cantidad)  #tupla pedida en consigna
        pedido.append(tupla_pedido)
        pedido_arepa = input('Por favor ingrese el tipo de arepa que quiere. Cuando haya terminado ingrese la letra x: ')
    return pedido

#C  (no me quedo claro, lo hice con mucha ayuda de apuntes)
def mostrar_pedido(pedido):
    """muestra el pedido completo en la pantalla."""
    cant_total_arepas = 0
    print('Su pedido es: ')
    for item in pedido:
        print(f'{item[0]} {item[1]} unidades')  #no me queda claro, lo encontre en apuntes.
        cant_total_arepas += item[1]
    print(f'El total de Arepas pedidas es de: {cant_total_arepas} unidades')
    return None

def main():
    lista_arepas = ('Reina', 'Pelua', 'Pabellón', 'Domino', 'Vegetarian') #lista de arepas PONER EN CAPS POR CONSTANTE
    show_menu(lista_arepas)  #A
    el_pedido = pedidos()  #B (por que el_pedido?)
    mostrar_pedido(el_pedido)  #C

###PROGRAMA PRINCIPAL: 
if __name__ == '__main__':
	main()