#while con if
positivos=0  #variable que comienza en 0
n=int(input('Número(0 para terminar):'))   #variable que el usuario ingresa
while n!=0:
    if n > 0:  #evaluamos si el num es positivo o mayor que 0
        positivos+=1
    n=int(input('Número (o para terminar):'))
print ('Cantidad de positivos;', positivos)
