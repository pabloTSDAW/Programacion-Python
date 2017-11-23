import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')

def cuadrado(lado):
    """Hace que la tortuga recorra un cuadrado con lado = lado"""
    for i in range(4):
        t.forward(lado)
        t.left(90)

def cuadrados(lado, num):
    """Realiza num cuadrados con incremento 1"""
    for i in range(num):
        cuadrado(lado*i)

def cuadrados2(lado, num):
    "Dibuja cudrados anexos"""
    for i in range(num + 1):
        cuadrado(lado)
        t.right(90*i)

def gira_cuadros(lado, num, angulo):
    """Crea num cuadrados de lado=lado y con giro= angulo"""
    for i in range(num):
        cuadrado(lado)
        t.right(angulo)
