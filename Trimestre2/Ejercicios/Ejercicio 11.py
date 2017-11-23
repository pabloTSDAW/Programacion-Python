entrada_incorrecta = True

def cak():
    "Transforma grados Celsius a grados Kelvin"
    celsius = int(input("Introduce una temperatura en Celsius: "))
    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError("Temperatura por debajo del mínimo")
    else:
        print(celsius,"grados Celsius son",kelvin, "Grados Kelvin")

while entrada_incorrecta:
    try:
        cak()
        entrada_incorrecta = False
    except ValueError as error1:
        print(error1)
        
            
