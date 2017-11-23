def abrir():
    """Abre un fichero del directorio de ejercicios y lo lee linea a linea"""
    fichero = input('Introduce el fichero que quieres abrir: ')
    f = open(fichero)
    linea = f.readline()
    while linea != '':   #Con bucle while es más eficiente
        print(linea)
        linea = f.readline()


def abrir2():
    """Abre un fichero del directorio de ejercicios, lo lee linea a linea
    y captura los posibles errores"""
    prueba = True
    while prueba:
        try:
            fichero = input('Introduce el fichero que quieres abrir: ')
            f = open(fichero, 'r')
            linea = f.readline()
            while linea != '':   #Con bucle while es más eficiente
                print(linea)
                linea = f.readline()
        except FileNotFoundError as error1:
            print('Fichero no encontrado')
        else:
            prueba = False

                
abrir2()


    


