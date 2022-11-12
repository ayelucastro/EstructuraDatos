#Ejercicio 10_5.13 Una aplicación interesante de las computadoras es dibujar gráficos convencionales y de barra. 
#Escriba un programa que lea cinco números (cada uno entre 1 y 30). Suponga que el usuario introduce valores válidos. 
# Por cada número leído, su programa debe imprimir una línea que contenga ese número de asteriscos adyacentes. 
# Los números se ingresan de a uno y a continuación se realiza la salida en pantalla pedida.
# Por ejemplo, si su programa lee el número 7, debe mostrar *******.

def grafica_barra() :
    n = int(input('Ingrese el número de * que quiere para crear una barra: ')) 
    for i in range(1, n+1) :
        print("*", end="")           
    return None
 
#PROGRAMA PRINCIPAL
grafica_barra()