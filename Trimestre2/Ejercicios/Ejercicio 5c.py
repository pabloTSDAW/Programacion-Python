from random import randint

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pen(pencolor='black', fillcolor='white')
t.speed('fastest')
t.shape('circle')
s.screensize(400,300)
t.up()
s.delay(5)

m=turtle.Turtle()
m.pencolor("black")
m.up()
m.speed(9)
m.goto(400,300)
m.down()
m.goto(-400,300)
m.goto(-400,-300)
m.goto(400,-300)
m.goto(400,300)
m.hideturtle()

#Apartado c

'''
def rebotes():
    """Hace que la pelota rebote con los limites de la pantalla"""
    t.left(200)
    while True:
        t.fd(5)
        if t.ycor() >= 290.00 and t.heading() in range(91,180):
            t.left((180 - t.heading())*2)
            t.fd(5)
        if t.ycor() >= 290.00 and t.heading() in range(0,90):
            t.right(t.heading() * 2)
            t.fd(5)
        if t.ycor() <= -290.00 and t.heading() in range(181,270):
            t.right(t.heading() * 2)
            t.fd(5)
        if t.ycor() <= -290.00 and t.heading() in range(271,359):
            t.left((360 - t.heading()) * 2)
            t.fd(5)
        if t.xcor() >= 390.00 and t.heading() in range(0,90):
            t.left((90 - t.heading()) * 2)
            t.fd(5)
        if t.xcor() >= 390.00 and t.heading() in range(271,359):
            t.right((90 - (360 - t.heading())) * 2)
            t.fd(5)
        if t.xcor() <= -390.00 and t.heading() in range(91,180):
            t.right((t.heading() - 90) * 2)
            t.fd(5)
        if t.xcor() <= -390.00 and t.heading() in range(181,270):
            t.left((270 - t.heading()) * 2)
            t.fd(5)'''

def rebotes():
    """Hace que la pelota rebote con los limites de la pantalla"""
    t.setpos(0,170)
    t.left(340)
    while True:
        t.fd(3)
        if t.ycor() >= 280:
            t.setheading(-t.heading())
            t.fd(5)
        if t.ycor() <= -280:
            t.setheading(-t.heading())
            t.fd(5)
        if t.xcor() <= -370:
            t.setheading((270-(360 - t.heading()))*2)
            t.fd(5)
        if t.xcor() >= 370:
            t.setheading(90
            t.fd(5)
        

        
rebotes()
