#salario: cuota hasta 40 horas, cuota y media a partir de 41 horas
#while con if

horas = int(input('Ingrese las horas trabajadas (-1 para terminar):'))   #variable que el usuario ingresa
tarifa = float(input('Ingrese la tarifa por horas del empleado ($00.00):'))   #variable que el usuario ingresawhile horas != -1:
while horas != -1:
    if horas <= 40:  #evaluamos la cuota a pagar
        salario = horas * tarifa
        print ('El salario es:', salario)
    elif horas > 40:  #evaluamos la cuota a pagar
        horas_extra = horas - 40
        tarifa_media = tarifa * 1.5
        salario_medio = horas_extra * tarifa_media
        print ('El salario es:', (salario + salario_medio))
    horas = int(input('Ingrese las horas trabajadas (-1 para terminar):'))   #variable que el usuario ingresa
    tarifa = float(input('Ingrese la tarifa por horas del empleado ($00.00):'))   #variable que el usuario ingresa

