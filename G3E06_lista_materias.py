

materias = ['matematicas' , 'fisica' , 'quimica' , 'historia' , 'lengua']

print(f'yo estudio: {materias [0]}')   #[aca adentro va el indice]
print(f'yo estudio: {materias [3]}')   #[imprime solo el indice]

"""for materia in materias:
    print(f'yo estudio: ' , materia)   #valid but not good, doesn´t work for numbers"""

for materia in materias:
    print(f'yo estudio: {materia}')   #will print 'text' and everything inside my list.


