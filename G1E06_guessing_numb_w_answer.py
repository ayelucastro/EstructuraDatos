#random guessing game_ valor min 0 y max 100

import random
num = random.randint(0, 100)
print(f'''
---------------------------
Correct answer: {num}
---------------------------
''')
intento = 1
print('valor minimo = 0')
print('valor maximo = 100')
print('Intente adivinar un número entero entre 0 y 100.')

num_ingresado = int(input('Escriba un número: '))
while num_ingresado != num:
    intento = intento + 1

    if num_ingresado > num:
        print('El ',num_ingresado, 'es demasiado grande! Inténtelo de nuevo.')
        num_ingresado = int(input('Escriba un número: '))
   
    elif num_ingresado < num:
        print('El ',num_ingresado, 'es demasiado pequeño! Inténtelo de nuevo.')
        num_ingresado = int(input('Escriba un número: '))

print('Le ha costado', intento , 'intentos.')