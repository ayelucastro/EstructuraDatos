def ingreso_notas(materias, notas):
	for materia in materias:
  		nota_alumno = int(input(f'¿Qué nota sacaste en {materia}? '))
  		notas.append(nota_alumno)
	return notas

def mostrar_notas(materias, notas):
	indice = 0
	for materia in materias:
		print(f'En {materia} te sacaste un {notas[indice]}')
		indice += 1
	return None

def main():
	lista_materias = ('Matemáticas', 'Física', 'Química', 'Historia','Lengua')
	notas_de_alumno = list()

	mis_notas = ingreso_notas(lista_materias, notas_de_alumno)
	mostrar_notas(lista_materias, mis_notas)
	return None