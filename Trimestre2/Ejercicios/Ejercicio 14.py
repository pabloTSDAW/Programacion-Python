def abrir():
    """Abre un fichero del directorio de ejercicios"""
    prueba = True
    while prueba:
        try:
            fichero = input('Introduce el fichero que quieres abrir: ')
            f = open(fichero, 'r')
        except FileNotFoundError as error1:
            print('Fichero no encontrado')
        else:
            prueba = False
            f.read()
            print(type(f))
            
    
abrir()


        
