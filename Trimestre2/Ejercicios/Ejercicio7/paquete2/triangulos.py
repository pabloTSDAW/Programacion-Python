def equilatero(lado):
    """Crea un triángulo equilátero de lado = lado"""
    for i in range(3):
        t.forward(lado)
        t.left(120)


def gira_triangulos(lado, num):
    """Crea muchos triángulos equiláteros"""
    for i in range(num):
        equilatero(lado)
        t.right(360/num)



