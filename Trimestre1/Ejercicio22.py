"""
    Escribir la funcion para crear una estructura LIFO
"""

def introduce(pila,c):
    pila.append(c)

def saca(pila):
    if pila == []:
        return None
    else:
        return pila.pop()

def vacia(pila):
    return pila == []
