#Ejercicio 5_6.6. Escribir un programa que cuente cuantas veces aparecen cada una de las vocales en una cadena. 
# No importa si la vocal aparece en mayúscula o en minúscula.

def count_vowels(s): 
    """devuelve cuantas veces aparecen cada una de las vocales en una cadena s."""
    counter_a = 0
    counter_e = 0
    counter_i = 0
    counter_o = 0
    counter_u = 0
    for letra in s.lower():
        if letra == 'a':
            counter_a += 1
        elif letra == 'e':
            counter_e += 1  
        elif letra == 'i':
            counter_i += 1  
        elif letra == 'o':
            counter_o += 1  
        elif letra == 'u':
            counter_u += 1  
    print('La cadena tiene: ' , counter_a , 'letras a.')
    print('La cadena tiene: ' , counter_e , 'letras e.')
    print('La cadena tiene: ' , counter_i , 'letras i.')
    print('La cadena tiene: ' , counter_o , 'letras o.')
    print('La cadena tiene: ' , counter_u , 'letras u.')
    return None

#programa principal
count_vowels('aeiouAEEIOOOUUU')

