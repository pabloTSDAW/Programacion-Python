"""
    Define una función a la que se le pasen como parámetros una cadena de
    caracteres y devuelva esa misma cadena sin blancos y al reves
"""

def sin_blanco (cad):
    acum = ""
    for c in cad:
        if c != " ":
            acum = acum + c
    return acum

def invierte (cad):
    acum = ""
    for c in cad:
        acum =  c + acum
    return acum
print(invierte(sin_blanco(" A A B B C C A A ")))

