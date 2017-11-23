def palabras(cadena, separadores):
    '''Dada una cadena, separa las palabras según los separadres que
    le indiquemos'''
    acum = ''
    for car in cadena:
        if car in separadores:
            acum += ' '
        else:
            acum += car
    palabra = acum.split()
    print(palabra)


palabras('Hola, ¿cómo estás?', ' ,.;:/?¿¡!()')
    
