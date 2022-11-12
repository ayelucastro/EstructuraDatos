def a_hms(segundos):
  h = segundos // 3600
  m = (segundos % 3600) // 60
  s = (segundos % 3600) % 60
  return h, m, s

hms = a_hms(600)  #se guarda como tupla
horas, minutos, segundos = a_hms(600)

print(hms)  #tupla
print(horas, minutos, segundos)  