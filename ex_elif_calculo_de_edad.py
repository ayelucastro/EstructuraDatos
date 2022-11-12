# Carnet de conducir
# Se le pide al usuario la edad y si es mayor o tiene 18 años, puede sacar el carnet.
# si menor de 18 -> no puedo sacar registro en CABA
# igual o mayor a 18 -> saco registro!
# mayor a 60 años -> duración 5 años
# mayor a 70 años -> duración 1 años
# mayor 90 años -> no puede manejar?
edad = int(input("Por favor ingrese su edad:"))
if edad >= 18 and edad < 60:
        print("Buenísimo podes sacar el registro de conducir")
elif edad >= 60 and edad < 70:
	print("Buenísimo, tu licencia tiene una duración de 5 años") 
elif edad >= 70 and edad < 90:
	print("Buenísimo, tu licencia tiene una duración de 1 año") 
elif edad >= 90:
	print("Lamentablemente, ya no podes manejar")
else:
	print("Lamentablemente, no podes sacar registro")
  
print("Nos vemos la próxima!!!")
