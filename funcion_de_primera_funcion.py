def primera():
  print("hola estoy en la primer funcion")
  # llamamos a la segunda función
  segunda()
  print("ahora estamos en la primer funcion")
  return None
  
def segunda():
  print("acá estamos en la segunda función")
  return None
  
#PROGRAMA PRINCIPAL
print("estamos en el programa principal")
primera()
print("termino nuestro programa principal")