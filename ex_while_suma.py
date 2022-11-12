#while
total=0
nro=int(input('Ingrese número (para salir ingresar 0): '))
while nro != 0:
        total += nro
        nro=int(input('Número: '))
print('Total:' ,total)