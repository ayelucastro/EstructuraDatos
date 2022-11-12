#Ejercicio 4_6.5. ¿Hay más letras “A” o más letras “E” en una cadena? Escribir un programa que lo decida. 
# Realizar una función, la misma debe devolver la cantidad de letras “A” y de letras “E” al “programa principal” (o función desde la cual fue invocada). 
# En el caso que no se encuentre la letra, devolver el valor cero.


def find_a_and_e(s): 
    """devuelve cuantas letras a y e hay en la cadena s."""
    counter_a = 0
    counter_e = 0
    valor = 0
    for letra in s:
        if letra == 'a':
            counter_a += 1
        elif letra == 'e':
            counter_e += 1  
    if counter_a > counter_e:
        print('La letra a es mayor en cantidad. Hay: ' , counter_a)
    elif counter_e > counter_a:
        print('La letra e es mayor en cantidad. Hay: ' , counter_a)
    print('La cadena tiene: ' , counter_a , 'letras a.')
    print('La cadena tiene: ' , counter_e , 'letras e.')
    if counter_a == 0:
        print(valor)
    elif counter_e == 0:
        print(valor)
    return None

#programa principal
find_a_and_e('olo')
