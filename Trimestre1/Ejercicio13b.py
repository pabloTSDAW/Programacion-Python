"""
    Contar los multiplos de dos y cuantos de esos multiplos de dos son multiplos
    de tres
"""
cont = 0
suma = 0
multi2 = 0
multi23 = 0

num = int(input("Introduce un numero: "))
while num != 0:
    cont = cont + 1
    suma = suma + num
    num_calc = num
    calc2 = num_calc % 2
    calc3 = num_calc % 3
    if calc2 == 0:
        multi2 = multi2 +1
        if calc2 == 0 and calc3 == 0:
            multi23 = multi23 + 1
    num = int(input("Introduce un numero: "))
    
print("Has introducido", cont, "numeros sin contar el numero 0")
print("Has introducido", multi2, "multiplos de 2")
print("Has introducido", multi23, "multiplos de 2 y de 3")
print("La suma de todos los numeros es de", suma)

