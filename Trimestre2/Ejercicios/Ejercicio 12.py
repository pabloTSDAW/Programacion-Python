
def division():
    """Divide 1 entre un numero introducido por el usuario"""
    try:
        b = int(input("Para hacer 1/b, dime b: "))
        x = 1 / b
    except ZeroDivisionError as error1:
        print("b no puede ser 0")
    else:
        print(x)
        

def division2():
    """Divide 1 entre un numero introducido por el usuario"""
    try:
        division()
    except ValueError as error2:
        print("b tiene que ser un número!!!")
    else:
        print(x)


def division3():
    """Divide 1 entre un numero introducido por el usuario"""
    try:
       division2()
    except:
        print("Escribe algo!!!")


division3()
        



