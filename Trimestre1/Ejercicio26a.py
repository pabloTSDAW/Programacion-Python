"""
    Define una funcion, que se le pasa una cadena y la funcion devuelve cuantas
    vocales tiene esa cadena
"""

def cuenta_vocales(texto):
    """Devuelve el numero de vocales de un texto"""
    
    contador = 0
    for c in texto:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            contador = contador + 1
    return contador

texto = input("Introduce un texto: ")
while texto != "":
    print(cuenta_vocales(texto))
    texto = input("Introduce un texto: ")
