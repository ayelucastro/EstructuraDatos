def triangulo_con_str():
    s = 'Hola, como estas en tu dia?'
    puntos = ""
    for letra in s:
        puntos = puntos + letra + "."
        print(puntos)
    return None
    

def str_con_puntos():
    s = 'Hola, como estas en tu dia?'
    for letra in s:
        puntos = ""
    for letra in s:
        puntos = puntos + letra + "."
    print(puntos)
    return None

#programa principal
str_con_puntos()