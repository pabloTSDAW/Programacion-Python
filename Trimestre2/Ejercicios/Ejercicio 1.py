import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed('fastest')
t.pen(pencolor='blue', fillcolor='green')

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


def estrella(lado, puntas):
    """Dibuja una estrella"""
    for i in range(puntas):
        t.fd(lado)
        t.rt(180-180/puntas)

        
    
    
