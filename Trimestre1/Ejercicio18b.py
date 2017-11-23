"""
    Escribir una funcion a la que se le pase una cadena y nos devolvera verdadero
    o falso, si es palindromo o no
"""

cad = input("Introduce una frase: ")
acum_blan = ""
for c in cad:
    if c != " ":
        acum_blan = acum_blan + c
acum_invert = ""
for c in acum_blan:
    acum_invert =  c + acum_invert

def es_palindromo (cad):
    if acum_invert == acum_blan:
        return True
    if acum_invert != acum_blan:
        return False
print("¿La cadena es palindromo?")
print(es_palindromo(acum_invert))
