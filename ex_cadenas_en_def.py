def find_a(s): 
    """devuelve cuantas letras a hay en la cadena s."""
    counter = 0 
    for letra in s:
        if letra == 'a':
            counter = counter + 1
    return counter

def find_a_v1(s): 
    """devuelve cuantas letras a hay en la cadena s."""
    counter = 0 
    for letra in s:
        if letra == 'a':
            counter += 1
    return counter

def swap_order(s):
    for letras in s:
        s.swapcase(s)
    return s


#programa a testear




#programas pricipal
#print(find_a('ama al')) #contara la cantida de a's en lo que ponga en ()
#print(find_a_v1('ama al'))
#print(swap_order('ama al'))