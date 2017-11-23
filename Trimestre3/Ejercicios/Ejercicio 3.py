#Apartado a
'''Crear un generador finito con los elementos de la sucesión de
Fibonacci menores que 100.'''

def fibonacci(n):
    '''Crea los n primeros elementos de la sucesión de Fibonacci'''
    x = 0
    y = 1
    while x + y < n:
        y = x + y
        yield y
        x = y - x
        
        
for j in fibonacci(100):
    print(j)



#Apartado b
'''Crear un generador con los cuadrados de los mil primeros números naturales.'''

def cuadrados(n):
    '''Crea los cuadrados de los n primeros números naturales'''
    x = 1
    while x < n:
        yield x*x
        x += 1

##for i in cuadrados(1000):
##    print(i)
