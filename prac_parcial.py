#funsion que 
def todos_libros (libros):
  for i in range(len(libros)):
    l = libros[i]
    print(f'{i+1}. {l}')
    
def cuantas_paginas (libros_con_pagina, nueva_lista):
  maximo= int
  maximo= input ("Ingrese cuantas paginas como maximo quiere leer: ")
  for x in range (len (libros_con_pagina)):
    l2=libros_con_pagina[x] #guardo en la var l2 el numero que esta como str
    int(l2) #convierto el str en un numero para compararlo con los datos que me ingresa en maximo
    if (l2 <=maximo):
       l=libros[x] #guardo en l el nombre del libro que esta en la ubicacion [x]
       k=libros_con_pagina[x]
       t=l+k
       nueva_lista.append(t) #agrego en la nueva lista el nombre en la ultima posicion

  for i in range(len(nueva_lista)):
    l = nueva_lista[i] #se le asigna a l nombre que tiene en la posicion "i"
    print(f'{i+1}. {l}')

def eliminar_libro(nueva_lista):
  print ("Que libros desea llevar: ")
  for i in range(len(nueva_lista)):
    l = nueva_lista[i] #se le asigna a l nombre que tiene en la posicion "i"
    print(f'{i+1}. {l}')
    
  lleva= int (input ("introduzca que libro desea llevar(comenzando por la posicion 0,1,2...): "))
  m=nueva_lista[lleva]
  print ("usted llevara el libro: " ,m)
  nueva_lista.remove(m)
  mi_copia= libros.copy()
  print (" la lista original de los libros de la biblioteca son: ")
  for i in range(len(mi_copia)):
    l = mi_copia[i] #se le asigna a l nombre que tiene en la posicion "i"
    print(f'{i+1}. {l}')
    
#programa_principal
libros= ["Harry Potter y la piedra filosofal de J.K Rowling. " ,
"Historias de cronopios y de famas de Julio Cortázar. " ,
"Yo robot de Isaac Asimov. " , 
"Crónica de una muerte anunciada de Gabriel García Márquez. " ,
"El retrato de Dorian Gray de Oscar Wilde. ",
"La sombra del viento de Carlos Ruiz Zafón. " ,
"Tokio blues de Haruki Murakami. " ,
"La casa de los espíritus de Isabel Allende. " ,
"La isla misteriosa de Julio Verne. " ,
"Mujercitas de Louisa May Alcott. "] 
libros_con_pagina= ["506", "326" ,"287" , "352" ,"239","412" ,"471" ,"526" ,"362" ,"432"] 

#Estos dos libro guarda si es menor a 300
#"Y2o robot de Isaac Asimov. "
#E8l retrato de Dorian Gray de Oscar Wilde. ",
todos_libros (libros)
nueva_lista=[]
cuantas_paginas (libros_con_pagina, nueva_lista)
eliminar_libro(nueva_lista)
#mi_copia= libros.copy()
#mi_copia.remove(m)
#print ("los libros que quedan disponibles en la biblioteca son: ")
#for i in range(len(mi_copia)):
  #l = mi_copia[i] #se le asigna a l nombre que tiene en la posicion "i"
  #print(f'{i+1}. {l}')