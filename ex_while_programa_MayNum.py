#pedir el ingreso de 4 numeros y devolver el mayor numero
contador=0
number=0
print("Ingrese 4 números para evaluar cual es el mayor.")
number=int(input("Ingrese un número:"))
el_mayor=number
contador+=1  #contador=contador+1
while contador<4:
    number=int(input("Ingrese un número:"))
    contador+=1
    if number>el_mayor:
        el_mayor=number 
print("El mayor número es: ",el_mayor)
