"""
    Escribir la funcion rotar que tiene una cadena y un numero, devuelve una
    cadena rotada n veces
"""

def rotar(mensaje,n):
    """Devuelve mensaje desplazado n veces"""
    
    n = n % len(mensaje)#Evita que n sea mayor que la longitud de la cadena
    recorte = len(mensaje) - n
    men_recor = mensaje[0:recorte]
    mensaje = mensaje[recorte:] + men_recor
    
    return mensaje


mensaje = input("Introduce una frase: ")
n = int(input("Introduce un numero: "))

print(rotar(mensaje,n))
