def a_hms(segundos):
  h = segundos // 3600
  m = (segundos % 3600) // 60
  s = (segundos % 3600) % 60
  return h, m, s

hms = a_hms(600)
horas, minutos, segundos = a_hms(600)

#print(hms)
#print(horas, minutos, segundos)
print(f'{horas}:{minutos}:{segundos}')
print(f'{hms[0]}:{hms[1]}:{hms[2]}')
print("veamos el tipo de datos de la variable hms")
print(type(hms))

