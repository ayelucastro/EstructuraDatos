#una empresa paga por comisiones.  Vendedores cobran $200 + 9% vtas brutas x semana.
#usar while para recibir ventas brutas de cada vendedor
vtas = int(input('Ingrese la venta en dolares (-1 para salir): '))
while vtas != -1:
    comision = vtas * 0.09
    print ('Salario es:' , (comision + 200))
    vtas = int(input('Ingrese la venta en dolares (-1 para salir): '))
