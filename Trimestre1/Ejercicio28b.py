"""
    Crear una lista por comprension con las cadenas invertidas de la lista anterior
"""

cad = "Hola Pepe"

lista = [cad[:i] for i in range(1, len(cad)+1)]

print(lista)
