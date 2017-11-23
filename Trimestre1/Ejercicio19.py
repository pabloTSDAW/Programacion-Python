"""
    Imprimir la tabla ASCII desde 0 hasta 255
"""

cont = 32

while cont != 256:
    print(chr(cont), " ", cont)
    cont = cont + 1
