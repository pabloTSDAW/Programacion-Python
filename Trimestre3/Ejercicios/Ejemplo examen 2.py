'''Generar un generador de potencias sucesivas. Le pasamos un numero
x y nos da la potencia 1, 2, 3, 4… de n. potencia(n)'''

def potencia(n):
    '''Genera las potencias de un numero n'''
    i = 1
    while i > 0:
        yield n**i
        i += 1

##for j in potencia(3):
##    print(j)

a = potencia(4)
next(a)



'''Hace un iterador finito. Queremos potencias de x en n elementos
potencia(x, n)'''


def potencia2(x, n):
    '''Devuelve las primeras n potencias de x'''
    for i in range(n):
        yield x**i


##for j in potencia2(3, 10):
##    print(j)

b = potencia2(3, 10)
next(b)
