#for
c=int(input('cantidad de números: '))
total=0
for x in range (c):
    numero=int(input('Numero a sumar: '))
    total = total + numero #total+=numero
print('Total de la suma: ' ,total)