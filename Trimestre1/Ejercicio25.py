"""
    Cada vez que introduzco un numero el programa lo inserta en una lista,
    ordenandolo ordenadamente, definimos la funcion inserta_ordenado(lista,x)
    no devuelve nada
"""

lista_ver = [1]
lista = lista_ver.copy()

x = int(input("Introduce un numero: "))
        
while x != 0:
    for c in lista_ver:
        if x < lista[c - 1] or x == lista:
            lista.insert(c,x)
    lista_ver = lista.copy()
    x = int(input("Introduce un numero: "))
    
