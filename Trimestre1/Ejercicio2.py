"""100 multiplos de un numero escrito por el usuario"""
cad_num=input("Introduce un numero")
numero=int(cad_num)
numero_op=1
while numero_op<100:
    numero_op=numero_op+1
    print(numero_op,numero*numero_op)
