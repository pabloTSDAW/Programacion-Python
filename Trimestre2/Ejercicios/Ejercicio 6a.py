import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('square')
t.shapesize(4,1)

#Apartado a

def turn(x,y):
    """Cuando pinchas en la tortuga, gira 180 grados"""
    t.left(180)

t.onclick(turn)
