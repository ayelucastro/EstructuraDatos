▼
" NO BORRAR SE USA EN EL AV"

def invertir_palabra( palabra ):
	palabra_invertida = ""
	for i in range(len(palabra)):  # si "naturales" -> range(9)
		indice = len(palabra) - 1 - i
		# print(indice)
		palabra_invertida = palabra_invertida + palabra[indice]
		# print(palabra_invertida)
	return palabra_invertida
  	
# prog. princ.
texto = "naturales"
mi_palabra_invertida = invertir_palabra(texto)
print(mi_palabra_invertida)
