centinela1=int(input ('Escriba los kilómetros usados (-1 para salir): '))
centinela2=int(input('Escriba los litros: '))
A= centinela1/centinela2
print('KPL en este reabastecimiento: ',A,)
print('Total KPL: ')
while centinela1 != '*':
  x=int(centinela1)
  if x>0:
    km=int(input('Escriba los kilómetros usados (-1 para salir): '))
    l=int(input('Escriba los litros: '))
    A= km/l
    print('KPL en este reabastecimiento: ',A,)
    print('Total KPL: ')
  elif x<0:
    km=int(input('Escriba los kilómetros usados (-1 para   salir): '))
    l=int(input('Escriba los litros: '))
    x= km/l
    print('KPL en este reabastecimiento: ',A,)
    print('Total KPL: ')
  else:
    break
