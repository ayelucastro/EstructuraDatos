"""Ejercicio 2
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario
por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta
no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70"""

listado_frutas = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

fruta = input ("Ingrese la fruta que desea: ")
fruta_encontrada = False

for clave, contenido in listado_frutas.items():
    if clave == fruta:
        peso = float (input("¿Cuántos kilos desea?: "))
        print ("Debe abonar $", peso * contenido)
        fruta_encontrada = True

if fruta_encontrada == False:
    print ("Esa fruta no esta disponible")
                      
    
