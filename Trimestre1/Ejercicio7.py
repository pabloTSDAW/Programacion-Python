"""El usuario introduce una cadena, y esa cadena sale letra a letra"""
entrada = input("Introduce una cadena para dividirla en las letras ")
posicion = 0
while posicion < len(entrada):
    print(entrada[posicion])
    posicion = posicion + 1
print("Ya se ha dividido la cadena que se ha puesto")
