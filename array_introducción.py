# referencias 
# https://likegeeks.com/es/tutorial-python-con-numpy/
# https://likegeeks.com/es/multiplicacion-matriz-numpy/
# https://aprendeia.com/introduccion-a-numpy-python-1/
# 
# primeras cuentas:
# https://www.learnpython.org/es/Numpy%20Arrays
# Aplicación científica:
# https://damianavila.github.io/Python-Cientifico-HCC/3_NumPy.html

import numpy

a = numpy.array([1, 2, 3])

newArray = numpy.append (a, [10, 11, 12])

print(newArray)


b = numpy.array([[2,3,4],[5,6,7]])
c = numpy.append(b,[[70,80,90]],axis = 0)
d = numpy.append(b,[[800],[900]],axis = 1)
print("Matriz b\n",b)
print("Matriz c\n",c)
print("Matriz d\n",d)

