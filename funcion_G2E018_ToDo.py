#Ejercicio 8: Prograna que realiza un cuadrado con *
def imprime_rectangulo():
    """recibe N números enteros para dibujar un rectangulo (int)"""
    imprime_ancho()
    imprime_laterales()
    return None


def imprime_ancho():
    """recibe N números enteros para dibujar un rectangulo (int)"""
    n = input('Escriba un número para crear un rectangulo: ')
    for j in range (n):
        print ('*', end="")
    return None

def imprime_laterales():
    """recibe N número entero para dibujar los laterales del rectangulo (int)"""
    n = input('Escriba un número para crear un rectangulo: ')
    print ('*', end='')
    for j in range(n-2):
        print (' ', end='')
    return None


#PROGRAMA PRINCIPAL
print("Vamos a dibujar un rectangulo.")
imprime_rectangulo()
