#Realizar un programa que cumpla con:
"""A) Solicitar al usuario que ingrese números enteros, los cuales se guardarán en una lista. 
Finalizar al ingresar el número 0, el cual no debe guardarse.
B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
C) Recorrer la lista para imprimir la sumatoria de todos los elementos. Realizar una función para 
sumar e imprimir desde el programa principal (función principal).
D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que 
sean menores que el número dado (realizarlo en una función). Imprimir esta nueva lista, 
iterando por ella."""

def ingresar_numeros():
    """A = ingresar números enteros, se guardarán en una lista. Finalizar con el 0, que no debe guardarse."""
    list_numb = []
    print("Vamos a crear una lista de números")
    num = int(input('Ingrese números enteros para crear la lista. (para terminar escriba 0): '))
    while num != 0:
        list_numb.append(num)		
        num = int(input('Ingrese números enteros para crear la lista. (para terminar escriba 0): '))
    return list_numb


def eliminar_numero(lista_numeros):
    """B = solicitar que ingrese un número y, if in list, eliminate 1st. if not show messsage."""
    print('Ahora, vamos a eliminar algún número de los que ingreso anteriormente.')
    num_eliminar = int(input('Ingrese alguno de los números que ingreso previamente: '))
    if num_eliminar in lista_numeros:
        lista_numeros.remove(num_eliminar)		
    else:
        print(f"El numero {num_eliminar} no está en esta lista de numeros")
    return lista_numeros

    
def suma_numeros(lista):
    """C = Imprimir la suma de todos los números de la lista en el programa principal"""
    sum = 0
    for num in lista:
        sum = sum + num
    return sum


def generar_nueva_lista(lista_menores):
    """D = solicitar otro numero, generar lista con los nums menores al ingresado."""
    list_numb_menores = []
    print('Ahora, vamos a generar una nueva lista usando algunos números de la lista original.')
    print('Tenga en cuenta que el número que ingrese será el mayor número de la nueva lista.')
    nuevonum = int(input('Ahora si. Ingrese un número para generar la nueva lista: '))
    for numero in lista_menores:
        if numero < nuevonum:
            list_numb_menores.append(numero)
    return list_numb_menores, nuevonum
    
def print_list(lista_enteros):
    """D = imprimir la lista."""
    for item in lista_enteros:
        print(f'{item} ', end = "")
    print()
    return None


#PROGRAMA PRINCIPAL

primer_lista = ingresar_numeros()
copy_primer_list = primer_lista.copy()

segunda_lista =  eliminar_numero(primer_lista)
print(segunda_lista)

suma = suma_numeros(segunda_lista)
print(f"La suma de los números que quedaron en la nueva lista es: {suma}")
	
#D: el enunciado pide usar la lista original. Para eso, tendríamos que realizar una copiarla antes de 
# modificarla. 
nueva_lista, copy_primer_list = generar_nueva_lista()   #a partir de aca mal
print(f"La lista de los numeros menores a {copy_primer_list } es:")
print_list(nueva_lista)
