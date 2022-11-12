"""Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa
no está en el diccionario"""

billetera = {'Euro':'€', 'Dollar':'$',
'Yen':'¥'}
#billetera ["Euro"] = "€"
#billetera ["Dollar"] = "$"
#billetera ["Yen"] = "¥"


moneda_buscada = input ("¿Qué moneda esta buscando?: ")

moneda_encontrada = False
for clave, contenido in billetera.items():
    if clave == moneda_buscada:
        print ("Su moneda esta disponible", clave, contenido)
        moneda_encontrada = True
if moneda_encontrada == False:
    print ("Su moneda no esta disponible")
   
    
    
    

