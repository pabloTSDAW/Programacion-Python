
'''Crear un generador infinito de códigos consecutivos
a partir de un valor inicial pasado como parámetro.'''

def codigos(n):
    '''Genera codigos consecutivos a partir del n'''
    while True:
        yield n
        n += 1


for j in codigos(10):
    print(j)


  
    
