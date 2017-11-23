entrada_incorrecta = True
while entrada_incorrecta:
    try:
        b = int(input("Dime b: "))
        x = 1 / b
        entrada_incorrecta = False
    except ZeroDivisionError as error1:
        print("b no puede ser 0")
        print(error1)
    except ValueError as error2:
        print("b tiene que ser un número!!!")
        print(error2)
    else:
        print(x)

