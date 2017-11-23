"""
    El programa lee una serie de numeros y los imprime en orden inverso y nos da
    la media, cuando el usuario añade un 0 se corta.
"""

lista = []
sum_tot = 0

num = int(input("Introduce un numero: "))
while num != 0:
    lista.append(num)
    sum_tot = sum_tot + 1
    
    print(lista)
    num = int(input("Introduce un numero: "))


