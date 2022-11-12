suma=0
numero=int(input('Número positivo: '))
while numero != 0:
    digito = numero % 10  #la resta del numero dividido 10
    suma += digito   #sumo la variable suma mas el digito
    numero = numero // 10    #la variable numero se pisa con el resto de la division del numero por 10
print("Suma de los digitos: ", suma)