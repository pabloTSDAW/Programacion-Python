"""Al introducir un numero te tiene que decir si es positivo o negativo"""
numero = 1
while numero != 0:
    numero_cad = input("Introduce un numero para saber si en negativo o positivo")
    numero = int(numero_cad)
    if numero < 0:
        print("Este numero es negativo")
    elif numero > 0:
        print("Este numero es positivo")
print("Has puesto 0, ya no puedes introducir mas numeros")
