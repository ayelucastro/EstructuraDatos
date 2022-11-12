def divide(a, b):
    return a / b
    
x=int(input("Ingrese dividendo:"))
y=int(input("Ingrese divisor:"))
print("el valor del dividendo es", x)
print("el valor del divisor es", y)
result = divide(x, y)
print("El resultado de dividir", x, "por", y, "es:",result)