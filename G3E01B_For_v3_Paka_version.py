" NO BORRAR SE USA EN EL AV"
" Esta versión está mejorada. Compará con la versión anterior del FOR y analizá las diferencias"
def invertir_palabra( palabra ):
	long = len(palabra) - 1
	palabra_invertida = ""
	for i in range(len(palabra)):  # si "naturales" -> range(9)
		indice = long - i
		# print(indice)
		palabra_invertida = palabra_invertida + palabra[indice]
		# print(palabra_invertida)
	return palabra_invertida
	
# prog. princ.
texto = "naturales"
mi_palabra_invertida = invertir_palabra(texto)
print(mi_palabra_invertida)