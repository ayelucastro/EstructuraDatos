#string se lo denomina s. Es como la i del for o lst para una lista.#


#  Ejercicio 1 _6.8.1. Escribir funciones que dada una cadena de caracteres texto:
# b) Devuelva los tres últimos caracteres.
# d) Devuelva dicha cadena en sentido inverso.
# Ej.: 'hola mundo!' debe imprimir '!odnum aloh'


def ult_char(x):
  return x[-3:]

def inverse(x):
  return x[::-1]


#programa principal
text = ult_char("Hola Mundo!")
print(text)

text = inverse("Hola Mundo!")
print(text)


 