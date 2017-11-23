"""
    Dada una lista queremos insertar detras de cada elemento el mismo elemento
"""

lista_ver = [1,4,3,4]
lista = lista_ver.copy()

for c in lista_ver:
    lista.insert(c,c)
lista
lista_ver
