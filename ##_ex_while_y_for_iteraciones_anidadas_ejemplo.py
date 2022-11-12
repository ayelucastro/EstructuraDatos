#iteraciones anidadas con while y for
pares=0
numero=int(input('Número (-1 para terminar el programa):'))   #ingresa un numero
while numero !=-1:        #chequea si el numero es distinto de -1   
    if numero%2 == 0:     #chequea si el numero es par
        pares += 1        #si es par lo suma
    suma = 0
    while numero!= 0:
        digito = numero%10
        suma += digito   #suma los digitos por separado 
        numero = numero//10
    print ('Suma de sus digitos:', suma)
    numero=int(input('Número (-1 para terminar el programa):'))
print('se ingresaron', pares, 'números pares')