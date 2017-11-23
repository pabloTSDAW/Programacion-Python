"""
    El usuario introduce una cadena y un caracter, el programa devuelve una
    cadena sin que aparezca el cararter indicado
"""
palabra = input("Introduce una palabra: ")
caracter = input("Indica un caracter que quieras eliminar: ")
acumulador = ""
for i in palabra:
    if i != caracter:
        acumulador = acumulador + i
print(acumulador)
