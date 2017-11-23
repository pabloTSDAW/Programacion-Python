'''Construir una expresión generadora con los numeros primos menores que mil. '''

def esprimo(x):
    """Nos dice si un número es primo o no"""
    i = 2
    if x == 1:
        return False
    while i <= x//2:
        if x%i == 0:
            return False
        i += 1
    return True


#lista por comprensión

primos = (i for i in range(1000) if esprimo(i))

for j in primos:
    print(j)
