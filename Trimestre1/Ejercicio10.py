"""
    Un usuario indica dos numeros y el programa produce multiplos del primero  el
    numero de veces del segundo
"""
multi = int(input("Introduce un multiplicador: "))
multip = int(input("Introduce cuantos multiplos quieres: "))
for i in range(multi, multi * multip + 1, multi):
    print(i)
    

             
