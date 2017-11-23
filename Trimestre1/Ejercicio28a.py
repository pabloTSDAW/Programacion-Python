"""
    Construir una lista por comprension que contenga de un texto "Hola Pepe"
    que contenga h, ho, hol, hola... y que cada uno me lo guarde een una
    posicion de la lista, no usar acumulador.
"""

cad = "Hola Pepe"

lista = [cad[:i] for i in range(1, len(cad)+1)]

print(lista)
