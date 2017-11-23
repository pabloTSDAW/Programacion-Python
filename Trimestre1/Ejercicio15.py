"""
    Define una función a la que se le pasen como parámetros una cadena de
    caracteres y devuelva esa misma cadena sin blancos
"""

def sin_blanco (cad):
    acum = ""
    for c in cad:
        if c != " ":
            acum = acum + c
    return acum
print(sin_blanco(" A A B B C C A A D D "))
