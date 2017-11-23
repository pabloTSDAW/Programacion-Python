#Apartado a
def cuentapalabras(cadena, pal):
    "Nos dice cuantas veces se repite una palabra en la cadena"""
    lista = []
    palabras = cadena.split()
    for i in palabras:
        if i == pal:
            lista.append(i)
    return len(lista)


def palabras(cadena):
    """Devuelve un diccionario con cada palabra y su número de ocurrencias
    en una cadena"""
    dic = {}
    palabra = cadena.split()
    for i in palabra:
        dic[i] = cuentapalabras(cadena, i)
    return dic


def abrir():
    """Abre un fichero del directorio de ejercicios, lo lee linea a linea
    y nos decuelve un diccionario con el numero de ocurrencias de cada palabra"""
    fichero = input('Introduce el fichero que quieres abrir: ')
    f = open(fichero)
    texto = f.readlines()
    dic = {}
    dic2 = {}
    for linea in texto:
        dic = palabras(linea)
        dic2.update(dic)
    print(dic2)
      
"""abrir()"""


def abrir2(): #Otra forma con cadena vacia y sumando las lineas
    """Abre un fichero del directorio de ejercicios, lo lee linea a linea
    y nos decuelve un diccionario con el numero de ocurrencias de cada palabra"""
    fichero = input('Introduce el fichero que quieres abrir: ')
    f = open(fichero)
    texto = f.readlines()
    dic = {}
    cadena = ''
    for linea in texto:
        cadena = cadena + linea
    dic = palabras(cadena)
    print(dic)

abrir2()

#Apartado b

def es_separador(car):
    """Nos dice si un caracter es separador o no"""
    separadores = ' ,.;:/?¿¡!()'
    if car in separadores:
        return True


def palabras2(cadena):
    """Devuelve un diccionario con cada palabra y su número de ocurrencias
    en una cadena"""
    dic = {}
    acum = ''
    for i in cadena:
        if es_separador(i):
            acum += ' '
        else:
            acum += i
    palabra = acum.split()
    for x in palabra:
        dic[x] = cuentapalabras(acum, x)
    return dic



def abrir():
    """Abre un fichero del directorio de ejercicios y lo lee linea a linea"""
    fichero = input('Introduce el fichero que quieres abrir: ')
    f = open(fichero)
    texto = f.readlines()
    dic = {}
    dic2 = {}
    for i in texto:
        palabras2(i)
        dic = palabras2(i)
        dic2.update(dic)
    print(dic2)

"""abrir()"""


#Apartado c
