#guia1_2
contador=0
total_litros=0
km=int(input('Escriba los kilómetros usados (-1 para salir): '))
while km!=-1:
    lts=int(input('Escriba los litros: '))
    contador=contador+km
    total_litros=total_litros+lts
    print('KPL en este reabastecimiento: ',(km/lts))
    print('Total KPL: ', (contador/total_litros))
    km=int(input('Escriba los kilómetros usados (-1 para salir): '))
