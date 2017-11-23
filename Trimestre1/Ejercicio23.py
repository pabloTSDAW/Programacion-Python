"""
    Basandonos en la estrucura de pila, vamos a escribir funciones para jugar a
    las torres de Hanoi, la funcion cima nos dice cual es el elemento que esta
    encima de la pila
"""

a = [3,2,1]
b = []
c = []

def cima(pila):
    """Muestra la el ultimo contenido de 'pila'"""
    
    if vacia(pila):
        return None
    else:
        return pila[-1]


def mueve(a,b):
    """Mueve la cima de 'a' a 'b'"""
    
    if not vacia(a):
        if vacia(b) or cima(a) < cima(b):
            introduce(b,saca(a))
            mostrar()
    else:
        print("Movimiento incorrecto")


def introduce(pila,c):
    """Introduce 'c' en 'pila'"""
    
    pila.append(c)


def saca(pila):
    """Saca el ultimo caracter de 'pila' y lo muestra"""
    
    if vacia(pila):
        return None
    else:
        return pila.pop()


def vacia(pila):
    """Te indica si 'pila' esta vacia"""
    
    return pila == []


def realiza():
    """Realiza el problema de las torres de Hanoi"""

    mostrar()
    mueve(a,c)
    mueve(a,b)
    mueve(c,b)
    mueve(a,c)
    mueve(b,a)
    mueve(b,c)
    mueve(a,c)
    return a,b,c


def mostrar():
    print(a,b,c)


#Codigo proncipal
realiza()
    
