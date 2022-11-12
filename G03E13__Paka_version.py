def domino_jugar(ficha_A, ficha_B):
  """
  La función verifica si las dos fichas de dominó encajan entre sí o no. Ej. (3,4) y (4,5) encajan, mientras que (3,4) y (6,1) no.
  (tup(int, int), tup(int,int)) -> bool
  """
  print(ficha_A, ficha_B)  #solo para debuguear
  jugar = False
  if ficha_A[0] == ficha_B[0] or ficha_A[0] == ficha_B[1] or ficha_A[1] == ficha_B[0] or ficha_A[1] == ficha_B[1]:
    jugar = True
  return jugar

def main():
	# para probar el programa descomentar de a uno los lotes de prueba
	"""
	#Lote de prueba1 -> True
	ficha1 = (3,4)
	ficha2 = (5,4)
	"""
	"""
	#Lote de prueba2 -> True
	ficha1 = (4,3)
	ficha2 = (5,4)
	"""
	"""
	#Lote de prueba3 -> True
	ficha1 = (4,3)
	ficha2 = (4,5)
	"""
	"""
	#Lote de prueba4 -> True
	ficha1 = (3,4)
	ficha2 = (4,5)
	"""
	"""
	#Lote de prueba4 -> False
	ficha1 = (4,3)
	ficha2 = (5,5)
	"""
	"""
	#Lote de prueba5 -> False
	ficha1 = (3,3)
	ficha2 = (5,4)
	"""
	"""
	#Lote de prueba6 -> False
	ficha1 = (3,3)
	ficha2 = (6,6)
	"""
 
	jugar_ok = domino_jugar(ficha1, ficha2)
	print("Parece que puedo jugar", jugar_ok)
