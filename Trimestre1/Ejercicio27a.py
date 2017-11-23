"""
    Define una funcion a la que se le pasa una cadena y
    nos devuelve el numero de veces que se repite una vocal
"""

def cuenta_vocales(texto):
    """Cuenta cada vocal de un texto por separado"""
    
    lista = [0,0,0,0,0]
    for c in texto:
        
        if c == "a":
            lista[0] = lista[0] + 1
        if c == "e":
            lista[1] = lista[1] + 1
        if c == "i":
            lista[2] = lista[2] + 1
        if c == "o":
            lista[3] = lista[3] + 1
        if c == "u":
            lista[4] = lista[4] + 1
            
    return lista

texto = input("Introduce un texto: ")
while texto != "":
    print(cuenta_vocales(texto))
    texto = input("Introduce un texto: ")
