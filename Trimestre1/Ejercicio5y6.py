"""Tiene que pedirte que introduzcas algo infinitamente hasta que introduzcas Fin y si escribes algo acabado en a te dice que acaba en a"""
entrada = input("Introduce lo que sea: ")
if entrada[len(entrada)-1] == "a":
    print("La ultima letra es la a")
while entrada != "Fin":
    print("Has introducido: '", entrada, "' y tiene", len(entrada), "caracteres." )
    entrada = input("Introduce algo mas: ")
    if entrada[len(entrada)-1] == "a":
        print("La ultima letra es la a")
print("Hasta luego")
