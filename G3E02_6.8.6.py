#devuelve solo las consonantes.  Ejemplo 'algoritmos' devuelve lgrtms

def remove_vowels(text):
    """devuelve solo consonantes de un texto."""
    consonants = ''
    for i in (text): 
        if i not in 'aeiou':
            consonants = consonants + i
    return consonants

# programa principal
print(remove_vowels ('ayelen'))
