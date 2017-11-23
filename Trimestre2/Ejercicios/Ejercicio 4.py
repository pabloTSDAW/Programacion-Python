from random import randint
import math

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed('normal')
t.pen(pencolor='blue', fillcolor='green')

#Apartado a y b

colores = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'gold','tomato']

def poligono(lado, vertices):
    """Crea un polígono de lado=lado"""
    for i in range(vertices):
        t.fd(lado)
        t.left(360/vertices)

def poligonos_color(lado, vertices, num):
    """Dibuja poligonos inscritos de distintos colores"""
    for i in range(1, num):
        t.fillcolor(colores[randint(0,i)])
        t.begin_fill()
        poligono(lado/i, vertices)
        t.end_fill()
        
def poligono_centrado(lado, num_lado):
    """Dibuja un polígono de lado = lado, centrado"""
    a = ((math.pi * 2) / num_lado) / 2
    y = (lado / (2 * math.tan(a)))
    x = lado / 2
    t.up()
    t.goto(-x, -y)
    t.down()
    for i in range(num_lado):
        t.forward(lado)
        t.left(360/num_lado)

def cuadrados_color_centrados(lado, vertices, num):
    """Dibuja poligonos inscritos centrados de distintos colores"""
    for i in range(1, num):
        t.fillcolor(colores[randint(0,i)])
        t.begin_fill()
        poligono_centrado(lado/i, vertices)
        t.end_fill()
