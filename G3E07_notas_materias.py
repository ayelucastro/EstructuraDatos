#listas para pedir informacion y entregarla
#En <materia> te has sacado un <nota>

materias = ['matematicas' , 'fisica' , 'quimica' , 'historia' , 'lengua']
notas = []

for materia in materias:
    nota_aux = int(input(f'Que nota sacaste en {materia}?: '))
    notas.append(nota_aux)
index_materias = 0
for nota in notas:
    print(f'En la materia {materias[index_materias]} te has sacado un {nota}')
    index_materias += 1
    



