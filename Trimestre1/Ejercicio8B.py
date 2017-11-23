"""
    Escribe un programa donde el usuario escribe una cadena, y el programa
    hace una salida de caracter descendiente
"""
entrada = input("Introduce una cadena para dividirla en las letras ")
longitud = len(entrada)
while longitud > 0:
    print(entrada[0:longitud])
    longitud = longitud - 1
print("Ya se ha acabado la salida de caracter descendiente")
