"""
    Escribe un programa donde el usuario escribe una cadena, y el programa
    hace una salida de caracter creciente
"""
entrada = input("Introduce una cadena para dividirla en las letras ")
posicion = 1
while posicion <= len(entrada):
    print(entrada[0:posicion])
    posicion = posicion + 1
print("Ya se ha acabado la salida de caracter creciente")
