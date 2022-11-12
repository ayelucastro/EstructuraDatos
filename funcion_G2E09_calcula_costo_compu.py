# Guía 2 Ejercicio 9
# Definicion de funciones
def costo_compu(pulgadas, memoria):
  """ la funcion recibe las pulgadas y la cantidad 
  de memoria para calcular el costo de la computadora"""
  PRECIO_BASE = 6000
  COSTO_POR_PULGADA = 60
  COSTO_POR_GIGA = 260
  CANT_CUOTAS = 12
  total_compu = PRECIO_BASE + COSTO_POR_PULGADA * pulgadas + COSTO_POR_GIGA * memoria
  valor_cuota = total_compu / CANT_CUOTAS
  print("El valor de la Computadora es: $",total_compu)
  print("El valor de cada una de las 12 cuotas es: $", valor_cuota)
  return None
  #no se devuelve nada
  
#Programa principal
# primer ejemplo de uso de la función. Llamada a la función costo_compu()
costo_compu(25,8)

""" ahora la llamamos con otros argumentos, por ejemplo queremos
saber cuanto sale una compu con pantalla de 32 pulgadas y 64GB de Ram."""
print("Calcularemos el costo de una computadora con pantalla de 32 pulgadas y 64GB de Ram")
costo_compu(32,64)

# Nota importante! No está bueno que se realizen más de una acción en una función.
# Habría que separar en varias funciones, por ej. calc_costo_compu(), calc_cuotas(), mostrar_valores()
# ¿¿¿Te animás a realizarlo???