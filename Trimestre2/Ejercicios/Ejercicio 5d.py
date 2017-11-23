from random import randint

#apartado d

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pen(pencolor='black', fillcolor='white')
t.turtlesize(2.0,2.0)
t.speed('fastest')
t.shape('circle')
s.tracer(1)
s.screensize(400,300)
s.bgcolor('green')

t.up()

m = turtle.Turtle()
m.shape('square')
m.pen(fillcolor="blue")
m.pencolor('white')
m.pensize(3)
m.speed('fastest')
m.hideturtle()

m2 = turtle.Turtle()
m2.hideturtle()

p1 = turtle.Turtle()
p1.shape('square')
p1.pen(fillcolor="white")
p1.up()
p1.shapesize(7,1)
p1.setpos(-400,0)
p2 = p1.clone()
p2.setpos(400,0)

def marcador():
    m.up()
    m.shapesize(3,3)
    m.setpos(0,300)
    
def campo():
    m.up()
    m.goto(400,0)
    m.down()
    m.rt(90)
    m.fd(300)
    m.rt(90)
    m.fd(800)
    m.rt(90)
    m.fd(600)
    m.rt(90)
    m.fd(800)
    m.rt(90)
    m.fd(300)
    m.up()
    m.goto(0,300)
    m.down()
    m.goto(0,-300)
    m.up()
    m.goto(-50,0)
    m.down()
    m.circle(50)
    
def rebotes():
    """Hace que la pelota rebote con los limites de la pantalla"""
    t.left(randint(0,180))
    while True:
        t.fd(2)
        if abs(t.ycor()) >= 300.00:
            t.right(t.heading() * 2)
            t.fd(2)
        if abs(t.xcor()) >= 400.00:
            t.left((t.heading() * 2))
            t.fd(2)
        if t.distance(p1) <= 50:
            m2.write("¡GOOOOOOOOOOOOOOOOOOOOOOOOOOL!", True, align="center", font=('arial',20))
            t.goto(0,0)
        if t.distance(p2) <= 50:
            m2.write("¡GOOOOOOOOOOOOOOOOOOOOOOOOOOL!", True, align="center", font=('arial',20))
            t.goto(0,0)
            

campo()
marcador()
m.write("0 - 0", True, align="center", font=('arial',30))
rebotes()




