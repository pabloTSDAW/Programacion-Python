"""
    Define una funcion a la que se le pasa una cadena y
    nos devuelve el numero de veces que se repite una vocal
"""

def cuenta_vocales(texto):
    #Cuenta cada vocal de un texto por separado
    
    lista = [0,0,0,0,0]
    for c in texto:
        if es_vocal_a(c):
            lista[0] = lista[0] + 1
        if es_vocal_e(c):
            lista[1] = lista[1] + 1
        if es_vocal_i(c):
            lista[2] = lista[2] + 1
        if es_vocal_o(c):
            lista[3] = lista[3] + 1
        if es_vocal_u(c):
            lista[4] = lista[4] + 1
    return lista


def es_vocal_a(c):
    #Te indica si un caracter es a o no
    return c in "aAáÁäÄ"


def es_vocal_e(c):
    #Te indica si un caracter es e o no
    return c in "eEéÉëË"


def es_vocal_i(c):
    #Te indica si un caracter es i o no
    return c in "iIíÍïÏ"


def es_vocal_o(c):
    #Te indica si un caracter es o o no
    return c in "oOóÓöÖ"


def es_vocal_u(c):
    #Te indica si un caracter es u o no
    return c in "uUúÚüÜ"


texto = input("Introduce un texto: ")
while texto != "":
    print(cuenta_vocales(texto))
    texto = input("Introduce un texto: ")

