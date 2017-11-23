"""
    Escribir una funcion a la que se le pase una cadena y nos devolvera verdadero
    o falso, si es palindromo o no
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

def es_palindromo (cad):
    if invierte(sin_blanco(cad)) == sin_blanco(cad):
        return True
    if invierte(sin_blanco(cad)) != sin_blanco(cad):
        return False

print("Cadena que es palindromo")
print(es_palindromo(invierte(sin_blanco("dabale arroz a la zorra el abad"))))
print("Cadena que no es palindromo")
print(es_palindromo(invierte(sin_blanco("Jose Pepito"))))

