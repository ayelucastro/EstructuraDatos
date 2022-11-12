"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$','Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje 
de aviso si la divisa no está en el diccionario."""

currency = {'Euro':'€', 'Dollar':'$','Yen':'¥'}

#print (currency)

divisa = input ('Ingrese una divisa por favor: ')

if divisa in currency:
    print (currency.values())
else:
    print ('La divisa que ingreso no esta en la lista.')