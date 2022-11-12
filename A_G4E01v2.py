"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$','Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje 
de aviso si la divisa no está en el diccionario."""

currency = {'Euro':'€', 'Dollar':'$','Yen':'¥'}
#print (currency)

divisa = input ('Ingrese la divisa que necesita por favor: ')

divisainDict = False
for key, content in currency.items():
    if key == divisa:
        print ('La divisa', content, 'esta disponible')
        divisainDict = True
if divisainDict == False:
    print ('La divisa que ingreso no esta en la lista.')