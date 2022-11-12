#anidar un if
frase=str(input('Frase: '))
print('vocales en la frase')
for x in 'aeiou':
    if x in frase:
        print (x)