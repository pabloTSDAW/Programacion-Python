"""El usuario introduce un numero que indicara la tabla de multipicar y otro que indicara la longitud"""
tabla=input("Introduce una tabla de multiplicar")
tabla_num=int(tabla)
longitud=1
longitud_max_cad=input("Introduce longitud de la tabla de multiplicar")
longitud_max=int(longitud_max_cad)
while longitud<longitud_max:
    longitud=longitud+1
    resultado=tabla_num*longitud
    print(tabla_num,"x",longitud,"=",resultado)
