a = 'Un divertido '
b = 'programa '
c = 'radio.'
s = ''
d = 'Como '
e = 'estuvo '
f = 'tu dia?'
sp = ' '
cad_1 = 'I love you!'
cad_2 = 'aeiou'

def tests_1():
    print('Un ' + 'divertido' + s + 'programa ' + 'de ' + 'radio.')
    print (a + b + 'de ' + c)   #Un divertido programa de radio.
    print(3 * b) #programa programa programa 
    print('3 ' + b)   #3 programa 
    return None  

def tests_2():
    print('Un' + s + 'divertido' + s + 'programa' + s + 'de ' + c + '.')
    return None

def print_vertical():
    for c in 'I love You':
        print(c)
    return None

#for c in cad_2: #print en vertical sin ser una funcion, usando variable
    print (c)

def look_in():
    if 'tu' in b:
        print('Este str es para vos.')
    return None

def errors_1():
    print(3 + b) # ERROR porque no puede sumar int y str
    return None
 
#programa a testear



#programas pricipal
#print(tests_1())  #si pongo print + la funcion me imprime el valor de return
#tests_1()   #si no pongo print + la funcion NO me IMPRIME el valor de return (NONE)
#tests_2()
print_vertical()
#look_in()