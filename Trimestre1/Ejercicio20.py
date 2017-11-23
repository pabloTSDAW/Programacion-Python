"""
    Crear una funcion, la funcion codifica lo que se le pase un mensaje y un
    numero, esta funcion lo que va a hacer es desplazar cada palabra de la
    cadena x caracteres
"""

mensaje = input("Introduce una frase: ")
n = int(input("Introduce un numero para codificar la frase: "))

def codifica(mensaje,n):
    
    frase = ""
    
    for c in mensaje:
        x = ord(c) + n
        frase = frase + chr(x)
    return frase

def decodifica(mensaje,n):
    frase = ""
    
    for c in mensaje:
        x = ord(c) - n
        frase = frase + chr(x)
    return frase

print("Este es tu mensaje codificado si has pedido codificar:")
print(codifica(mensaje,n))
print("Este es tu mensaje decodificado si has pedido decodificar:")
print(decodifica(mensaje,n))
