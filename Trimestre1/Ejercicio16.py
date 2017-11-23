"""
    Define una función a la que se le pasen como parámetros una cadena de
    caracteres y les de la vuelta
"""

def invierte (cad):
    acum = ""
    for c in cad:
        acum =  c + acum
    return acum
print(invierte("Hola Pepe"))
