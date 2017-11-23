"""
    Escribir una funcion que nos cuente el numero de vocales
    que tiene un texto
"""


def cuenta_vocales(texto):
    """Devuelve el numero de vocales de un texto"""
    
    contador = 0
    for c in texto:
        if es_vocal(c):
            contador += 1
    return contador


def es_vocal(c):
    """Te indica si un caracter es una vocal o no"""
    
    return c in "aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ"


texto = input("Introduce un texto: ")
while texto != "":
    print(cuenta_vocales(texto))
    texto = input("Introduce un texto: ")
