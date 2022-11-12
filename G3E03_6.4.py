"""Escribir una funcion contar (c, s) que cuente cuantas veces aparece un caracter c dado en una cadena s."""
#hecho en clase
def contar_character ( character, text ):
    counter = 0
    for item in text:
        if character == item:
            counter += 1       #es la abreviacion de contador = contador + 1
    return counter

#hecho por mi
def find_a_v1(s): 
    """devuelve cuantas letras a hay en la cadena s."""
    counter = 0 
    for letra in s:
        if letra == 'a':
            counter += 1
    return counter

#Programa principal
print(contar_character('a', 'mariana'))

print(find_a_v1('ama al que te ama'))