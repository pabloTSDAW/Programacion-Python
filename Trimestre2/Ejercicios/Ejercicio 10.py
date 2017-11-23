entrada_incorrecta = True

def leenota():
    nota=int(input("Introduce una nota: "))
    if nota not in range(0, 11):
        raise ValueError("La nota no está comprendida entre 0 y 10")
    else:
        print("La nota es: ", nota)

while entrada_incorrecta:
    try:
        leenota()
        entrada_incorrecta = False
    except ValueError as error1:
        print(error1)
