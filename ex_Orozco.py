# Nota interna: No modificar. Se utiliza en presentación EDDP IFTS21 

LETRA_CANCION = "Nosotros no somos como los Orozco, yo los conozco, son ocho los monos: Pocho, Toto, Cholo, Tom, Moncho, Rodolfo, Otto, Pololo. Yo pongo los votos sólo por Rodolfo, los otros son locos, yo los conozco, no los soporto. Stop. Stop."

letra = 'o'
cantidad_letras = 0

for caracter in LETRA_CANCION:
  if caracter.lower() == letra:
    cantidad_letras += 1

print(cantidad_letras)