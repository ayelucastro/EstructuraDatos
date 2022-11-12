def saludar(nombre):
  """ recibe un nombre e imprime en pantalla un saludo   #las 3 comillas son docstring, help de la funcion
  se espera que nombre sea un srt (str) -> None"""   #aca se aclara para que fue hecha la funcion
  print("Hola", nombre)
  print("Ya nos vamos!!!")
  return None  #es importante que pongamos que no returns anything

# fin definición de las funciones

# nuestro programa
usuario = input("Ingrese su nombre: ")
saludar(usuario)

# que pasa si en lugar de ingresar un nombre se ingresa un número entero o un número real?