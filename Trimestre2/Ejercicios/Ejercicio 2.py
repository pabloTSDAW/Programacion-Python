import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed('normal')
t.pen(pencolor='blue', fillcolor='green')

#Apartado a

def equilatero(lado):
    """Crea un triángulo equilátero de lado = lado"""
    for i in range(3):
        t.forward(lado)
        t.left(120)
    

def circulo_triangulos(lado, triangulos):
    """Crea un círculo con triangulos"""
    for i in range(triangulos):
        equilatero(lado)
        t.up()
        t.rt(360/triangulos)
        t.fd(50)
        t.down()
