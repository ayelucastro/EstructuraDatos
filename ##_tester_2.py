# IFTS21 – Primer parcial de Estructura de Datos - Fecha: 24/10/2022
# Nombres y Apellidos: 
# Nombre del tema: 
 

def mostrar_lista(LISTA_LIBROS): # punto a
    """funcion que imprime la lista de libros"""
    print('Los libros que tenes en la biblioteca son:','\n')
    for item in LISTA_LIBROS(['title'], ['author']):
        print(item)   #will print 'text' in my list.
    return None  


def main():
    LISTA_LIBROS = ({'title': 'Harry Potter y la piedra filosofal',
    'author': 'de J.K Rowling', 'pgs': 506},
    {'title': 'Historias de cronopios y de famas',
    'author': ' de Julio Cortázar', 'pgs': 326}, {'title': 'Yo robot', 
    'author': ' de Isaac Asimov', 'pgs': 287}, {'title': 'Crónica de una muerte anunciada', 
    'author': ' de Gabriel García Márquez', 'pgs': 352})

    """" 'El retrato de Dorian Gray', ' de Oscar Wilde', 239, 'La sombra del viento', 
    ' de Carlos Ruiz Zafón', 412, 'Tokio blues', ' de Haruki Murakami', 471, 'La casa de los espíritus', 
    ' de Isabel Allende', 526, 'La isla misteriosa', ' de Julio Verne', 362, 'Mujercitas', ' de Louisa May Alcott', 432)
    LISTA_LIBROS = ('Harry Potter y la piedra filosofal de J.K Rowling', 'Historias de cronopios y de famas de Julio Cortázar', 
    'Yo robot de Isaac Asimov', 'Crónica de una muerte anunciada de Gabriel García Márquez', 'El retrato de Dorian Gray de Oscar Wilde',
    'La sombra del viento de Carlos Ruiz Zafón', 'Tokio blues de Haruki Murakami', 'La casa de los espíritus de Isabel Allende',
    'La isla misteriosa de Julio Verne', 'Mujercitas de Louisa May Alcott')"""
    mostrar_lista(LISTA_LIBROS)   # punto a

    
   

###PROGRAMA PRINCIPAL: 
if __name__ == '__main__':
	main()