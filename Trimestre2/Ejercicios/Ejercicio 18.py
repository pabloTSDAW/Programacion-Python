#Apartado a

def reconocer():
    '''Nos dice si una palabra está en el lemario'''
    entrada = str(input('Dime una palabra: '))
    fichero = open('lemario2.txt')
    for palabra in fichero:
        if entrada == palabra.strip('\n'):
            print('Está en el diccionario')
        else:
            pass


#Apartado b
        
def anagrama(pal):
    '''Dada una palabra, nos da una lista de anagramas en el lemario'''
    for palabra in fichero:
        if sorted(pal) == sorted(palabra.strip('\n')):
            print(palabra)
            

anagrama('ramo')

      




