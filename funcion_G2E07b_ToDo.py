G2E7 Parte B
def es_negativo(numero):
  """ es_negativo devuelve True si numero es < 0 y False si numero es => 0 (numero) -> bool"""
  return numero < 0
# comparar con el ejemplo de la otra función es_negativo vista en clase 

def contar_negativos(cantidad):
  """ contar_negativos pide el ingreso de cantidad de números al usuario y devuelve el total_negativos ingresados. (numero) -> int""" 
  
  total_negativos = 0
  for i in range(cantidad):
    texto = "Escriba el número " + str(i+1) + ": "
    num = int(input(texto))  # Tengan en cuenta que input sólo permite un parámeto sólo
    if es_negativo(num):
      total_negativos += 1
  return total_negativos
  
print("NUMEROS NEGATIVOS")
cantidad_numeros = int(input("¿Cuántos valores va a introducir? "))
negativos_contados = contar_negativos(cantidad_numeros) 
print("La cantidad de números negativos ingresados es: ", negativos_contados)