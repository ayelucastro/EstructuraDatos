def cuadrado(x):
  """Dado un número x, calcula x² (numero) -> numero"""  #las triple comillas son el comentario para la funcion
  return x * x # También podríamos haber hecho x ** 2

# fin definición de las funciones

# nuestro programa
# para poder usar la función que creamos, hay que llamarla.
# por ejemplo
# print(cuadrado(32))
# print(cuadrado(8))

# o podemos guardar lo que devuelve la función en una variable
resultado = cuadrado(8.2)
print (resultado)

# poner help(cuadrado) en la consola. Ver que pasa.