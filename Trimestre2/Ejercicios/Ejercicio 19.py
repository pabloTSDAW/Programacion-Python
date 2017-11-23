nombre = set('carlos'+'áóéíú')


def esta(nom):
    '''Nos dice si un nombre tiene sus letras en la palabra Carlos'''
    for letra in nom:
        if letra in nombre:
            return True

        
def nombres(arch):
    '''Nos dice los nombres del lemario que no tienen ninguna letra
    coincidente con Carlos'''
    fichero = open(arch)
    for palabra in fichero:
        palabra = palabra.strip('\n')
        palabra = palabra.lower()
        if esta(palabra) == True:
            pass
        else:
            print(palabra)

nombres('nombres.txt')

                
                






