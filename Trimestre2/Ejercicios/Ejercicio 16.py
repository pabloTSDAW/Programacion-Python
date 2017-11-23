#Apartado a
def escribir():
    """Escribe un fichero mediante entrada por teclado"""
    f = open('ficheroB.txt', 'w')
    linea = input("Escribe una linea: ")
    while linea != '':
        f.write(linea + '\n')
        f.close()
        linea = input("Escribe una linea: ")
        f = open('ficheroB.txt', 'w')


#Apartado b
def escribir2():
    """Escribe un fichero mediante entrada por teclado y lo protege"""
    f = open('ficheroB.txt', 'w')
    linea = input("Escribe una linea: ")
    while linea != '':
        f.write(linea + '\n')
        f.close()
        linea = input("Escribe una linea: ")
        f = open('ficheroB.txt', 'a')

escribir2()
