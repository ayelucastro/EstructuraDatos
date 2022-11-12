def es_negativo(numero):
  """ es_negativo devuelve True si numero es < 0 y False si numero es => 0 (numero) -> bool"""
  if numero < 0:
    resultado = True
  else:
    resultado = False
  # seguro que hay formas mejores de hacer ésto!!
  return resultado


#PROGRAMA PRINCIPAL
print(es_negativo(10))
print(es_negativo(-10))
print(es_negativo(0))
