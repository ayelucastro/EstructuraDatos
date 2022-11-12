INTENTOS_MAX = 7

def ahorcado():
    """Subrutina principal del juego del ahorcado"""
    global INTENTOS_MAX   
    imprimirEntrada() 
    continuar = True
    while continuar:
        textoOriginal = leerTextoOriginal()  # Lee texto válido (puede tener acentos y mayúsculas)
        limpiarPantalla()
        imprimirEntrada()
        texto = preparar(textoOriginal)      # saca acentos, mayúsculas y espacios iniciales y finales
        intentadas = ""                      # string con caracteres usados
        intentos = 0                         # contador de intentos fallidos  
        ronda = 1                            # número de rondas
        while intentos < INTENTOS_MAX and not adivino(texto, intentadas):
            imprimirRonda(texto, intentadas, intentos, ronda)
            letraIntento = leerIntento(intentadas)
            if aciertaIntento(texto, letraIntento):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos += 1
            intentadas += letraIntento
            ronda += 1
        if adivino(texto, intentadas):
            imprimirMensajeVictoria(textoOriginal)
        else:
            imprimirMensajeDerrota(textoOriginal)
        continuar = leerJugarNuevamente()
    imprimirMensajeDespedida()

def limpiarPantalla():
    print("\n" * 40)
   
def imprimirEntrada():
    """Subrutina que imprime un mensaje de bienvenida"""
    print("                 Bienvenido al juego de                         ")
    print("                                                                ")
    print("   #    #     # ####### ######   #####     #    ######  ####### ")
    print("  # #   #     # #     # #     # #     #   # #   #     # #     # ")
    print(" #   #  #     # #     # #     # #        #   #  #     # #     # ")
    print("#     # ####### #     # ######  #       #     # #     # #     # ")
    print("####### #     # #     # #   #   #       ####### #     # #     # ")
    print("#     # #     # #     # #    #  #     # #     # #     # #     # ")
    print("#     # #     # ####### #     #  #####  #     # ######  ####### ")
    print("")
    print("Creado por ASCII ART")
    
def leerTextoOriginal():
    """Función que lee de la consola la palabra a ser adivinada y devuelve como resultado el texto leído"""
    texto = input("Ingrese la palabra a adivinar (hasta 30 caracteres). Sólo puede contener letras: ")
    while not esTextoValido(texto):
        print("El texto sólo puede contener letras y no más de 30 caracteres")       
        texto = input("Ingrese la palabra a adivinar: ")
    return texto

def esTextoValido(texto):
    """Función booleana que dice si un string es un texto válido para adivinar en el juego.
    Entradas: texto a analizar.
    Salidas: True si el texto contiene sólo letras y tiene al menos un caracter,
    False en caso contrario.
    Restricciones: texto debe ser un string. 
    """
    if type(texto) != str or len(texto)> 30 or texto == "":
        return False
    for letra in texto:
        if letra.lower() not in "aábcdeéfghiíjklmnñoópqrstuúüvwxyz":
            return False
    return True

def preparar(texto):
    """Convierte el texto a minúsculas, sustituye acentos.
    Entradas: texto a procesar.
    Salidas: texto sin mayúsculas ni acentos """
    texto = texto.lower()  
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    return texto
    
def adivino(texto, intentadas):
    """Función booleana que dice si el usuario ya adivinó el texto
    Entradas:
    - texto: texto preparado (sin tildes, ni acentos)
    - intentadas: letras que el usuario ha intentado
    Salidas: True si todas las letras del texto ya han sido intentadas y False en caso contrario.
    Restricciones:
    - texto debe ser un string de letras sin acentos.
    - intentadas debe ser un string de letras sin acentos."""
    for letra in texto:
        if letra not in intentadas:
            return False
    return True

def imprimirRonda(texto, intentadas, intentos, ronda):
    """Esta función imprime los mensajes requeridos para cada ronda del juego.
    Imprime el número de ronda actual, un mensaje que indica las letras que ya fueron utilizadas, cantidad de intentos
    fallidos y también escribe el texto enmascarado.
    Entradas:
    - texto: texto preparado sin tildes ni acentos.
    - intentadas: letras que el usuario ha intentado.
    - intentos: cantidad de intentos fallidos.
    - ronda: número de ronda por la que va el juego.
    Salidas: Impresión en pantalla de la información de la ronda.
    Restricciones: ninguna."""
    print()
    print("_" * 120)
    print()
    print("RONDA NÚMERO: ", ronda)
    print("Letras que ya fueron utilizadas: ", intentadas)
    print("Cantidad de intentos fallidos: ", intentos)
    print()
    print(enmascarar(texto, intentadas))
    print()

def enmascarar(texto, intentadas):
    """Retorna un string con un guión bajo por cada letra que no ha sido adivinada. Si una letra del 
    texto aparece en las letras intentadas, entonces la agrega como tal en lugar del guión.    
    Entradas:
    - texto: texto a adivinar.
    - intentadas: letras que el usuario ha intentado.
    Salidas: string con el texto enmascarado.
    Restricciones: ninguna."""    
    resultado = ""    
    for letra in texto:
        if letra in intentadas:
            resultado += letra + " "
        else:
            resultado += "_ "        
    return resultado
        
def leerIntento(intentadas):
    """Función que pide al usuario que escriba una letra para adivinar. Si ya se encuentra en las intentadas o no es una
    letra, debe imprimir un mensaje de error y volver a pedir la letra.
    Entradas:
    - intentadas: letras que el usuario ha intentado.
    Salidas: string con la letra elegida por el usuario.
    Restricciones: ninguna."""
    print()
    letra = input("Escriba una letra: ")
    letra = letra.lower()
    while len(letra) != 1 or letra not in "abcdefghijklmnñopqrstuvwxyz" \
        or letra in intentadas:
        print("Por favor ingrese una letra que no haya intentado. Intentadas: ", intentadas)
        letra = input("Escriba una letra: ")
        letra = letra.lower()
    print()
    return letra

def aciertaIntento(texto, letra):
    """Función booleana que dice si un intento es correcto o no.
    Entradas:
    - texto que se está adivinando.
    - letra que intentó el usuario.
    Salidas: True si la letra se encuentra en el texto a adivinar y False en caso contrario.
    Restricciones: ninguna."""
    return letra in texto

def imprimirMensajeAcierto():
    print("¡Ha adivinado! :D")

def imprimirMensajeNoAcierto():
    print("¡Letra no encontrada! :(")
    
def imprimirMensajeVictoria(textoOriginal):
    print()
    print("_" * 120)
    print()
    print("¡Felicidades! Ha adivinado el texto: ", textoOriginal)

def imprimirMensajeDerrota(textoOriginal):
    print()
    print("_" * 120)
    print()
    print("Ha perdido. El texto a adivinar era: ", textoOriginal)

def leerJugarNuevamente():
    """Función booleana que pregunta al usuario si desea jugar de nuevo. Sólo acepta "S" o "N" como respuesta.
    Entradas: ninguna.
    Salidas: True si el usuario escribe "S", False en caso contrario.
    Restricciones: ninguna."""
    print()
    respuesta = input("¿Desea jugar de nuevo? (S/N)")
    respuesta = respuesta.lower()
    while respuesta not in ["s", "n"]:
        respuesta = input("¿Desea jugar de nuevo? (S/N)")
        respuesta = respuesta.lower()
    return respuesta == "s"

def imprimirMensajeDespedida():
    print("Gracias por jugar al ahorcado. Nos vemos pronto")

ahorcado()








