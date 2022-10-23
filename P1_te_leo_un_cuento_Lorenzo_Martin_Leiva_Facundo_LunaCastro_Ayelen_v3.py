# IFTS21 – Primer parcial de Estructura de Datos - Fecha: 24/10/2022
# Nombres y Apellidos: Leiva, Facundo - Lorenzo, Martin - Luna Castro, Ayelen
# Nombre del tema: te leo un cuento
 

def mostrar_lista(mostrar_lista_libros): # punto a
    """funcion que imprime la lista de libros, solo nombres y autores"""
    print('Los libros que tenes en la biblioteca son:','\n')
    for item in mostrar_lista_libros:
        print(item ,'\n')   #will print 'text' in my list.
    return None  


def cant_pag(): # punto b1
    """funcion para que el usuario ingrese la cantidad de paginas que desea leer"""
    max_pag = int(input('Hasta cuantas paginas desearia leer?:  '))
    if max_pag <= 239:
        print('Lo lamentamos, los libros tienen entre 240 y 530 paginas.', '\n')
        max_pag = int(input('Hasta cuantas paginas desearia leer?:  ')) 
        if max_pag >= 531:
            print('Lo lamentamos, los libros tienen entre 240 y 530 paginas.', '\n')
            max_pag = int(input('Hasta cuantas paginas desearia leer?:  ')) 
    return max_pag


def lista_cant_pag(LISTA_LIBROS_COMPLETA, max_pag): # punto b2
    """ la función analiza la lista de libros, busca y guarda los libros que tienen la cantidad de páginas igual o menor a las que 
    ingreso el lector. (lista de tuplas)"""
    libros_filtrados = []
    for i in range(0, len(LISTA_LIBROS_COMPLETA), 3) :
        if LISTA_LIBROS_COMPLETA[i+2] <= max_pag:
            libros_filtrados.append(LISTA_LIBROS_COMPLETA[i])
    return libros_filtrados

def sugerencias(lista_sugerida): # punto c
    """Esta función le sugiere al lector los libros que contienen la cantidad de páginas que indico."""
    print('\n', 'La siguiente lista contiene los títulos sugeridos según la cantidad de páginas que ingreso.','\n')
    for item in lista_sugerida:
        print(item ,'\n')
    return None


def eliminar_libro(lista_libros): # punto d EXTRA
    """Esta funcion le consulta al lector cual es el libro que se quiere llevar y lo elimina de la lista de los libros disponibles, 
    luego imprime la lista de libros disponibles para prestar de la biblioteca."""
    libro_eliminar = input('Podría ingresar que libro decidio leer? (Por favor, respete las mayúsculas y minúsculas al escribir):   ')
    lista_libros.remove(libro_eliminar)		
    print('\n','Gracias! Ahora queda la siguiente lista de libros.' ,'\n')
    for item in lista_libros:
        print('\n', item ,'\n')
    return lista_libros


def main():
    LISTA_LIBROS_COMPLETA = ('El retrato de Dorian Gray', ' de Oscar Wilde', 239, 
    'Yo robot', ' de Isaac Asimov', 287, 
    'Historias de cronopios y de famas', ' de de Julio Cortázar', 326, 
    'Crónica de una muerte anunciada', ' de Gabriel García Márquez', 352,
    'La isla misteriosa', ' de Julio Verne', 362, 
    'La sombra del viento', ' de Carlos Ruiz Zafón', 412, 
    'Mujercitas', ' de Louisa May Alcott', 432,
    'Tokio blues', ' de Haruki Murakami', 471, 
    'Harry Potter y la piedra filosofal', ' de J. K. Rowling', 506,
    'La casa de los espíritus', ' de Isabel Allende', 526)    

    mostrar_lista_libros = ['Harry Potter y la piedra filosofal de J.K Rowling', 'Historias de cronopios y de famas de Julio Cortázar', 
    'Yo robot de Isaac Asimov', 'Crónica de una muerte anunciada de Gabriel García Márquez', 'El retrato de Dorian Gray de Oscar Wilde',
    'La sombra del viento de Carlos Ruiz Zafón', 'Tokio blues de Haruki Murakami', 'La casa de los espíritus de Isabel Allende',
    'La isla misteriosa de Julio Verne', 'Mujercitas de Louisa May Alcott']
    
    lista_libros = ['Harry Potter y la piedra filosofal', 'Historias de cronopios y de famas', 'Yo robot', 'Crónica de una muerte anunciada',
    'El retrato de Dorian Gray', 'La sombra del viento', 'Tokio blues', 'La casa de los espíritus', 'La isla misteriosa', 'Mujercitas']
   
    mostrar_lista(lista_libros)   # punto a
    #cant_pag() # punto b1
    max_pag = cant_pag() #variable local
    lista_cant_pag(LISTA_LIBROS_COMPLETA, max_pag) # punto b2
    libros_filtrados = lista_cant_pag(LISTA_LIBROS_COMPLETA, max_pag) #variable local
    sugerencias(libros_filtrados)   # punto c
    eliminar_libro(lista_libros)  # punto d EXTRA

     

###PROGRAMA PRINCIPAL: 
if __name__ == '__main__':
	main()