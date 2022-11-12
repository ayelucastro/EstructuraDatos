"""Se tiene un diccionario con las fechas de nacimiento de un conjunto de personas. 
Las fechas están en formato DD/MM/YYYY. 
Ejemplo:
{"Juan": "27/05/1993", "Alicia": "30/11/1990", "Elena": "27/05/1985"}

Se pide escribir una función que reciba este diccionario y agrupe las personas que 
celebran su cumpleaños el mismo día, devolviendo un diccionario en el que las claves 
son fechas en formato DD/MM, y los valores listas de nombres. 
Ejemplo:
{"30/11": ["Alicia"], "27/05": ["Juan", "Elena"]}"""