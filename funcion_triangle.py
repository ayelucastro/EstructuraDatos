# Function to print triangle

def triangle():
    n = int(input('Escriba un número para crear un triangulo: '))
    i = 1
    j = 0
    # while checkea la condicion
    # if true then enter loop and print
    while(i <= n):
        while(j <= i-1):
	        print("* ",end="")
	        j += 1

    # printing next line for each row
        print("\r")
        j = 0; i += 1
    return None


#PROGRAMA PRINCIPAL
print('Vamos a dibujar un triangulo')
triangle()
print('termino nuestro programa principal')
