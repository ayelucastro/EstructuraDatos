fecha = "31-03-2019"
lista_fecha = fecha.split('-')  # El método split genera una lista
fecha_ar = '/'.join(lista_fecha)
print(lista_fecha)  # Tener cuidado! ésta no es la forma de imprimir los elementos de una lista, es sólo para mostrar que lista_fecha contiene una lista y para ver sus elementos.
# para imprimir el contenido de una lista, hay que recorrerla (por ejemplo con un for) y sacar por pantalla cada uno de los elementos.
print(fecha_ar)