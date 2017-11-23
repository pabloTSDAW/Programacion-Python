def multiplicar(tabla):
    """Realiza la tabla de multiplicar de un numero"""
    i = 0
    print('La tabla de multiplicar de', tabla, 'es: ')
    for i in range(11):
        print('{tabla} x {i:2d} = {resultado:5d}'.format(tabla = tabla, i = i,
                                                   resultado = tabla * i))
    
        
