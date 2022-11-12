#G2E06B Variaciones!!!!
# Ejemplo con Main!!! <----- <-----
def sumador_entre_numeros(numero1, numero2):
  """Esta función recibe dos numeros numero1 y numero2, devuelve la sumatoria de todos los enteros entre numero1 y numero2 (incluyéndolos).
  (int, int) -> int """ 
#  print(num1)  # si corremos esta linea 
#  Python nos tira -> NameError: name 'num1' is not defined
  suma = 0
  aux = numero1
  while aux <= numero2:
    suma = suma + aux
    aux += 1
  return suma

def imprimir_resultado(numero1, numero2, suma):
  print("La suma desde",numero1,"hasta",numero2,"es",suma )
  for x in range(numero1, numero2):
        print(x, "+", end=" ")
  print(numero2,"=",suma)
  return None

def main():
  print("SUMA ENTRE VALORES")
  num1 = int(input("Escriba un número entero positivo: "))
  #texto = "Escriba un número mayor que " + str(num1) + ": "
  # num2 = int(input(texto))
  num2 = int(input("Escriba un número mayor que " + str(num1) + ": "))

  mi_suma = sumador_entre_numeros(num1, num2)
  imprimir_resultado(num1, num2, mi_suma)
  # FIN DEL PROGRAMA
  return None

if __name__ == "__main__":
	main()

# Para ver un poco más sobre el uso de if __name__ == "__main__"
# https://www.freecodecamp.org/espanol/news/python-if-name-main/
# https://docs.python.org/es/3.8/library/__main__.html